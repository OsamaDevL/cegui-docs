# CEGUI Falagard Docs, Reformatted

**Read it here: https://osamadevl.github.io/cegui-falagard-docs/**

An unofficial, easier-to-read copy of the Falagard skinning pages from the
[CEGUI 0.8.7 documentation](https://static.cegui.org.uk/docs/0.8.7/). It covers the two tutorial pages and the four reference pages.
The text is the original. Only the layout changed: a contents sidebar, highlighted XML and C++, copy buttons,
dark mode and a phone layout.

This is not an official CEGUI project page.

## Pages

| # | Page | Markdown | Original |
|---|------|----------|----------|
| 1 | Introduction and overview | [falagard-1-introduction.md](falagard-1-introduction.md) | [fal_intro](https://static.cegui.org.uk/docs/0.8.7/fal_intro.html) |
| 2 | Introduction to Falagard 'looknfeel' XML | [falagard-2-looknfeel-xml.md](falagard-2-looknfeel-xml.md) | [fal_tut1](https://static.cegui.org.uk/docs/0.8.7/fal_tut1.html) |
| 3 | Falagard XML Element Reference | [falagard-3-element-reference.md](falagard-3-element-reference.md) | [fal_element_ref](https://static.cegui.org.uk/docs/0.8.7/fal_element_ref.html) |
| 4 | Falagard XML Enumeration Reference | [falagard-4-enumeration-reference.md](falagard-4-enumeration-reference.md) | [fal_enum_ref](https://static.cegui.org.uk/docs/0.8.7/fal_enum_ref.html) |
| 5 | CEGUI Widget Base Type Requirements | [falagard-5-base-type-requirements.md](falagard-5-base-type-requirements.md) | [fal_baseclass_ref](https://static.cegui.org.uk/docs/0.8.7/fal_baseclass_ref.html) |
| 6 | Falagard Window Renderer Requirements | [falagard-6-window-renderer-requirements.md](falagard-6-window-renderer-requirements.md) | [fal_wr_ref](https://static.cegui.org.uk/docs/0.8.7/fal_wr_ref.html) |

## How it's built

The pages are generated from CEGUI's own Doxygen sources at tag
[`v0-8-7`](https://github.com/cegui/cegui/tree/v0-8-7/doc/doxygen/falagard), saved in [`source/`](source/).
To rebuild `index.html` and the Markdown files (Python 3.9+, no extra packages):

```bash
python tools/convert.py .
```

[`tools/convert.py`](tools/convert.py) does the conversion and [`tools/template.html`](tools/template.html) holds the page layout.

## License

Copyright (c) 2006 - 2011 Paul D Turner & The CEGUI Development Team

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2
or any later version published by the Free Software Foundation; with
no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in [GNU-FDL-1.2.md](GNU-FDL-1.2.md).

This is a modified version: the documentation was converted from Doxygen to Markdown and HTML. Only formatting was changed.
