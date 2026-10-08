# Install Owen Burnett Officecraft in Claude

Install the operator and reviewer as two separate skill archives. Each archive must keep one direct skill root; do not unzip and recombine their contents.

## Before you begin

You need a Claude environment that supports installing skills and permission to add them. Download the matching **complete release ZIP** from [Release downloads](https://github.com/Stunspot/owen-burnett-officecraft/releases), then extract it. Repository source alone does not supply the generated Claude archives.

Open the extracted folder containing `release-manifest.json` and the top-level `START-HERE.md`. This is the **package root**. Its `claude/` folder contains:

```text
claude/
  owen-burnett-officecraft-v0.2.0.zip
  officecraft-reviewer-v0.2.0.zip
```

If you reached this guide inside `source/owen-burnett-officecraft-v0.2.0/docs/`, return to that package root before looking for `claude/`. Keep each inner skill ZIP intact for installation.

## Install

1. In your Claude environment, open its skill-installation workflow.
2. Add `owen-burnett-officecraft-v0.2.0.zip` as one skill.
3. Add `officecraft-reviewer-v0.2.0.zip` as a second skill.
4. Start a new conversation or task after the host reports installation.
5. Give a small office-production request, then confirm the host selected an appropriate route before relying on it for a consequential job.

## Expected archive shape

Each archive should contain one top-level folder named for the installed skill. The operator and reviewer are deliberately separate so the reviewer can examine a job without depending on the operator's hidden context.

## Confirm the installation honestly

An uploaded archive is not evidence that the skill is discoverable, invoked, able to create the requested artifact, or able to inspect its result. Confirm those steps in order. If compatible file creation is available, Officecraft should create the editable file and report the checks actually performed. Missing rendering or inspection leaves a named inspection gap; it does not prevent creation. Only when file creation itself is unavailable should Officecraft provide a source-ready production specification.

Use [Troubleshooting and recovery](TROUBLESHOOTING.md) when the host cannot install the archive or lacks the requested route.


For matched-version updating, removal, rollback, and retained-data cleanup, read [Lifecycle](LIFECYCLE.md).

## Version 0.2 continuation

Before replacing an older installation, preserve the original skill archives and your Officefiles. Install both matched 0.2 archives; do not mix the new operator with the previous reviewer. Existing version 1 project records require [copy-first migration](MIGRATION-AND-REVIEW.md). Installation does not convert or approve user work.
