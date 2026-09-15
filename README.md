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

This repository owns the PLS standard, its distributable agent skill, and a
companion design-writing guide and skill. PLS governs project layout; the
companion guides readable, precise system design. Adopting projects own their
documentation, implementation, and adoption decisions.

## Project map

| Question | Location |
|---|---|
| What rules does PLS define? | [PLS](src/pls/references/PLS.md) |
| What project-specific rules must agents follow here? | [Agent instructions](AGENTS.md) |
| What is happening with the PLS project? | [Project Record](docs/project-record.md) |
| How do I install and use the PLS agent skill? | [Operations](docs/operations.md) |
| Where is the maintained PLS package? | [PLS agent skill](src/pls/SKILL.md) |
| How should system design documents be written? | [Design writing guide](src/design-writing/references/design-writing.md) |
| Which skill creates, revises, or reviews a design? | [Design writing skill](src/design-writing/SKILL.md) |
| Where is the Python install/update tool? | [Installer](tools/pls_skill.py) |
| Where are the complete release bundles? | [GitHub Releases](https://github.com/brightskye/pls/releases), built under ignored `releases/<version>/` |
| How are the bundles built? | [Builder](tools/build_release.py) and [release workflow](.github/workflows/release.yml) |
| Where are the installer and bundle checks? | `tests/` |
| Under what terms may PLS be used? | [MIT License](LICENSE) |

## Distribution

Download `pls.zip` from [GitHub Releases](https://github.com/brightskye/pls/releases).
The upcoming `v0.3.0-draft.3` bundle described here is prepared but unpublished;
the published `v0.3.0-draft.2` contains only the PLS skill.

The new complete bundle includes the PLS skill, the companion design-writing skill,
their rules and guides, the Python installer, instructions, license, and release
metadata. Extract it and run its `install.py` from the target project. The
shared Python installer selects one skill per operation: PLS is the default and
`--skill design-writing` selects the companion. Each selected skill is kept with
its own updater and receipt in `<skills_parent>/<skill>/`; install both with two
commands. Installation uses the bundled files without a development checkout or
network access; the extracted bundle is no longer needed after installation.
Later updates download release bundles, not the source tree.

The Python route requires Python 3.10 or newer and no extra packages. `npx`
can install a release ZIP, but the checked `skills` CLI does not track archive
installs for `update`; rerun `add` with the selected new bundle instead.

The maintained skills stay in `src/pls/` and `src/design-writing/`; installer
and builder sources stay in `tools/`. See [Operations](docs/operations.md) for
installation, updates, development routes, migration, and publication status.

## Design writing

The [design-writing skill](src/design-writing/SKILL.md) uses a bundled,
standalone [writing guide](src/design-writing/references/design-writing.md).
It supports human and agent readers, with Orca as an example, and works with
the adopting project's documentation layout. The source is self-contained in
`src/design-writing/`; it does not require the PLS skill or an Orca checkout.

The planned `v0.3.0-draft.3` bundle includes this companion beside
`skills/pls/`. The shared installer selects one skill per operation, so a user
who wants both runs two install commands. The companion does not change the
PLS standard or its version. Draft3 preparation is pending commit and
publication; the latest verified remote bundle remains draft2.

## License

PLS is available under the [MIT License](LICENSE).

## Current state

The structure-first PLS v0.3 text is a working draft. The published
[`v0.3.0-draft.2`](https://github.com/brightskye/pls/releases/tag/v0.3.0-draft.2)
bundle has a verified single-folder Python installation and updater. The
`v0.3.0-draft.3` bundle is prepared for commit and publication with both
selectable skills; it is not yet a live release. The standard covers the main
project layout as well as its documentation and has not been promoted to a
stable release.
