# PLS Operations

## Release bundle

Use the complete `pls.zip` asset from [GitHub Releases](https://github.com/brightskye/pls/releases).
It contains:

```text
pls/
  install.py
  README.md
  LICENSE
  release.json
  skills/pls/
    SKILL.md
    references/PLS.md
```

The maintained skill and rules stay in `src/pls/`, and the installer source
stays in `tools/pls_skill.py`. These are copied into the release; users do not
need a development checkout or a separate installer download. Generated ZIPs
and checksums use ignored `releases/<version>/` locally and GitHub Releases
for distribution. The standard remains a working draft. Bundle versions such
as `0.3.0-draft.1` identify packaged revisions of that draft.

The first complete bundle,
[`v0.3.0-draft.1`](https://github.com/brightskye/pls/releases/tag/v0.3.0-draft.1),
is published and tested. `0.3.0-draft.2` is being prepared and is not yet
published or a verified release. See the [Project Record](project-record.md)
for the verification results and limits.

## Install with Python

Download and extract `pls.zip`. From the target project's root, run the
extracted bundle's installer:

```bash
python3 /absolute/path/to/pls/install.py install
```

This copies the skill, rules, updater, instructions, release metadata, and
license into `.agents/skills/pls/` without network access. It requires Python
3.10 or newer, with no Node.js, Git, or extra Python packages. On Windows,
`py -3` can replace `python3` when using the Python launcher. The extracted
bundle is no longer needed after installation.

The managed directory contains the complete Python route:

```text
.agents/skills/pls/
  SKILL.md
  references/PLS.md
  install.py
  README.md
  LICENSE
  release.json
  .pls-install.json
```

For a different location, pass `--dest` with the parent skills directory; the
installer creates or updates its `pls/` child there. Other agent hosts may use
different skill locations; use the path documented by that host.

The installed `.pls-install.json` records the release, source commit, file
hashes for every installed bundle file, and update selection. Keep this
generated receipt unchanged; it is the baseline for detecting local edits. The
installer refuses to overwrite an existing path during installation, or update
an unmanaged or edited copy.

Use one installation method for each copy. A source or `npx` installation,
or a symlink, keeps its original update route and does not include this
updater. Do not run two installers on the same destination at once.

## Update a Python installation

Run the updater installed in the managed directory:

```bash
python3 /absolute/path/to/project/.agents/skills/pls/install.py update
```

The updater resolves the managed directory from its own installed path, so this
command works even when the current working directory is elsewhere. Pass
`--dest` to override that location. It downloads the newest published PLS
release bundle and checks its SHA-256 checksum before replacing every managed
file, including the skill, instructions, release metadata, license, and
`install.py` itself. It does not fetch `src/pls` or read a local PLS checkout.
Updates require HTTPS access to GitHub. The newest published bundle may be a
working-draft prerelease; unpublished GitHub drafts are excluded. Updating is
always an explicit operation.

To select a release and keep subsequent updates pinned to it:

```bash
python3 /absolute/path/to/project/.agents/skills/pls/install.py update --release v0.3.0-draft.2
```

Use `--release latest` to follow new published bundles again. To update offline,
download and extract the desired bundle, then select it explicitly:

```bash
python3 /absolute/path/to/project/.agents/skills/pls/install.py update --bundle /absolute/path/to/new/pls
```

`--bundle` also accepts a release ZIP. A pinned installation remains pinned
to the newly selected bundle after an offline update; a latest-following
installation continues to follow latest.

The tool stages the complete replacement first. Changed, added, missing, or
symlinked installed files stop the update. Failed downloads leave the old copy
in place. If replacement fails, restoration is attempted; if restoration also
fails, the error names the preserved original directory. An unchanged package
reports that it is already up to date. The updater itself is replaced as part
of a successful update, so later runs use the new bundle's behavior. The
downloaded or extracted update bundle is no longer needed after the update.

To migrate an unchanged Python installation from the published draft.1 bundle
to the new bundled installer, download and extract the new bundle, then run its
installer once from the target project:

```bash
python3 /path/to/new/pls/install.py update --bundle /path/to/new/pls
```

The migration replaces the old managed directory only after checking its
receipt and local files. A Python-managed `--ref` installation can use this
same explicit bundle migration. Unmanaged source, `npx`, and symlink
installations keep their original update routes.

Installing or updating the skill does not change a project's recorded PLS
version or reorganize its files. A human must accept that adoption separately.

## Install a bundle with npx

With Node.js/npm available, use the release asset URL:

```bash
npx skills@latest add https://github.com/brightskye/pls/releases/download/v0.3.0-draft.1/pls.zip --skill pls --agent codex
```

The [skills CLI](https://github.com/vercel-labs/skills) installs the skill found
inside the ZIP. Add `--global` for a user-wide copy or use another supported
agent name as needed. This route installs the skill payload only; it does not
include the Python updater or the bundle's outer files.

The checked CLI version, 1.5.23, does not put archive installs in its lock file.
Therefore `npx skills update pls --project` cannot update this installation.
To use a newer release, preserve local edits and rerun `add` with the new
release asset URL. Use Python when release tracking and a dedicated update
command are wanted.

## Use the installed skill

The installed directory must contain `SKILL.md` and `references/PLS.md`.
Codex can select the skill when its description matches the request; in CLI or
the IDE extension, `$pls` selects it explicitly. If the skill does not appear,
restart the agent. See the official
[Build skills guide](https://learn.chatgpt.com/docs/build-skills) for discovery
locations and behavior.

```text
$pls scaffold this new project
$pls review this project's structure
$pls reorganize this project using PLS
$pls tell me where this release package belongs
```

Review is read-only unless changes are requested. Scaffold creates only needed
areas. Reorganize improves the recorded layout; adopting a different version
requires human acceptance. The bundled standard owns placement and adoption
rules. PLS does not introduce a separate scaffold command or linter.

## Development and older installations

Direct `src/pls/` installation remains available for development. The old
standalone Python tool's `--ref` route still downloads a Git branch, tag, or
commit. Such installations keep their saved ref unless changed explicitly and
do not include the bundled updater. A Python-managed `--ref` installation can
be migrated with the explicit `update --bundle` command above. The complete
Python bundle route is the single-folder installation described above.

A Git source installation made with `npx` keeps using its existing Git update
route. CLI 1.5.23 supports branch/tag URLs but not raw commit SHAs. A local-path
CLI install needs `add` again to refresh it. These are source installations,
not release bundle installations.

For an intentional development symlink, point the host's `pls` skill path at
`/absolute/path/to/pls/src/pls`. A link to the former `deploy/pls/` must be
repointed; inspect it first. Older pinned Git revisions retain their original
layout. Update a linked `main` checkout with:

```bash
git -C /absolute/path/to/pls pull --ff-only
```

A source link makes checkout changes immediately visible to every project
using it. Release bundle installations are independent copies.

## Build and publish a bundle

From a clean, committed PLS checkout:

```bash
python3 -m unittest discover -s tests -v
python3 tools/build_release.py --version 0.3.0-draft.1
```

The builder writes `releases/0.3.0-draft.1/pls.zip` and `pls.zip.sha256`, records
the source commit, and refuses to overwrite an existing version output.
`--output-dir` selects another build output location. Only the skill package,
installer, license, generated instructions, and release metadata are included.
The same inputs produce the same ZIP bytes.

After committing and pushing the desired source, publish a matching new tag:

```bash
git tag v0.3.0-draft.1
git push origin v0.3.0-draft.1
```

The [release workflow](../.github/workflows/release.yml) runs the tests, builds
the ZIP, and attaches it and its checksum to a GitHub prerelease. It uses the
repository-scoped GitHub Actions token; no personal token or credentials are
bundled. Do not reuse an existing release tag or replace its assets. Choose a
new bundle version for changed contents.

## Verification and release status

Use the maintained installer and bundle tests, plus `git diff --check`.
Before declaring a new bundle usable, extract it outside the checkout, install
without network access, verify the installed bytes, and check updates and
local-edit protection. Check the published release download after publication.
The Project Record records current results and limitations.

A working-draft bundle is not a stable PLS standard release. Stable promotion
remains a separate human decision. Existing adopting projects do not migrate
merely because a bundle was built or published.
