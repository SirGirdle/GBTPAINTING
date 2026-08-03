#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GBT Painting & Decorating — static site generator.

Dev tool only. Run `python3 generate.py` to (re)build every static HTML page,
placeholder image, sitemap, robots.txt and the pages.json manifest into the
repo root. The generated HTML is what gets committed and deployed — the host
needs no build step.
"""
import json
import os

from build import pages, components as C
from build.data import BIZ, SERVICES, AREAS, REGION
from build.svg import gallery_svg, favicon_svg, _PALETTES

ROOT = os.path.dirname(os.path.abspath(__file__))


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return path


def write_page(url_path, html):
    """url_path like '/services/x/' -> services/x/index.html ; '/' -> index.html"""
    rel = url_path.strip("/")
    out = "index.html" if rel == "" else os.path.join(rel, "index.html")
    return write(out, html)


def main():
    manifest = []
    built = []

    def page(url, html, title, group):
        built.append(write_page(url, html))
        manifest.append({"path": url, "title": title, "group": group})

    # --- Core pages -------------------------------------------------------
    page("/", pages.home(), "Home", "core")
    page("/" + REGION["slug"] + "/", pages.region_hub(), "Areas Covered — Essex", "region")
    page("/contact/", pages.contact(), "Contact", "core")
    page("/testimonials/", pages.testimonials(), "Reviews", "core")
    page("/thank-you/", pages.thank_you(), "Thank You", "system")
    page("/privacy-policy/", pages.legal("privacy"), "Privacy Policy", "legal")
    page("/terms-of-service/", pages.legal("terms"), "Terms of Service", "legal")

    # --- Service pages ----------------------------------------------------
    for s in SERVICES:
        page(C.svc_url(s), pages.service_page(s), s["name"] + " Colchester", "service")

    # --- Area pages -------------------------------------------------------
    for a in AREAS:
        page(C.area_url(a), pages.area_page(a),
             "Painting & Decorating " + a["name"], "area")

    # --- Placeholder gallery images (SVG) --------------------------------
    for theme in _PALETTES:
        write("assets/images/%s.svg" % theme, gallery_svg(theme))
    write("assets/images/favicon.svg", favicon_svg())

    # --- sitemap.xml ------------------------------------------------------
    urls = []
    for m in manifest:
        if m["group"] == "system":
            continue
        priority = "1.0" if m["path"] == "/" else ("0.8" if m["group"] in ("service", "area") else "0.6")
        urls.append(
            "  <url><loc>%s%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>"
            % (BIZ["domain"], m["path"], priority))
    sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + "\n".join(urls) + "\n</urlset>\n")
    write("sitemap.xml", sitemap)

    # --- robots.txt -------------------------------------------------------
    write("robots.txt",
          "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BIZ["domain"])

    # --- _redirects (Cloudflare Pages) -----------------------------------
    write("_redirects",
          "# Cloudflare Pages redirects\n"
          "/home    /    301\n"
          "/index.html    /    301\n")

    # --- content/pages.json ----------------------------------------------
    write("content/pages.json", json.dumps(
        {"business": BIZ["name"], "domain": BIZ["domain"],
         "generated_pages": len(manifest), "pages": manifest},
        indent=2, ensure_ascii=False))

    print("Built %d pages, %d images." % (len(built), len(_PALETTES) + 1))
    for b in built:
        print("  ", b)


if __name__ == "__main__":
    main()
