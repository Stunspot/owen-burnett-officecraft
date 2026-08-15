# Use an Officefile for substantial work

An Officefile is a resumable local project folder. Use one when the job spans several artifacts, has consequential facts or source custody, needs revision history, or will be handed to another person or host.

For a one-page low-risk file, skip the ceremony. Officecraft should not build office bureaucracy to solve office bureaucracy.

## Start an Officefile

From the operator skill folder, run the included initializer with a new destination:

```text
python scripts/init_officefile.py <new-officefile-folder>
```

Use a new empty destination. The initializer is designed to refuse overwriting an existing project. Keep imported originals in `sources/` or preserve a clearly recorded original location before editing copies.

The resulting structure is:

```text
officefile/
  sources/
    manifest.json
  state/
    brief.json
    content-ledger.json
    artifact-register.json
    decisions.jsonl
  working/
  output/
  review/
    officecraft-review.json
  HANDOFF.md
```

## What each part protects

| Location | Purpose |
|---|---|
| `sources/manifest.json` | Identifies supplied material, custody, content status, and hashes where recorded. |
| `state/brief.json` | Records audience, purpose, requested outcomes, constraints, approval owner, and delivery authority. |
| `state/content-ledger.json` | Holds controlled names, dates, units, metrics, claims, decisions, and their source status. |
| `state/artifact-register.json` | Names every planned or produced artifact, its format, editability, source relationship, status, and check evidence. |
| `state/decisions.jsonl` | Retains consequential choices without becoming a transcript. |
| `working/` | Holds editable working materials and format specifications. |
| `output/` | Holds produced artifacts only after they exist. |
| `review/officecraft-review.json` | Records operator and independent-review status, digest-bound reviewed artifacts, and any separately supplied approval record. |
| `HANDOFF.md` | Gives a person-readable receipt for the current state and next action. |

## Resume safely

1. Read `HANDOFF.md`, then read the brief, content ledger, and artifact register before changing a deliverable.
2. Confirm which file is the canonical editable source for each derivative. A PDF is often a final-form derivative, not the place to make a revision.
3. Put new facts, changed dates, changed metrics, and changed recommendations in the content ledger first.
4. Update the affected editable source, regenerate each derivative that depends on it, and rerun the checks affected by the change.
5. Record material decisions, the current artifact status, evidence actually obtained, and the next owner action.

## Validate and inspect without overstating the result

The operator includes these standard-library scripts:

```text
python scripts/validate_officefile.py <officefile-folder>
python scripts/inspect_office_artifacts.py <officefile-folder>
python scripts/package_officefile.py <officefile-folder> <output-zip>
```

Validation checks Officefile state, required records, controlled references, and declared artifact status. An artifact marked `reviewed` must have a passing review tied to its current digest and Officefile state. An artifact marked `approved` must additionally have a scoped, timestamped approval record from the approval owner named in the brief. These records preserve evidence custody; they are not digital signatures and do not prove the approver's identity.

Inspection inventories files and performs bounded container checks; validation directly repeats the relevant current-container check before accepting saved inspection evidence. Neither route renders pages or slides, calculates workbook formulas, executes macros, decrypts files, or proves accessibility. Packaging requires a valid Officefile, binds the ZIP to the validated file snapshot, and refuses an overwrite.

Read a script result as evidence for exactly that script's scope. Use native or rendered inspection where available for visual and final-format claims.

## Worked shape, not a finished packet

The operator includes a fictional `monday-leadership-packet` example. It demonstrates a shaped Officefile for a brief, deck, workbook, and PDF handout. Its outputs are intentionally planned only: no DOCX, PPTX, XLSX, or PDF exists in that example, and it records no native opening, formula calculation, renderer, visual inspection, accessibility review, or independent review.

That limitation is deliberate. Use the example to understand the state model, not as evidence that an office artifact was generated.
