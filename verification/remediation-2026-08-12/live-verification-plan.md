# Post-publication live verification plan

Target the exact final `main` commit after the complete local evidence package is published through protected review.

1. Confirm remote `main` equals the intended final commit.
2. Confirm GitHub Pages uses the committed official deployment workflow to publish the `/docs` artifact from `main`.
3. Require the PR-associated `line-ending-policy` check on the exact public feature-branch head before merge; use manual dispatch only for diagnosis.
4. Merge through branch protection, then poll the official Pages deployment until it succeeds for the final commit.
5. Request the product landing page, all 17 generated documentation routes, the direct 404 page, and an unknown route.
6. Require HTTP 200 for the 19 named routes, HTTP 404 with the custom recovery body for the unknown route, and zero broken internal links.
7. Compare the three live PNG hashes byte-for-byte with the committed README, Pages, and social assets.
8. Confirm landing-page Open Graph and Twitter metadata point to the exact social card and name Owen Burnett Officecraft.
9. Confirm the live repository README wires the exact README hero and the repository metadata points to the live Pages URL.
10. Assign repository PASS only after all observations succeed; otherwise record LIVE VERIFICATION FAIL and repair the diagnosed layer.