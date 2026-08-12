# Public publication preflight update

GitHub official documentation observed 2026-08-12 states standard GitHub-hosted runners are free and unlimited for public repositories. Owen Burnett Officecraft is public. Its line-ending workflow runs on `pull_request` or deliberate dispatch without a push trigger. Its official Pages workflow runs once when docs or the workflow change on `main`, or on deliberate dispatch.

The release plan invokes two public standard-runner jobs: one PR line-ending job and one post-merge Pages job. `2 jobs x 1 attempt x 360 ceiling minutes x 0 billable multiplier = 0 billed minutes` (720 raw runner-minute conservative ceiling). Zero retries or duplicate push checks are planned. No private allowance, paid capacity, or ruleset change is used.
