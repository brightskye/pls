# Project map

Documentation root: `docs/`.

A relative documentation root starts at the project root; an absolute root is
used as written.

`Project` means the directory containing the project's root README.
`Documentation` means the documentation root declared above. `Absolute` means
that the location is a complete filesystem path, with no base added.

| Area | Base | Location |
|---|---|---|
| Source | Project | `src/` |
| Tests | Project | `tests/` |
| Configuration | Project | `config/` |
| Tools | Project | `tools/` |
| Assets | Project | `assets/` |
| Releases | Project | `releases/` |
| Legacy | Project | `legacy/` |
| Local-only material | Project | `.local/` |
| Disposable working context and session handoffs | Project | `.local/agent-note/` |
| Project Journal | Documentation | `journal.md` |
| Architecture | Documentation | `architecture.md` |
| Specifications | Documentation | `specifications.md` |
| Quality | Documentation | `quality.md` |
| Operations | Documentation | `operations.md` |
| User guidance | Documentation | `user.md` |

These are starting locations. Keep only the areas this project needs, replace
rows with existing owners or tool conventions, and add navigation links to
actual entry points using normal Markdown link paths. A map does not require
empty folders or documents. The root README remains the project entry point;
agent instruction files use their host's required location.
