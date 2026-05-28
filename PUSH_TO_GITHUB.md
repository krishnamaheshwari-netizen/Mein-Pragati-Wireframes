# Push the wireframes to GitHub

This folder is a complete, self-contained static site. To share it with the client for online review with per-screen comments, push it to GitHub and enable Pages.

There are two ways to do this. **Pick one.**

---

## Option A — One-command push (recommended)

A helper script is included: `deploy.sh`. It will:

1. Wipe any stale `.git/` directory in this folder
2. `git init` a fresh repo on branch `main`
3. Commit every file under `wireframes/` as a single initial drop
4. Add your remote
5. Push to `main`

Run it from this folder:

```bash
cd "<path-to>/Crisil Mein Pragati/wireframes"
./deploy.sh https://github.com/<org>/<repo>.git
```

If your repo is private or 2FA-protected, use a Personal Access Token (PAT) in the URL:

```bash
./deploy.sh https://<your-username>:<your-PAT>@github.com/<org>/<repo>.git
```

If the remote already has commits and you want to overwrite, append `--force`:

```bash
./deploy.sh https://github.com/<org>/<repo>.git --force
```

> The script auto-detects whether to push to root or a `wireframes/` subdirectory. If you want the wireframes inside a `wireframes/` subfolder of a larger repo, see Option B.

---

## Option B — Add to an existing repo as a subfolder

If you have an existing project repo and want `wireframes/` to live inside it:

```bash
# 1. Clone your existing repo
git clone https://github.com/<org>/<repo>.git
cd <repo>

# 2. Remove any old wireframes folder (if present)
rm -rf wireframes

# 3. Copy this folder into the repo (excluding any stale .git)
cp -R "<path-to>/Crisil Mein Pragati/wireframes" .
rm -rf wireframes/.git    # important: do not nest git repos

# 4. Commit and push
git add wireframes/
git commit -m "Add Mein Pragati revamp wireframes"
git push
```

---

## Step 2 — Enable GitHub Pages

After the push:

1. Repo → **Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: `main`
4. **Folder**: `/` (if you used Option A and the folder content is at the repo root) **or** `/wireframes` (if you used Option B with a subfolder)
5. Click **Save**

Within ~60 seconds, the site is live at:

```
https://<org>.github.io/<repo>/
```

The `.nojekyll` file in this folder tells Pages to serve everything as-is, so paths to `shared/`, `phase-0/`, etc. work without Jekyll processing.

---

## Step 3 — Wire up giscus for threaded comments (optional but recommended)

The combined `index.html` already has a built-in commenter that saves to the reviewer's browser and exports as markdown. That works offline and over `file://`, but comments don't sync across reviewers.

For threaded, persistent comments tied to GitHub Discussions:

1. In the repo: **Settings** → enable **Discussions**
2. Discussions tab → New category → name it "Wireframe feedback"
3. Visit https://giscus.app/
4. Enter your repo
5. Mapping: **Specific term**
6. Category: **Wireframe feedback**
7. Copy the four values it gives you: `data-repo`, `data-repo-id`, `data-category`, `data-category-id`
8. Open `index.html` and search for `data-giscus-placeholder` (around the comment-pane block). Uncomment the giscus `<script>` tag and paste the four values in.
9. Commit + push.

From then on, every screen has its own threaded discussion. Reviewers sign in with GitHub once and their comments persist across sessions.

---

## Step 4 — Share with the client

Once Pages is live, send the client:

```
https://<org>.github.io/<repo>/
```

They can:

- Browse What's New (default landing) — tabbed walkthrough by role
- Click any **View** button → drops them into the navigator at that screen
- Click through inter-wireframe links inside any screen
- Leave per-screen comments (localStorage commenter works immediately; giscus once configured)
- Click **Export feedback** in the top-right to download all their comments as markdown

---

## If something goes wrong

| Symptom | Fix |
|---|---|
| `git push` rejected — "non-fast-forward" | Re-run `./deploy.sh <url> --force` |
| Pages site shows 404 | Wait 60 seconds after the first push; refresh. Then check Settings → Pages shows a green checkmark. |
| Pages renders the README instead of `index.html` | Pages serves `index.html` by default when both exist — should be fine. If not, rename README.md → README.markdown or move it. |
| Stale `.git/` from a previous attempt blocks push | `./deploy.sh` handles this automatically. Or manually: `rm -rf .git && git init -b main` |
| giscus script does nothing | Check repo is public, Discussions is enabled, category exists, all four IDs are filled in |

---

## What you're pushing

A static site totalling ~1.1 MB:

- `index.html` — combined What's New + Wireframes navigator (188 KB)
- `README.md` — repo-level readme
- `.nojekyll` — tells GitHub Pages to skip Jekyll
- `shared/` — design tokens, components, manifest, postMessage helper
- `phase-0/` through `phase-4/` — 68 built wireframes
- `_build/generate.py` — the template-based wireframe generator (not served, just stored)
- `whats-new.html` — legacy redirect stub → `index.html`

No build step. No dependencies beyond Google Fonts (CDN) and optionally giscus (CDN).
