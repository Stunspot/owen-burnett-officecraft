# Trust, privacy, network behavior, and limits

Officecraft is a pair of local skill packages plus Officefile helpers. It contains no hosted service, account, API key, telemetry client, automatic updater, background process, or built-in office renderer.

## Data and storage

The skills do not create durable state by themselves. When a substantial job uses an Officefile, the authorized working path may contain supplied sources, briefs, ledgers, decisions, working files, outputs, review records, and handoff notes. The user or active host chooses that path and owns its retention.

The surrounding Codex or Claude host, connected application, file tool, native Office application, model provider, and cloud destination may store prompts, uploads, generated files, revisions, metadata, tool calls, billing records, or logs under their own policies. A locally installed skill does not make those systems local or private.

## Network behavior

Officecraft itself makes no required network call. A selected host capability may use a model provider, connector, Google Workspace, Canva, Microsoft Office, storage service, or another network route. Confirm the account, target, cost, privacy boundary, and authority before using it. When no compatible route exists, Officecraft should produce a source-ready production packet instead of claiming file execution.

## Security boundaries

Treat imported files, comments, formulas, links, macros, templates, and embedded content as untrusted source material. Preserve originals and work from copies. Keep executable content dormant. Uploading, sharing, emailing, publishing, connecting an account, overwriting an external target, and removing metadata remain separate authorized actions.

## What Officecraft cannot establish

Officecraft cannot guarantee source truth, template rights, universal host discovery, native compatibility, formula recalculation, visual quality, accessibility, metadata removal, cloud privacy, approval, or external delivery. File presence proves existence only. Structural checks, render inspection, native verification, reviewer disposition, accountable approval, and delivery are separate evidence states.

See [Host capabilities and evidence](HOST-CAPABILITIES-AND-EVIDENCE.md), [Verification and readiness](VERIFICATION-AND-READINESS.md), and [Security policy](SECURITY.md).