---
id: PLS
short_name: PLS
title: Project Layout Standard
version: 0.3.0
status: working
authority: working
owner: victor
updated: 2026-09-04
---

# Project Layout Standard (PLS) v0.3 — structure-first draft

> This is the current working standard, not a stable release.

## 1. Purpose

PLS gives people and AI agents a predictable way to explore and maintain a
project.

It defines:

- the normal top-level areas of a project;
- the purpose of each area;
- the normal location of project documents and supporting artifacts; and
- a small set of rules for creating, placing, and updating them.

PLS is a set of written rules. It is not a program, project manager, software
framework, build system, test system, or approval process.

PLS does not replace the conventions of a programming language, framework, or
tool. Those conventions control the internal layout and format of source code,
tests, agent skills, deployment packages, and other technical artifacts. PLS
controls how the main project areas are named or mapped so that people and
agents can find them.

The desired result is simple: a person understands the layout, and an agent
places each document or artifact where that person expects to find it.

## 2. Rule words

- **MUST** and **MUST NOT** are required.
- **SHOULD** and **SHOULD NOT** describe the normal choice.
- **MAY** means optional.

Only the uppercase words above create PLS requirements.

## 3. Human and agent responsibilities

The project Owner or Maintainer decides which project areas are needed. They
may use the default PLS names, explicitly chosen existing names, or names
required by the project's language, framework, or tools. Mapping an existing
name is a deliberate project choice, not the default meaning of adopting PLS.

An AI agent MAY recommend or create the initial structure when a human asks it
to set up a project. The human remains responsible for accepting important
structure and ownership decisions.

After setup, an agent MUST follow the locations recorded in the root
`README.md` or its directly linked project map. It MUST NOT silently reorganize
the project or change which location owns important information.

PLS makes human and agent decisions more consistent. It cannot guarantee that
every judgment will be correct.

## 4. The project entry point

Every project MUST have a root `README.md`. It is the first file for people and
agents exploring the project.

The `README.md` MUST explain:

- what the project is;
- why it exists;
- what it must achieve;
- what is inside and outside its scope;
- any important constraints;
- where its main areas are located; and
- where its current state can be found.

When details make the README difficult to use, the project MAY move them into
linked documents. The README MUST retain a short summary and direct links.

The project map SHOULD be in the root README. A large project MAY keep a more
detailed map in `docs/README.md` when the root README links to it directly.

The map can be a short list or table:

```markdown
Project layout standard: PLS 0.3

## Project map

| Question | Location |
|---|---|
| What is true now and what happens next? | [Project Record](docs/project-record.md) |
| Where is the product implemented? | `src/` |
| Where are repeatable checks? | `tests/` |
| What can be installed or distributed? | `deploy/` |
```

A project claiming that it follows PLS v0.3 MUST state that in the README. No
separate profile, module list, or declaration is required.

## 5. Default project structure

A new project SHOULD start with only the locations it needs. The following
layout provides normal PLS names:

```text
README.md
AGENTS.md                 # when AI agents regularly work on the project
src/                      # or the source layout expected by the project's tools
tests/                    # repeatable checks
config/                   # safe project configuration and examples
docs/
  project-record.md       # current state, plans, decisions, and history
  architecture.md         # overall solution structure
  specifications.md       # exact behavior and contracts
  quality.md              # verification approach and important results
  operations.md           # installation and operation
  user.md                 # supported user guidance
deploy/                   # deployable packages and installation options
tools/                    # maintained project tools; scripts/ is also familiar
assets/                   # project-owned non-source assets
legacy/                   # inactive material kept for history or migration
.local/                   # ignored local-only working or sensitive artifacts
```

Except for the root README, every location above is optional. A project MUST
NOT create an empty file or directory merely to resemble this layout.

An existing location or one normally used by the project's language,
framework, or tools MAY replace a default name. For example, source may live in
`app/`, `packages/`, or the project root. The project map MUST point to the real
location.

A project SHOULD create a new top-level area only when the area has a clear,
lasting purpose and no suitable existing location.

## 6. What each project area is for

| Area | Question it answers | Normal location |
|---|---|---|
| Entry point | What is this project and where do I start? | `README.md` |
| Agent instructions | What project-specific rules must an agent follow? | `AGENTS.md` or host-equivalent |
| Source | Where is the product implemented? | `src/` or the usual location for the project's tools |
| Tests | Where are repeatable checks with expected results? | `tests/` or the usual location for the project's tools |
| Configuration | Where are safe project settings and examples? | `config/` or the usual location for the project's tools |
| Documentation | Where is the project explained and managed? | `docs/` |
| Deployment | What packages or integrations can be installed, distributed, or launched? | `deploy/` |
| Tools | Where is maintained project automation? | `tools/` or `scripts/` |
| Assets | Where are project-owned non-source assets? | `assets/` or the usual location for the project's tools |
| Legacy | What inactive material is retained for history or migration? | `legacy/` |
| Local-only | Where may temporary, machine-local, or sensitive artifacts be kept outside version control? | `.local/` when the project's tools do not specify a location |

The normal locations are defaults, not forced names. A project follows PLS
when its actual layout is clear and mapped, even when its language, framework,
or tools use different names.

### 6.1 Source, tests, and configuration

Use the layout expected by the project's language, framework, and tools inside
these areas. PLS does not define package names, test file formats, or framework
folders.

Code placed in Source MUST form part of the delivered product or a supported
runtime capability. Code used only to build, test, evaluate, inspect, or
maintain the project MUST instead use Tests, Tools, or Deployment according to
its purpose. Import convenience alone does not make supporting code product
source. A language, framework, build, or packaging convention MAY require
another arrangement.

Tests contain repeatable checks with expected results. One-time experiments
and temporary agent checks do not become project tests unless the project
chooses to maintain and repeat them.

Configuration files and safe examples belong in the location expected by the
project. Configuration meaning belongs in Specifications. Configuration
procedures belong in Operations. Secrets and machine-specific private values
MUST NOT be committed merely to make configuration easier to explain.

### 6.2 Documentation

The `docs/` area explains and manages the project. These question-based
locations are the normal starting point:

| Documentation area | Question it answers | Normal location |
|---|---|---|
| Project Record | What happened, what is true now, what comes next, and why were important choices made? | `docs/project-record.md` |
| Architecture | How is the solution organized? | `docs/architecture.md` |
| Specifications | Exactly how must something behave? | `docs/specifications.md` |
| Quality | How do we check that it works well enough? | `docs/quality.md` |
| Operations | How do we install, run, diagnose, and recover it? | `docs/operations.md` |
| User guidance | How does a supported user use it? | `docs/user.md` |

Create only the areas that contain useful information. Existing projects MAY
keep familiar document names when a human chooses a mapped alternative or the
project's tools make the existing name useful.

When one documentation area becomes too large for one file, replace
`docs/<area>.md` with:

```text
docs/<area>/
  README.md
  <focused-detail>.md
```

The area's `README.md` becomes its entry point and links to the detailed files.

### 6.3 Deployment

The `deploy/` area contains technical artifacts that people or tools use to
install, distribute, integrate, or launch the project. Each deployment option
SHOULD have a focused subdirectory when it contains more than one file.

Examples include:

```text
deploy/
  skill/                    # an installable agent skill
  container/                # container deployment files
  systemd/                  # service unit and related files
```

These examples do not require a project to create every option or use these
exact names.

A deployable package may need its own internal root files or folders. The
standard for that package type controls its internal layout. PLS controls why
the package is under `deploy/` and how the project links to it.

Deployment instructions belong in `docs/operations.md` or another mapped
Operations document. The deployable files themselves belong in `deploy/` or a
location normally used by the project's deployment tool.

### 6.4 Tools and assets

The `tools/` or `scripts/` area contains automation that the project expects to
maintain and use again. A project SHOULD NOT add a permanent script for a
one-time check when a direct command or an existing tool is sufficient.

The `assets/` area contains project-owned files that are neither source code
nor ordinary documentation, such as images, templates, or sample media. Use a
location expected by the project's tools when one already exists.

### 6.5 Legacy, local-only, and temporary material

Content under `legacy/` MUST be clearly identified as noncurrent. People and
agents SHOULD exclude it from normal project reading unless their task concerns
history or migration.

A project SHOULD NOT use a permanent `misc/` directory as a dumping ground.
Place durable material according to its purpose. Temporary agent output SHOULD
normally stay outside the tracked project.

When temporary, machine-local, or sensitive artifacts need a location inside
the project workspace and no project tool normally controls that location, the
project SHOULD use `.local/`. It MUST be ignored by version control and MUST NOT
own requirements, current state, design, operating procedures, maintained test
cases, or other information needed to understand or use the project. Existing
tool-defined local locations MAY remain.

Create `.local/` only when material actually needs it. It is a placement
boundary, not a general dumping ground or permission to retain generated
output.

## 7. Documentation rules

### 7.1 Project Record

The Project Record combines information that explains the project across time.
Use these sections when they contain useful information:

```markdown
## Current
What exists, works, is incomplete, or is blocked now.

## Next
Planned work and expected outcomes.

## Proposals
Ideas under consideration that are not yet accepted.

## Decisions
Important choices, their reasons, and whether they still apply.

## History
Completed work, replaced plans, and superseded decisions.
```

Large plans, decision records, proposals, or historical records MAY use
separate files. The Project Record MUST remain their normal entry point.

The project's Current information MUST describe what is actually implemented
or available. It MUST NOT present a plan, specification, or unverified agent
statement as proof that something works. Record a known difference between
intended and actual behavior in Current until it is resolved.

A decision record owns the reason for a choice. The resulting current design
or behavior belongs in Architecture or Specifications. A reader MUST NOT need
to reconstruct the current design from old decisions.

### 7.2 Architecture and Specifications

Use this placement test:

1. If information explains a goal or obligation that remains true when the
   implementation is replaced, put it in the README or linked project details.
2. If it explains components, responsibilities, boundaries, dependencies, or
   flows, put it in Architecture.
3. If an implementer or tester needs exact details, put it in Specifications.

Architecture describes the overall solution. Specifications describe exact
interfaces, schemas, formats, state changes, validation rules, and required
behavior.

### 7.3 Cross-cutting subjects

Security, privacy, data, reliability, and compatibility do not automatically
need separate folders. Place each piece according to the question it answers:

- overall boundaries and system shape belong in Architecture;
- exact requirements and behavior belong in Specifications;
- verification belongs in Quality; and
- operating procedures belong in Operations.

Split out a focused document only when that makes the project easier to use.

### 7.4 Evaluations and evidence

Evaluation methods, acceptance thresholds, and important retained results
belong to Quality.

Executable evaluation cases and code used only to run or score them SHOULD use
the project's existing test layout, such as `tests/evals/`, rather than product
source or a root `evals/` directory.

Evaluation and test output is temporary by default. Running a check does not
authorize an agent to create a permanent evidence structure or retain its
output merely because it might be useful. Temporary machine-local or sensitive
output that must remain in the workspace SHOULD use `.local/` unless the
project's tools specify another location.

When important results must be retained, their meaning and conclusion belong
to Quality. Safe retained artifacts MAY live in an expanded Quality area, such
as `docs/quality/evidence/`, or in an appropriate external system linked from
Quality. Sensitive artifacts MAY live in `.local/evidence/` only when the human
explicitly chooses to retain them; Quality MUST link to that boundary without
exposing private content. Maintained evaluation cases MUST NOT live in
`.local/`. A root `evidence/` directory is not a PLS default.

An agent's backup idea is not evidence. If the idea is useful to the project,
put it under Proposals in the Project Record. Otherwise, keep it as temporary
working material outside the tracked project.

## 8. Ownership and navigation

Each important subject MUST have one location that owns its full current
meaning.

Another location MAY summarize the subject, but it MUST link to the owner and
MUST NOT maintain a second independent definition.

An artifact and its explanation may both be needed. For example, a deployment
file belongs in `deploy/`, while Operations explains how and when to use it.
The project map or Operations document SHOULD link to the artifact instead of
copying its technical content.

Current, planned, proposed, and historical information MUST be visibly
different. A newer file does not automatically become authoritative.

When two locations conflict, an agent MUST report the conflict rather than
silently choosing one. Preserve information that may be unique, let the human
choose the owner, and turn the other location into a summary or history.

## 9. Agent procedure

Before creating or moving a top-level project area, project document, or
supporting artifact, an agent MUST:

1. read the root README and any agent instruction file used by the project;
2. identify the purpose of the material;
3. use the project map to find the existing location or owner;
4. follow a location required or normally used by the project's tools when one
   exists;
5. update the existing location instead of creating a duplicate;
6. create a new top-level area or document only when no suitable location
   exists and the new location will remain useful;
7. add or update the appropriate navigation link; and
8. report uncertainty or conflict instead of silently guessing.

An ordinary edit inside an established area does not require rereading PLS
unless it changes project structure, document ownership, or navigation.

An agent SHOULD load only the information needed for its task. It SHOULD NOT
load working, generated, evidence, or legacy material by default.

Agent instructions MAY contain tool commands and project-specific safety rules.
They MUST link to project documentation rather than copying its requirements,
architecture, status, or specifications.

## 10. Verification without process clutter

Verification is an action. Evidence is a retained artifact. Performing a check
does not mean the project needs a permanent verification document.

Projects SHOULD prefer:

1. human inspection;
2. familiar existing linters, formatters, and link checkers;
3. existing tests or continuous integration; and
4. custom validation only when the earlier choices cannot protect an important
   requirement.

An agent MUST NOT create a permanent gate, review record, verification report,
evidence bundle, manifest, digest, or checklist merely to prove that it followed
a process.

An agent MUST NOT invent an approval gate. A gate is justified only when the
Owner has established a real decision that cannot proceed until stated
conditions are met.

For a one-time check, use a direct command and report the result. An agent
SHOULD NOT commit a script solely to preserve that command.

A custom validation script SHOULD be added only when:

- it protects an identified project requirement;
- the same check is expected to run again;
- an existing familiar tool is not sufficient; and
- the project is willing to maintain the script.

Testing a validator is appropriate when that validator is itself a maintained
project product. Otherwise, a project SHOULD NOT create validators that exist
mainly to check other validators.

## 11. Adopting PLS

Installing or invoking a PLS agent skill does not change the layout standard
or version an existing project follows. A human MUST accept a migration before
an agent changes the recorded standard or version, or reorganizes the project
for a different one.

For a new project:

1. Choose the language, framework, and tools that affect the layout.
2. A human or agent creates only the project areas currently needed.
3. The root README records the project map.
4. The human reviews important structure and ownership choices.
5. Agents follow the recorded structure afterward.

For an existing project:

1. Preserve useful information and artifacts. Do not assume their existing
   names or locations must remain.
2. Inventory current locations, ownership, links, and any tool conventions that
   constrain placement.
3. Move useful material into the normal PLS areas and names. Keep a mapped
   alternative only when the project's language, framework, or tools require or
   normally use it, or when the human explicitly chooses it.
4. Add or update the project map in the root README and explain any retained
   alternative locations.
5. Resolve duplicated or conflicting ownership and separate current, proposed,
   and historical information.
6. Update affected links and instructions, verify that moved material remains
   reachable, and retire empty or obsolete structural wrappers.

An instruction to **adopt PLS** authorizes this material-preserving structural
migration and the matching declaration change. It does not authorize deleting
unique information, changing product behavior, or moving private or external
material unless that material is also in the requested scope.

An instruction to **review**, **map**, or **align** an existing project does not
by itself authorize structural changes. In those cases, an agent may recommend
a migration or document the current layout using mapped alternatives.

## 12. How a project follows PLS

A project follows this PLS working model when:

- its root README identifies PLS v0.3, provides the required orientation, and
  contains or directly links to the project map;
- its important areas have clear purposes and can be found from that map;
- its source, tests, configuration, deployment artifacts, and other technical
  areas use the conventions of their language, framework, and tools or clearly
  mapped alternatives;
- each important subject has one clear owner;
- current, planned, proposed, and historical information are distinguishable;
- agents receive the placement and safety instructions they need when agents
  work on the project; and
- verification effort is appropriate to the project's actual risk.

No PLS-specific validator, profile, module declaration, evidence folder, or
release gate is required.

## 13. Final principle

Create the least project structure that makes the project predictable. Add a
location when real use needs it, not because a template or agent can generate
it.
