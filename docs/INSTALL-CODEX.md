# Install Owen Burnett Officecraft in Codex

Install the operator and the reviewer as separate skills. Do this only on a Codex host you control.

## Before you begin

You need this repository or the matching GitHub release, permission to add user skills on the target machine, and a way to start a fresh Codex task after copying the skills. Installation is local setup; it does not connect accounts, modify an existing office file, or send anything externally.

The repository and complete release archive contain these two direct skill folders:

```text
codex/
  owen-burnett-officecraft/
  officecraft-reviewer/
```

## Install

1. Locate the target Codex user skill folder. On a default Windows setup this is commonly `C:\Users\<your-user>\.codex\skills`; use the active host's documented skill location if it differs.
2. Copy the complete `owen-burnett-officecraft` folder into that location. Keep the folder name unchanged.
3. Copy the complete `officecraft-reviewer` folder into that same location. Keep the folder name unchanged.
4. Start a new Codex task so the host can discover the newly copied skills.
5. Ask for a small office-production job in ordinary language, such as the request in [First Officecraft job](FIRST-JOB.md).

## Confirm the installation honestly

Do not call the installation active merely because the folders exist. In a fresh task, confirm that the host can select or invoke the intended skill for a relevant request. Then distinguish:

- folders copied;
- skill discovered;
- skill invoked;
- requested artifact route available;
- artifact actually created and inspected.

If the skill does not appear or does not route the job, preserve the copied folders, record the host/version and symptom, then follow [Troubleshooting and recovery](TROUBLESHOOTING.md). Do not delete unrelated skills to make room.

## What Codex may use

When the active Codex host exposes applicable document, presentation, spreadsheet, PDF, or connected-native capabilities, Officecraft may route a job through them. Those capabilities remain host dependencies. The Officecraft release does not include, copy, or redistribute bundled OpenAI office skills.

The availability of an installed host capability is not a claim that a particular document, deck, workbook, PDF, connector, or renderer will work in every Codex installation.


For matched-version updating, removal, rollback, and retained-data cleanup, read [Lifecycle](LIFECYCLE.md).
