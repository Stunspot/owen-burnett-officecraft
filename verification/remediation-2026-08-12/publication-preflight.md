# Public publication preflight update

GitHub official documentation observed 2026-08-12 states standard GitHub-hosted runners are free and unlimited for public repositories. Owen Burnett Officecraft is public. Its one workflow is a standard `ubuntu-latest` line-ending job with `workflow_dispatch` only; Pages uses legacy `main:/docs` deployment.

The protected release plan invokes one feature-branch dispatch: `1 trigger x 1 job x 1 attempt x 360 ceiling minutes x 0 billable multiplier = 0 billed minutes` (360 raw runner-minute conservative ceiling). No private allowance, paid capacity, duplicate trigger, or ruleset change is used.