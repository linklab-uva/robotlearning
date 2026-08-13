# Learning in Robotics — 2027 Visual Refresh

This refresh keeps the existing Jekyll/GitHub Pages workflow intact. Markdown content, collections, announcements, assignments, and visibility controls continue to work as before.

## What changed

- Replaced the legacy dark-blue patterned header with a light, sticky, translucent research-site header.
- Updated typography to Inter + Space Grotesk.
- Increased the content width and whitespace for a more contemporary editorial layout.
- Added a dedicated hero treatment driven by `hero_image` front matter in `index.md`.
- Modernized announcements, faculty/TA cards, lecture cards, schedules, archive rows, links, code, headings, and footer styling.
- Reworked mobile navigation as a clean horizontal-scroll menu; no JavaScript dependency was added.
- Replaced the homepage hero image with the newly generated Learning in Robotics banner.
- Cleaned up `head.html` metadata and fixed the malformed author meta tag.

## Workflow remains unchanged

Edit Markdown / YAML / SCSS -> commit -> push -> GitHub Pages rebuilds the site.

No React, Bootstrap, Tailwind, npm build, or JavaScript framework was introduced.

## Files with meaningful changes

- `_css/main.scss`
- `_sass/_user_vars.scss`
- `_sass/_base.scss`
- `_sass/_layout.scss`
- `_sass/_header.scss`
- `_sass/_mobile-header.scss`
- `_includes/head.html`
- `_includes/header.html`
- `_layouts/home.html`
- `index.md`
- `_images/robotlearning_updated.png`

## Local build note

The editing container did not include Bundler/Jekyll, so a full local Jekyll render could not be executed here. The source structure and Liquid/Sass integration were preserved to match the existing repository conventions.
