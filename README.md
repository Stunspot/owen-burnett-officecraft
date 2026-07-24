# Owen Burnett Officecraft

**Bring the rough notes. Leave with an office packet that still agrees with itself.**

Owen Burnett Officecraft is a free, dual-host occupational Augment for turning workplace material into coherent documents, presentations, spreadsheets, PDFs, and coordinated deliverable families. It combines an office-production operator with an independent reviewer and a resumable **Officefile** project record.

## Start with one useful job

Install both matched skills, start a fresh task, and ask naturally:

```text
Use Owen Burnett Officecraft.

Turn these meeting notes into a concise decision memo for leadership.
Preserve the supplied facts, show any unresolved conflicts, and leave me with
an editable source plus a delivery-ready PDF if the active host supports both.
```

Officecraft should identify the available artifact route, keep claims within the supplied evidence, and distinguish a source-ready production packet from files that were actually created and inspected.

Continue with [Start here](START-HERE.md) for installation, a first job, verification, and recovery.

## What ships

- `codex/owen-burnett-officecraft/` — the office-production operator;
- `codex/officecraft-reviewer/` — the independent evidence reviewer;
- `claude/` — one installable Claude skill archive for each capability;
- `docs/` — installation, first-job, Officefile, troubleshooting, provenance, and readiness guidance;
- the [`v0.1.0` release](https://github.com/Stunspot/owen-burnett-officecraft/releases/tag/v0.1.0) — complete and per-skill archives with SHA-256 custody.

Install the operator and reviewer as a matched version. The reviewer examines the supplied job record and evidence; it does not silently approve publication, delivery, or unsupported quality claims.

## What Officecraft adds

- routes a request to document, presentation, spreadsheet, PDF, or coordinated-packet work;
- stabilizes names, dates, figures, units, conclusions, and requested actions across artifacts;
- preserves substantial work in a resumable Officefile rather than relying on chat memory;
- keeps editable sources, derivatives, review evidence, and delivery authority distinct;
- degrades honestly when the current host lacks a renderer, native application, connector, or file-production route;
- challenges the finished packet through a separately installable reviewer.

## Installation

- [Install in Codex](docs/INSTALL-CODEX.md)
- [Install in Claude](docs/INSTALL-CLAUDE.md)
- [Run the first Officecraft job](docs/FIRST-JOB.md)
- [Troubleshoot or recover](docs/TROUBLESHOOTING.md)

The repository publishes standalone Codex and Claude skills. A Codex plugin and public Directory submission are deliberately deferred for this release; repository publication does not imply marketplace submission, approval, discoverability, or installation.

## Evidence boundary

The v0.1.0 packages passed deterministic structure, schema, path-safety, archive, link, and Officefile tests in the recorded release environment. Bounded behavioral evaluations also exercised selected prompt-level cases. These receipts support package and bounded-behavior claims only.

They do not establish:

- universal host discovery or activation;
- native Office rendering or spreadsheet recalculation;
- formal accessibility conformance;
- representative-user success;
- broad reliability across hosts and document types;
- approval to send, publish, upload, overwrite, or connect an account.

Read [Verification and readiness](docs/VERIFICATION-AND-READINESS.md) before carrying a stronger claim into customer work.

## Support, privacy, and security

Use [GitHub Issues](https://github.com/Stunspot/owen-burnett-officecraft/issues) for sanitized defects and documentation problems. Do not attach customer documents, credentials, private Officefiles, unredacted screenshots, or proprietary templates.

- [Support and recovery](SUPPORT.md)
- [Security policy](SECURITY.md)
- [Host capabilities and evidence](docs/HOST-CAPABILITIES-AND-EVIDENCE.md)

Officecraft operates inside the capabilities and data practices of the active Codex or Claude host. A local skill package does not make the surrounding host local, private, or authorized to receive sensitive material.

## Provenance and license

This public repository is a fresh customer/source history assembled from the verified v0.1.0 distribution. Private development history, canonical persona source copies, workstation paths, and host-private evaluation traces are not included.

Owen Burnett Officecraft is free software under the [MIT License](LICENSE.md). Third-party applications, connected services, templates, brand assets, and user-supplied material remain subject to their own terms and permissions.
