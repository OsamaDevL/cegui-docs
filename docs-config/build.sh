#!/usr/bin/env bash
# Build the full CEGUI 0.8.7 docs with Doxygen + doxygen-awesome-css.
# Expects (relative to the repo root, where this runs):
#   cegui/  - checkout of github.com/cegui/cegui at tag v0-8-7
#   theme/  - checkout of github.com/jothepro/doxygen-awesome-css at a release tag
# Output: _build/html
set -euo pipefail

mkdir -p _build

# 1. CEGUI's own Doxyfile template, with its CMake placeholders filled in, plus our overrides
sed -e 's#\${PROJECT_SOURCE_DIR}#cegui#g' \
    -e 's#\${CEGUI_VERSION}#0.8.7#g' \
    cegui/doc/doxygen/doxyfile.in > _build/Doxyfile
cat docs-config/Doxyfile.overrides >> _build/Doxyfile

# 2. Doxygen's default page header, with the theme's scripts added
doxygen -w html _build/header.html _build/footer.html _build/default.css _build/Doxyfile
python3 - <<'EOF'
from pathlib import Path
p = Path("_build/header.html")
s = p.read_text(encoding="utf-8")
scripts = """<script type="text/javascript" src="$relpath^doxygen-awesome-darkmode-toggle.js"></script>
<script type="text/javascript" src="$relpath^doxygen-awesome-fragment-copy-button.js"></script>
<script type="text/javascript" src="$relpath^doxygen-awesome-paragraph-link.js"></script>
<script type="text/javascript" src="$relpath^doxygen-awesome-interactive-toc.js"></script>
<script type="text/javascript">
  DoxygenAwesomeDarkModeToggle.init();
  DoxygenAwesomeFragmentCopyButton.init();
  DoxygenAwesomeParagraphLink.init();
  DoxygenAwesomeInteractiveToc.init();
</script>
</head>"""
assert "</head>" in s
p.write_text(s.replace("</head>", scripts, 1), encoding="utf-8")
EOF
echo "HTML_HEADER = _build/header.html" >> _build/Doxyfile

# 3. Run Doxygen
doxygen _build/Doxyfile

# 4. Add the hand-made Falagard page alongside
mkdir -p _build/html/falagard
cp falagard/index.html _build/html/falagard/index.html
touch _build/html/.nojekyll

echo "Doxygen warnings: $(grep -c . _build/warnings.log || true)"
echo "HTML files: $(find _build/html -name '*.html' | wc -l)"
