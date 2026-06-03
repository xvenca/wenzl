---
name: multilingual-content-parity
description: "Use when editing website pages, markdown content, translations, or repeated copy so all language variants stay in sync. Covers cs, cu, de, en, es, no, pl, ru, uk and requires validation that every language variant renders correctly, reads naturally, and preserves the same meaning."
---

# Multilingual Content Parity

Use this skill whenever a change touches site copy, page text, headings, descriptions, frontmatter text, or any repeated content block.

## Language variants in this repository

- `cs`
- `cu`
- `de`
- `en`
- `es`
- `no`
- `pl`
- `ru`
- `uk`

## Required workflow

1. Treat every content edit as a multilingual change until proven otherwise.
2. Search for all duplicated or equivalent text across the repository before editing.
3. Update every affected language variant in the same change set. Do not stop after updating only one language.
4. Check both dedicated pages and broader summary pages when the same topic appears in multiple places.
5. Prefer natural, idiomatic wording in each language over literal translation.
6. If a translation is uncertain, rewrite it more simply so it still sounds native.

## Required validation

After editing content:

1. Run `hugo --minify`.
2. Verify the rendered or generated output for every affected language variant.
3. Confirm that the change appears in all listed language variants.
4. Confirm that each language reads naturally and still communicates the same meaning.
5. Call out any language where the wording remains uncertain and fix it before finishing.

## Minimum completion standard

Do not consider the task complete until:

- all affected language variants have been edited,
- the site build passes,
- representative rendered output has been checked for every affected language,
- and the final response explicitly says which language variants were updated and how they were validated.