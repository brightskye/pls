# Project Layout Standard

Project layout standard: PLS 0.3 working draft

Project key: `pls`

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
companion design-writing guide and skill. PLS governs project layout and
retrievable discussion and decision records; the companion guides readable,
precise system design. Adopting projects own their documentation,
implementation, and adoption decisions.

## Project map

| Question | Location |
|---|---|
| What rules does PLS define? | [PLS](src/pls/references/PLS.md) |
| How are discussions, decisions, and changed decisions saved and retrieved? | [Project Journal standard](src/pls/references/journal.md) |
| What project-specific rules must agents follow here? | [Agent instructions](AGENTS.md) |
| What is happening with the PLS project? | [Project Journal](docs/journal.md) |
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
The published `v0.3.0-draft.3` bundle described here contains the PLS skill and
the companion design-writing skill.

The complete bundle includes both skills, their rules and guides, the Python
installer, instructions, license, and release metadata. Extract it and run its
`install.py` from the target project. The
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

The published `v0.3.0-draft.3` bundle includes this companion beside
`skills/pls/`. The shared installer selects one skill per operation, so a user
who wants both runs two install commands. The two skills are independently
selectable, and the companion does not change the PLS standard or its version.

## License

PLS is available under the [MIT License](LICENSE).

## Current state

The structure-first PLS v0.3 text is a working draft. The published
[`v0.3.0-draft.3`](https://github.com/brightskye/pls/releases/tag/v0.3.0-draft.3)
bundle is the latest verified release and contains two independently
selectable skills with their shared Python installer and per-skill updater.
The standard remains the PLS 0.3.0 working draft and has not been promoted to
a stable release. See the [Project Journal](docs/journal.md) for release
verification and limitations.

The source now includes an unpublished
[Project Journal standard](src/pls/references/journal.md) and matching PLS
skill routes. The Journal name, retained history, growth rules, and selective
reading direction are accepted. Detailed metadata and workflow remain a
working draft. The `0.3.0-draft.4` candidate has passed release review;
[verification and remaining publication work](docs/journal.md#draft4-release-preparation)
are recorded in the Journal. The published draft3 bundle and installed
copies do not yet contain this revision.

Projects may declare a disposable working context and session handoff
location in their project map. This project uses the default
`.local/agent-note/`; no override is configured. Its temporary, ignored,
non-authoritative role is unchanged.

The normal location is `docs/journal.md` or an expanded `docs/journal/`.
This repository now uses [its Journal](docs/journal.md), migrated from the
former Project Record with record IDs and history preserved. Other projects
retain their own mapped locations until they choose to migrate.
