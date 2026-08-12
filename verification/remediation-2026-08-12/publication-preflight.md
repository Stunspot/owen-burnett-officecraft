# Public publication preflight update

GitHub official documentation observed 2026-08-12 states standard GitHub-hosted runners are free and unlimited for public repositories. Owen Burnett Officecraft is public. Its one workflow is a standard `ubuntu-latest` line-ending job with `pull_request` and `workflow_dispatch`, and no `push` trigger; Pages uses legacy `main:/docs` deployment.

The protected release plan invokes one PR-associated job: `1 pull_request trigger x 1 job x 1 attempt x 360 ceiling minutes x 0 billable multiplier = 0 billed minutes` (360 raw runner-minute conservative ceiling). Zero retries or duplicate push jobs are planned. No private allowance, paid capacity, or ruleset change is used.
