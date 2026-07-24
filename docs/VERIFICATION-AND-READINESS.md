# Verification and readiness

This page separates what the package is designed to do from what has been observed in a specific host. Read it before you call a deliverable ready, a skill active, or a release proven.

## Product-level evidence boundaries

The v0.1.0 operator and reviewer define a source-faithful Officefile workflow, format routing, bounded inspection scripts, an independent review contract, and a shaped fictional example. The example intentionally contains no produced DOCX, PPTX, XLSX, or PDF. It makes no claim of native-app opening, formula calculation, rendering, visual inspection, accessibility review, or independent review.

The Officefile scripts can establish only their stated invariants:

- initialization creates a new project skeleton without overwriting an existing destination;
- validation checks declared Officefile records, controlled references, and artifact-state invariants;
- inspection inventories files and performs bounded OOXML/PDF container checks without opening native apps or executing embedded code;
- packaging requires a valid Officefile and rejects an overwrite.

They do not create office files, render a page or slide, calculate a workbook, decrypt content, execute macros, or prove visual quality, accessibility, privacy, or final approval.

## Build evidence for this revision

The maintained v0.1.0 build recorded these bounded checks on 2026-07-21:

- all 16 Officefile unit tests passed, including linked-directory containment, bounded PDF/OOXML/CSV/Markdown checks, invalid-format evidence, review and approval custody, and snapshot-bound packaging;
- both skills passed the package validator for Codex and Claude profiles;
- the operator's 14-case and reviewer's 6-case behavioral suites passed structural validation;
- all 17 customer Markdown files passed the Hesperos structural accessibility linter;
- three isolated operator smoke cases and three isolated reviewer smoke cases were each judged `DEMONSTRATED` in one context-only trial per case using the local `qwen35` adapter.

The operator run fingerprint was `f060817acda64a3d17752eef9b08981508ca95452c83d1e1b26f632654170ecc`; the reviewer run fingerprint was `04ff05de0c8b9933f3f00b947f07158eee8201557b1dbe4e18a5d5c023987235`. These small, model-mediated smoke samples check selected evidence and authority boundaries. They are not a reliability estimate, representative-user test, live tool-use test, native-file-production test, or release approval. The release manifest records the assembled kit's files and hashes separately.

## Known unobserved surfaces for this build

The following were not established by the current build-host observations:

- fresh-host Codex installation, discovery, invocation, or activation;
- fresh-host Claude installation, discovery, invocation, or activation;
- live Google, Canva, or Excel connection and operation;
- native Office automation;
- cloud publication, sharing, emailing, upload, or external delivery;
- representative-user task success.

The host probe observed possible routes. It did not turn those routes into a universal support guarantee.

## What to verify for your own job

Before external use, obtain evidence appropriate to the risk:

1. Confirm the operator and, when needed, reviewer are discoverable in a fresh host.
2. Confirm the chosen artifact route is available and preserves needed editability or native semantics.
3. Confirm each requested output exists at its named location.
4. Run structural validation and bounded inspection where relevant.
5. Open or render the actual pages, slides, sheets, and final PDF when visual quality matters.
6. Check controlled names, dates, metrics, units, conclusions, source relationships, metadata, and privacy boundary across the packet.
7. Use the independent reviewer for consequential work, then obtain your accountable owner's approval before any external action.

## Readiness language

Use the narrowest honest statement:

| Observation | Claim you may make |
|---|---|
| Skill folders or archives are present | The package was copied or uploaded. |
| Host discovers the skill in a fresh task | The skill was discovered on that host. |
| The relevant route creates a file | The artifact was produced on that job. |
| A named file check ran | That structural or container check ran. |
| Actual pages/slides/sheets were viewed | That rendered or native surface was inspected. |
| Connected native surface confirmed a result | That result was native-verified. |
| Accountable owner agrees to a next use | The owner approved that named use. |

No earlier row implies a later one. Nothing in this guide grants external-delivery authority.
