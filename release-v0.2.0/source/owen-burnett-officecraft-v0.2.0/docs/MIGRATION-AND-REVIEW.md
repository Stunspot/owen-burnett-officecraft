# Keep earlier work and make current review usable

Officecraft 0.2 uses version 2 of the artifact register and review wrapper. Other Officefile records keep their existing formats. The change records which inputs produced each output and which intended use a review supports. Existing version 1 Officefiles need a separate migrated copy before making current readiness claims.

## Preserve your existing Officefile

Use the matched 0.2 operator and reviewer. From the operator skill folder, run:

```text
python scripts/migrate_officefile.py ORIGINAL NEW-COPY
```

Replace both names with your paths. The destination must not exist, its parent folder must exist, and it must sit outside the original. A successful result names the new copy. The original files remain unchanged. In the copy, `history/pre-v2` retains the original brief, artifact register and review; the output files are preserved, but their current status becomes working. Old approvals remain historical evidence and do not become approvals of an unverified revision.

If migration refuses an existing destination, choose a different name. If a copy fails partway, it retains `MIGRATION-INCOMPLETE.txt`; continue using the original and inspect the stated failure. Do not delete the original or interpret the partial copy as a completed migration.

## Establish what each current output used

Ask Officecraft to reconcile the copied project's sources and dependencies. Each derivative needs its governing editable artifact; cycles and duplicate current file identities are rejected. Record the source IDs, controlled ledger items and other upstream artifacts actually used.

Regenerate the affected output, or document an actual comparison that establishes it remains faithful. Then capture its current inputs into a new record:

```text
python scripts/capture_artifact_binding.py NEW-COPY ART-BRIEF --record-kind produced --evidence "working/build.py and review/content-check.md" --output NEW-COPY/review/brief-production.json
```

Use your actual artifact ID and evidence. The parent of the new output record must exist. An existing output is refused. The helper does not rewrite the artifact register: Officecraft adopts the returned `input_basis` only after checking the real production evidence. Capturing current hashes alone does not make an old artifact current.

## Adopt an actual review

The reviewer supplies an `officecraft-review-entry/v2` object. Preserve the previous review wrapper in history, then copy the entire new entry into its `independent_review` field. Operator self-review belongs in `operator_review`. Both use the same binding: current Officefile state, intended use, actual reviewer/time, artifact digest and production-basis digest. A template is not a completed review.

PASS_WITH_CONDITIONS is useful while a stated condition remains open. It does not support approval for the affected use until the condition is met or the accountable owner explicitly accepts its stated residual. A met condition cites resolution evidence; an accepted residual names its owner, scope, time and rationale. Open material defects still require REVISE or BLOCKED. A review never supplies user approval.

Read both current reviews together for the exact artifact, production basis, Officefile state and intended use. An operator PASS cannot override an independent open condition, and the reverse is also true. A current REVISE or BLOCKED verdict prevents claiming that same scope passed review. Another use or artifact keeps its own scope.

Before approving an affected use, resolve every relevant current condition or record the same accountable owner's explicit acceptance of each residual. If reviews disagree, preserve the current evidence and resolve the stated issue against the real output. Move a superseded entry to history when a genuine new review replaces it; changing a status label is not resolution.

Run validation after adoption. If it reports a stale basis or digest, preserve the old review and review the corrected current output; do not edit old hashes to silence the error. The native checker validates consistency, not the truth of evidence or an approver's identity.

## Know when the return is complete

The new output agrees with its governing inputs, affected derivatives have been regenerated or genuinely reconciled, the actual files have been inspected at the available depth, and the current review identifies the intended use and remaining conditions. HANDOFF.md names the editable source, current derivative, preserved prior version and next owner action. See [Officefile and resume](OFFICEFILE-AND-RESUME.md) for the normal workflow.
