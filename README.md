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
| What rules does PLS define? | [PLS](deploy/pls/references/PLS.md) |
| What project-specific rules must agents follow here? | [Agent instructions](AGENTS.md) |
| What is happening with the PLS project? | [Project Record](docs/project-record.md) |
| How do I install and use the PLS agent skill? | [Operations](docs/operations.md) |
| What can be installed or distributed from this project? | `deploy/` |
| Where is the deployable agent skill? | [PLS agent skill](deploy/pls/SKILL.md) |
| Under what terms may PLS be used? | [MIT License](LICENSE) |

## Distribution

The self-contained `deploy/pls/` directory can be installed from a Git
repository without access to the rest of this checkout. It contains the skill
entry point and the authoritative PLS standard. Pin an immutable commit or
release tag when reproducible rules matter; use `main` only when deliberately
following the working draft. See [Operations](docs/operations.md) for install
and update routes.

## License

PLS is available under the [MIT License](LICENSE).

## Current state

The structure-first PLS v0.3 text is a working draft. It covers the main
project layout as well as its documentation. It has not been promoted to a
stable release.
