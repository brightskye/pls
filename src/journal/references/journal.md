# Project Journal Companion

Status: Working draft for review. This standalone guide defines portable
Markdown records, their lifecycle, and selective retrieval for any project. It
does not require PLS, Orca, a database, a RAG service, or another external
dependency.

## Rule words

- **MUST** and **MUST NOT** are required by this guide.
- **SHOULD** and **SHOULD NOT** describe the normal choice.
- **MAY** means optional.

Only the uppercase words above create requirements in this guide. A project's
own instructions and adopted local policy may add requirements; they do not
silently weaken the content and evidence rules below.

## Purpose and reading route

Readers MUST be able to find what was discussed, what was decided, what applies
now, and why a decision changed throughout the project's lifetime. Accepted
choices MUST remain distinguishable from suggestions and unfinished work.

Use [placement](#placement-and-ownership) to choose a home,
[growth](#keeping-a-growing-journal-usable) to keep it manageable,
[layout examples](#small-and-expanded-journals) for small and expanded projects,
[record content](#record-content) when saving,
[changes](#decision-changes-and-history) when revising a decision, and
[retrieval](#retrieval-without-a-database) when resuming or reviewing work.

## Placement and ownership

| Material | Owner and normal location |
|---|---|
| Durable discussion summaries | Discussions in `docs/journal.md`, or `docs/journal/discussions/` when expanded |
| Decisions and their rationale | Decisions in the Project Journal, or `docs/journal/decisions/` |
| Substantial proposals | Proposals in the Project Journal, or its mapped proposal files |
| Required system behavior | The owning Architecture or Specification |
| Documentation, implementation, and verification progress | Current in the Project Journal |
| Disposable working context and session handoffs | The location declared by the project map or local policy |

The Project Journal MUST remain the entry point for its records. Its common
locations are `docs/journal.md` or an expanded `docs/journal/README.md`, but
the project's actual map owns the path. Existing `project-record` locations
and other mapped names remain in use until a separately authorized migration
or explicit mapping decision. Installing this guide or skill does not migrate
files, rename an area, or choose an arbitrary fallback path.

Use one owning entry point. When expanding the single file into a directory,
move its content to the mapped files and update the project map. Any retained
old entry point serves only as a navigation link, with no independent records.

A small project MAY keep
records as individually identified sections in one file. Expand into files
only when that improves navigation. A durable discussion MAY still contain
open questions; an unresolved outcome does not make the discussion temporary.

Each decision MUST have one owning record. Discussions, indexes, and Current
link to that record instead of maintaining independent decision wording or
acceptance. Architecture and Specifications express the resulting behavior;
the decision record owns its rationale and history.

Recording authority comes from the user's request or established project
instructions. Retain purposeful summaries and necessary supporting excerpts.
Saving project history does not authorize copying whole transcripts, publishing
private content, implementing a decision, or changing external systems. The
project map or adopted local policy owns any disposable context location and
lifecycle; changing that location does not change where durable Journal
records belong.

## Keeping a growing journal usable

The journal grows through linked records. Its entry point and current view
MUST remain concise enough to locate the relevant work without reading the
project's lifetime history.

| Part | Keep here | When it grows |
|---|---|---|
| Entry point | Area and topic links, with brief orientation | Move detailed navigation into linked topic indexes |
| Current and Next | Current status, active work, open follow-through, and owner links | Move completed context to dated history; retain links |
| Discussions | Focused, dated records grouped by topic | Split a topic into periods or subtopics and link each part |
| Decisions | Independently changeable choices and their history | Move identified entries into individual files when useful |

Start with the smallest useful structure. Split when a reader repeatedly has
to scan unrelated material, active work is buried in history, or a topic's
dated records are hard to locate. A fixed number of files, words, or days is
not required. Create only the files and indexes that actual content needs.

Discussion records SHOULD cover a bounded, coherent exchange. Start a new
linked record for a later period or distinct subtopic when extending the old
one would make it difficult to use. A topic index can connect several records;
one topic need not become one indefinitely growing record.

When splitting a file, move complete identified records where possible.
Preserve record IDs, dated entry anchors, original meaning, and reasons. If
dated entries from one discussion record need separate files, retain one
owning metadata block and link each part to that parent record. Entry identity
remains the parent record ID plus entry anchor; avoid duplicate record metadata.
Update navigation, inbound links, source locators, and replacement/amendment
links in the same edit. Verify that both original and current decisions remain
reachable. Keep one owning copy of each record.

Summaries MAY be shortened. Their underlying dated discussion, choices, and
reasons MUST remain retrievable under the history retention rules. Older
records can stay in place; moving them to an archive does not remove them
from relevant searches or change their applicability.

## Small and expanded journals

A small project can use one `docs/journal.md` with linked sections:

```text
Project Journal
  Current       Brief status and links to active decisions
  Next          Upcoming work and expected outcomes
  Proposals     Ideas still under consideration
  Discussions   DISC-0003: Capture routing, with dated entries
  Decisions     DEC-0008: Original route; DEC-0014: Accepted replacement
  History       Dated milestones linking to the relevant records
```

Each discussion and decision carries its own metadata beneath its stable
heading. Current links to `DEC-0014`; that decision links to `DEC-0008` and the
source discussion. Unused sections can be omitted.

The same material can expand into focused files as it grows:

```text
docs/journal/
  README.md
  current.md
  next.md
  proposals.md
  discussions/
    capture/
      README.md
      2026-09.md
      2026-10.md
  decisions/
    DEC-0008-original-capture-route.md
    DEC-0014-agent-note-route.md
  history.md
```

The journal README links to its areas. The capture index links to both dated
discussion files, relevant decision records, and the owning data design.
Each dated file can contain one or several identified discussion records;
the month in its filename is a grouping aid. Decision IDs and source dates
stay unchanged when their entries move out of the original journal file.

For a current routing question, read the topic index, `DEC-0014`, and the
owning design. For why routing changed, also follow `DEC-0008` and the linked
discussion entries. Unrelated topics and months need not be loaded.

## Record content

Records MUST use UTF-8 Markdown and carry the following named metadata. Use
YAML frontmatter for a file containing one record. In a shared file, put a
fenced `yaml` metadata block immediately below each record's stable heading or anchor;
document-level status does not determine the status of its individual records.

| Field | Meaning |
|---|---|
| `id` | Stable identifier, unique within the project |
| `kind` | `discussion` or `decision` |
| `title` | Short, specific subject; include important domain terms |
| `project` | Stable project key recorded in the project map; reuse an existing key |
| `topics` | Short list of consistent topic names for navigation and filtering |
| `scope` | Where the content applies, including relevant subsystem, phase, conditions, or exceptions |
| `status` | The record lifecycle defined below |
| `occurred` | Source discussion or decision date/time; `null` when unknown |
| `created` | When this record was first saved |
| `updated` | When its content or lifecycle last changed |
| `sources` | References supporting the summary or decision, including acceptance when applicable |

The identity is `(project, id)`, independent of filename and title. Reuse
existing ADR identifiers and project conventions. For new records, a project
SHOULD use readable numbered IDs such as `DISC-0001` and `DEC-0001`. Allocate
unused IDs, and preserve them across moves, edits, and retirement. Resolve
duplicate IDs before claiming a save complete; no global registry is required.

Use ISO 8601 dates; include an offset or `Z` when recording a time. Preserve
source chronology separately from save time. A historical backfill MUST NOT
invent a decision date, participant, reason, acceptance, or source reference.
Record missing evidence explicitly.

Source references SHOULD include a durable message, document, or discussion
entry locator. When a source cannot be accessed later, retain enough permitted
context to understand the proposal and response and state the limitation.
A bare "yes" is insufficient evidence without the proposal it answers.
Use relative Markdown paths with stable anchors for local references. An ID
reference MUST resolve through the Project Journal's links; qualify it with
the project key when it refers to another authorized project.

When more than one location could own a source or record, state the candidate
owners, applicable scope, and unresolved conflict explicitly. Do not silently
choose an owner from recency, filename, or similarity alone.

### Discussion records

A discussion record has status `open` or `closed`; either MAY contain accepted,
rejected, or unresolved individual outcomes. Group related discussion by
coherent topic, with separately dated entries and stable entry anchors.

Each entry MUST preserve its question or purpose, material options and reasons,
constraints, outcomes linked by decision ID, remaining questions, and sources.
Summarize what was actually discussed. Distinguish an agent's suggestion from
the user's instruction and from an accepted choice.

An optional overview can orient the reader, but its decision statements MUST
link to the owning records. Add a dated follow-up when an open question is
resolved. An older recommendation MUST retain its dated meaning and gain a
link to the resulting decision, identifying any unresolved remainder, so
retrieving that entry alone cannot present it as the latest open choice.

### Decision records

A decision record MUST preserve one independently changeable choice, its exact
scope and conditions, the reason given, important alternatives and why they
were not chosen, its source, and links to affected design or operating rules.
Short decisions MAY use a few paragraphs; significant architectural choices
SHOULD use an ADR with context, decision, and consequences.

Decision status is `proposed`, `accepted`, `rejected`, `withdrawn`, or
`superseded`. Record the authority and evidence for acceptance in the record.
Keep a dated lifecycle entry for acceptance and each later status change,
including its source. Preserve an explicitly different effective date when
given; use `unknown` for historical event dates that cannot be recovered.
A proposal's age, an assistant's recommendation, or its presence in a design
document MUST NOT establish acceptance.

Interpret confirmation against the specific proposal or clearly identified
bundle it answers. Accept only the confirmed scope. Ask a focused question
only when the existing context cannot resolve a material ambiguity; do not
request confirmation again for an already clear decision.

## Direct record editing and alignment

1. **Locate:** Read the Project Journal map and the relevant topic's decisions,
   open questions, and design owners. Extend a matching discussion instead of
   creating a duplicate. Split independently changeable choices into records.
2. **Record:** Save the meaningful discussion and exact outcomes. Once the user
   confirms a choice, record its acceptance and source before moving to another
   topic or ending the recording turn. A temporary note MUST NOT remain its
   only saved copy until some later cleanup.
3. **Align:** Update the affected Architecture or Specification and close or
   annotate earlier proposals, recommendations, and open questions. Update
   navigation links and Current's follow-through status in the same session.
   Preserve unrelated content and manual edits.
4. **Verify:** Read back the affected records. Check the approved scope, source,
   lifecycle, replacement links, design wording, remaining questions, and
   reachable index entries against the instruction. Report the saved outcome
   and any unfinished synchronization explicitly.

A complete authoritative save means the records and necessary document updates
are saved, consistent, and findable from the Project Journal after the Record,
Align, and Verify steps. If interruption, conflicting edits, or a missing
decision prevents alignment, preserve the accepted record and list the exact
pending owner updates in Current. Report a partial save; do not silently
downgrade the decision or claim all records are synchronized. An optional
search-index update MAY follow later without blocking the save.

In repository mode, direct edits MUST stay within the user's or project's
authorization and the mapped project files. In managed or vault mode, use the
project's established adapter or runtime and adopted local policy for writes.
This guide does not invent commands, choose arbitrary paths, or silently fall
back to direct file writes when that adapter is unavailable. An adapter policy
MAY control transport, permissions, and placement, but it MUST preserve the
record metadata, lifecycle, source evidence, relationship, retention, and
alignment semantics in this guide. If a policy or adapter conflicts with those
semantics, record the conflict and pending owner explicitly.

Keep three meanings separate:

| Meaning | Owner | Example |
|---|---|---|
| Decision status | Decision record | `accepted` |
| Documentation alignment | Current, linked to the decision and affected owners | `pending`, `synced`, or `not-applicable` |
| Implementation progress | Current, with relevant verification evidence | `not-started`, `in-progress`, `implemented`, `verified`, or `not-applicable` |

An accepted decision with pending implementation stays accepted. Identify any
unsettled detail separately instead of labelling the entire direction proposed.
A draft design MAY contain accepted decisions alongside explicit open design.
When the design has not caught up, report the accepted target and the stale
document separately; stale design text does not reverse acceptance.
Readiness and deployment claims remain governed by the project's own checks.

## Runtime capture and handoff

Runtime capture is a transport concern separate from direct record editing. A
raw-capture acknowledgement means that content was received or queued for
processing. It remains pending processing and MUST NOT be reported as a
completed Journal save. A receipt, queue entry, or handoff status does not by
itself establish record metadata, acceptance, alignment, source ownership, or
verification.

The managed system's processor MUST perform the same Locate, Record, Align,
and Verify work before the result is a completed Journal record. Its agent
adapter supplies the authorized input and reports the returned state; it does
not become a second record writer or processor. If processing fails, is
interrupted, or cannot resolve the mapped owner, retain the pending status and
report the exact follow-through rather than claiming completion.

Use only the interface declared by the project for that operation. If no
supported wait or processing command exists, report the returned pending state.
Ordinary repository journaling needs no runtime. Each project's adoption owns
its deployment, rule locations, and integration mechanics.

## Decision changes and history

A change to an accepted choice MUST create a new decision record that preserves
what changed, why it changed, the applicable scope, and evidence of acceptance.
Keep the original choice, rationale, important alternatives, and dated
discussion accessible. A wording correction that preserves meaning MAY update
the existing record; note a correction that affects historical interpretation.
Returning to a previously rejected or replaced option also creates a new
decision, with the new reason and acceptance linked to that earlier history.

For a complete replacement, the new record lists the old ID in `supersedes`.
After acceptance, mark the old record `superseded` and add `superseded_by` with
the replacement ID. For a partial change, use `amends` and `amended_by`, state
the affected clauses or scope, and leave the unaffected original in force.
Relationship fields contain lists of qualified IDs or local record links.
Proposed changes MUST NOT retire an accepted choice.

If acceptance is clear but its relationship to an older choice is ambiguous,
preserve both records and flag the unresolved relationship. Obtain the missing
scope or replacement decision before presenting one as the sole applicable
rule. Dates and similarity alone cannot resolve this ambiguity.

Discussion history and superseded or rejected decision records MUST remain
retrievable for the project's lifetime unless an explicit retention, privacy,
or legal requirement authorizes their removal. An overview MAY be condensed;
it MUST NOT replace or erase the retained dated history and reasons. Follow
the [growth rules](#keeping-a-growing-journal-usable) when splitting files.
An archive move changes location, not decision identity or authority.

Material in the configured disposable context location MAY be retired after
its durable discussion and decision content has been recorded and checked,
or review has established that nothing durable needs retention.

## Retrieval without a database

The Project Journal MUST provide a concise topic index linking to records and
their design or operating-rule owners where applicable. A small project's
headings and links can serve as this index. Larger projects MAY use discussion
and decision indexes. Index summaries are navigation aids; read the owning
record to establish status and scope.

Readers and agents SHOULD begin with the mapped journal entry point, use
Current when resuming work, and follow the relevant topic links. For large
files, locate headings or search matches before reading the relevant sections.
Routine recall MUST NOT require loading the whole journal. Widen the search
when evidence is missing or conflicting, or the user requests a broader review.

For each lookup:

1. Establish the project, topic, and intent: current rule, original reasoning,
   change history, or possible conflict. Read only authorized project material.
2. Use the topic index, identifiers, links, and ordinary text search. Include
   earlier names and related constraints when the question requires them.
3. Read complete relevant decision records, matching dated discussion entries
   with their parent metadata, linked amendments or replacements, and the
   owning design. Compare scope, acceptance, and time.
   For an "as of" question, use the state and events applicable at that date.
4. Answer with record IDs and source links. State current applicability and
   distinguish recorded reasons from inference. Report missing source material,
   unclear relationships, or documents still awaiting synchronization.

Before recommending a change on a resumed topic, check its accepted decisions.
Before saying something remains undecided, check for a later recorded outcome.
If two accepted records conflict, expose the conflict instead of silently
choosing one. Retrieval is read-only unless the user also requests an update.

A conflict check MUST state what records or scope it covered. A result such as
"no conflict found in the reviewed records" does not establish that all lifetime
history was examined. Missing replacement metadata is a review lead, not proof
of an accidental contradiction.

## Optional indexes and RAG

Projects MAY add file indexes, full-text search, or semantic retrieval. The
Markdown records MUST remain readable and searchable without that service.
Generated indexes are replaceable projections, kept in an ignored local
location or an explicitly selected external service. They do not own decisions.

An indexer MUST retain the record's project, ID, type, topic, scope, status,
chronology, relationships, and source locator, together with a fingerprint of
the indexed source content. Each retrieved chunk MUST identify its parent
record and section or entry. Preserve sufficient scope and status with the
chunk; retrieve the full record and related decisions before judging a conflict.

Refresh changed records and detect moved or removed sources. On retrieval,
verify index hits against current source content; refresh stale hits or fall
back to source-file search. A missing or failed index MUST NOT prevent reading
saved history or turn an accepted decision into an unknown one.

Topic similarity helps find candidates; it does not prove acceptance,
applicability, supersession, or complete search coverage. Searches across
projects and indexing by an external service require the applicable access
and retention authority. This guide does not require embeddings, a database
product, a background service, or new software merely to follow it.

## Compact examples

These illustrative records show content and relationships, not accepted rules
for an adopting project. A shared Markdown file can carry the same metadata
inside each identified section instead of separate file frontmatter.

```yaml
id: DEC-0014
kind: decision
title: Store agent note captures in Inbox Notes
project: example
topics: [capture, routing]
scope: Agent-created note captures; external web clipping excluded
status: accepted
occurred: 2026-09-14
created: 2026-09-14T09:00:00Z
updated: 2026-09-14T09:00:00Z
sources: ["DISC-0003#entry-2026-09-14-01"]
supersedes: [DEC-0008]
```

The body states the choice and recorded reason: agent note captures go to
`Inbox/Notes/` so `Inbox/Raw/` can be reserved for external capture tools. It
identifies the confirmed proposal and response and links the owning data
design. `DEC-0008` keeps the original routing and reason, gains
`status: superseded` and `superseded_by: [DEC-0014]`, and remains searchable.
Current separately reports that the design is synchronized but implementation
is not started. A question about why routing changed follows both records.

````markdown
### DISC-0003: Agent capture routing

```yaml
id: DISC-0003
kind: discussion
title: Agent capture routing
project: example
topics: [capture, routing]
scope: Agent note capture
status: closed
occurred: 2026-09-14
created: 2026-09-14T08:30:00Z
updated: 2026-09-14T09:00:00Z
sources: ["retained proposal and confirmation excerpt"]
```

#### Entry 2026-09-14-01

Discussed separating agent notes from external clipping. The user confirmed
Inbox Notes for agent captures while retaining Inbox Raw for external tools.
Outcome: DEC-0014. The earlier recommendation is resolved by that decision.
The exact processing schema remains a separately tracked open design question.
````

## Check the recording flow

Use ordinary document review and relevant project checks. A focused trial
SHOULD confirm that a short acceptance updates the correct choice, an
unimplemented choice stays accepted, a replacement preserves both reasons,
and retrieval can find original and current decisions without an index.
Existing projects SHOULD reconcile important retained outcomes and flag
unrecoverable evidence explicitly rather than inventing a complete history.
