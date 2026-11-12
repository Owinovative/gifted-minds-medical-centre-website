# Gifted Minds Medical Centre website

An independently hostable, multi-page institutional website for Gifted Minds Medical Centre in Kisumu, Kenya. Built with static HTML, CSS and a small JavaScript file; no build process, database, PHP or framework is required.

## Pages

- `index.html` — homepage and route into the institution’s information.
- `about.html` — story, history, mission, vision and values.
- `services.html` — documented current services.
- `team.html` — supplied team portraits and the roles named in the facility profile.
- `facilities.html` — supplied environment photographs and documented rooms/capacity.
- `insurance.html` — accredited arrangements and partnerships in progress.
- `community.html` — outreach and community health activities.
- `contact.html` — phone, email, WhatsApp, address and directions.

## Run locally

From this directory, start the static server on the project’s development port:

```sh
python -m http.server 4173 --bind 127.0.0.1
```

Open `http://127.0.0.1:4173`. If that port is already in use, choose another available port such as 4174, 8080 or 5500; do not use port 8000 for this project.

## Technology and assets

- HTML documents are independent and can be opened directly by the static server.
- `styles.css` contains design tokens, shared components and responsive layouts.
- `script.js` handles the accessible mobile navigation and dynamic copyright year.
- `assets/hospital-logo.png` is a proportion-preserving, optimized derivative of the supplied official `pictures/Hospital Logo.png`; it appears in the shared navigation and footer. `assets/favicon.png` is a square favicon derivative on white. The source logo remains unchanged.
- `assets/images/` contains the selected photographs as optimized WebP assets; the originals remain in `pictures/` as private source material. See [ASSET-INVENTORY.md](ASSET-INVENTORY.md) for image selection notes.
- `pictures/Gifted minds hospital profile.docx` is the private source document. It is excluded from Git and is not linked from the website.
- `DESIGN-RESEARCH.md` documents the healthcare website research and the resulting design direction.

## Content accuracy

The hospital profile is the primary reference for facility information. SHIF and Birdview Insurance are presented as accredited according to that profile; private insurers and corporate schemes are marked as being pursued. The site does not present proposed future services as operating services. WhatsApp uses the existing project contact number `+254 100 261 446`.

## SEO and deployment

Each page has a unique title, description and Open Graph metadata. Canonical URLs are omitted because the production domain has not been supplied. `robots.txt` permits indexing. A sitemap should be generated after the canonical production host is confirmed; no production domain is guessed here.

When the public origin is known, generate the sitemap with `python scripts/generate-sitemap.py https://your-confirmed-domain.example`, then add a matching `Sitemap: https://your-confirmed-domain.example/sitemap.xml` line to `robots.txt` before deployment.

Deploy only the eight HTML pages, `styles.css`, `script.js`, `assets/`, `robots.txt`, and an optional generated sitemap to any static host. Do not upload `pictures/`, `scripts/`, `.git/`, or local tooling directories: the original profile DOCX and unselected source material are kept there. The public photo and logo derivatives are already under `assets/`.

## Git workflow

Use a feature branch for redesign work, stage the site source and public assets, check the staged diff for private material, and commit meaningful milestones. `.gitignore` excludes credentials, local tool directories and the hospital profile document.
