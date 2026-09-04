# PLS Project Record

## Current

PLS v0.3 is a project-layout, structure-first working draft. The active text is
the bundled [`PLS standard`](../deploy/pls/references/PLS.md).

PLS defines a root README, a project map, purpose-based top-level areas,
question-based documentation locations, one owner for each important subject,
a short agent procedure, a consistent ignored `.local/` boundary when
temporary or sensitive project-local artifacts are needed, and proportional
verification using familiar tools. It does not require every default directory,
profiles, module activation, a PLS-specific validator, evidence folders, or
release gates.

The self-contained PLS agent skill is
[`deploy/pls/`](../deploy/pls/SKILL.md). Its `references/PLS.md` is both the
project's authoritative standard and the version distributed with the skill,
so a Git installer may copy that directory without relying on the repository
parent or fetching rules at runtime.

The repository has a clean public initial tree and an `origin` target of
`https://github.com/brightskye/pls.git`. It contains no predecessor Git history
or private review archive. PLS is available under the MIT License. The public
push has not yet occurred.

## Next

- Review the working standard as a human reader.
- Review whether any real project needs an explicitly mapped alternative to a
  normal PLS location.
- Publish the clean repository at `https://github.com/brightskye/pls`.
- Decide when the draft is clear enough to tag as a PLS release.

## Proposals

There are no separate active proposals. Record a proposed change here until it
becomes large enough to need its own document.

## Decisions

- PLS is maintained as an independent project.
- PLS is distributed under the MIT License.
- PLS means Project Layout Standard and covers the main project layout, not
  only documentation.
- The root README owns project purpose, scope, and the project map.
- PLS defines the purpose and placement of project areas. The project's
  language, framework, and tools define their internal technical formats.
- Source contains delivered product or supported runtime code. Test and
  evaluation support belongs in Tests, maintained development automation in
  Tools, and install or launch artifacts in Deployment unless a project
  convention requires another arrangement.
- `deploy/` owns deployable project options. The self-contained PLS agent
  package therefore lives at `deploy/pls/`, matching its skill name.
- Project state, plans, proposals, decisions, and history form one Project
  Record.
- Architecture explains the overall solution; Specifications explain exact
  behavior.
- Evaluation methods and important retained results belong to Quality.
- Routine evaluation output and agent backup ideas are not permanent evidence.
- `.local/` is the normal optional ignored location for temporary,
  machine-local, or sensitive workspace artifacts when project tools do not
  specify another location; it must not own information needed to use the
  project.
- Maintained evaluation cases belong in the project's test layout. Sensitive
  evaluation evidence belongs in `.local/evidence/` only when the human
  explicitly chooses retention, while Quality owns and links to its meaning.
- Familiar linters, tests, and human review are preferred over custom
  validation machinery.
- The agent skill is a deployment adapter, not a second owner of PLS rules.
- PLS deployment does not depend on one fixed repository path.
- The installed skill reads its bundled standard without fetching mutable
  remote content. Updates are explicit and may follow a pinned release or the
  working draft.
- Adopting PLS means preserving useful material while migrating obsolete
  structure to the normal PLS areas and names. A mapped existing name is an
  explicit exception for a project convention or Owner choice, not the default
  adoption result.

## History

On 2026-09-04, the PLS v0.3 working draft and its agent adapter were packaged
as one self-contained `deploy/pls/` Git distribution and prepared in a clean
public repository. The standard remains independent of the adapter while also
being available to directory-based Git installers; no duplicate rules file or
runtime network lookup is required.

On 2026-09-05, the Owner selected the MIT License for public use, modification,
and distribution of PLS.
