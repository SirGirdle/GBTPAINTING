# GBT Painting & Decorating — Demo Website

A high-converting local-service website for **GBT Painting & Decorating**
(Colchester, Essex · established 2008), built to the *Local Service Site*
blueprint. This is a **demo** — copy, prices and reviews are illustrative and
the contact form endpoint is a placeholder.

**Live preview:** run a static server (see below) and open `/`.

## What's in the demo (24 pages)

| Type | Pages |
|---|---|
| Home | `/` — brand, all services, who-I-work-with, gallery, reviews, FAQ, areas |
| Service pages | 8 × `/services/{service}-colchester/` (interior, exterior, wallpapering, murals, tiling, fascias/soffits/gutters, end-of-tenancy, landlord) |
| Area pages | 9 × `/areas/painting-decorating-{area}/` — Stanway, Highwoods, Wivenhoe, West Mersea, East Mersea, West Bergholt, Copford, Tiptree, Dedham (each with **genuinely local copy**) |
| Region hub | `/essex-painting-decorating-services/` |
| Reviews | `/testimonials/` |
| Contact | `/contact/` |
| Thank-you | `/thank-you/` (form redirect) |
| Legal | `/privacy-policy/`, `/terms-of-service/` |

Every commercial page carries the conversion kit from the spec: sticky promo
bar (WhatsApp + 10% offer), tap-to-call header, above-the-fold quote form,
price anchor, trust ticks, before/after galleries, review cards, FAQ
accordion, full-bleed CTA band and a sticky WhatsApp float. SEO is baked in:
unique title/meta/canonical/OG per page, JSON-LD (`HomeAndConstructionBusiness`,
`Service`+`Offer`, `FAQPage`, `BreadcrumbList`), `sitemap.xml` and `robots.txt`.

## How it's built

The site is **static HTML** (no build step needed to host). A small Python
generator assembles the pages from data + shared components so every page gets
consistent chrome and the services × areas matrix stays in sync.

```
build/
  data.py         business details, services, areas (local copy), reviews, FAQs
  components.py   shared partials — header, footer, forms, sections, JSON-LD
  pages.py        page builders (home, service, area, region, contact, …)
  svg.py          inline icons + generated placeholder gallery images
generate.py       writes all HTML, images, sitemap, robots, content/pages.json
assets/           styles.css (design system), site.js, generated images
content/pages.json  manifest — source of truth for nav/footer & any CMS/WP migration
```

### Regenerate after editing content

```bash
python3 generate.py
```

### Preview locally

```bash
python3 -m http.server 8099
# then open http://localhost:8099/   (root-relative links need a server)
```

## Going live (client checklist)

- **Photos:** swap the generated SVG placeholders in `assets/images/` for real
  before/after shots — the highest-value asset for a visual trade.
- **Form:** the quote form posts to `https://formsubmit.co/{email}`
  (`build/data.py → BIZ["email"]`); confirm the address or point it at a CRM.
- **Brand:** colours live in `assets/styles.css :root`; logo/favicon in `build/svg.py`.
- **Details:** phone, WhatsApp, email, hours, Google reviews link and schema
  values are all in `build/data.py`.
- **Deploy:** static — Cloudflare Pages (no build command, output `/`) or any
  static host. Point the client's domain at it and it's live.

_Demo generated to the Local Service Site build spec._
