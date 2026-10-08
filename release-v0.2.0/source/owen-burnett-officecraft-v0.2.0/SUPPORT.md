# Support and recovery

Use [GitHub Issues](https://github.com/Stunspot/owen-burnett-officecraft/issues) for reproducible product defects, installation failures, and documentation problems.

Include:

- Officecraft version or commit;
- host and host version;
- affected skill or artifact route;
- the smallest reproducible request;
- exact observed behavior or error; and
- a sanitized fixture when one is necessary.

Do not attach customer documents, credentials, Officefiles, source-custody material, unredacted screenshots, tokens, cookies, account exports, or proprietary templates.

For security-sensitive reports, follow [SECURITY.md](SECURITY.md) rather than publishing exploit details or confidential evidence in a public issue.

## Recovery order

1. Preserve the current Officefile and artifacts away from the installed skill directories.
2. Record the exact operator and reviewer versions.
3. Compare the installed skills or archives with the matching GitHub release.
4. Reinstall only the two Officecraft skills through the host's supported route.
5. Start a fresh task and repeat one low-risk request.
6. Report discovery, invocation, artifact execution, and inspection as separate observations.

Removing or reinstalling Officecraft should not delete Officefiles or customer artifacts stored outside the skill directories.
