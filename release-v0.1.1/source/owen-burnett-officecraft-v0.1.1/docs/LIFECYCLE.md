# Update, remove, and clean up Officecraft

The two installed skills, Officefiles, generated artifacts, release downloads, host conversations, and connected-service copies are separate things. Removing one does not silently remove the others.

## Update the matched skills

1. Record the installed operator and reviewer versions.
2. Preserve Officefiles and customer artifacts outside the skill directories.
3. Download and verify the replacement release.
4. Back up both complete installed skill folders or uploaded-skill records.
5. Replace the operator and reviewer as one matched version; do not mix files between releases.
6. Start a fresh host task and verify discovery, explicit invocation, and one low-risk first job.

A copied folder or uploaded archive is not a completed update until the fresh host discovers and invokes the intended skills.

## Remove Officecraft

For Codex, move only `owen-burnett-officecraft` and `officecraft-reviewer` out of the active skill directory. For Claude, disable or remove those exact uploaded skills through the host's supported controls. Start a fresh task and confirm they are no longer listed or selected.

Removal does not delete Officefiles, produced documents, decks, workbooks, PDFs, exports, backups, host history, or provider-side records.

## Clean up retained data

Review each location separately:

- Officefile `sources/`, `state/`, `working/`, `output/`, `review/`, and `HANDOFF.md`;
- generated DOCX, PPTX, XLSX, PDF, CSV, Markdown, preview, and export files;
- source attachments, templates, brand assets, and backups;
- host conversation, upload, tool, and connector history;
- native Office or cloud-service comments, revisions, hidden content, and shared copies;
- downloaded release ZIPs and extracted skill folders.

Use recoverable deletion where practical. Confirm exact paths and shared destinations before deletion. Connected-service cleanup follows that service's retention and sharing controls; Officecraft has no remote deletion authority of its own.

## Roll back

Restore both previously recorded skill artifacts, start a fresh host task, verify discovery, and repeat one low-risk first job. File restoration alone does not prove discovery, invocation, file production, or healthy behavior.

Officecraft has no automatic updater, telemetry service, hosted account, background cleanup process, or support SLA.