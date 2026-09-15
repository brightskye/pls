# PLS project instructions

## Start here

- Read `README.md` for the project purpose and project map.
- Read `src/pls/references/PLS.md` before changing the standard.
- Read `docs/journal.md` before stating the current PLS status or
  changing its direction.

## Working rules

- Use the simplest wording that preserves the intended rule.
- Keep the standard focused on predictable project areas and the placement of
  documents and supporting artifacts.
- Let language, framework, test, deployment-package, and tool standards govern
  the internal format of their own areas.
- Do not reintroduce profiles, activated modules, mandatory release gates, or a
  PLS-specific validator without an explicit Owner decision.
- Do not add scripts, evidence packages, manifests, or review records merely to
  demonstrate that a process was followed.
- Keep `src/pls/`, `src/journal/`, and `src/design-writing/` independently
  self-contained. Each skill uses its own bundled guide without requiring a
  sibling skill or fetching replacement rules while it is being used.
- Read `src/journal/references/journal.md` when saving or retrieving project
  discussions and decisions. PLS owns placement; Journal owns record rules.
- Update `docs/journal.md` when the current direction or release state
  materially changes.

## Verification

Use human review and familiar existing tools. For a documentation-only change,
`git diff --check` is normally sufficient unless the change creates a specific
reason for another check. After changing the skill package, run the host's
familiar skill validator when one is available and verify a copy of
`src/pls/` works without its repository parent.
