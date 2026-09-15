---
name: journal
description: Record, update, or retrieve a project's durable discussions, decisions, and change history. Use when a human asks to save or revise Journal material, or to find the current rule, original rationale, or recorded history. Retrieval is read-only.
---

# Use Journal

This skill uses the standalone [Journal guide](references/journal.md). The
guide is independent of PLS and Orca. Read its relevant sections for the
requested operation. Read the target project's root README,
agent instructions, and project map first; follow the mapped Journal entry
point, including an existing `project-record` location. Installing this skill
does not rename, move, or migrate existing records.

Use the requested operation:

- **Record:** save a meaningful discussion or decision, including its source,
  scope, status, and reasons. A clear acceptance applies only to the confirmed
  proposal or bundle.
- **Update:** revise an existing record or align its owning documents. Preserve
  prior decisions, reasons, and amendment or replacement links.
- **Retrieve:** read the mapped entry point and only the relevant records,
  links, and owners. Report IDs, current applicability, recorded reasons,
  source limits, and conflicts. Do not edit files, implement a decision, or
  treat retrieval as authorization to change anything.

For Record and Update, follow the guide's locate, record, align, and verify
flow. In repository mode, make authorized edits in the mapped project files.
In managed or vault mode, use only the project's established adapter or
runtime and adopted local policy. Do not invent commands or paths, silently
fall back to direct writes, or make an external service mandatory for ordinary
Journal use.

Keep direct record editing separate from runtime handoff. A runtime raw-capture
acknowledgement means that capture is queued or received and remains pending
processing; it is not a completed Journal save. A record is complete only when
the guide's record, alignment, and verification work is complete.
