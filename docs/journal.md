# PLS Project Journal

Project key: `pls`

Recordkeeping topic: [discussion](#disc-0001-project-recordkeeping),
[history](#dec-0001-preserve-retrievable-project-history),
[Journal naming](#dec-0002-name-the-area-project-journal),
[growth](#dec-0003-keep-journal-reading-focused),
[disposable context location](#dec-0004-allow-a-configured-disposable-context-location), and
[working rules](../src/journal/references/journal.md), and
[separate Journal ownership](#dec-0007-separate-journal-from-layout-rules).

## Current

PLS remains the 0.3.0 working draft. This repository maintains three independent
packages: [PLS](../src/pls/SKILL.md) for layout,
[Journal](../src/journal/SKILL.md) for shared discussion and decision rules, and
[design-writing](../src/design-writing/SKILL.md) for system designs. Each guide
is maintained with its owning skill and works without the other packages.

[DEC-0007](#dec-0007-separate-journal-from-layout-rules) accepts the Journal
extraction. The shared guide preserves metadata, sources, acceptance, reasons,
linked changes, retention, growth, and retrieval. PLS retains placement and
ownership rules. Direct repository recording performs the record, alignment,
and verification steps; a managed saving system owns execution and reports a
raw capture separately from a completed journal save. Agent adapters follow
the selected interface. Orca's later vault integration can adopt a versioned
guide and keep local execution rules in configurable vault locations.

The `0.3.0-draft.5` candidate passes all 47 package tests, three skill
validators, Markdown and local-link checks, and independent Journal behavior
trials. Actual draft4 updaters also passed offline migration, local-edit
protection, sibling preservation, and receipt checks. Publication and Orca's
installation update remain pending. The latest published bundle is
[`v0.3.0-draft.4`](https://github.com/brightskye/pls/releases/tag/v0.3.0-draft.4),
which has two skills and keeps Journal guidance inside PLS. The standard has
not been promoted to stable. Native Windows remains untested.

PLS keeps its existing `docs/journal.md`. Adopting projects follow their current
maps; separately authorized migrations are independent of this extraction.
Extraction preserves existing record IDs, dates, accepted choices, and
reasons. Vault copying, Runtime integration, and record migration are
separate from the package change and remain unimplemented.

## Next

- Publish the verified draft5 bundle and complete the authorized Orca skill
  upgrade, preserving its current mapped record locations.
- Migrate other projects' `project-record` locations and update installed
  skills only when those separate actions are requested.
- Review whether any real project needs an explicitly mapped alternative to a
  normal PLS location.
- Decide when the draft is clear enough for a stable PLS release.

## Proposals

The metadata, status vocabulary, and detailed save/retrieval workflow in the
[Journal reference](../src/journal/references/journal.md) are proposed
details for the accepted recordkeeping direction. They have passed release
review and remain open to feedback before stable acceptance. Their draft
status does not reopen the accepted purpose, Journal name, history retention,
growth rules, or selective reading direction.

## Discussions

### DISC-0001: Project recordkeeping

```yaml
id: DISC-0001
kind: discussion
title: Retrievable discussion and decision history
project: pls
topics: [recordkeeping, retrieval, decision-history]
scope: Reusable PLS documentation rules; no RAG implementation or Orca migration
status: open
occurred: 2026-09-15
created: 2026-09-15
updated: 2026-09-15
sources:
  - Retained user instructions in entries 2026-09-15-01 through 2026-09-15-05
```

#### Entry 2026-09-15-01

The user described a recurring failure: agents miss accepted choices or keep
presenting them as recommendations. The requested improvement is organized,
retrievable project records. RAG can be added later; the records must work
without it.

The user requested "a pls standard for ways to save discussions and decision"
and specified that it should optionally integrate with RAG for indexing and
search. The user then clarified: "a changed decision must be save and recorded"
so future readers can recall why it changed and why the original choice was
made. These retained excerpts are the available acceptance source; no separate
durable message locator is recorded here.

Outcome: [DEC-0001](#dec-0001-preserve-retrievable-project-history). The new
reference proposes stable record metadata, dated discussion entries, separate
acceptance/documentation/implementation states, linked replacements and partial
amendments, and source-based retrieval. Exact format and workflow remain for
review. No RAG product, service, database, or record migration was selected.

Follow-up: the [later entry](#entry-2026-09-15-02) records acceptance of the
Journal name and growth rules. Detailed record format and workflow still
require review.

#### Entry 2026-09-15-02

The user suggested "journal as the folder name instead of project-record"
and asked whether it would eventually become too large. The assistant proposed
Project Journal at `docs/journal.md` or `docs/journal/`, with concise current
views, separately retained dated history, splitting by topic or period when
needed, preserved IDs and links, and selective retrieval. The proposed purpose
remained the same as the existing Project Record.

The user asked whether these rules were enough for a solid foundation. The
assistant proposed consolidating the draft around Journal and the growth
rules, including small and expanded examples, while leaving record migration
and publication separate. The user replied "do it", authorizing that revision.
These retained proposal and response details are the source; no separate
durable message locator is recorded here.

Outcomes: [DEC-0002](#dec-0002-name-the-area-project-journal) and
[DEC-0003](#dec-0003-keep-journal-reading-focused). The naming and growth
questions are resolved. Exact metadata and workflow remain the existing draft
for review; no fixed size limit, indexing product, or migration was selected.

Later outcome: PLS's own record migration was explicitly requested and
completed in [entry 2026-09-15-04](#entry-2026-09-15-04). Other project
migrations remain separate.

#### Entry 2026-09-15-03

While the Journal revision was being prepared, the user asked to make the
location for "Disposable working context and session handoffs" configurable,
referring to `.local/agent-note/`. This is a direct request to change the
standard's placement rule; it does not select a new path for either workspace.

Outcome: [DEC-0004](#dec-0004-allow-a-configured-disposable-context-location).
The revision keeps the existing path as the default and lets the project map
declare an override. Temporary context stays ignored and non-authoritative;
durable outcomes retain their Journal or owning-document destination. No
separate runtime configuration or note migration was requested.

#### Entry 2026-09-15-04

The user asked why PLS still used `project-record.md` after the Journal
revision. The assistant explained that it had treated PLS's own record
migration as separate work and proposed moving it to `docs/journal.md`,
updating links and agent instructions, and preserving history while leaving
Orca's migration separate. The user replied "let's migrate".

PLS's own record is now `docs/journal.md`. Its record IDs, decision status,
dated entries, and original reasons are preserved. README, agent instructions,
Operations, and source locators point to the new location. This applies
[DEC-0002](#dec-0002-name-the-area-project-journal); it does not change that
decision's meaning. Orca's local pointers were updated without migrating its
own records. No release, installation, or disposable-context move was made.

The retained proposal and response above are the migration source; no
separate durable message locator is recorded here.

#### Entry 2026-09-15-05

The user reconsidered whether Journal rules should belong in PLS, individual
agents, or the Orca vault. The proposed change separated layout from detailed
recordkeeping: keep a shared Journal guide and companion skill in this
repository, let Orca adopt a versioned copy with separate execution rules, and
keep agent adapters thin. The user replied, "i like this suggestion. How can
we achieve it?"

The implementation proposal was to extract `src/journal/`, narrow PLS to
layout and placement, distinguish direct repository saves from Runtime-managed
handoffs, add Journal to the bundle and installer, verify independent skills,
and update Orca's design and installed skills. Existing journals would remain
in place. The user answered "yes" to that proposal. These retained proposal
and response excerpts are the source; no separate durable message locator is
recorded here.

Outcome: [DEC-0007](#dec-0007-separate-journal-from-layout-rules). Existing
shared record semantics remain; package ownership and execution routing are
clarified. This does not authorize silent vault migration or weaker acceptance
and history rules.

## Decisions

### DEC-0001: Preserve retrievable project history

```yaml
id: DEC-0001
kind: decision
title: Preserve retrievable project discussion and decision history
project: pls
topics: [recordkeeping, retrieval, decision-history]
scope: Reusable PLS recordkeeping standard; optional indexing compatibility
status: accepted
occurred: 2026-09-15
created: 2026-09-15
updated: 2026-09-15
sources: ["journal.md#entry-2026-09-15-01"]
amended_by: ["journal.md#dec-0007-separate-journal-from-layout-rules"]
```

PLS will define an organized way to save discussions and decisions, including
the history of changed decisions. Records preserve the initial choice and its
reason, the later change and its reason, and enough links to retrieve both.
They support ordinary retrieval and optional RAG integration. Acceptance and
implementation remain distinct so pending work cannot erase an agreement.

The purpose is to prevent accepted decisions from being missed or repeatedly
treated as recommendations. A current summary alone cannot answer why the
project changed direction. Implementing RAG is deferred while the recordkeeping
standard is established. No other storage option was rejected by this decision.

Lifecycle: accepted on 2026-09-15 by the user through the request and
clarification retained in [DISC-0001](#entry-2026-09-15-01). Detailed rules live
in the [working reference](../src/journal/references/journal.md); Current
tracks their review, publication, and adoption separately.

On 2026-09-15, [DEC-0007](#dec-0007-separate-journal-from-layout-rules)
amended the package and rule ownership: the shared Journal guide now owns
detailed recordkeeping independently of the PLS layout standard. The original
history-retention requirement remains accepted.

### DEC-0002: Name the area Project Journal

```yaml
id: DEC-0002
kind: decision
title: Name the recordkeeping area Project Journal
project: pls
topics: [recordkeeping, naming]
scope: PLS area name and default paths; existing project migration excluded
status: accepted
occurred: 2026-09-15
created: 2026-09-15
updated: 2026-09-15
sources: ["journal.md#entry-2026-09-15-02"]
amends: ["journal.md#dec-0005-original-project-record-grouping"]
```

The area is Project Journal, normally `docs/journal.md` or an expanded
`docs/journal/`. This amends only the name and default paths of the earlier
choice to group project state, plans, proposals, decisions, and history in
Project Record. Those responsibilities remain in force. Existing mapped
locations continue until a separate migration or explicit mapping decision.

The new name is shorter and expresses the project's development through
discussions and decisions. The old area already combined that material;
the reason for choosing its exact former label was not separately recorded.
Keeping one chronological file for everything is not required.

Lifecycle: accepted on 2026-09-15 by the user's instruction to make the
revision described in [DISC-0001](#entry-2026-09-15-02). The
[PLS area definition](../src/pls/references/PLS.md#71-project-journal) owns
the resulting placement rule.

### DEC-0003: Keep journal reading focused

```yaml
id: DEC-0003
kind: decision
title: Grow journal records while keeping reading focused
project: pls
topics: [recordkeeping, growth, retrieval]
scope: Journal organization, retained history, and routine retrieval
status: accepted
occurred: 2026-09-15
created: 2026-09-15
updated: 2026-09-15
sources: ["journal.md#entry-2026-09-15-02"]
```

Keep the entry point and current view concise. Split growing discussions by
topic or period and use separate decision files when helpful. Preserve IDs,
links, dated meaning, and original reasons. Readers start at navigation and
current context, then follow only the records needed for their question.

This addresses the user's concern that accumulated history will become too
large to navigate or load. History remains useful even when its overview is
shortened. A mandatory daily file, automatic deletion, or RAG installation
is not part of this decision; no fixed word or record limit was selected.

Lifecycle: accepted on 2026-09-15 through the same
[source confirmation](#entry-2026-09-15-02). The
[Journal growth rules](../src/journal/references/journal.md#keeping-a-growing-journal-usable)
and [retrieval rules](../src/journal/references/journal.md#retrieval-without-a-database)
own the required behavior.

### DEC-0004: Allow a configured disposable context location

```yaml
id: DEC-0004
kind: decision
title: Configure the disposable working context and session handoff location
project: pls
topics: [recordkeeping, working-context, placement]
scope: Temporary context location; authority and lifecycle unchanged
status: accepted
occurred: 2026-09-15
created: 2026-09-15
updated: 2026-09-15
sources: ["journal.md#entry-2026-09-15-03"]
amends: ["journal.md#dec-0006-original-temporary-note-location"]
```

Projects can configure where disposable working context and session handoffs
are saved. `.local/agent-note/` remains the default. The project map declares
an alternative; agent instructions point to that declaration. The selected
location stays temporary, non-authoritative, and ignored within a versioned
workspace. Selection does not move existing notes automatically.

This relaxes the earlier placement choice to support project-specific paths.
The earlier `.local/agent-note/` choice provided a predictable ignored home
for temporary notes; that boundary and its pending/reviewed/retired lifecycle
remain in force. The location no longer has to be fixed to that path or
owned by a project tool.

Lifecycle: accepted on 2026-09-15 through the user's
[request](#entry-2026-09-15-03). The
[disposable context specification](../src/pls/references/PLS.md#disposable-working-context-and-session-handoffs)
owns the resulting location rule. No workspace override has been selected.

### DEC-0005: Original Project Record grouping

```yaml
id: DEC-0005
kind: decision
title: Group durable project material in Project Record
project: pls
topics: [recordkeeping, naming]
scope: Original durable recordkeeping area and normal path
status: accepted
occurred: null
created: 2026-09-15
updated: 2026-09-15
sources:
  - https://github.com/brightskye/pls/blob/1b28c0d50f8e9866a032534828b8c0d3476b550b/docs/project-record.md#decisions
  - https://github.com/brightskye/pls/blob/1b28c0d50f8e9866a032534828b8c0d3476b550b/src/pls/references/PLS.md
amended_by: ["journal.md#dec-0002-name-the-area-project-journal"]
```

Project state, plans, proposals, decisions, and history form one Project
Record. It contains durable project material, not temporary conversation
notes, working handoffs, or raw transcripts. The original normal location was
`docs/project-record.md`.

This is a backfill of a choice already recorded under Decisions and applied
in the governing standard. The source was committed on 2026-09-05; the
original acceptance date, message locator, and reason for the exact former
label are unknown. The known purpose is to group durable project material
separately from temporary context.

Lifecycle: the previously recorded choice remains accepted within its
unamended scope. On 2026-09-15,
[DEC-0002](#dec-0002-name-the-area-project-journal) amended the area name and
normal paths. The grouping and durability boundary remain in force. This
backfill assigns an ID and reciprocal link; it does not make a new choice.

### DEC-0006: Original temporary note location

```yaml
id: DEC-0006
kind: decision
title: Keep temporary agent conversation notes in .local/agent-note/
project: pls
topics: [recordkeeping, working-context, placement]
scope: Original temporary note location, lifecycle, and authority boundary
status: accepted
occurred: 2026-09-05
created: 2026-09-15
updated: 2026-09-15
sources:
  - https://github.com/brightskye/pls/blob/5ec1c115616c664b00f2d6850584bf5bfe6a4f18/docs/project-record.md#history
  - https://github.com/brightskye/pls/blob/5ec1c115616c664b00f2d6850584bf5bfe6a4f18/src/pls/references/PLS.md
amended_by: ["journal.md#dec-0004-allow-a-configured-disposable-context-location"]
```

`.local/agent-note/` is the normal ignored location for deliberately retained
temporary agent conversation notes. Notes move through `pending`, `reviewed`,
and short-lived `retired` states; retired notes are safe to delete rather
than forming an archive. Durable outcomes are promoted to their owning
project documents, and notes never become project authority.

The retained history records the user's selection on 2026-09-05. It keeps
temporary notes separate from durable project material in a predictable
ignored location. A durable message locator and the reason for choosing this
exact name over another ignored path are unknown.

Lifecycle: accepted on 2026-09-05 according to the retained history. On
2026-09-15,
[DEC-0004](#dec-0004-allow-a-configured-disposable-context-location) amended
only the location rule to allow a project-declared alternative. The default,
lifecycle, and authority boundary remain in force. This record was backfilled
with a stable ID on 2026-09-15.

### DEC-0007: Separate Journal from layout rules

```yaml
id: DEC-0007
kind: decision
title: Separate shared Journal rules from layout and agent integration
project: pls
topics: [recordkeeping, skill-ownership, agent-integration]
scope: Shared guide, companion skill, distribution, and adoption boundaries
status: accepted
occurred: 2026-09-15
created: 2026-09-15
updated: 2026-09-15
sources: ["journal.md#entry-2026-09-15-05"]
amends: ["journal.md#dec-0001-preserve-retrievable-project-history"]
```

Maintain Journal as an independent guide and skill at `src/journal/`, alongside
PLS and design-writing. PLS owns layout, placement, navigation, and document
ownership. Journal owns shared record content, acceptance, history, and
retrieval rules. Agents use the same definitions; their adapters own only
agent-specific triggers, context access, interface calls, and presentation.

A project chooses its authoritative journal location. Direct repository
recording applies the shared record/alignment/verification flow. An external
Runtime owns managed capture and processing; a durable queued input is reported
as captured and pending, not as a completed journal record. The completed
record must still meet the adopted shared standard.

Orca can adopt a versioned copy in its configurable vault-rule locations and
keep integration rules separate. The shared source remains here. Updating a
package does not implicitly update a vault copy or move records. Existing
project maps and records remain in place through this extraction.

This narrows PLS's layout responsibility and avoids agents or vaults maintaining
independently edited versions of the same general rules. It also keeps ordinary
project journals usable without Orca. The earlier PLS-contained guide remains
part of published draft4; shared metadata and history requirements are retained.

Lifecycle: accepted on 2026-09-15 through the proposal and confirmation in
[DISC-0001](#entry-2026-09-15-05). This partially amends DEC-0001's rule ownership,
not its accepted history-preservation goal. Current tracks package verification,
release, and adoption independently of future Runtime or vault integration.

### Earlier recorded decisions

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
- [DEC-0005](#dec-0005-original-project-record-grouping) preserves the original
  Project Record grouping and its later naming amendment.
- Architecture explains the overall solution; Specifications explain exact
  behavior.
- Evaluation methods and important retained results belong to Quality.
- Routine evaluation output and agent backup ideas are not permanent evidence.
- `.local/` is the normal optional ignored location for temporary,
  machine-local, or sensitive workspace artifacts when project tools do not
  specify another location; it must not own information needed to use the
  project.
- [DEC-0006](#dec-0006-original-temporary-note-location) preserves the original
  temporary note location and its later configuration amendment.
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

On 2026-09-15, after the user explicitly requested migration, PLS moved its
own `docs/project-record.md` to `docs/journal.md`. Navigation, agent
instructions, Operations links, and source locators were updated. Existing
records and historical content were preserved. The
[migration discussion](#entry-2026-09-15-04) records the scope and source.
Other projects and installed skills were unchanged; the revision remains
unpublished.

Later on 2026-09-15, the user authorized consolidating the working rules as
Project Journal and adding growth rules and small/expanded examples.
[DEC-0002](#dec-0002-name-the-area-project-journal) records the naming change;
[DEC-0003](#dec-0003-keep-journal-reading-focused) records growth and retrieval.
The rule reference and linked PLS guidance were revised. Existing project
records were preserved in place; no release or installation was performed.

In the same revision, the user requested a configurable location for
disposable working context and session handoffs.
[DEC-0004](#dec-0004-allow-a-configured-disposable-context-location) records
that change, keeping `.local/agent-note/` as the default. The standard and
skill routes now use the configured location; no existing notes were moved.

On 2026-09-15, the user requested the reusable recordkeeping standard and
explicit preservation of original and changed decisions with their reasons.
[DISC-0001](#disc-0001-project-recordkeeping) preserves the request and open
details; [DEC-0001](#dec-0001-preserve-retrievable-project-history) records the
accepted direction. The working reference and skill routes were added to
source. This revision has not been published or installed in Orca. Existing
project records were preserved; no historical migration was performed.

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

### Earlier release verification

The following checks describe the published draft2 and draft3 revisions.

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

### Draft4 release preparation

On 2026-09-15, the user requested a check for obvious mistakes and unfinished
modifications and asked that PLS be made ready for release. This authorized
release preparation; publication and installed-skill updates remain separate.

The review checked both the PLS rules and the requested Journal behavior.
It corrected stale bundle and release examples, clarified the default
working-context location, and replaced broad amendment links with specific
predecessor records and reciprocal links. Unknown historical evidence remains
explicit. Current was shortened, with earlier verification retained in History.

The builder now rejects a missing or empty Journal guide, and installer tests
include that guide in payload and receipt checks. All 40 installer and builder
tests pass. Candidate checks include both skill validators, Markdown and local
links, deterministic builds, and offline installs of both skills. Upgrades
using each installed updater from the actual published draft3 bundle pass
from an unrelated directory after the extracted source is moved away. Receipt
hashes match, updating one skill preserves the sibling, and local edits are
rejected without being overwritten.

The candidate is `0.3.0-draft.4`; the standard remains the 0.3.0 working draft.
The complete reviewed revision uses a clean local commit for its bundle under
ignored `releases/0.3.0-draft.4/`. The bundle's `release.json` records its exact
source commit. At preparation time, there was no draft4 tag or GitHub release,
and live installations retained their selected versions. Checks run on
Linux/WSL; native Windows remains untested.

### Draft4 publication

On 2026-09-15, commit
[fc8b0e788f711b2614946c64c27b0f3dba9b3310](https://github.com/brightskye/pls/commit/fc8b0e788f711b2614946c64c27b0f3dba9b3310)
was published as [`v0.3.0-draft.4`](https://github.com/brightskye/pls/releases/tag/v0.3.0-draft.4).
The release ships both independently selectable skills, the Journal guide, and
configurable disposable context rules. The PLS 0.3.0 standard remains a
working draft; native Windows remains untested, and no live adopter
installations changed. The [release workflow](https://github.com/brightskye/pls/actions/runs/34958738777)
passed 40 tests; the published ZIP and checksum matched the verified local
bundle; and both draft3 updaters selected draft4 with exact payload and
receipt hashes while preserving the sibling skill. The published checksum is
`d369afbf065b979dd8479e163bf8b056d64d9cfe0a84e30d14a1d612ae131466`.

### Separate Journal package

On 2026-09-15, the user approved [DEC-0007](#dec-0007-separate-journal-from-layout-rules).
The existing guide was moved from `src/pls/references/journal.md` to
`src/journal/references/journal.md`, with a standalone Journal skill. PLS's
entry point and guide were narrowed to layout and placement. The bundle and
installer now select each of the three skills independently. The next candidate
is draft5; verification, publication, and installation results are recorded
here when completed. Existing journal records and locations were preserved.

The candidate passed 47 unit tests, all three skill validators, Markdown and
local-link checks, and two independent agent trials. The repository trial
preserved an old decision and its reason, linked its accepted replacement,
and aligned design and Current without claiming implementation. The managed
trial submitted the authorized input through the fixture Runtime and reported
captured/pending while the published journal stayed unchanged.

Offline integration used the actual published draft4 ZIP and its installed
updaters from an unrelated working directory. Updates protected local edits,
preserved the sibling skill, removed the former PLS-contained guide, and
matched new payloads and receipt hashes. All three skills also installed
independently without the source checkout; Journal's own updater retained its
identity and latest-release selection. Native Windows remains untested.
Publication and live installation are separate results recorded when complete.
