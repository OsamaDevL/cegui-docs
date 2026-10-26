# CEGUI 0.8.7 Docs, Reformatted

**Read it here: https://osamadevl.github.io/cegui-docs/**

An unofficial, easier-to-read rebuild of the [CEGUI 0.8.7 documentation](https://static.cegui.org.uk/docs/0.8.7/):
every guide, tutorial and XML format page, plus the full API reference.
It's built from CEGUI's own sources with the same tool the original used (Doxygen), and a modern theme
([doxygen-awesome-css](https://github.com/jothepro/doxygen-awesome-css)). The theme adds a cleaner layout, dark mode,
copy buttons on code, and an on-page contents list.

This is not an official CEGUI project site.

**Page names match the official site,** so official page links work here by swapping the host. For example:
`https://static.cegui.org.uk/docs/0.8.7/fal_intro.html` → `https://osamadevl.github.io/cegui-docs/fal_intro.html`.

There is also a hand-made single page for the Falagard skinning tutorial and reference:
**https://osamadevl.github.io/cegui-docs/falagard/** (sources and Markdown in [`falagard/`](falagard/)).

## How it's built

[`.github/workflows/docs.yml`](.github/workflows/docs.yml) runs on every push to `main`:

1. Checks out CEGUI at tag [`v0-8-7`](https://github.com/cegui/cegui/tree/v0-8-7) and the theme at `v2.5.0`.
2. Runs [`docs-config/build.sh`](docs-config/build.sh). It takes CEGUI's own `doc/doxygen/doxyfile.in`,
   applies [`docs-config/Doxyfile.overrides`](docs-config/Doxyfile.overrides) (theme and paths), and runs Doxygen.
3. Publishes the result to GitHub Pages.

To build locally (needs Doxygen and Graphviz):

```bash
git clone --depth 1 --branch v0-8-7 https://github.com/cegui/cegui.git cegui
git clone --depth 1 --branch v2.5.0 https://github.com/jothepro/doxygen-awesome-css.git theme
bash docs-config/build.sh   # output in _build/html
```

## License

- **CEGUI code and the API reference** generated from its source comments: MIT License,
  Copyright (C) 2004 - 2012 Paul D Turner & The CEGUI Development Team. See CEGUI's
  [COPYING](https://github.com/cegui/cegui/blob/v0-8-7/COPYING) file.
- **Falagard skinning manual** (the `fal_*` pages and the [`falagard/`](falagard/) folder): GNU Free Documentation
  License 1.2 or later, Copyright (c) 2006 - 2011 Paul D Turner & The CEGUI Development Team, with no Invariant Sections,
  no Front-Cover Texts and no Back-Cover Texts. See [falagard/GNU-FDL-1.2.md](falagard/GNU-FDL-1.2.md).
  This copy is modified: only the formatting changed.
- **Theme:** doxygen-awesome-css, MIT License.
- The build scripts in this repo are offered under the MIT License.
