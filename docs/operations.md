# PLS Operations

## Product package

The maintained product is [`src/pls/`](../src/pls/SKILL.md), a self-contained
agent skill. Its `SKILL.md` is a thin adapter and
`references/PLS.md` is the authoritative standard distributed with it. The
installed skill does not need the repository parent or network access to read
its rules.

## Install the agent skill

Choose one installation method for each installed copy. The skill and
`references/PLS.md` are installed and updated together. Neither method changes
the project's recorded PLS version or reorganizes its files.

The `src/pls/` package and Python tool are published on GitHub. A `main`
installation follows the working draft, not the latest stable GitHub release.

### With the skills CLI (Node.js)

From the target project's root, run:

```bash
npx skills@latest add https://github.com/brightskye/pls/tree/main/src/pls --skill pls --agent codex
```

This uses the existing [skills CLI](https://github.com/vercel-labs/skills),
which requires Node.js/npm and Git. The explicit GitHub folder URL selects the
self-contained package without moving it or copying the rules into another
source location. For a fixed version, replace `main` in that URL with a release
tag that contains `src/pls/`. The checked CLI version, 1.5.23, supports branch
and tag URLs but fails on a raw commit SHA. Use the Python route when an exact
commit is required.

The default is a project installation. Add `--global` for a user installation.
Use the CLI's agent option for other supported hosts. Its own lock file tracks
the source for updates; retain that file with the project installation.

### With the standalone Python tool

Download [`tools/pls_skill.py`](../tools/pls_skill.py) from GitHub and keep it
at a convenient local path. It is one standalone file and does not need a PLS
checkout, Node.js, Git, or third-party Python packages. It requires Python
3.10 or newer and HTTPS access to the public GitHub API and archive service.

From the target project's root, run the downloaded file:

```bash
python3 /absolute/path/to/pls_skill.py install
```

This installs the current `main` skill in `.agents/skills/pls/`. To select a
fixed Git version, add `--ref <tag-or-commit>`. To use a different agent's skill
location, set `--dest` to its **parent skills directory**; the tool creates
`pls/` inside it. For example, a user-wide Codex installation uses:

```bash
python3 /absolute/path/to/pls_skill.py install --dest ~/.agents/skills
```

On Windows, `py -3` can replace `python3` when using the Python launcher.
The download is resolved to one Git commit before the package is copied.
The installed `.pls-install.json` records that commit, the selected ref, and
file hashes so updates can detect local edits. It is installation metadata,
not a second copy of the rules or a project adoption declaration. Keep this
generated receipt unchanged; it is the baseline for the local-edit checks.

The tool refuses an existing destination. It does not replace copied,
symlinked, or `npx`-managed installations. Keep using their original updater,
or preserve and move the old installation before switching methods. Do not
run two installers against the same destination at once.

### With Codex's built-in installer

Choose an immutable release tag or commit when reproducibility matters. Ask
Codex to install the self-contained directory from the public repository:

```text
$skill-installer install the skill from https://github.com/brightskye/pls/tree/<tag-or-commit>/src/pls
```

Select a revision that contains `src/pls/`. Revisions before the source-layout
migration use `deploy/pls/` instead.

Use `main` in place of `<tag-or-commit>` only when intentionally following the
working draft. The installer downloads a local copy, so invoking PLS afterward
does not fetch rules from GitHub. Codex normally detects a newly installed skill
automatically; restart it if the skill does not appear.

This installer uses Python, but it refuses an existing destination and does
not provide the update behavior of the standalone PLS tool.

### Install from a local clone

A clone-and-symlink installation is convenient for PLS development or an
explicit rolling update channel. Choose any location for the complete PLS
repository. Set these example variables to the real repository and user skill
directories, then create the link:

```bash
PLS_REPO_DIR=/absolute/path/to/pls
PLS_USER_SKILLS_DIR=/absolute/path/to/.agents/skills
mkdir -p "$PLS_USER_SKILLS_DIR"
ln -s "$PLS_REPO_DIR/src/pls" "$PLS_USER_SKILLS_DIR/pls"
```

Do not replace an existing path until you have checked what it contains. Codex
supports symbolic links for skill directories and follows their targets. Other
agent hosts may use a different skill directory; use the location documented
by that host.

### Verify an installation

Confirm that the installed skill contains both its entry point and standard:

```bash
PLS_INSTALLED_SKILL=/absolute/path/to/installed/pls
test -f "$PLS_INSTALLED_SKILL/SKILL.md"
test -f "$PLS_INSTALLED_SKILL/references/PLS.md"
```

The official [Build skills](https://learn.chatgpt.com/docs/build-skills)
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
$pls tell me where this release package belongs
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

For product source, configuration, build and installer scripts, and complete
versioned packages, follow the standard
[Project areas](../src/pls/references/PLS.md#6-what-each-project-area-is-for).

Lint is not a separate PLS action. PLS review handles purpose, ownership, and
navigation. Existing project linters handle Markdown, source, configuration,
and link mechanics.

Installing or invoking the skill does not change a project's recorded layout
standard or version. A human must accept that migration first.

## Update the skill

### Skills CLI installation

From the target project's root:

```bash
npx skills@latest update pls --project
```

For a global installation, replace `--project` with `--global`. The update
follows the recorded source. To choose a different branch or tag, rerun the
scoped `add` command with that revision in the GitHub URL. Preserve any local
edits before using the CLI to replace the installed skill.

### Python installation

From the target project's root:

```bash
python3 /absolute/path/to/pls_skill.py update
```

Use the same `--dest` as installation when it was customized. Without
`--ref`, updates keep the previously selected branch, tag, or commit. An
installation pinned to a commit stays there. To change versions deliberately:

```bash
python3 /absolute/path/to/pls_skill.py update --ref <tag-or-commit>
```

The tool checks the existing receipt and files, downloads and stages the full
replacement, then replaces the installed directory. Edited, added, missing,
or symlinked files stop the update. A failed download leaves the old copy in
place. If replacement fails, the tool attempts to restore it; if restoration
also fails, the error names the preserved original directory. An unchanged
installation reports that it is already up to date.

Updates refresh the installed skill and rules, not the downloaded Python
tool itself. Download a newer tool explicitly when its behavior needs updating.

### Copied or clone-and-symlink installation

After the source-layout migration, a local symlink targeting `deploy/pls/` must
be repointed to `src/pls/` using the installation and removal procedures in this guide. Inspect
the link first and preserve any copied installation or local changes. Copied
skill installations remain usable at their existing version until deliberately
reinstalled. Older pinned Git revisions continue to use their original path.

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

## Check changes to the distribution tool

Run the maintained installer tests from the PLS repository root:

```bash
python3 -m unittest discover -s tests -v
git diff --check
```

The tests use real skill files and temporary installations, with GitHub
responses substituted locally. They check installation, updates, version
selection, local-edit protection, archive paths, and failure recovery.
They do not prove that an unpublished GitHub revision can be installed. After
publishing a layout or installer change, check both GitHub installation routes
and their updates in temporary projects before announcing them as ready.

On 2026-09-06, both GitHub installation routes passed against publication
commit [5ec1c115616c664b00f2d6850584bf5bfe6a4f18](https://github.com/brightskye/pls/commit/5ec1c115616c664b00f2d6850584bf5bfe6a4f18)
in temporary WSL projects. Literal `npx` installation from `src/pls/` and
`update pls --project` passed using `skills` 1.5.23; its lock retained the
repository, `main` ref, and nested skill path. The standalone Python tool was
downloaded from that commit and passed installation, unchanged update, exact
commit pinning, and local-edit protection checks. Both routes installed files
that matched the published skill and rules. The target project's recorded
standard stayed unchanged in the Python check. All 11 installer tests passed.

A local-path CLI install must be refreshed by rerunning `add`; its `update`
command needs a tracked remote source.

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
