---
name: pls
description: Scaffold, organize, place, or review project structure and documentation using the Project Layout Standard. Use for project setup, document placement, layout adoption, and navigation. Durable Journal records are handled by the optional Journal companion. Ordinary coding without these needs is outside this skill.
---

# Use PLS

This skill is the agent interface to PLS. The rules are owned by the bundled
[PLS standard](references/PLS.md). Use that local reference; do not replace it
with mutable remote content while working on a project.

Read the target project's root README and agent instructions first.
For layout work, read the PLS standard completely. Follow the project's
recorded adoption and ownership; placing a documentation entry point does not
adopt a new standard or reorganize the project. A project MAY use a separately
installed Journal companion for discussion and decision records. That
companion follows the project's mapped entry point, including an existing
`project-record` location, until a migration is requested.

For project-map setup or location changes, use the standard's
[map and location rules](references/PLS.md#41-find-or-create-the-project-map)
and the [basic project map](assets/project-map.md). Resolve declared roots and
area overrides before selecting a destination. Keep existing maps and owners
unless the requested task changes them.

For disposable working context or session handoffs, follow the standard's
[location and lifecycle rules](references/PLS.md#disposable-working-context-and-session-handoffs).
Resolve the project's declared location before using the default
`.local/agent-note/`.

Use the action requested by the human:

- **Scaffold:** create the smallest useful starting structure for a new
  project.
- **Review:** report how well an existing project follows PLS without changing
  it unless changes are also requested.
- **Reorganize:** improve an existing layout within its recorded standard and
  project map.
- **Adopt:** preserve useful material while migrating it into the normal PLS
  areas and names, update the project declaration, map, links, and instructions,
  and retire obsolete structural wrappers. Retain another location only for a
  project tool convention or an explicit human choice.
- **Place:** decide where a new document or supporting artifact belongs.

Follow [Adopting PLS](references/PLS.md#11-adopting-pls) for scaffolding,
reorganization, and migration. Follow the
[Agent procedure](references/PLS.md#9-agent-procedure) when placing or changing
project material. The linked standard, not this skill, owns those rules.
Do not interpret preservation of useful material as preservation of its current
names or paths. PLS describes where project material belongs; it does not
define a Journal record format or save workflow.

Do not invent a need to retain evaluation or verification output. Maintained
evaluation cases and evaluation-only runners use the project's test layout;
maintained development automation uses Tools. Temporary machine-local or
sensitive output may use an ignored `.local/` area when it must remain in the
workspace, but retaining sensitive evidence requires an explicit human choice.
Treat `.local/` as a placement boundary, not permission to accumulate evidence.

PLS does not have a special scaffold command or linter. Make requested changes
directly. Use an existing project linter or link checker when it is available
and relevant; use PLS review for questions that require human judgment.
