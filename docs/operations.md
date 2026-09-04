# PLS Operations

## Deployment options

The `deploy/` directory contains PLS artifacts that can be installed or
distributed. Each option has its own focused directory.

The current option is [`deploy/pls/`](../deploy/pls/SKILL.md), a self-contained
agent skill. Its `SKILL.md` is a thin adapter and
`references/PLS.md` is the authoritative standard distributed with it. The
installed skill does not need the repository parent or network access to read
its rules.

## Install the agent skill for Codex

### Install directly from GitHub

Choose an immutable release tag or commit when reproducibility matters. Ask
Codex to install the self-contained directory from the public repository:

```text
$skill-installer install the skill from https://github.com/brightskye/pls/tree/<tag-or-commit>/deploy/pls
```

Use `main` in place of `<tag-or-commit>` only when intentionally following the
working draft. The installer downloads a local copy, so invoking PLS afterward
does not fetch rules from GitHub. Codex normally detects a newly installed skill
automatically; restart it if the skill does not appear.

### Install from a local clone

A clone-and-symlink installation is convenient for PLS development or an
explicit rolling update channel. Choose any location for the complete PLS
repository. Set these example variables to the real repository and user skill
directories, then create the link:

```bash
PLS_REPO_DIR=/absolute/path/to/pls
PLS_USER_SKILLS_DIR=/absolute/path/to/.agents/skills
mkdir -p "$PLS_USER_SKILLS_DIR"
ln -s "$PLS_REPO_DIR/deploy/pls" "$PLS_USER_SKILLS_DIR/pls"
```

Do not replace an existing path until you have checked what it contains. Codex
supports symbolic links for skill directories and follows their targets. Other
agent hosts may use a different skill directory; use the location documented
by that host.

### Verify either installation

Confirm that the installed skill contains both its entry point and standard:

```bash
PLS_INSTALLED_SKILL=/absolute/path/to/installed/pls
test -f "$PLS_INSTALLED_SKILL/SKILL.md"
test -f "$PLS_INSTALLED_SKILL/references/PLS.md"
```

The official [Build skills](https://developers.openai.com/codex/build-skills)
guide describes Codex skill discovery, Git repository installation, symlinks,
and supported locations.

## Use the agent skill

Codex can select the skill automatically when a request matches its
description. In Codex CLI or the IDE extension, `$pls` invokes it explicitly.

| Action | What it does | Changes files? |
|---|---|---|
| Scaffold | Creates the smallest useful structure for a new project. | Yes, when requested |
| Review | Explains how well an existing project follows PLS. | No, unless changes are also requested |
| Reorganize or adopt | Improves an existing project layout or adopts PLS. | Yes, when requested |
| Place | Chooses the right existing location for a new document or artifact. | Only when creation or movement is requested |

Examples:

```text
$pls scaffold this new project
$pls review this project's structure
$pls reorganize this project using PLS
$pls tell me where this deployment package belongs
```

Scaffolding does not create every default directory. Review is read-only unless
changes are requested. Reorganization improves the currently recorded layout.
Adoption preserves useful material while moving it to normal PLS areas and
names; an existing location remains only when a tool convention requires or
normally uses it, or the human explicitly chooses it as a mapped alternative.
It does not create evaluation or evidence areas merely to record the migration.
Maintained evaluation cases use the project's test layout; temporary
machine-local or sensitive output may use ignored `.local/`, while retaining
sensitive evidence requires an explicit human choice.

Product source contains only code delivered as the product or a supported
runtime capability. Evaluation-only runners belong with Tests, maintained
development automation belongs in Tools, and install or launch artifacts belong
in Deployment unless a project tool requires another arrangement.

Lint is not a separate PLS action. PLS review handles purpose, ownership, and
navigation. Existing project linters handle Markdown, source, configuration,
and link mechanics.

Installing or invoking the skill does not change a project's recorded layout
standard or version. A human must accept that migration first.

## Update the skill

An installation copied from GitHub is a snapshot. Select a newer release or
commit deliberately and use the agent host's supported replacement or reinstall
procedure. Do not replace an existing skill directory until its identity and
contents have been checked.

For a clone-and-symlink installation, review and update the clone. Following a
tag keeps the installed rules fixed; following `main` opts into the latest
working draft. A fast-forward update of an intentional `main` checkout is:

```bash
git -C "$PLS_REPO_DIR" pull --ff-only
```

The symlink uses the updated files without another copy step. Codex normally
detects skill changes automatically; restart it if an update does not appear.

Updating an installed skill does not change a target project's recorded PLS
version or authorize a structural migration. A human must accept that change.

## Remove a symlink installation

Before removing the installation, confirm that it is the expected symbolic
link. Then unlink it:

```bash
test -L "$PLS_USER_SKILLS_DIR/pls"
unlink "$PLS_USER_SKILLS_DIR/pls"
```

Removing the link does not remove the PLS repository.

For distribution through ChatGPT and Codex beyond direct Git installation, PLS
may later package the same skill as a plugin. The standalone skill remains the
source package for that option.

## Publication boundaries

PLS is distributed under the [MIT License](../LICENSE). A release tag must
match the version and status recorded by the bundled standard; the current PLS
v0.3 text remains a working draft until explicitly promoted.
