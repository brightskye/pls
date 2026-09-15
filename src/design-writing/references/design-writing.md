# Design writing guide

These rules guide design documents for human and agent readers. They are
reusable across projects; the Orca example illustrates their application.
**Status:** Draft for review. This guide does not declare any system design
complete or implemented.

## Reader outcome and scope

The design set explains what the system achieves, how its parts cooperate, and
exactly how it operates within its stated scope. Implementation follows the
accepted design. Readers must be able to derive an implementation plan without
inventing missing system behavior.

Open with the problem, intended users, desired outcomes, scope, and important
constraints. Give enough context for someone who has not read the discussion.
Identify the design's status and link to its detailed specifications. Keep
actual implementation and verification status in the project's current record.

## Views and reading order

Start with orientation, then explain structure, behavior, and detail. Cover the
following questions across the design set. These are views, not required files
or an inflexible template. Link to each detail's owner instead of repeating it.

| View | Question to answer |
|---|---|
| Purpose and use cases | Who needs the system, what do they want to achieve, and what is outside scope? |
| System context | What is inside the system, what is external, and where are the important boundaries? |
| Components | What does each part own, receive, produce, and depend on? |
| Workflows | What triggers each operation, which parts act in what order, and when is it complete? |
| Data | What records exist, who owns them, and how are they validated, changed, retrieved, retained, and removed? |
| Interfaces | What exact commands, messages, formats, responses, and errors cross each boundary? |
| Deployment and operation | Where does each part run, how is it configured, and how does it recover from failure? |
| Acceptance | What observable results demonstrate that the use cases and constraints are satisfied? |

## Define operating behavior

**Rules:** State the responsible component, trigger, conditions, action, and
result. Specify defaults, precedence, state changes, and completion meaning
where they affect behavior. Define formats and decision logic in the owning
specification; examples illustrate the rules rather than replacing them.\
**Failures:** Cover relevant invalid input, partial completion, retries,
interruption, and recovery. Explain what remains durable, what can safely run
again, and what the caller sees. Include concurrency and duplicate handling
when operations can overlap or repeat.\
**Constraints:** Make performance, capacity, reliability, privacy, and access
requirements concrete where they affect the design. Give measurable conditions
and how to check them. Do not invent targets; mark missing decisions explicitly.\
**Semantic processing:** When a model makes decisions, define its evidence,
allowed outputs, decision rules, uncertainty handling, and validation. Include
representative examples and counterexamples. "Use an LLM to classify it" leaves
the behavior unspecified.

## Connect use cases to behavior

A user story states the actor, goal, and benefit. Expand each core story into
a use case with its trigger, required context, normal path, important alternate
or failure paths, and observable outcome. Link it to the responsible workflow
and specification, then to its acceptance checks. Lightweight identifiers or
section links are enough; a separate traceability system is unnecessary.

**Orca example:** A user saves a supplied link so they can revisit it later.
The following target behavior illustrates the writing rules. It is not a
complete request schema or a claim about current implementation.

| Part | Designed behavior |
|---|---|
| Input | Preserve the supplied URL and any requested accompanying text. |
| Handoff | The Adapter submits the selected input to Runtime. |
| Durable capture | Runtime stores the JSON capture in `Inbox/Notes/` and persists the processing task. |
| Success | Acknowledge saved and queued only after both capture and task are durable. |
| Later work | Process the note in the background; archive the original only after required outputs are verified. |
| Failure | Capture persistence failure is not success. Later processing failure retains the captured input for recovery. |
| Boundary | Link saving does not authorize fetching or summarizing the page, or broad conversation profiling. |

A final specification must resolve the exact request, receipt, persistence,
and recovery contracts behind this example. A component diagram alone cannot
supply those details.

## Write for a reader following the system

**Purposeful prose:** Each section answers a reader question. Each paragraph
explains one rule, relationship, reason, or example. Put its main point first,
define unfamiliar terms when introduced, and order explanations so that their
prerequisites are already clear. Remove repetition and move supporting detail
to its linked owner. Each paragraph should be easy to summarize in one
sentence. Cut words that add no meaning while retaining the detail needed to
understand the design.\
**Presentation:** Use short paragraphs, tables for comparisons, and numbered
steps for sequences. Compact explanatory groups can use bold labels followed
by descriptions, one point per line, with blank lines around the group. Keep
related points together. Do not repeat a table in the prose after it.\
**Diagrams:** Include a system-context diagram and focused diagrams for major
interactions. Use flows for processing, sequences for timing and handoffs, and
state diagrams for lifecycle changes when useful. Keep each readable at normal
viewing size; split crowded diagrams instead of shrinking them.\
**Diagram meaning:** Use consistent component names and make arrow meaning
clear. Explain the diagram's takeaway and essential behavior in adjacent text.
Keep editable diagram sources with the design and update both together. Check
the rendered result; syntax validity alone does not prove readability.

## Decisions, open work, and implementation

State settled design directly. Keep a short reason beside a consequential
choice when it helps readers understand the solution. Link to a decision record
for detailed alternatives and chronology. Conversation attribution belongs in
history; actual authority and approval roles remain part of system behavior.

Mark proposals, assumptions, and open questions clearly. For unresolved design,
state the missing decision, its consequence, and what would resolve it. Drafts
can support a plan that includes design work. A final design for a declared
scope must resolve the behavior required to implement that scope.

Specify behavior, contracts, and consequential technical choices precisely.
Resolve choices that would be costly to reverse or would change component
boundaries, compatibility, or observable behavior. Explain the important
trade-offs. Internal coding choices may remain flexible where they preserve
those rules. A plan organizes tasks, dependencies, and verification; it does
not silently decide missing product behavior.

When implementation reveals a necessary design change, resolve it in the owning
design and update affected examples, diagrams, and acceptance checks. Follow the
project's existing decision authority. Record actual divergence in its current
record; do not silently treat code as approval for a changed design.

## Review before calling the design final

**Orientation:** Can a new reader explain the system's purpose and boundaries?\
**Operation:** Can they follow every core use case through components, data,
completion, and relevant failures without guessing?\
**Agreement:** Do terms, diagrams, examples, and linked specifications describe
the same behavior, with one owner for each rule?\
**Implementation:** Can tasks and acceptance checks be derived, and are all
behavioral decisions needed for the stated scope resolved?\
**Readability:** Does every section and paragraph serve a clear purpose, with
readable diagrams and no unnecessary repetition?

Review the complete affected reading path after meaningful changes. Formatting
checks and link checks support this review; they do not establish design
completeness. Do not add sections, documents, or process just to fill a template.
