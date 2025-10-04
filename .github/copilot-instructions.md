# Copilot Instructions for AI Coding Agents

## Project Overview
- This is a Hugo-based static website for wenzel.no, showcasing local crafts, farming, and beekeeping in Bergen, Norway.
- Content is bilingual (Norwegian Bokmål and English) and organized in `content/no/` and `content/en/` directories.
- The site is minimalist, image-heavy, and avoids any commercial or sales language.

## Architecture & Structure
- **Framework:** Hugo static site generator. No backend, no database.
- **Content:** Markdown files for each section and language. Example: `content/no/birokt.md`, `content/en/beekeeping.md`.
- **Assets:** Images stored in `static/images/` (use placeholders if needed).
- **Config:** Site configuration in `config.toml` (see README for example).
- **Theme:** Use a lightweight Hugo theme (preferably Tailwind CSS-based).

## Key Patterns & Conventions
- **Bilingual Support:** All content must exist in both Norwegian and English. Use Hugo’s i18n for translations.
- **Frontmatter:** Each markdown file uses YAML frontmatter for title, description, and image.
- **No Pricing/Sales:** Never mention prices or direct sales. Focus on portfolio and community.
- **Contact Info:** Only email and phone (no social media, no American servers).
- **Navigation:** Simple menu, language toggle (NO/EN), links to all sections.
- **QR Code:** Oyster Mushroom section uses a QR code linking to the homepage (implement as Hugo shortcode or static image).
- **SEO:** Meta descriptions in frontmatter, Bergen-focused keywords.
- **Accessibility:** Alt tags for images, readable text (min 16px font).
- **Performance:** Compress images (<200KB), minify CSS/JS, use Hugo’s minification.

## Developer Workflows
- **Build:** `hugo --minify` to generate the static site in `public/`.
- **Local Test:** `hugo server` to run locally and preview changes.
- **Image Optimization:** Compress images before adding to `static/images/`.
- **Theme Customization:** Use Tailwind CSS via CDN or local build.
- **Deployment:** Host on independent European servers (avoid AWS/Google Cloud).

## Examples
- Section markdown: `content/no/birokt.md` and `content/en/beekeeping.md` with matching frontmatter and visuals.
- Config: See `config.toml` example in README for language and menu setup.
- QR code: Use Hugo shortcode like `{{</ qrcode url="https://wenzel.no" >}}` in markdown.

## References
- See `README.md` for full architecture, setup, and conventions.
- Key directories: `content/no/`, `content/en/`, `static/images/`, `config.toml`.

---
Project tasks and priorities (single source of truth)

- The file `doc/implementation-plan.md` is the canonical task list. Treat it as a lightweight internal Jira: create, update, and resolve tasks there.
- When you complete work, update that file to mark tasks as done (add `[x]` or the word `done` near the task). The repository has an automation that regenerates status badges from that file.
- If you open PRs, reference the task by number and update the plan with the PR link and status.

AI agent responsibilities

- Read `doc/implementation-plan.md` before making changes. Use its P0/P1/P2 priorities to pick the next work item.
- When implementing a task, add a short line under the task with a `PR:` link and `status:` (e.g., `PR: #12 status: in-review`).
- After merging, mark the task done in `doc/implementation-plan.md`.

If any conventions or workflows are unclear, ask the user for clarification or examples from the codebase.