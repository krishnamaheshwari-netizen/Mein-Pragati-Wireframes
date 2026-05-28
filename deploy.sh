#!/usr/bin/env bash
# deploy.sh — push the Mein Pragati wireframes to a GitHub remote.
#
# Usage:
#   ./deploy.sh <remote-url>
#   ./deploy.sh <remote-url> --force
#
# Examples:
#   ./deploy.sh https://github.com/dhwani/mein-pragati-wireframes.git
#   ./deploy.sh https://krishnam:ghp_xxxx@github.com/dhwani/mein-pragati-wireframes.git --force
#
# What it does:
#   1. Wipes any stale .git/ in this folder
#   2. git init -b main
#   3. Stages every tracked file (respects .gitignore)
#   4. Commits as the initial drop
#   5. Adds the remote and pushes to main
#
# Run from the wireframes/ folder.

set -euo pipefail

REMOTE_URL="${1:-}"
FORCE_FLAG="${2:-}"

if [[ -z "$REMOTE_URL" ]]; then
    echo "Error: missing remote URL." >&2
    echo "Usage: $0 <remote-url> [--force]" >&2
    echo "Example: $0 https://github.com/dhwani/mein-pragati-wireframes.git" >&2
    exit 1
fi

# Confirm we're in the wireframes folder
if [[ ! -f "index.html" || ! -d "shared" ]]; then
    echo "Error: this script must be run from the wireframes/ folder." >&2
    echo "Expected files: index.html, shared/, phase-0/ ... phase-4/" >&2
    exit 1
fi

echo "==> Cleaning any stale .git/ directory"
rm -rf .git

echo "==> Initializing fresh git repo (branch: main)"
git init -b main >/dev/null

# Use existing git config if available; otherwise prompt
if ! git config user.email >/dev/null; then
    git config user.email "wireframes@dhwaniris.com"
fi
if ! git config user.name >/dev/null; then
    git config user.name "Mein Pragati Wireframes"
fi

echo "==> Staging all files"
git add -A

FILE_COUNT=$(git diff --cached --name-only | wc -l | tr -d ' ')
echo "    ${FILE_COUNT} files staged"

echo "==> Committing"
git commit -m "Mein Pragati revamp wireframes — initial drop

Combined index.html (What's New + Wireframes navigator) - 188 KB
68 built wireframes across 5 user roles (Sakhi, FO, NGO, Admin, Beneficiary)
14 planned screens shown as placeholders
8 Dhwani-proposed enhancements (Our suggestions tab)
Inter-wireframe navigation via postMessage
In-browser per-screen comments (localStorage)
giscus block ready to wire up for online comments
.nojekyll for GitHub Pages
Light theme - CRISIL red #D6002A" >/dev/null

echo "==> Adding remote: ${REMOTE_URL}"
git remote add origin "$REMOTE_URL"

echo "==> Pushing to main"
if [[ "$FORCE_FLAG" == "--force" ]]; then
    git push --force -u origin main
else
    git push -u origin main
fi

cat <<EOF

==> Done.

Next steps:
  1. GitHub: Settings -> Pages -> Source: "Deploy from a branch", Branch: main, Folder: /
  2. Wait ~60s, your site is live at https://<org>.github.io/<repo>/
  3. (Optional) Enable Discussions, run giscus.app, paste the IDs into index.html
     -> see PUSH_TO_GITHUB.md for step-by-step

Share the Pages URL with the client. They can browse, click through links,
and leave comments per screen.
EOF
