# Owen Burnett Officecraft site source

The static project site is published from this `docs/` directory.

## Source and evidence boundary

The site describes the public v0.1.1 dual-host distribution in this repository. Its product claims are derived from:

- `README.md` and `START-HERE.md`;
- `codex/owen-burnett-officecraft/SKILL.md`;
- the operator's operating, routing, format-production, cross-artifact, quality, and host-capability references;
- `codex/officecraft-reviewer/SKILL.md` and its review rubric;
- the included Officefile schemas, initialization, inspection, validation, packaging, and release evidence.

The page does not claim universal host activation, native rendering, spreadsheet recalculation, formal accessibility conformance, representative-user success, external delivery authority, or marketplace publication.

## Files

- `index.html` - semantic product overview;
- generated `*.html` documentation routes - locally built from the customer Markdown sources;
- `style.css` - responsive product and documentation presentation;
- `assets/officecraft-readme-hero.png` - 1600x900 README composition;
- `assets/officecraft-pages-hero.png` - 1200x800 Pages composition;
- `assets/officecraft-social-card.jpg` - 1200x630 Open Graph composition with exact product text;
- `scripts/build_pages.py` - deterministic local Markdown-to-HTML builder;
- `.nojekyll` - direct static-file serving marker.

## Deployment

GitHub Pages publishes the static `docs/` directory through `.github/workflows/deploy-pages.yml` when documentation changes reach `main`, or through a deliberate workflow dispatch. Publication is complete only after the official Pages deployment succeeds and the live routes and assets are rechecked.

## Review notes

The page uses one H1, semantic landmarks, a skip link, visible keyboard focus, descriptive links, meaningful alternative text, responsive layout, and reduced-motion handling. These checks support structural accessibility only; they are not a claim of formal accessibility conformance, browser coverage, file rendering, formula correctness, security, or representative-user success.
