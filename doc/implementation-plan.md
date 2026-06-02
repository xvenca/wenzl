# Implementation plan — Wenzel.no

This document is a practical, prioritized workplan to take the Hugo site from scaffold to a polished, production-ready site with strong SEO, accessibility, and AI-readability. Tasks are grouped, each with a short description, owner (suggested), acceptance criteria, and a rough time estimate.

## How to use this plan
- Pick a priority column (P0/P1/P2). Start at the top and work down.
- Create small, focused branches for each task (e.g. `feat/seo-meta`, `chore/images-opt`).
- Open PRs and rely on the CI (`.github/workflows/ci.yml`) to validate builds. Dependabot/auto-merge is enabled but review failing checks before merging.

## P0 — Critical (ship-ready)

1) Build / Deploy pipeline verification
   - What: Ensure `ci.yml` and `deploy.yml` run successfully on GitHub Actions; verify `gh-pages` deploy publishes correct site.
   - Owner: Dev
   - Acceptance: Actions pass on push/PR; `gh-pages` contains up-to-date `public/`; site is reachable.
   - ETA: 1-2 hours
   - status: deploy.yml now uploads via FTP from the `prod` GitHub Environment and targets `/public_html/`; pending live-site verification after the corrected server directory deploy.

2) Content parity & frontmatter hygiene [x]
   - What: Review every `content/*/*.md`. Ensure each file has: `title`, `description`, `image` (or fallback), `tags` (optional), `date` (if applicable). Add `summary` field where necessary.
   - Owner: Content lead / Dev
   - Acceptance: No missing frontmatter keys; Hugo builds without warnings about missing fields; social preview metadata uses image/fallback.
   - ETA: 3-6 hours

3) SEO basics / structured metadata
   - What: Add JSON-LD for Organization and Website, ensure meta tags (we added OG/Twitter). Add `sitemap.xml` (Hugo generates it by default) and verify `/robots.txt`.
   - Files: `layouts/_default/baseof.html`, `config.toml` (params), `static/robots.txt` (exists)
   - Acceptance: `curl -s https://<dev-site>/sitemap.xml` returns valid sitemap; Rich Results test shows Organization structured data.
   - ETA: 2-4 hours

4) Accessibility sweep (A11y) [x]
   - What: Keyboard nav, skip link, proper heading order, alt text on images, `aria` labels. Fix any issues found by `axe` or Lighthouse.
   - Files: `layouts/_default/*.html`, shortcodes (e.g., `figure.html`) and content image alt text.
   - Acceptance: Lighthouse A11y score >= 90; no critical violations in `axe-core` scan.
   - ETA: 4-8 hours

5) Performance baseline [x]
   - What: Optimize images, enable lazy-loading, ensure Tailwind (CDN) approach is acceptable; plan a compiled CSS pipeline later.
   - Tools: Lighthouse, PageSpeed Insights
   - Acceptance: Lighthouse Performance >= 50 (initial), improvement plan documented.
   - ETA: 2-4 hours (baseline + plan)

## P1 — Important (short-term improvements)

6) Image optimization and pipeline
   - What: Replace SVG placeholders with compressed photos; use Hugo image processing in templates to produce responsive `srcset` and resized images. Add `static/images/optimized/` or use page bundles.
   - Files: `layouts/_default/single.html`, `figure.html`, content frontmatter updates
      - Acceptance: Images served at appropriate sizes with `srcset`; average image <200KB.
      - ETA: 1-2 days
      - note: `figure` shortcode updated to generate responsive `srcset` when images are available as page or site resources (assets). Implementation committed 2025-10-04; content needs images moved to page bundles or `assets/images/` to exercise processing.

7) Tailwind build pipeline (production)
   - What: Move from CDN tailwind to compiled CSS with Purge (remove unused classes). Add `package.json`, `tailwind.config.js`, PostCSS, and an npm build step. Wire into CI to produce `assets/main.css` used by templates.
   - Acceptance: Final CSS < 50KB gzipped (approx); CI builds succeed and pages render identically.
   - ETA: 1 day

8) Real QR code generation for Oyster Mushroom stub
   - What: Replace placeholder shortcode with an SVG QR generator at build-time. Options: Hugo `resources.ExecuteAsTemplate` with pre-generated SVGs or a small node script to create QR SVGs in `static/` during CI.
   - Acceptance: Scannable QR SVG generated and embedded; shortcode fallback still works offline.
   - ETA: 0.5–1 day

9) Add richer OpenGraph images (per-page)
   - What: Generate or design OG-preview images per content type. Use page frontmatter `og_image` if available; otherwise fallback to site image.
   - Acceptance: Social preview shows image and description correctly for shared links on Facebook/Twitter/Telegram.
   - ETA: 1-2 days

10) Standalone swarm collection topic [x]
   - What: Add a separate multilingual page and menu entry for swarm collection and building protection with swarm traps.
   - Acceptance: All language variants have a dedicated page; main navigation links to it; homepage swarm-related cards point there instead of the general beekeeping page.
   - ETA: 2-4 hours
   - status: done locally; validated with `hugo --minify` pending commit/push.

11) Pollinators in cities topic [x]
   - What: Add a separate multilingual page and menu entry for pollinator-friendly cities with planting, habitat, and gentle maintenance guidance.
   - Acceptance: All language variants have a dedicated page; main navigation links to it; homepage city cards point there instead of the general beekeeping page.
   - ETA: 3-5 hours
   - status: done locally; validated with `hugo --minify` pending commit/push.

## P2 — Longer-term and polish

12) Content enhancements for AI-readability
    - What: Structure content for AI crawlers: add explicit `summary`, clear H1/H2/H3 hierarchy, descriptive alt text, add JSON-LD `FAQ` or `HowTo` where relevant, produce a `/human.txt` and `/ai.txt` (optional) describing site purpose and license.
    - Why: Improves discoverability by search engines and generative models that rely on structured content.
    - Acceptance: Clear content hierarchy; JSON-LD validated; improved SERP features over time.
    - ETA: ongoing (per page)
    - note: Added Bergen neighborhood keywords (Åsane, Fana, Laksevåg) to meta descriptions for local SEO [x]

13) Automated link and spelling checks
    - What: Add a GitHub Action to run a link-checker for site content and a spell-check GitHub Action for markdown.
    - Acceptance: Daily check runs; failing links reported in PRs.
    - ETA: 0.5 day

14) Privacy & analytics (European-friendly)
    - What: Add lightweight, privacy-first analytics (Plausible self-hosted or Matomo) or server logs; publish a short privacy policy. Avoid Google Analytics unless you want it.
    - Acceptance: Analytics capture basic visits without third-party trackers; privacy text present on `/kontakt` or `/privacy`.
    - ETA: 1 day

## QA and testing
- Add Lighthouse checks into CI (optional) to measure performance, accessibility, SEO baseline per PR. [x]
- Run `hugo --minify` in CI (done). Add smoke tests: check home page contains expected links (use a tiny script or `html-validate`).

## Operational tasks
- Set branch protection: require `CI — Build` to pass before merging. (Repository admin)
- Review Dependabot auto-merge logs regularly; configure policies to skip major version auto-merge.

## Acceptance criteria for 'launch'
- All P0 tasks completed and merged to `main`.
- CI green and `gh-pages` publishes without manual steps.
- Lighthouse: Accessibility >= 90, Best Practices >= 90, SEO >= 90 (performance can be improved iteratively).
- Images optimized and social previews verified.

## Useful commands and recommended workflow
- Run dev server locally:
  ```powershell
  hugo server -D
  ```
- Build production artifacts:
  ```powershell
  hugo --minify
  ```
- Test site build locally (CI mirrors this): ensure `public/` is created and contains `index.html`.

## Suggested immediate next 48h sprint
1. Finish frontmatter hygiene across `content/` (P0).
2. Run an accessibility scan and fix obvious issues (P0).
3. Implement image optimization + responsive `srcset` (P1).
4. Add simple Lighthouse check to CI and enable branch protection (operational).

If you want, I can take the first sprint items and implement them autonomously. Tell me which of these I should do first and I'll start.  

<!-- CI trigger: update 2025-10-04 to force GitHub Actions run -->

---
Last updated: 2025-10-04