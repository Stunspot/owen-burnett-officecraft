# Install Owen Burnett Officecraft in Claude

Install the operator and reviewer as two separate skill archives. Each archive must keep one direct skill root; do not unzip and recombine their contents.

## Before you begin

You need a Claude environment that supports installing skills, this repository or the matching GitHub release, and permission to add skills to that environment. The expected archives are:

```text
claude/
  owen-burnett-officecraft-v0.1.1.zip
  officecraft-reviewer-v0.1.1.zip
```

## Install

1. In your Claude environment, open its skill-installation workflow.
2. Add `owen-burnett-officecraft-v0.1.1.zip` as one skill.
3. Add `officecraft-reviewer-v0.1.1.zip` as a second skill.
4. Start a new conversation or task after the host reports installation.
5. Give a small office-production request, then confirm the host selected an appropriate route before relying on it for a consequential job.

## Expected archive shape

Each archive should contain one top-level folder named for the installed skill. The operator and reviewer are deliberately separate so the reviewer can examine a job without depending on the operator's hidden context.

## Confirm the installation honestly

An uploaded archive is not evidence that the skill is discoverable, invoked, able to create the requested artifact, or able to inspect its result. Confirm those steps in order. If the current Claude environment has no compatible file-production or inspection tool, Officecraft should produce a source-ready production packet rather than pretend a DOCX, deck, workbook, or PDF exists.

Use [Troubleshooting and recovery](TROUBLESHOOTING.md) when the host cannot install the archive or lacks the requested route.


For matched-version updating, removal, rollback, and retained-data cleanup, read [Lifecycle](LIFECYCLE.md).
