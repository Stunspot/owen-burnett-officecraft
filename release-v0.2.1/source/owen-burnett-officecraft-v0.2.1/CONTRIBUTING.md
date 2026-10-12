# Contributing

Contributions are welcome when they preserve Officecraft's source custody, one-content-spine discipline, host-capability boundaries, independent review, and honest handoff language.

Before proposing a change:

1. state the customer problem and affected artifact route;
2. update operator and reviewer distributions together when their shared contract changes;
3. preserve Codex and Claude package parity and archive topology;
4. add or update tests for Officefile state, schemas, packaging, or safety behavior;
5. update every affected customer document and generated Pages route;
6. inspect every changed visual and office artifact on its actual surface;
7. keep private paths, customer files, credentials, host-private traces, and unrelated work out of the change.

Install the documentation builder with `python -m pip install -r requirements-docs.txt`, then regenerate the committed site with `python scripts/build_pages.py`. Run the Officefile tests and the small synthetic package tests locally:

```text
python -B -m unittest discover -s codex/owen-burnett-officecraft/tests -p "test_*.py" -v
python -B -m unittest discover -s tests -p "test_*.py" -v
```

The CI workflow uses these checks and verifies that regenerated Pages files match source. It does not rebuild an accepted release or seal the candidate. The old 0.1.1 documentation-fingerprint helper has been retired; retained Hesperos authorship records identify the documentation revisions they cover.

After readiness and independent review are accepted and release is authorized, the maintainer can build once into a **new** repository directory:

```text
python -B tools/build_customer_release.py --output-dir release-candidates/accepted-0.2.0
python -B tools/verify_customer_release.py --root release-candidates/accepted-0.2.0/package
```

An existing output directory is refused and preserved. Verify the same command from a fresh native extraction of the complete ZIP before distribution. These checks prove packaging and byte custody; document rendering and intended-use readiness have separate evidence. Do not rely on GitHub Actions as the acceptance gate. A file existing is not evidence that it rendered, recalculated, remained accessible, or earned approval.

Use a focused GitHub issue for reproducible defects. Security-sensitive material follows [SECURITY.md](SECURITY.md). Contributions are accepted under the repository [MIT License](LICENSE.md).