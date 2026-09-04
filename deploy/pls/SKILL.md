---
name: pls
description: Scaffold, organize, place, or review project structure and documentation using the Project Layout Standard. Use when setting up a project, deciding where a document or supporting artifact belongs, simplifying an existing layout, adopting PLS, or checking whether people and agents can navigate a project predictably. Do not use for an ordinary code task unless project structure, placement, navigation, or information ownership must change.
---

# Use PLS

This skill is a deployment adapter. The rules are owned by the bundled
[PLS standard](references/PLS.md). Use that versioned local reference; do not
replace it with mutable remote content while working on a project.

Before scaffolding, reorganizing, adopting, placing, or reviewing project
material, read the standard completely. Then read the target project's root
README and any agent instruction file.

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
names or paths.

Do not invent a need to retain evaluation or verification output. Maintained
evaluation cases and evaluation-only runners use the project's test layout;
maintained development automation uses Tools. Temporary machine-local or
sensitive output may use an ignored `.local/` area when it must remain in the
workspace, but retaining sensitive evidence requires an explicit human choice.
Treat `.local/` as a placement boundary, not permission to accumulate evidence.

PLS does not have a special scaffold command or linter. Make requested changes
directly. Use an existing project linter or link checker when it is available
and relevant; use PLS review for questions that require human judgment.
