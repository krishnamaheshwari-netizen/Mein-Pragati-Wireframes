# Mein Pragati — Revamp Wireframes

Single-page navigable wireframe app for the CRISIL Mein Pragati revamp (Jan-June 2026). Combines the **What's New** explainer and the **Wireframes** navigator into one shareable file.

- 68 built wireframes across 5 user roles (Sakhi · FO · NGO Partner · CRISIL Admin · Beneficiary)
- 14 planned screens shown as placeholders
- 8 Dhwani-proposed enhancements (the "Our suggestions" tab in What's New)
- Inter-wireframe navigation — click any element with `data-link-to` to walk the flow
- Per-screen comments (offline via localStorage; online via giscus once configured)
- Light theme throughout · CRISIL brand red `#D6002A`

## Open it

Just double-click `index.html` in any modern browser. No server needed — the screen manifest is embedded inline so `file://` works directly.

If you'd prefer a local server (recommended when iterating on the manifest):

```bash
cd wireframes
python3 -m http.server 8000
# open http://localhost:8000
```

## What's where

```
wireframes/
├── index.html                  ← single entry point (What's New + Wireframes)
├── whats-new.html              ← redirect to index.html (legacy URL)
├── shared/
│   ├── tokens.css              ← design tokens
│   ├── components.css          ← component library
│   ├── manifest.json           ← screen catalogue (68 built + 14 planned)
│   └── wireframe-nav.js        ← inter-wireframe postMessage helper
├── phase-0/   5 wireframes — Stabilise (rejected loop)
├── phase-1/   18 wireframes — Foundation (messages, dashboard, sync, notifications, feedback)
├── phase-2/   20 wireframes — Workflow (attendance, best activities, bulk onboarding, training, reports)
├── phase-3/   12 wireframes — Sakhi & Beneficiary (My Budget, receipts, badges, training videos)
├── phase-4/   13 wireframes — Strategic (SHG, PM cockpit, SROI, archive, audit)
├── _build/
│   └── generate.py             ← template-based generator (regenerates wireframes from specs)
├── .nojekyll                   ← GitHub Pages: serve files as-is
└── README.md
```

## How to use

### As a stakeholder reviewer

1. Open `index.html`. The default landing is the **What's New** view — a tabbed walkthrough by user role.
2. Click any **View** button on a card → app switches to **Wireframes** mode and loads that screen.
3. Inside the navigator: left sidebar lists screens by role; click a row to load the wireframe in the canvas. The right metadata panel describes purpose, features, look-and-feel.
4. Inside any wireframe, hover over clickable elements (filter chips, links, buttons) — they're cursor-pointer; clicking jumps you to the linked screen.
5. Leave comments per screen in the right metadata panel. Comments are saved on your device.
6. Click **Export feedback** in the top-right to download all your comments as a markdown file you can email back.

### As the build owner

Adding a new wireframe:
1. Either write it by hand (any HTML using `shared/tokens.css` + `shared/components.css` and including `shared/wireframe-nav.js`) OR add a spec to `_build/generate.py`.
2. Run `python3 _build/generate.py` to emit the file and update the manifest.
3. Refresh the browser.

## Deploying for online review

### Step 1 — Push to GitHub

```bash
cd "Crisil Mein Pragati"   # the project folder (parent of wireframes/)
git init
git add wireframes/
git commit -m "Mein Pragati revamp wireframes — initial"
git remote add origin https://github.com/<org>/<repo>.git
git branch -M main
git push -u origin main
```

(If your repo already exists, just `git add wireframes/` from inside that repo's working tree.)

### Step 2 — Enable GitHub Pages

1. Repo → Settings → Pages
2. Source: **Deploy from a branch**
3. Branch: `main` · folder: `/wireframes` (or `/docs` if you copy the folder)
4. Save. Within a minute, your site is live at `https://<org>.github.io/<repo>/`

The `.nojekyll` file is included so GitHub Pages serves the HTML/CSS/JS as-is without Jekyll processing.

### Step 3 — Enable per-screen comments via giscus

The combined `index.html` includes a built-in commenter (saves to the reviewer's browser, exportable as markdown). For threaded, persistent comments tied to GitHub accounts, enable **giscus**:

1. Visit https://giscus.app/
2. Pick your repo (must be public, or your reviewers need access)
3. Set **Discussions** category to "Wireframe feedback" (create it in repo Settings → Discussions)
4. Set **Mapping** to "Specific term"
5. giscus generates a `<script>` block with `data-repo`, `data-repo-id`, `data-category`, `data-category-id`
6. In `index.html`, find the comment block:

```html
<!-- ===== giscus (GitHub Discussions comments) ===== -->
```

Uncomment the `<script>` tag and paste the values from giscus.app. The `data-term` is dynamically set per screen by the comment-injection code (look for `giscus-${currentScreenId}` in the script).

Once configured, every screen gets its own threaded GitHub Discussion. Comments persist across reviewers and sessions.

## Companion documents

This wireframes folder is the visual layer. The underlying analysis lives one level up:

- `../01_functional_knowledge_brief.md` — what the programme does
- `../02_architectural_map.md` — what the existing code does + pain points
- `../03_ui_inventory.md` — every existing screen, field by field
- `../04_implementation_plan.md` — 13-sprint sequenced delivery plan + open questions
- `../05_wireframe_plan.md` — the screen-by-screen plan that drives this folder

## Tech stack

Pure HTML / CSS / vanilla JS. No build step. No dependencies beyond:

- Google Fonts (Inter, JetBrains Mono, Material Symbols Rounded) — loaded from CDN
- (Optional) giscus.app for online comments

The Python generator in `_build/generate.py` is only used when adding new screens — it has no runtime presence.

## License

Internal — CRISIL Foundation / Dhwani RIS confidential. Not for redistribution.
