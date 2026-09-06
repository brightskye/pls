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
| Where are the installer checks? | [Tests](tests/test_pls_skill.py) |
| Under what terms may PLS be used? | [MIT License](LICENSE) |

## Distribution

The self-contained `src/pls/` directory can be installed from a Git
repository without access to the rest of this checkout. It contains the skill
entry point and the authoritative PLS standard. Pin an immutable commit or
release tag when reproducible rules matter; use `main` only when deliberately
following the working draft.

Use `npx skills` for installation and updates through the existing Node.js
skill manager, or download the standalone [Python tool](tools/pls_skill.py)
for the same PLS package without Node.js or extra Python packages. Both install
the skill and its rules together. No build step is needed. See
[Operations](docs/operations.md) for commands, update behavior, and publication
status.

## License

PLS is available under the [MIT License](LICENSE).

## Current state

The structure-first PLS v0.3 text is a working draft. It covers the main
project layout as well as its documentation. It has not been promoted to a
stable release.
