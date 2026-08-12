# Troubleshooting and recovery

Preserve evidence before resetting anything. A missing route, broken export, or unobserved artifact is a condition to diagnose, not an invitation to flatten the project into random copies.

## The skill folder is present, but the host does not use Officecraft

**Check:** Start a fresh task and confirm the exact skill folder name is unchanged.

**If it is still not selected:** Record the host/version, installation location, and request that failed to select it. Confirm the host's current skill-discovery instructions before changing its configuration.

**Recovery:** Keep the installed folders intact. Use the [universal production-packet approach](OFFICEFILE-AND-RESUME.md) in the meantime, or ask the host owner to repair discovery. Folder presence alone is not activation evidence.

## The requested DOCX, PPTX, XLSX, or PDF route is unavailable

**Check:** Establish whether the active host has a compatible file-production route and writable destination for this job.

**If it is unavailable:** Continue with the brief, source manifest, content ledger, format-specific specification, and quality checklist.

**Recovery:** Hand off a **production packet pending compatible tooling**. State that the requested office file does not yet exist. Re-enter when a compatible artifact route is observed.

## A file exists, but no one inspected its pages, slides, or sheets

**Check:** Look for a recorded render, export view, or native readback for the exact file version.

**If none exists:** Treat visual quality as unobserved. Container validity or file existence does not reveal clipping, collisions, unreadable text, or awkward layout.

**Recovery:** Open or render the canonical editable source or final artifact through an available route, inspect it, fix the earliest authoritative source, regenerate derivatives, and record the check.

## Workbook figures disagree with the deck or brief

**Check:** Compare the controlled metric, period, unit, and denominator in the content ledger and source data.

**If they differ:** Do not edit every output independently. Identify the canonical source, correct it there, update the ledger, regenerate the affected artifacts, and reread the relevant packet section for semantic drift.

**Recovery:** Record the decision and the artifacts changed. Leave genuinely conflicted source material visible until an accountable owner resolves it.

## A template or cloud-native artifact cannot be safely opened

**Check:** Confirm the connected account, target/copy, permission, and template authority. Do not infer that a generic import/export preserves native semantics.

**Recovery:** Preserve the original. Prepare an adaptation plan and ask for the authorized native route or an explicit alternate. Do not upload, share, overwrite, or connect an account merely to clear the warning.

## Validation or packaging fails

**Check:** Read the full script result. `validate_officefile.py` identifies missing or inconsistent Officefile state; `package_officefile.py` refuses invalid Officefiles and existing output ZIPs.

**Recovery:** Repair the cited record or missing file, then rerun the narrow command. Do not delete the existing project or package to force a clean result. If a package output already exists, choose a new versioned output path after confirming the desired source state.

## The user asks to send, publish, upload, or overwrite

**Check:** Confirm the exact destination, authority, privacy boundary, and current host capability.

**Recovery:** Stop at a reviewable or handed-off local artifact until an accountable owner authorizes the irreversible action. A reviewer verdict does not grant that authority.

## Safe stopping state

When work cannot continue, leave the sources, Officefile records, artifact register, current outputs, check evidence, and `HANDOFF.md` intact. Record the blocking condition and the event that makes re-entry safe. This gives the next operator a fact trail instead of a mystery pile of almost-final files.


For matched-version updating, removal, rollback, and retained-data cleanup, read [Lifecycle](LIFECYCLE.md).
