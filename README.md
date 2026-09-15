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

This repository maintains three independent guides and skills: PLS for project
layout, Journal for retrievable discussion and decision history, and
design-writing for precise system designs. Each skill works with its own
bundled guide. Adopting projects own their documents, implementation, storage
locations, and adoption decisions.

## Project map

| Question | Location |
|---|---|
| What rules does PLS define? | [PLS](src/pls/references/PLS.md) |
| How are discussions, decisions, and changed decisions saved and retrieved? | [Project Journal standard](src/journal/references/journal.md) |
| What project-specific rules must agents follow here? | [Agent instructions](AGENTS.md) |
| What is happening with the PLS project? | [Project Journal](docs/journal.md) |
| How do I install and use the skills? | [Operations](docs/operations.md) |
| Where is the maintained PLS package? | [PLS agent skill](src/pls/SKILL.md) |
| Which skill records or retrieves project history? | [Journal skill](src/journal/SKILL.md) |
| How should system design documents be written? | [Design writing guide](src/design-writing/references/design-writing.md) |
| Which skill creates, revises, or reviews a design? | [Design writing skill](src/design-writing/SKILL.md) |
| Where is the Python install/update tool? | [Installer](tools/pls_skill.py) |
| Where are the complete release bundles? | [GitHub Releases](https://github.com/brightskye/pls/releases), built under ignored `releases/<version>/` |
| How are the bundles built? | [Builder](tools/build_release.py) and [release workflow](.github/workflows/release.yml) |
| Where are the installer and bundle checks? | `tests/` |
| Under what terms may PLS be used? | [MIT License](LICENSE) |

## Distribution

The next bundle, `0.3.0-draft.5`, separates Journal from the PLS layout skill.
The currently published
[`v0.3.0-draft.4`](https://github.com/brightskye/pls/releases/tag/v0.3.0-draft.4)
still bundles Journal rules inside PLS. The source revision contains three
independently selectable skills:

| Skill | Responsibility | Install selection |
|---|---|---|
| `pls` | Layout, placement, navigation, and document ownership | Default |
| `journal` | Discussion and decision records, history, and retrieval | `--skill journal` |
| `design-writing` | System design documents and implementation readiness | `--skill design-writing` |

The complete bundle includes the guides, Python installer, instructions,
license, and release metadata. Each selected skill keeps its own updater and
receipt in `<skills_parent>/<skill>/`. Install each wanted skill explicitly;
updating PLS does not install Journal or move project records.

Python 3.10 or newer is required, with no extra packages. Installation uses the
extracted bundle offline; later updates download release bundles. The source
packages stay in `src/`, and installer and builder sources stay in `tools/`.
See [Operations](docs/operations.md) for installation, upgrades from draft4,
alternative routes, and publication status.

## Design writing

The [design-writing skill](src/design-writing/SKILL.md) uses a bundled,
standalone [writing guide](src/design-writing/references/design-writing.md).
It supports human and agent readers, with Orca as an example, and works with
the adopting project's documentation layout. The source is self-contained in
`src/design-writing/`; it does not require the PLS skill or an Orca checkout.

The design-writing companion remains independently selectable. Installing
Journal or PLS does not install it or change its guide.

## License

PLS is available under the [MIT License](LICENSE).

## Current state

PLS remains the 0.3.0 working draft. Journal's
[separate ownership](docs/journal.md#dec-0007-separate-journal-from-layout-rules)
is accepted: PLS defines placement, the Journal guide defines shared record
semantics, and saving systems own their execution paths. Orca can adopt a
versioned copy while keeping its integration rules in configured vault
locations. Agent adapters follow the selected system's interface.

The `0.3.0-draft.5` source revision implements the package separation. The
latest published bundle is draft4 until draft5 publication is verified.
[Current](docs/journal.md#current) records verification, release, and adoption
status. Existing record locations remain in place; native Windows is untested.

Projects may declare a disposable working context and session handoff
location in their project map. This project uses the default
`.local/agent-note/`; no override is configured. Its temporary, ignored,
non-authoritative role is unchanged.

The normal location is `docs/journal.md` or an expanded `docs/journal/`.
This repository now uses [its Journal](docs/journal.md), migrated from the
former Project Record with record IDs and history preserved. Other projects
retain their own mapped locations until they choose to migrate.
