# Vervant's public website and developer guides

Welcome! This repository holds the public home for Vervant: the product website, practical PDF guides, invoice examples and a small demo you can try in your browser.

- [Visit Vervant](https://vervant-pdf-api.deed.page/)
- [Try the invoice preview](https://vervant-pdf-api.deed.page/tools/invoice-preview/)
- [Plan a PDF workflow](https://vervant-pdf-api.deed.page/tools/workflow-brief/)
- [Browse the developer guides](https://vervant-pdf-api.deed.page/guides/)
- [Read the rendering and security guide](https://vervant-pdf-api.deed.page/guides/secure-html-to-pdf.html)
- [Share a question or idea](https://github.com/VervantHorizon/vervant-website/discussions/1)

The public site is hosted on deed.page Free. The hosted Vervant API is still being prepared and is not open for public use. Its production Docker image passes a PDF and network-isolation smoke test in GitHub Actions, but Railway does not expose the namespace/security controls the renderer needs. We will keep the API offline until a compatible production host has been tested. Please don't send personal, confidential or production customer documents.

The invoice preview runs entirely in your browser. It doesn't upload or store what you enter, and it uses your browser's print dialog to save a PDF. It's a layout example, not the hosted API or accounting/tax software.

We're building Vervant for SaaS teams that want an easier way to create consistent PDFs from HTML. Thanks for stopping by and taking a look.
