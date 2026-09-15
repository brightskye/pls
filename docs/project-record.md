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

The latest verified remote bundle,
[`v0.3.0-draft.3`](https://github.com/brightskye/pls/releases/tag/v0.3.0-draft.3),
contains the PLS and companion design-writing skills. Its shared Python
installer selects one skill per operation, defaulting to `pls` and accepting
`--skill design-writing`; each selected skill has its own updater and
`.pls-install.json` receipt. Installing both skills therefore requires two
commands. The installed updater updates the selected skill directory,
including itself, from published GitHub bundles. The extracted download is no
longer needed. Maintained skills remain in `src/pls/` and
`src/design-writing/`, with installer and builder sources in `tools/`. Generated
bundles use ignored `releases/<version>/` outputs and GitHub Releases for
distribution. The standard remains the PLS 0.3.0 working draft.

The published draft2's 30 installer and builder tests passed locally and in the
GitHub release workflow. These include migration of old receipts, self-update
from an unrelated working directory, and preservation of local updater edits.
The published ZIP matched the local build byte for byte and passed its
checksum.
Offline installation and GitHub updates through the installed updater passed
after the extracted installer was moved away. The installed PLS skill also
passed its validator. Live checks ran on Linux/WSL; native Windows remains
untested.

Orca now uses this complete project-local installation. Its GitHub update
check passed after the old home-folder installation and dangling source link
were moved to temporary recovery storage. No separate persistent installer
location is needed. Orca's recorded adoption of the standard was unchanged.

The checked `skills` CLI 1.5.23 can install the archive's skill payload but does
not include the outer Python updater or track archive installs for updates.
This route was verified with draft.1; the archive layout remains unchanged.
Use Python for the complete single-folder installation and dedicated update
command. Source Git installation remains a development and compatibility
route.

The repository is publicly available at
[`brightskye/pls`](https://github.com/brightskye/pls) with clean public
history. It contains no predecessor Git history or private review archive and
is available under the MIT License. The local `main` branch tracks the
published GitHub branch. The `src/pls/` source layout, updated working rules,
Python tool, tests, and installation instructions are published. Existing
installed copies remain at their selected version until explicitly updated.

A companion [design-writing skill](../src/design-writing/SKILL.md) and
[standalone guide](../src/design-writing/references/design-writing.md) are now
maintained in `src/design-writing/`. They cover system views, use cases,
operating behavior, readable prose and diagrams, and implementation readiness.
The guide remains a draft for review and uses Orca as an example. The package
is self-contained and independent of the PLS skill. The published draft3
bundle includes it as a separately selectable skill. Draft3 publication did
not upgrade or install any live adopting project. Orca keeps a local copy of
the guide for its readers.

All 39 draft3 installer and builder tests passed locally and in the GitHub
release workflow, and both skill packages passed the skill validator. The
published ZIP matched the committed local build byte for byte and passed its
checksum. Separate temporary installations matched the bundled skill files
and receipt hashes. After the extracted installer was moved away, both
installed updaters passed real GitHub updates from an unrelated directory,
with correct skill identity and no changes to the sibling. A locally edited
companion was correctly rejected. Migration using the published draft2
updater also passed during candidate verification. No live adopter
installation was upgraded. Checks ran on Linux/WSL; native Windows remains
untested.

## Next

- Review the working standard as a human reader.
- Review whether any real project needs an explicitly mapped alternative to a
  normal PLS location.
- Decide when the draft is clear enough for a stable PLS release.

## Proposals

There are no separate active proposals. Record a proposed change here until it
becomes large enough to need its own document.

## Decisions

- The reusable design-writing guide and skill are maintained by this project
  as a separate companion in `src/design-writing/`. Its bundled guide owns
  writing guidance; the PLS standard retains ownership of project layout.
  Copied guides and skill installations adopt revisions explicitly.
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
- Complete release bundles are the normal user distribution. Their installer
  installs offline and updates from GitHub release bundles. Direct source
  links and Git downloads are development routes. Each bundle includes the
  installer; users need no separate tool download or development checkout.
- The installed skill reads its bundled standard without fetching mutable
  remote content. Updates are explicit and may follow a pinned release or the
  working draft.
- The Python bundle route keeps the updater, instructions, metadata, license,
  skill, and rules in one managed installation directory. A successful update
  replaces all managed files, including the updater. Python-managed `--ref`
  installations can migrate with an explicit bundle update; unmanaged source,
  `npx`, and symlink routes remain separate and do not include that updater.
- A release bundle may contain multiple skills. The Python installer selects
  one skill per operation and defaults to `pls`. The `--skill design-writing`
  option selects the companion; each skill has its own directory, updater,
  and receipt. Installing both requires two commands. Legacy
  PLS receipts and PLS-only bundles remain supported for PLS; a PLS-only
  bundle cannot provide the companion skill.
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

On 2026-09-06, the Owner requested a complete bundle and use of that bundle
instead of direct source links. A versioned ZIP builder, bundled offline
installation, release-based updates, and a GitHub prerelease workflow were
implemented and published at commit
[0c195bc56e76b6367bf612a9ef980f4a761194fe](https://github.com/brightskye/pls/commit/0c195bc56e76b6367bf612a9ef980f4a761194fe).
The tagged `v0.3.0-draft.1` workflow passed all 23 tests and published the ZIP
and checksum. The published download, Python installation and update checks,
and `npx` archive installation passed. Orca's project-local bundle installation
and update check also passed. The `npx` archive-update limitation is documented;
Python provides the tested bundle update route. The standard remains a working
draft.

On 2026-09-06, the Owner requested that the next bundled installer keep the
complete Python installation in one `.agents/skills/pls/` directory and update
the updater together with the skill, rules, instructions, metadata, and
license. Commit
[05d9a3e30f96bd42928ecf3d13f87a682af2312f](https://github.com/brightskye/pls/commit/05d9a3e30f96bd42928ecf3d13f87a682af2312f)
was published as `v0.3.0-draft.2`. All 30 release tests passed, and the published
bundle passed offline installation and independent GitHub update checks.
Orca was migrated and its updater verified after retiring the separate
home-folder installation and source link. The standard remains a working draft.

On 2026-09-15, the Owner requested that Orca's writing guide become a standalone
Markdown document maintained in PLS and a reusable design-writing skill. The
guide was extracted with its Orca example, bundled beside the new skill, and
linked from the project map. Orca's README now links to its standalone copy.
Existing edited documents were preserved as dated `.bak` files. No standard,
release, installer, or adopting-project behavior changed.

Later on 2026-09-15, draft3 preparation was approved to include both
`skills/pls/` and `skills/design-writing/` in one release bundle. The shared
Python installer selects one skill per operation, with PLS as the default and
the companion selected explicitly; each installed skill owns its updater and
receipt. At that point, commit and publication were pending, and the latest
verified remote was draft2. No live adoption or install was made by this
preparation.

Later on 2026-09-15, commit
[da0f5eaf613d55bbc9a1b8800e1de61b13ae96ee](https://github.com/brightskye/pls/commit/da0f5eaf613d55bbc9a1b8800e1de61b13ae96ee)
was published as `v0.3.0-draft.3`. Its [GitHub Actions release workflow](https://github.com/brightskye/pls/actions/runs/34945194130)
completed successfully. The bundle contains two independently selectable
skills. All 39 installer and builder tests passed, both skill packages passed
the skill validator, and the published ZIP matched the committed local build.
Temporary offline installation, online updates, and local-edit protection
passed. No live adopter installation was upgraded. The standard remains the
PLS 0.3.0 working draft; checks ran on Linux/WSL and native Windows remains
untested.
