# Publishing the Vervant website on Render

This repository is prepared for a **static site only** deployment on Render.

## What this creates

- One Render Static Site named `vervant-public-site`.
- Source: this GitHub repository, branch `main`.
- No Docker image, web service, worker, database, persistent disk, environment secret or backend process.
- Automatic deploys after commits to `main`.
- A few standard security response headers.

Render's static-site tier is listed as free. Do not add a paid plan or create a dynamic web service for this website.

## Connect and publish

1. Sign in to Render and connect the GitHub account that can access `VervantHorizon/vervant-website` (the repository name is `vervant-website`, without a space).
2. Choose **New → Blueprint** and select this repository.
3. Render should detect `render.yaml` and show exactly one resource: `vervant-public-site`, type **Static Site**.
4. Before applying, confirm the summary has no paid resources, no web service, no database and no disk. Stop if anything else appears.
5. Apply the Blueprint and wait for the static-site deploy to finish.
6. Verify the homepage, guides, privacy page, invoice preview and workflow planner return HTTP 200.
7. The Render URL is now the canonical public address. Keep the previous deed.page deployment available as a temporary fallback until all links and search references have been checked.

## Important separation

This Blueprint publishes only static HTML, CSS, JavaScript and images. It does **not** deploy the Vervant PDF API, run Chromium or create a place to process customer documents. The hosted API remains offline until a compatible, isolated runtime has been selected and tested.
