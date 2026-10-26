"""Convert the CEGUI 0.8.7 Falagard .dox pages to Markdown and one HTML page.

Usage: python tools/convert.py <project_dir>
Reads <project_dir>/source/*.dox (from tag v0-8-7 of github.com/cegui/cegui,
doc/doxygen/falagard), writes the Markdown files and falagard-docs.html into <project_dir>.
Only the format changes; the text is kept as written.
"""
import html
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1])
SRC = ROOT / "source"
OFFICIAL = "https://static.cegui.org.uk/docs/0.8.7/"
TREE_URL = "https://github.com/cegui/cegui/tree/v0-8-7/doc/doxygen/falagard"
BLOB_URL = "https://github.com/cegui/cegui/blob/v0-8-7/doc/doxygen/falagard"

# (source name, markdown file, group label, number in group, group size, TOC depth)
PAGES = [
    ("fal_intro", "falagard-1-introduction.md", "Tutorial", 1, 2, 3),
    ("fal_tut1", "falagard-2-looknfeel-xml.md", "Tutorial", 2, 2, 3),
    ("fal_element_ref", "falagard-3-element-reference.md", "Reference", 1, 4, 2),
    ("fal_enum_ref", "falagard-4-enumeration-reference.md", "Reference", 2, 4, 2),
    ("fal_baseclass_ref", "falagard-5-base-type-requirements.md", "Reference", 3, 4, 2),
    ("fal_wr_ref", "falagard-6-window-renderer-requirements.md", "Reference", 4, 4, 2),
]
MD_FILE = {p[0]: p[1] for p in PAGES}
LEVELS = {"page": 1, "section": 2, "subsection": 3, "subsubsection": 4, "paragraph": 5}

# id -> (page name, raw title); filled before rendering
TITLES = {}
# pages outside this set that the text links to, with their official titles
EXTERNAL_TITLES = {"xml_animation": "Animation XML files."}
UNRESOLVED = set()

# ---------------------------------------------------------------- parsing

def unescape(s):
    return re.sub(r"\\([<>&])", r"\1", s)


def parse(text):
    """Blocks: ('h', level, id, title) | ('p', text) | ('ul', [text]) | ('tree', [item])
    | ('code', lang, text) | ('math', text). A tree item is {'text': str, 'children': [[item]]}."""
    text = text.replace("\r\n", "\n").replace("@cwidget", "@c widget")   # typo in fal_element_ref
    lines = text.split("\n")
    blocks = []
    para, items = [], None
    i = 0

    def flush_para():
        nonlocal para
        if para:
            blocks.append(("p", " ".join(s.strip() for s in para)))
        para = []

    def flush():
        nonlocal items
        flush_para()
        if items:
            # a few @arg items in fal_element_ref end with a stray "</li>" that Doxygen ignores
            blocks.append(("ul", [re.sub(r"\s*</li>\s*$", "", it) for it in items]))
        items = None

    while i < len(lines):
        s = lines[i].strip()
        i += 1
        if s in ("/**", "*/"):
            flush(); continue
        m = re.match(r"@(page|section|subsection|subsubsection|paragraph)\s+(\S+)\s+(.*)$", s)
        if m:
            flush()
            blocks.append(("h", LEVELS[m.group(1)], m.group(2), m.group(3).strip()))
            continue
        if s == "@code":
            flush()
            body = []
            while lines[i].strip() != "@endcode":
                body.append(lines[i]); i += 1
            i += 1
            code = "\n".join(body).strip("\n")
            blocks.append(("code", guess_lang(code), code))
            continue
        m = re.match(r"@f\$\s*(.*?)\s*@f\$$", s)
        if m:
            flush(); blocks.append(("math", m.group(1).replace("{*}", "*"))); continue
        if s.startswith("<ul"):
            flush()
            chunk, depth = [], 0
            while True:
                chunk.append(s)
                depth += len(re.findall(r"<ul\b", s)) - len(re.findall(r"</ul>", s))
                if depth <= 0:
                    break
                s = lines[i].strip(); i += 1
            blocks.append(("tree", parse_html_list("\n".join(chunk))))
            continue
        if not s:
            flush(); continue
        m = re.match(r"@par\s+(.*)$", s)
        if m:
            flush(); para.append(m.group(1)); continue
        m = re.match(r"(?:@arg|@li|-)\s+(.*)$", s) or re.match(r"(@ref\s+\w+)\s*<br>$", s)
        if m:
            flush_para()
            items = items or []
            items.append(m.group(1)); continue
        if items is not None:          # continuation of a list item
            items[-1] += " " + s; continue
        para.append(s)
    flush()
    return blocks


def parse_html_list(src):
    """Parse a raw HTML <ul>/<li> block (where <li> is often left unclosed) into nested items."""
    root, lists = None, []
    for tok in re.split(r"(</?ul>|</?li>)", src):
        if tok == "<ul>":
            new = []
            if lists and lists[-1]:
                lists[-1][-1]["children"].append(new)
            elif root is None:
                root = new
            lists.append(new)
        elif tok == "</ul>":
            lists.pop()
        elif tok == "<li>":
            lists[-1].append({"text": "", "children": []})
        elif tok == "</li>":
            pass
        else:
            t = " ".join(tok.split())
            if t and lists and lists[-1]:
                lists[-1][-1]["text"] = (lists[-1][-1]["text"] + " " + t).strip()
    return root or []


def guess_lang(code):
    first = code.lstrip()
    if first.startswith("<") or (first.startswith("...") and "<" in code):
        return "xml"
    if first.startswith(("{", '"')):
        return "text"
    return "cpp"

# ---------------------------------------------------------------- inline markup

INLINE = re.compile(r'@ref\s+(\w+)(?:\s+"([^"]*)")?|@c\s+(\S+)|@e\s+(\S+)|\\([<>&])')


def ref_target(name, fmt, page):
    if name in TITLES:
        target_page = TITLES[name][0]
        if fmt == "md" and target_page != page:
            return f"{MD_FILE[target_page]}#{name}"
        return "#" + name
    UNRESOLVED.add(name)
    return OFFICIAL + name + ".html"


def clean_code(tok):
    tok = unescape(tok)
    if len(tok) > 1 and tok[0] == tok[-1] == "'":
        tok = tok[1:-1]
    return tok


def inline(text, fmt, page):
    out, pos = [], 0
    esc = html.escape if fmt == "html" else (lambda x: x)
    for m in INLINE.finditer(text):
        out.append(esc(text[pos:m.start()]))
        pos = m.end()
        ref, label, code, emph, ch = m.groups()
        if ref:
            url = ref_target(ref, fmt, page)
            if label is None:
                label = TITLES[ref][1] if ref in TITLES else EXTERNAL_TITLES.get(ref, ref)
            if fmt == "html":
                out.append(f'<a href="{url}">{html.escape(unescape(label))}</a>')
            else:
                out.append(f"[{label}]({url})")
        elif code:
            c = clean_code(code)
            out.append(f"<code>{html.escape(c)}</code>" if fmt == "html" else f"`{c}`")
        elif emph:
            out.append(f"<em>{esc(emph)}</em>" if fmt == "html" else f"*{emph}*")
        else:
            out.append(html.escape(ch) if fmt == "html" else "\\" + ch)
    out.append(esc(text[pos:]))
    return "".join(out)

# ---------------------------------------------------------------- Markdown

def md_tree(items, page, depth=0):
    lines = []
    for it in items:
        lines.append("  " * depth + "- " + inline(it["text"], "md", page))
        for sub in it["children"]:
            lines.extend(md_tree(sub, page, depth + 1))
    return lines


def to_markdown(blocks, page):
    md = []
    for b in blocks:
        if b[0] == "h":
            _, lvl, hid, title = b
            md.append(f'<a id="{hid}"></a>\n{"#" * lvl} {title}')
            if lvl == 1:
                md.append(f"> CEGUI 0.8.7 · Falagard skinning system · converted from "
                          f"[`{page}.dox`]({BLOB_URL}/{page}.dox) "
                          f"([original page]({OFFICIAL}{page}.html)). Text unchanged; format only.")
        elif b[0] == "p":
            md.append(inline(b[1], "md", page))
        elif b[0] == "ul":
            md.append("\n".join("- " + inline(it, "md", page) for it in b[1]))
        elif b[0] == "tree":
            md.append("\n".join(md_tree(b[1], page)))
        elif b[0] == "code":
            md.append(f"```{b[1]}\n{b[2]}\n```")
        elif b[0] == "math":
            md.append(f"```text\n{b[1]}\n```")
    md.append(LICENSE_MD)
    return "\n\n".join(md) + "\n"


LICENSE_MD = """---

Copyright (c) 2006 - 2011 Paul D Turner & The CEGUI Development Team

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2
or any later version published by the Free Software Foundation; with
no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in [GNU-FDL-1.2.md](GNU-FDL-1.2.md).

*Modified version:* converted from the Doxygen sources of CEGUI 0.8.7 to Markdown.
Only formatting was changed; the text is the original."""

# ---------------------------------------------------------------- HTML + highlighting

def span(cls, s):
    return f'<span class="{cls}">{html.escape(s)}</span>'


XML_TOK = re.compile(r'(<!--.*?-->)|(<\?.*?\?>)|(</?)([\w:.\-]+)|([\w:\-]+)(\s*=\s*)("[^"]*")|(/?>)', re.S)
CPP_TOK = re.compile(r'(//[^\n]*)|("[^"]*")|\b(void|const|enum|return|class|struct)\b|\b(CEGUI::\w+|UDim|UVector2|URect|Window|WindowManager|VerticalAlignment|HorizontalAlignment|Absolute|Relative)\b|\b(\d+(?:\.\d+)?f?)\b')


def highlight(code, lang):
    if lang == "text":
        return html.escape(code)
    out, pos = [], 0
    tok = XML_TOK if lang == "xml" else CPP_TOK
    for m in tok.finditer(code):
        out.append(html.escape(code[pos:m.start()]))
        pos = m.end()
        g = m.groups()
        if lang == "xml":
            if g[0]: out.append(span("c", g[0]))
            elif g[1]: out.append(span("p", g[1]))
            elif g[2]: out.append(span("pn", g[2]) + span("t", g[3]))
            elif g[4]: out.append(span("a", g[4]) + html.escape(g[5]) + span("s", g[6]))
            else: out.append(span("pn", g[7]))
        else:
            if g[0]: out.append(span("c", g[0]))
            elif g[1]: out.append(span("s", g[1]))
            elif g[2]: out.append(span("k", g[2]))
            elif g[3]: out.append(span("t", g[3]))
            else: out.append(span("n", g[4]))
    out.append(html.escape(code[pos:]))
    return "".join(out)


LANG_LABEL = {"xml": "XML", "cpp": "C++", "text": "Property string"}


def html_tree(items, page):
    out = ["<ul>"]
    for it in items:
        out.append(f"<li>{inline(it['text'], 'html', page)}")
        for sub in it["children"]:
            out.append(html_tree(sub, page))
        out.append("</li>")
    out.append("</ul>")
    return "".join(out)


def to_html(blocks, meta):
    page, _, group, num, total, toc_depth = meta
    out, toc = [], []
    for b in blocks:
        if b[0] == "h":
            _, lvl, hid, title = b
            text = html.escape(unescape(title))
            if lvl == 1:
                out.append(f'<header class="part-head" id="{hid}"><p class="eyebrow">{group} · {num} of {total}</p>'
                           f'<h1>{text}</h1>'
                           f'<p class="src">Source: <a href="{BLOB_URL}/{page}.dox"><code>{page}.dox</code></a> · '
                           f'<a href="{OFFICIAL}{page}.html">original page</a></p></header>')
                toc.append((1, hid, title))
            else:
                tag = f"h{lvl}"
                out.append(f'<{tag} id="{hid}"><a class="anchor" href="#{hid}" aria-label="Link to this section">#</a>{text}</{tag}>')
                if lvl <= toc_depth and title != "Section Contents":
                    toc.append((lvl, hid, title))
        elif b[0] == "p":
            out.append(f"<p>{inline(b[1], 'html', page)}</p>")
        elif b[0] == "ul":
            out.append("<ul>" + "".join(f"<li>{inline(it, 'html', page)}</li>" for it in b[1]) + "</ul>")
        elif b[0] == "tree":
            out.append(html_tree(b[1], page))
        elif b[0] == "code":
            lang = b[1]
            out.append(f'<figure class="code" data-lang="{lang}"><figcaption><span>{LANG_LABEL[lang]}</span>'
                       f'<button type="button" class="copy">Copy</button></figcaption>'
                       f'<pre><code>{highlight(b[2], lang)}</code></pre></figure>')
        elif b[0] == "math":
            out.append(f'<p class="formula"><code>{html.escape(b[1])}</code></p>')
    return "\n".join(out), toc


def nav_html(toc, group, num):
    page_entry, rest = toc[0], toc[1:]
    _, pid, ptitle = page_entry
    sub = "".join(
        f'<li class="n{lvl}"><a href="#{hid}">{html.escape(unescape(t))}</a></li>' for lvl, hid, t in rest)
    return (f'<li class="toc-part"><a class="part-link" href="#{pid}"><small>{group} {num}</small>'
            f'{html.escape(unescape(ptitle))}</a><ul>{sub}</ul></li>')


def main():
    parsed = {}
    for meta in PAGES:
        name = meta[0]
        parsed[name] = parse((SRC / f"{name}.dox").read_text(encoding="utf-8"))
        for b in parsed[name]:
            if b[0] == "h":
                TITLES[b[2]] = (name, b[3])

    parts_html, nav = [], []
    for meta in PAGES:
        name, md_name, group, num = meta[:4]
        (ROOT / md_name).write_text(to_markdown(parsed[name], name), encoding="utf-8")
        body, toc = to_html(parsed[name], meta)
        parts_html.append(f'<section class="part">{body}</section>')
        if group == "Reference" and num == 1:
            nav.append('<li class="group">Reference</li>')
        elif group == "Tutorial" and num == 1:
            nav.append('<li class="group">Tutorial</li>')
        nav.append(nav_html(toc, group, num))

    fdl = (SRC / "gnufdl.dox").read_text(encoding="utf-8")
    fdl = re.sub(r"^/\*\*\s*\n@page\s+\S+\s+[^\n]*\n", "", fdl).rstrip().removesuffix("*/").rstrip()
    (ROOT / "GNU-FDL-1.2.md").write_text("# GNU Free Documentation License\n\n```text\n" + fdl.strip("\n") + "\n```\n", encoding="utf-8")

    template = (Path(__file__).parent / "template.html").read_text(encoding="utf-8")
    page = (template.replace("{{NAV}}", "\n".join(nav))
                    .replace("{{CONTENT}}", "\n".join(parts_html))
                    .replace("{{FDL}}", html.escape(fdl.strip("\n"))))
    # Fragment for the Claude artifact (the host wraps it in its own document)
    (ROOT / "falagard-docs.html").write_text(page, encoding="utf-8")
    # Standalone document for GitHub Pages
    head, body = page.split("</style>", 1)
    standalone = ('<!doctype html>\n<html lang="en">\n<head>\n' + head
                  + "body { margin: 0; }\n</style>\n</head>\n<body>\n" + body.strip() + "\n</body>\n</html>\n")
    (ROOT / "index.html").write_text(standalone, encoding="utf-8")
    print("ok; unresolved refs:", sorted(UNRESOLVED) or "none")


if __name__ == "__main__":
    main()
