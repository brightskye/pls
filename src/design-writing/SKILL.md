---
name: design-writing
description: >-
  Create, revise, or review software design documents for clear system views
  and precise operating behavior. Use when turning requirements or discussions
  into a design, restructuring an existing design, or assessing whether it
  supports implementation. Ordinary prose editing and code-only implementation
  are outside this skill.
---

# Design writing

Use the bundled [writing guide](references/design-writing.md) for the design
rules and examples. Read it when creating, restructuring, or reviewing a design
set; for a narrow correction, read the relevant sections. The guide works with
the target project's existing documentation layout. Its Orca example illustrates
behavioral precision; use the target project's own paths, rules, and authority.

## Establish the task

Read the target project's instructions and documentation map, then the supplied
requirements and relevant design owners. Distinguish accepted behavior from
proposals, assumptions, and current implementation. Follow the user's requested
scope and existing authorization when resolving uncertainty.

**Create:** Turn requirements and accepted decisions into a design that explains
the system and defines its operation. Select the views needed for its scope.\
**Revise:** Preserve settled behavior unless the requested change replaces it.
Update the affected explanations, contracts, examples, diagrams, and links in
their existing owners.\
**Review:** Report concrete omissions, contradictions, and readability problems
with their locations and effects on implementation. Review is read-only unless
the user requests edits.

## Write and check

Apply the guide's operating rules to the requested document or design set.
Connect core use cases to workflows, responsible components, data, completion,
relevant failures, and acceptance checks. Keep detailed rules in one owning
place and link the other views to them. Use focused diagrams that remain
readable when rendered and explain their essential meaning in text.

Resolve missing behavioral decisions with the available evidence or user input;
otherwise identify them as open design and continue independent work. A draft
may identify design work for a plan. A final design must resolve the behavior
needed for its declared scope. Implementation plans organize delivery; private
coding choices remain flexible within the specified behavior.

Review the complete affected reading path for consistent terms, behavior,
diagrams, and references. Run applicable documentation checks. For a full
design, confirm that an implementer can derive tasks and acceptance checks
without inventing system behavior. For a narrow revision, verify the requested
change and its affected links without expanding into unrelated design work.

Report the result and any concrete decisions still needed. Creating or editing
a design does not authorize implementation, installation, or publication.
