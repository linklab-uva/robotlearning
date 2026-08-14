# GitHub Pages parity fix

This version preserves the visual design and changes only deployment plumbing.

## What changed

- All internal Jekyll asset/page URLs use `relative_url`, so the `/robotlearning` project-page base path is handled consistently.
- The main stylesheet URL includes a build revision query string, preventing stale GitHub Pages/CDN/browser CSS from surviving a deploy.
- The obsolete Font Awesome 5.2 URL with a failing SRI hash was replaced with Font Awesome 5.15.4 from cdnjs.
- The Gemfile uses the `github-pages` dependency bundle and is pinned to the v232 line currently reported by GitHub Pages.
- The stale 2020 `Gemfile.lock` was removed and is ignored, matching GitHub's documented Pages workflow recommendation.
- The unused empty `assets/css/style.scss` entry point was removed.

## Local preview

From the repository root:

```bash
bundle install
bundle exec jekyll serve --livereload
```

Then open:

`http://localhost:4000/robotlearning/`

## Deploy

Commit these source changes to the Pages source branch and push normally. No generated `_site` files should be committed.
