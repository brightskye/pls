# PLS Project Record

## Current

PLS v0.3 is a project-layout, structure-first working draft. The active text is
the bundled [`PLS standard`](../src/pls/references/PLS.md).

PLS defines a root README, a project map, purpose-based top-level areas,
question-based documentation locations, one owner for each important subject,
a short agent procedure, a consistent ignored `.local/` boundary when
temporary or sensitive project-local artifacts are needed, a temporary
`.local/agent-note/` lifecycle, and proportional verification using familiar
tools. It does not require every default directory, profiles, module
activation, a PLS-specific validator, evidence folders, or release gates.

The working standard places product code, skills, and bundled resources in
Source, safe service settings and templates in Configuration, and maintained
build and installer scripts in Tools. Complete versioned packages use Releases.
The current rules are owned by [Project areas](../src/pls/references/PLS.md#6-what-each-project-area-is-for).
There is no default Deployment area.

The self-contained PLS agent skill is
[`src/pls/`](../src/pls/SKILL.md). Its `references/PLS.md` is both the
project's authoritative standard and the version distributed with the skill,
so a Git installer may copy that directory without relying on the repository
parent or fetching rules at runtime.

The distribution now documents the `skills` CLI and provides a standalone
Python install/update tool in [`tools/pls_skill.py`](../tools/pls_skill.py).
Both use the existing `src/pls/` package; no second source location or build
step is required. The Python tool uses only the standard library, remembers
the selected Git ref, protects local edits, and stages a complete replacement
before updating. All 11 [installer tests](../tests/test_pls_skill.py) pass with
isolated installations and substituted GitHub responses.
Live GitHub installation and updates from `src/pls/` passed using both literal
`npx` with `skills` 1.5.23 and the standalone Python tool downloaded from the
published commit. Installed files matched the published package. Python commit
pinning and local-edit protection also passed. The checks ran in temporary WSL
projects; [Operations](operations.md#check-changes-to-the-distribution-tool)
records their scope. The checked `skills` CLI supports branch/tag selection but
fails on raw commit SHAs, so exact commit selection uses the Python tool.

The repository is publicly available at
[`brightskye/pls`](https://github.com/brightskye/pls) with clean public
history. It contains no predecessor Git history or private review archive and
is available under the MIT License. The local `main` branch tracks the
published GitHub branch. The `src/pls/` source layout, updated working rules,
Python tool, tests, and installation instructions are published. Existing
installed copies remain at their selected version until explicitly updated.

## Next

- Review the working standard as a human reader.
- Review whether any real project needs an explicitly mapped alternative to a
  normal PLS location.
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
- Source contains the delivered product, including code, agent skills, and
  bundled resources. Test and evaluation support belongs in Tests, maintained
  build and installer scripts in Tools, and service settings and templates in
  Configuration. Familiar tool-specific locations remain supported.
- Complete versioned packages use Releases and include the installer and other
  project files needed by users. Installer sources remain in Tools. Generated release
  outputs stay outside Git by default, and `.local/` is only a temporary build
  location, not their permanent distribution home.
- Deployment is not a default top-level area. Classify maintained files by
  their purpose. The self-contained PLS product package lives at `src/pls/`.
- Project state, plans, proposals, decisions, and history form one Project
  Record. It contains durable project material, not temporary conversation
  notes, working handoffs, or raw transcripts.
- Architecture explains the overall solution; Specifications explain exact
  behavior.
- Evaluation methods and important retained results belong to Quality.
- Routine evaluation output and agent backup ideas are not permanent evidence.
- `.local/` is the normal optional ignored location for temporary,
  machine-local, or sensitive workspace artifacts when project tools do not
  specify another location; it must not own information needed to use the
  project.
- `.local/agent-note/` is the normal ignored location for deliberately retained
  temporary agent conversation notes. Notes move through `pending`, `reviewed`,
  and short-lived `retired` states; retired notes are safe to delete rather
  than forming an archive. Durable outcomes are promoted to their owning
  project documents, and notes never become project authority.
- Maintained evaluation cases belong in the project's test layout. Sensitive
  evaluation evidence belongs in `.local/evidence/` only when the human
  explicitly chooses retention, while Quality owns and links to its meaning.
- Familiar linters, tests, and human review are preferred over custom
  validation machinery.
- The agent skill is an interface to the bundled PLS rules, not a second owner.
- PLS installation does not depend on one fixed repository path.
- The maintained `src/pls/` package supports direct GitHub skill installation.
  The `skills` CLI is the Node.js option; a standalone Python tool provides
  explicit installation and updates without extra Python dependencies.
  Each installed copy keeps one installation method. Updating that copy does
  not authorize migration of its adopting project.
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

On 2026-09-05, the `brightskye/pls` GitHub repository was created and the clean
`main` history was published using a repository-scoped deploy key.

On 2026-09-05, the Owner clarified that Project Record contains only durable
project material and selected `.local/agent-note/` for temporary agent
conversation notes with visible pending, reviewed, and retired states.

On 2026-09-06, the Owner clarified installer and release placement: maintained
build and installer scripts use Tools, complete release packages include the
installer under `releases/<version>/` or a mapped distribution location, and
Deployment remains optional for deployment-specific files and integrations.
The existing PLS skill stays at `deploy/pls/`. This updates the working draft;
it does not publish a new stable PLS release or migrate adopting projects.

Later on 2026-09-06, the Owner approved removing Deployment from the default
layout and placing maintained files by purpose. This supersedes the earlier
same-day decision to retain it as a separate area. The PLS package moved from
`deploy/pls/` to `src/pls/`; navigation, agent instructions, and installation
paths were updated. Existing copied skill installations and older Git refs
retain their original layout until deliberately updated.

Later on 2026-09-06, the Owner requested convenient GitHub installation and
rules updates through both `npx skills` and Python. The existing `src/pls/`
package was retained, and the standalone Python installer/updater and its
tests were added in Tools and Tests. This prepares distribution; it does not
publish the local changes or promote the working draft to a stable release.

On 2026-09-06, the Owner authorized publication and live GitHub testing. Commit
[5ec1c115616c664b00f2d6850584bf5bfe6a4f18](https://github.com/brightskye/pls/commit/5ec1c115616c664b00f2d6850584bf5bfe6a4f18)
published the source-layout and distribution changes. Both installation and
update routes passed against the new GitHub path, with matching package files.
The working draft remains PLS v0.3; publication did not promote it to stable.
