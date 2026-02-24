# GitHub Pages Deployment Guide

## Why the 404 Error Occurred

GitHub Pages requires an **`index.html`** file at the root of your site. When you visit `https://username.github.io/repo-name/`, GitHub looks for `index.html` to serve. Without it, you get a "404 File not found" error.

## What Was Fixed

1. **`index.html`** – Created by copying your portfolio. This is now the entry point for your site.
2. **`.nojekyll`** – Added to prevent Jekyll from processing your site (avoids issues with certain folder names).

## Deployment Checklist

### For a Dedicated Portfolio Repo (Recommended)

1. **Create a new repository** on GitHub (e.g., `portfolio` or `stephen-portfolio`).

2. **Copy these files** into the repo root:
   - `index.html` (required at root)
   - `portfolio-standalone.html` (optional backup)
   - `images/` folder with: `profile.png`, `reach-africa.png`, `society-money-transfer.png`, `ysat.png`
   - `.nojekyll` (empty file)

3. **Do NOT include** in the repo:
   - `dhoal/` (Django project – not needed for static hosting)
   - `venv/` (virtual environment)

4. **Push to GitHub** and enable Pages:
   - Settings → Pages → Source: "Deploy from a branch"
   - Branch: `main` (or `master`)
   - Folder: `/ (root)`

### Repository Structure

```
your-repo/
├── index.html          ← Served at yoursite.github.io/repo-name/
├── portfolio-standalone.html
├── .nojekyll
└── images/
    ├── profile.png
    ├── reach-africa.png
    ├── society-money-transfer.png
    └── ysat.png
```

### If Using This Repo (my_portfolio_tech) Directly

If your repo root is `my_portfolio_tech`, ensure:
- `index.html` is at the root of `my_portfolio_tech`
- `images/` folder is at the root of `my_portfolio_tech`
- In GitHub Pages settings, set the source to the branch and root folder

### Custom Domain (Optional)

To use a custom domain, add a `CNAME` file with your domain and configure DNS.

## Verify Deployment

After pushing, wait 1–2 minutes, then visit:
- `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`

Your portfolio should load from `index.html`.
