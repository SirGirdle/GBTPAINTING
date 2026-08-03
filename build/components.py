# -*- coding: utf-8 -*-
"""Reusable HTML partials and section builders."""
import json
from .data import BIZ, SERVICES, AREAS, REVIEWS, GALLERY_LABELS, REGION
from .svg import icon, google_logo

TEL = "tel:+44" + BIZ["phone_raw"].lstrip("0")
TEL_LAND = "tel:+44" + BIZ["landline_raw"].lstrip("0")


def wa_link(text="Hi GBT, I'd like a free quote for painting &amp; decorating."):
    from urllib.parse import quote
    return "https://wa.me/%s?text=%s" % (BIZ["whatsapp"], quote(text.replace("&amp;", "&")))


def svc_url(s):
    return "/services/%s-colchester/" % s["slug"]


def area_url(a):
    return "/areas/painting-decorating-%s/" % a["slug"]


# --- Document shell -------------------------------------------------------
def document(title, description, canonical, body, jsonld=None, og_type="website", og_image="/assets/images/exterior.svg"):
    ld = ""
    if jsonld:
        for block in jsonld:
            ld += '\n<script type="application/ld+json">%s</script>' % json.dumps(block, ensure_ascii=False)
    canonical_url = BIZ["domain"] + canonical
    return """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#102741">
<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="{biz}">
<meta property="og:image" content="{domain}{ogimg}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/styles.css">{ld}
</head>
<body>
{chrome_top}
{body}
{chrome_bottom}
</body>
</html>""".format(
        title=title, desc=description, canon=canonical_url, ogtype=og_type,
        biz=BIZ["name"], domain=BIZ["domain"], ogimg=og_image, ld=ld,
        chrome_top=promo_bar() + header() + mobile_nav(),
        body=body,
        chrome_bottom=cta_band() + footer() + wa_float() + lightbox() + '\n<script src="/assets/site.js" defer></script>',
    )


# --- Promo bar ------------------------------------------------------------
def promo_bar():
    return """<div class="promo-bar"><div class="promo-inner">
<span>📸 Send photos on WhatsApp &amp; <strong>save 10%</strong> — I reply in ~10 minutes</span>
<a class="promo-wa" href="{wa}" data-track="promo-whatsapp" target="_blank" rel="noopener">{ic} WhatsApp a photo</a>
</div></div>""".format(wa=wa_link(), ic=icon("whatsapp"))


# --- Header ---------------------------------------------------------------
def _services_dropdown():
    items = "".join('<a href="%s">%s</a>' % (svc_url(s), s["name"]) for s in SERVICES)
    return items


def _areas_dropdown():
    items = "".join('<a href="%s">%s</a>' % (area_url(a), a["name"]) for a in AREAS)
    return items


def header():
    from .svg import logo_mark
    return """<header class="site-header"><div class="header-inner">
<a class="brand" href="/" aria-label="{biz} home">
{logo}
<span class="brand-txt"><span class="brand-name">GBT Painting</span><span class="brand-sub">&amp; Decorating · Est 2008</span></span>
</a>
<nav class="main-nav" aria-label="Primary">
<a href="/">Home</a>
<div class="nav-dd"><button aria-haspopup="true">Services {cd}</button>
<div class="nav-dd-menu two-col">{svcs}</div></div>
<div class="nav-dd"><button aria-haspopup="true">Areas {cd}</button>
<div class="nav-dd-menu two-col">{areas}</div></div>
<a href="/testimonials/">Reviews</a>
<a href="/contact/">Contact</a>
</nav>
<div class="header-cta">
<a class="header-phone" href="{tel}" data-track="header-call">{ph}<span><small>Call today</small>{phone}</span></a>
<button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="navMobile">{menu}</button>
</div>
</div></header>""".format(
        biz=BIZ["name"], logo=logo_mark(), cd=icon("chev-down"),
        svcs=_services_dropdown(), areas=_areas_dropdown(),
        tel=TEL, ph=icon("phone"), phone=BIZ["phone_display"], menu=icon("menu"),
    )


def mobile_nav():
    from .svg import logo_mark
    svcs = "".join('<a href="%s">%s</a>' % (svc_url(s), s["name"]) for s in SERVICES)
    areas = "".join('<a href="%s">%s</a>' % (area_url(a), a["name"]) for a in AREAS)
    return """<div class="nav-mobile" id="navMobile" aria-label="Mobile menu">
<div class="nm-top">{logo}<button class="nm-close" id="navClose" aria-label="Close menu">{close}</button></div>
<a href="/">Home</a>
<div class="nm-group-title">Services</div><div class="nm-sub">{svcs}</div>
<div class="nm-group-title">Areas we cover</div><div class="nm-sub">{areas}</div>
<a href="/testimonials/">Reviews</a>
<a href="/contact/">Contact</a>
<div class="nm-cta">
<a class="btn btn-gold btn-block" href="{tel}" data-track="mobile-call">{ph} Call {phone}</a>
<a class="btn btn-wa btn-block" href="{wa}" target="_blank" rel="noopener">{wapp} WhatsApp us</a>
</div></div>""".format(
        logo=logo_mark(), close=icon("close"), svcs=svcs, areas=areas,
        tel=TEL, ph=icon("phone"), phone=BIZ["phone_display"], wa=wa_link(), wapp=icon("whatsapp"),
    )


# --- Footer ---------------------------------------------------------------
def footer():
    from .svg import logo_mark
    svc_links = "".join('<li><a href="%s">%s</a></li>' % (svc_url(s), s["name"]) for s in SERVICES)
    company_links = (
        '<li><a href="/">Home</a></li>'
        '<li><a href="/testimonials/">Reviews</a></li>'
        '<li><a href="/contact/">Contact</a></li>'
        '<li><a href="/%s/">Areas covered</a></li>'
        '<li><a href="/privacy-policy/">Privacy policy</a></li>'
        '<li><a href="/terms-of-service/">Terms of service</a></li>'
    ) % REGION["slug"]
    areas = "".join('<a href="%s">%s</a>' % (area_url(a), a["name"]) for a in AREAS)
    return """<footer class="site-footer">
<div class="footer-grid">
<div class="footer-col footer-brand">
<a class="brand" href="/">{logo}<span class="brand-txt"><span class="brand-name">GBT Painting</span><span class="brand-sub">&amp; Decorating</span></span></a>
<p class="footer-blurb">Trusted painting, decorating and tiling in Colchester and across Essex since 2008. Homeowners, landlords and letting agents — fully insured, clean and reliable.</p>
<div class="footer-social">
<a href="{fb}" aria-label="Facebook" target="_blank" rel="noopener">{fbi}</a>
<a href="{wa}" aria-label="WhatsApp" target="_blank" rel="noopener">{wai}</a>
<a href="{tel}" aria-label="Call">{phi}</a>
</div>
</div>
<div class="footer-col"><h4>Company</h4><ul>{company}</ul></div>
<div class="footer-col"><h4>Services</h4><ul>{svcs}</ul></div>
<div class="footer-col"><h4>Contact</h4>
<div class="fc-row">{phi}<span><strong>{phone}</strong><br>{land}</span></div>
<div class="fc-row">{maili}<a href="mailto:{email}">{email}</a></div>
<div class="fc-row">{clocki}<span>{hours}</span></div>
<div class="fc-row">{pini}<span>Colchester &amp; {region}</span></div>
</div>
</div>
<div class="footer-col" style="max-width:var(--maxw);margin:0 auto;padding:0 24px 30px">
<h4>Areas Covered</h4><div class="footer-areas">{areas}</div>
</div>
<div class="footer-bottom">
<span>&copy; <span id="footYear">2026</span> GBT Painting &amp; Decorating. All rights reserved.</span>
<span>Colchester &middot; {region} &middot; Established 2008 &middot; <em>Demo site</em></span>
</div>
</footer>""".format(
        logo=logo_mark(), fb=BIZ["facebook_url"], fbi=icon("facebook"),
        wa=wa_link(), wai=icon("whatsapp"), tel=TEL, phi=icon("phone"),
        company=company_links, svcs=svc_links, phone=BIZ["phone_display"],
        land="Landline: " + BIZ["landline_display"], maili=icon("mail"), email=BIZ["email"],
        clocki=icon("clock"), hours=BIZ["hours"], pini=icon("mappin"),
        region=BIZ["region"], areas=areas)


# --- Quote form -----------------------------------------------------------
def quote_form(on_dark=False, heading="Get Your Free Quote", sub="I'll get back to you within a few hours", source="Website"):
    checks = "".join(
        '<label><input type="checkbox" name="svc" value="{n}">{n}</label>'.format(n=s["name"])
        for s in SERVICES[:6]
    )
    cls = "quote-card on-dark" if on_dark else "quote-card"
    return """<form class="{cls}" action="https://formsubmit.co/{email}" method="POST">
<input type="hidden" name="_subject" value="New quote request — GBT Painting ({src})">
<input type="hidden" name="_next" value="{domain}/thank-you/">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="true">
<input type="text" name="_honey" style="display:none">
<input type="hidden" name="Services requested" value="">
<div class="qc-head"><h3>{heading}</h3><p>{sub}</p></div>
<div class="qc-form">
<div class="fg-row">
<div class="fg"><label for="qn-{sid}">Name</label><input id="qn-{sid}" type="text" name="Name" required placeholder="Your name"></div>
<div class="fg"><label for="qt-{sid}">Phone</label><input id="qt-{sid}" type="tel" name="Phone" required placeholder="Mobile number"></div>
</div>
<div class="fg"><label for="qe-{sid}">Email</label><input id="qe-{sid}" type="email" name="Email" required placeholder="you@email.com"></div>
<div class="fg"><label>What do you need? <span style="font-weight:400;color:var(--muted)">(tick any)</span></label>
<div class="qc-services">{checks}</div></div>
<div class="fg"><label for="qm-{sid}">Message</label><textarea id="qm-{sid}" name="Message" placeholder="Rooms, rough timescale, anything useful…"></textarea></div>
<button class="btn btn-gold btn-block btn-lg" type="submit" data-track="quote-submit">{ic} Get My Free Quote</button>
<p class="qc-note">{lock} No obligation · I'll reply within a few hours</p>
</div></form>""".format(
        cls=cls, email=BIZ["email"], src=source, domain=BIZ["domain"],
        heading=heading, sub=sub, checks=checks, ic=icon("arrow-right"),
        lock=icon("check"), sid=abs(hash(source)) % 10000,
    )


# --- Hero building blocks -------------------------------------------------
def hero_ticks(items=None):
    items = items or BIZ["usps"]
    lis = "".join("<li>%s%s</li>" % (icon("check"), t) for t in items)
    return '<ul class="hero-ticks">%s</ul>' % lis


def hero_pill():
    return ('<span class="hero-pill"><span class="stars">★★★★★</span> Rated {r} · {c} happy customers</span>'
            .format(r=BIZ["rating"], c=BIZ["review_count"]))


def hero_price(label, value, unit=""):
    u = ' <small>%s</small>' % unit if unit else ""
    return ('<span class="hero-price"><span class="lbl">{l}</span><span class="val">{v}{u}</span></span>'
            .format(l=label, v=value, u=u))


# --- Section head ---------------------------------------------------------
def sec_head(title, sub="", left=False):
    cls = "sec-head left" if left else "sec-head"
    subhtml = '<p class="sec-sub">%s</p>' % sub if sub else ""
    return '<div class="{cls}"><h2 class="sec-title">{t}</h2><div class="gold-rule"></div>{s}</div>'.format(
        cls=cls, t=title, s=subhtml)


# --- Service cards --------------------------------------------------------
def service_cards():
    cards = ""
    for s in SERVICES:
        cards += """<article class="card">
<div class="svc-icon">{ic}</div>
<h3>{name}</h3><p>{short}</p>
<a class="card-link" href="{url}">View service {ar}</a>
</article>""".format(ic=icon(s["icon"]), name=s["name"], short=s["short"],
                     url=svc_url(s), ar=icon("arrow-right"))
    return '<div class="grid grid-4">%s</div>' % cards


def service_pill_row(current_slug=None):
    pills = ""
    for s in SERVICES:
        if s["slug"] == current_slug:
            continue
        pills += '<a class="area-tag" href="%s">%s</a>' % (svc_url(s), s["name"])
    return '<div class="tag-grid">%s</div>' % pills


def area_pill_row():
    pills = "".join('<a class="area-tag" href="%s">%s</a>' % (area_url(a), a["name"]) for a in AREAS)
    return '<div class="tag-grid">%s</div>' % pills


# --- Gallery --------------------------------------------------------------
def gallery(themes):
    slots = ""
    for t in themes:
        label, place = GALLERY_LABELS.get(t, ("Recent work", BIZ["city"]))
        slots += """<figure class="ba-slot">
<img src="/assets/images/{t}.svg" alt="{label} in {place} by GBT Painting &amp; Decorating" loading="lazy" width="800" height="600">
<figcaption class="ba-tag">{label} · {place}</figcaption>
<span class="ba-zoom">{zoom}</span>
</figure>""".format(t=t, label=label, place=place, zoom=icon("search"))
    return '<div class="ba-grid g3">%s</div>' % slots


# --- Reviews --------------------------------------------------------------
def review_card(r, on_dark=True):
    name, place, service, stars, text = r
    initials = "".join(w[0] for w in name.split()[:2]).upper()
    return """<article class="rev-card">
<div class="rev-top"><span class="rev-stars">{st}</span>{g}</div>
<p class="rev-text">&ldquo;{text}&rdquo;</p>
<div class="rev-author"><span class="rev-ava">{ini}</span>
<span><span class="rev-name">{name}</span><span class="rev-meta">{place} · {service}</span></span></div>
</article>""".format(st="★" * stars, g=google_logo(), text=text, ini=initials,
                     name=name, place=place, service=service)


def reviews_section(subset=None, dark=True, heading="What Colchester Customers Say"):
    subset = subset if subset is not None else REVIEWS[:6]
    cards = "".join(review_card(r) for r in subset)
    cls = "section section--navy" if dark else "section section--alt"
    return """<section class="{cls}"><div class="container">
{head}
<div class="grid grid-3">{cards}</div>
<div class="rev-cta"><a class="btn btn-gold btn-lg" href="{g}" target="_blank" rel="noopener" data-track="google-reviews">{star} Read all reviews on Google</a></div>
</div></section>""".format(cls=cls, head=sec_head(heading, "Real reviews from homeowners and landlords across %s and %s." % (BIZ["city"], BIZ["region"])),
                           cards=cards, g=BIZ["google_reviews_url"], star=icon("star"))


# --- FAQ ------------------------------------------------------------------
def faq_section(faqs, heading="Frequently Asked Questions", alt=True):
    items = ""
    for q, a in faqs:
        items += """<div class="faq-item">
<button class="faq-q" aria-expanded="false">{q}<span class="ic">{plus}</span></button>
<div class="faq-a"><div class="faq-a-inner">{a}</div></div>
</div>""".format(q=q, a=a, plus=icon("plus"))
    cls = "section section--alt" if alt else "section"
    return """<section class="{cls}"><div class="container">
{head}
<div class="faq">{items}</div>
</div></section>""".format(cls=cls, head=sec_head(heading), items=items)


# --- CTA band -------------------------------------------------------------
def cta_band(heading=None, sub=None):
    heading = heading or "Ready for a Fresh Finish?"
    sub = sub or "Free, no-obligation quotes across Colchester &amp; Essex. Call, email or send a photo on WhatsApp — I'll do the rest."
    return """<section class="cta-band"><div class="cta-inner">
<h2>{h}</h2><p>{s}</p>
<div class="cta-actions">
<a class="btn btn-gold btn-lg" href="{tel}" data-track="cta-call">{ph} Call {phone}</a>
<a class="btn btn-wa btn-lg" href="{wa}" target="_blank" rel="noopener" data-track="cta-whatsapp">{wapp} WhatsApp a photo</a>
<a class="btn btn-navy-outline btn-lg" href="/contact/">Request a quote</a>
</div></div></section>""".format(h=heading, s=sub, tel=TEL, ph=icon("phone"),
                                 phone=BIZ["phone_display"], wa=wa_link(), wapp=icon("whatsapp"))


# --- Trust strip ----------------------------------------------------------
def trust_strip():
    items = [
        ("verified", "Established 2008"),
        ("shield", "Fully insured"),
        ("star", "5.0 Google rating"),
        ("leaf", "Low-odour, quality paints"),
        ("thumb", "Clean &amp; tidy, guaranteed"),
    ]
    inner = "".join('<span class="trust-item">%s%s</span>' % (icon(k), v) for k, v in items)
    return '<div class="trust-strip"><div class="trust-inner">%s</div></div>' % inner


# --- WhatsApp float + lightbox -------------------------------------------
def wa_float():
    return ('<a class="wa-float" href="%s" target="_blank" rel="noopener" aria-label="Chat on WhatsApp" data-track="float-whatsapp">%s</a>'
            % (wa_link(), icon("whatsapp")))


def lightbox():
    return ('<div class="lightbox" id="lightbox" role="dialog" aria-label="Image preview">'
            '<button class="lightbox-close" aria-label="Close">%s</button><img src="" alt=""></div>'
            % icon("close"))


# --- Info sidebar card ----------------------------------------------------
def info_card():
    rows = [
        ("clock", "<strong>%s</strong>" % BIZ["hours"]),
        ("mappin", "Colchester &amp; %s villages" % BIZ["region"]),
        ("shield", "Fully insured, established %s" % BIZ["established"]),
        ("check", "Free written quotes"),
    ]
    lis = "".join("<li>%s<span>%s</span></li>" % (icon(k), v) for k, v in rows)
    return """<div class="info-card">
<h3>Talk to GBT today</h3>
<ul>{lis}</ul>
<div style="display:grid;gap:10px;margin-top:18px">
<a class="btn btn-gold btn-block" href="{tel}" data-track="side-call">{ph} {phone}</a>
<a class="btn btn-wa btn-block" href="{wa}" target="_blank" rel="noopener">{wapp} WhatsApp</a>
</div></div>""".format(lis=lis, tel=TEL, ph=icon("phone"), phone=BIZ["phone_display"],
                       wa=wa_link(), wapp=icon("whatsapp"))


# --- JSON-LD helpers ------------------------------------------------------
def local_business_ld():
    return {
        "@context": "https://schema.org",
        "@type": "HomeAndConstructionBusiness",
        "@id": BIZ["domain"] + "/#business",
        "name": BIZ["name"],
        "image": BIZ["domain"] + "/assets/images/exterior.svg",
        "description": "Professional painting, decorating and tiling in Colchester and across Essex since 2008.",
        "telephone": "+44" + BIZ["phone_raw"].lstrip("0"),
        "email": BIZ["email"],
        "url": BIZ["domain"],
        "priceRange": "££",
        "foundingDate": BIZ["established"],
        "areaServed": [a["name"] for a in AREAS] + [BIZ["city"], BIZ["region"]],
        "address": {"@type": "PostalAddress", "addressLocality": BIZ["city"],
                    "addressRegion": BIZ["region"], "addressCountry": "GB"},
        "openingHours": "Mo-Sa 08:00-18:00",
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": BIZ["rating"],
                            "reviewCount": "150", "bestRating": "5"},
    }


def breadcrumb_ld(trail):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name,
             "item": BIZ["domain"] + url}
            for i, (name, url) in enumerate(trail)
        ],
    }


def faq_ld(faqs):
    import re
    def strip(t):
        return re.sub("<[^>]+>", "", t).replace("&amp;", "&").replace("&ldquo;", '"').replace("&rdquo;", '"')
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": strip(q),
             "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
            for q, a in faqs
        ],
    }
