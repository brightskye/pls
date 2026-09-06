# Project Layout Standard

Project layout standard: PLS 0.3 working draft

PLS defines a small, predictable project layout for people and AI agents.
It explains what each main area is for, where documents and supporting
artifacts belong, and how to avoid unnecessary folders and process clutter.

## Goals

- Make projects easy for people to explore and understand.
- Give agents clear placement rules for documents and supporting artifacts.
- Keep the structure small enough that projects will use it.
- Respect familiar language, framework, and tool conventions.
- Add folders, files, tools, and verification records only when they provide
  real value.

## Scope

This repository owns the PLS standard and its distributable agent skill. It
does not own the documentation, implementation, or adoption decisions of
projects that use PLS.

## Project map

| Question | Location |
|---|---|
| What rules does PLS define? | [PLS](src/pls/references/PLS.md) |
| What project-specific rules must agents follow here? | [Agent instructions](AGENTS.md) |
| What is happening with the PLS project? | [Project Record](docs/project-record.md) |
| How do I install and use the PLS agent skill? | [Operations](docs/operations.md) |
| Where is the maintained product package? | [PLS agent skill](src/pls/SKILL.md) |
| Where is the Python install/update tool? | [Installer](tools/pls_skill.py) |
| Where are the complete release bundles? | [GitHub Releases](https://github.com/brightskye/pls/releases), built under ignored `releases/<version>/` |
| How are the bundles built? | [Builder](tools/build_release.py) and [release workflow](.github/workflows/release.yml) |
| Where are the installer and bundle checks? | `tests/` |
| Under what terms may PLS be used? | [MIT License](LICENSE) |

## Distribution

Download `pls.zip` from [GitHub Releases](https://github.com/brightskye/pls/releases).
The complete bundle includes the skill, rules, Python installer, instructions,
license, and release metadata. Extract it and run its `install.py` from the
target project. The Python installer then keeps the skill, rules, updater,
instructions, metadata, and license together in `.agents/skills/pls/`.
Installation uses the bundled files without a development checkout or network
access; the extracted bundle is no longer needed after installation. Later
updates download release bundles, not the source tree.

The Python route requires Python 3.10 or newer and no extra packages. `npx`
can install a release ZIP, but the checked `skills` CLI does not track archive
installs for `update`; rerun `add` with the selected new bundle instead.

The maintained skill stays in `src/pls/`; installer and builder sources stay
in `tools/`. See [Operations](docs/operations.md) for installation, updates,
development routes, migration, and publication status.

## License

PLS is available under the [MIT License](LICENSE).

## Current state

The structure-first PLS v0.3 text is a working draft. The published
`v0.3.0-draft.1` bundle remains the current public release; `0.3.0-draft.2`
is being prepared and is not yet published or a verified release. The draft
covers the main project layout as well as its documentation and has not been
promoted to a stable release.
