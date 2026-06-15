# Tushar Tilwani — Personal Website

A fast, static personal website positioning **Tushar Tilwani** as a **Frontend / Full Stack
Software Engineer** with big-tech experience at **eBay, Oracle Cloud, and Amazon**. Built for
strong SEO and AI-search visibility (Google, ChatGPT, Claude, Gemini, Copilot, Perplexity).

**Live URL (GitHub Pages):** https://tushar-tilwani.github.io/me/

## Stack

Plain **HTML + CSS + a few lines of vanilla JS** — no build step, no framework, no dependencies.
This keeps the site fast, accessible, and trivially deployable on GitHub Pages.

- System-font stack (zero network font requests) for fast first paint.
- Responsive, mobile-first layout; automatic light/dark theme via `prefers-color-scheme`.
- Semantic HTML, skip link, visible focus states, and `prefers-reduced-motion` support.
- JavaScript is progressive enhancement only — the page is fully readable with JS disabled.

## File structure

```
me/
├── index.html              # All page content + SEO meta + JSON-LD structured data
├── assets/
│   ├── styles.css          # Responsive styles, light/dark themes
│   ├── main.js             # Mobile nav toggle + footer year (progressive enhancement)
│   ├── favicon.svg         # Inline SVG icon (TT monogram)
│   └── og-image.png        # 1200×630 social-share card (Open Graph / Twitter)
├── scripts/
│   └── generate-og-image.py# Regenerates assets/og-image.png (needs Python + Pillow)
├── robots.txt              # Allows all crawlers incl. AI bots; points to sitemap
├── sitemap.xml             # Single-page sitemap
├── site.webmanifest        # PWA manifest
├── .nojekyll               # Tells GitHub Pages to serve files as-is
└── README.md
```

## Run locally

No build needed. Any static file server works:

```bash
cd me
python3 -m http.server 8000
# then open http://localhost:8000
```

Or just open `index.html` directly in a browser (some features like the manifest resolve better
when served over `http://`).

## Regenerate the social-share image

The Open Graph / Twitter card is a raster PNG (social platforms reject SVG here). To re-render it
after changing copy:

```bash
python3 -m pip install pillow      # one-time, if not already installed
python3 scripts/generate-og-image.py   # writes assets/og-image.png
```

## Deploy to GitHub Pages

This repo's remote is already `https://github.com/Tushar-Tilwani/me`. To publish:

1. Commit and push to the default branch:
   ```bash
   git add .
   git commit -m "Add personal website"
   git push origin main
   ```
2. On GitHub: **Settings → Pages → Build and deployment**.
   - **Source:** *Deploy from a branch*
   - **Branch:** `main` · **Folder:** `/ (root)`
3. Save. The site publishes at **https://tushar-tilwani.github.io/me/** within a minute or two.

### Optional: custom domain

If you later add a custom domain (e.g. `tushartilwani.com`):

1. Add a `CNAME` file at the repo root containing just the domain.
2. Configure DNS per GitHub's instructions, and set the domain under **Settings → Pages**.
3. **Update the canonical URL** everywhere it appears — see the note below.

## ⚠️ Canonical URL — single source to update

The canonical/site URL `https://tushar-tilwani.github.io/me/` is hard-coded in a few places. If you
move to a custom domain or rename the repo, update it in **all** of these so search engines and
social previews stay consistent:

- `index.html` — `<link rel="canonical">`, all `og:*`/`twitter:*` URL + image tags, and every
  `url`/`@id`/`image` field inside the JSON-LD `<script type="application/ld+json">` block.
- `robots.txt` — the `Sitemap:` line.
- `sitemap.xml` — the `<loc>` value.

A quick find-and-replace of `tushar-tilwani.github.io/me` covers it.

## SEO & AI-search notes

- **Metadata:** descriptive `<title>`, meta description, keywords, robots, and canonical.
- **Social cards:** Open Graph + Twitter/X tags with a real 1200×630 PNG image.
- **Structured data (JSON-LD):** schema.org `Person`, `WebSite`, and `ProfilePage` in a single
  `@graph`, with verified `sameAs` links (LinkedIn, GitHub), `knowsAbout` skills, `alumniOf`, and
  `hasOccupation`. This helps both classic search engines and AI answer engines understand and
  attribute the profile.
- **Semantic headings:** one `<h1>` carrying the primary role keyword; section `<h2>`s and project
  `<h3>`s use natural, keyword-aware phrasing (no stuffing).
- **Crawlability:** `robots.txt` explicitly allows AI crawlers and points to `sitemap.xml`.

## Content source of truth

All copy is drawn from Tushar's resume and background profile. Metrics, titles, dates, and company
names are factual and not embellished. Phone number is intentionally omitted from this public page;
**LinkedIn is the primary contact**.
