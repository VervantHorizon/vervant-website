# Publishing the Ubelta website on Render

This repository is a **static pre-launch website**. The existing Render Static Site remains the hosting target.

## Current configuration

- Render service: ver-vant-public-site (legacy service slug; do not confuse it with the separate API/preflight service).
- Source: this GitHub repository, branch main.
- Publish path: repository root (.).
- Build command: true.
- Auto-deploy: enabled on commits to main.
- No Docker image, web service, worker, database, persistent disk, environment secret or backend process is required.

## What is and is not live

The public page introduces QuotePath Starter, Supplier Follow-up Desk Kit and the From Enquiry to Payment bundle. It is a pre-launch preview only. Product pricing, checkout and download delivery are not enabled. Do not accept payments or promise digital delivery until payment onboarding, approved commercial terms and an end-to-end test purchase are complete.

## Verification after a deploy

1. Confirm the Render deploy status is live.
2. Check the homepage, mobile layout, language switcher and in-page navigation.
3. Confirm /robots.txt, /sitemap.xml and the branded /404.html are served.
4. Confirm obsolete Vervant-era routes no longer appear in the sitemap.
5. Confirm the page does not claim that checkout, downloads or automated workflows are active.

The public service URL currently retains its legacy vervant-public-site.onrender.com subdomain. A Ubelta-owned custom domain can be attached later, once one is available and verified.
