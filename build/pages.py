# -*- coding: utf-8 -*-
"""Page builders — assemble full pages from components + data."""
from .data import BIZ, SERVICES, AREAS, REVIEWS, REGION, FAQ_GENERAL
from .svg import icon
from . import components as C


def _price_str(s):
    return "£%d" % s["price_from"]


# =========================================================================
# HOME
# =========================================================================
def home():
    top_links = (' <a href="%s">interior</a> and <a href="%s">exterior painting</a>, '
                 '<a href="%s">wallpapering</a> and <a href="%s">tiling</a>'
                 % (C.svc_url(SERVICES[0]), C.svc_url(SERVICES[1]),
                    C.svc_url(SERVICES[2]), C.svc_url(SERVICES[4])))
    hero = """<section class="hero"><div class="hero-inner">
<div class="hero-copy">
{pill}
<h1><span class="hl">Colchester</span> Painting &amp; Decorating You Can Trust</h1>
<p class="hero-intro">Friendly, reliable painting and decorating across Colchester and Essex since 2008. From{links} — I bring careful prep, a clean finish and honest prices to every home.</p>
{ticks}
<div class="hero-actions">
<a class="btn btn-gold btn-lg" href="{tel}" data-track="hero-call">{ph} Call {phone}</a>
{price}
</div>
</div>
<div>{form}</div>
</div></section>""".format(
        pill=C.hero_pill(), links=top_links, ticks=C.hero_ticks(),
        tel=C.TEL, ph=icon("phone"), phone=BIZ["phone_display"],
        price=C.hero_price("Rooms from", "£180", "· free quotes"),
        form=C.quote_form(on_dark=True, source="Home hero"),
    )

    services = """<section class="section"><div class="container">
{head}
{cards}
</div></section>""".format(
        head=C.sec_head("Painting &amp; Decorating Services",
                        "Everything to refresh and protect your home — inside and out."),
        cards=C.service_cards())

    who = """<section class="section section--alt"><div class="container">
{head}
<div class="grid grid-4">
{cards}
</div></div></section>""".format(
        head=C.sec_head("Who I Work With", "A trusted local decorator for homeowners, landlords and agents."),
        cards="".join(
            '<article class="feat"><div class="feat-icon">%s</div><h3>%s</h3><p>%s</p></article>' % (icon(k), t, d)
            for k, t, d in [
                ("house", "Homeowners", "Complete interior &amp; exterior transformations for your home."),
                ("shield", "Landlords", "Durable, cost-effective decorating that protects your investment."),
                ("keys", "Estate &amp; Letting Agents", "Getting properties 'sale-ready' or 'let-ready' with minimal fuss."),
                ("calendar", "End of Tenancy", "Fast, professional redecoration between tenants to cut void periods."),
            ]))

    gallery = """<section class="section"><div class="container">
{head}
{g}
<p class="text-center" style="margin-top:26px"><a class="btn btn-navy" href="/testimonials/">See more of my work {ar}</a></p>
</div></section>""".format(
        head=C.sec_head("Recent Work Around Colchester",
                        "Painting, wallpapering, murals, tiling and the odd jobs in between."),
        g=C.gallery(["interior", "exterior", "wallpaper", "tile", "mural", "frontdoor"]),
        ar=icon("arrow-right"))

    why = """<section class="section section--navy"><div class="container">
{head}
<div class="grid grid-4">
{cards}
</div></div></section>""".format(
        head=C.sec_head("Why Choose GBT?"),
        cards="".join(
            '<article class="feat"><div class="feat-icon">%s</div><h3>%s</h3><p>%s</p></article>' % (icon(k), t, d)
            for k, t, d in [
                ("verified", "17+ Years' Experience", "Serving Colchester and the surrounding villages since 2008."),
                ("thumb", "One Reliable Tradesman", "You deal with me from quote to completion — no call centres."),
                ("leaf", "Careful &amp; Clean", "Furniture protected, low-odour paints, tidy every single day."),
                ("pound", "Honest, Clear Pricing", "Free written quotes and fair prices — no nasty surprises."),
            ]))

    reviews = C.reviews_section(REVIEWS[:6], dark=False)

    cover = """<section class="section"><div class="container">
{head}
<div class="cover-region">
<h3>{pin} Across {region}</h3>
{areas}
</div>
<p class="text-center" style="margin-top:8px;color:var(--muted)">Don't see your area? I cover Colchester and the surrounding towns and villages — <a href="/contact/">just ask</a>.</p>
</div></section>""".format(
        head=C.sec_head("Where I Cover",
                        "Based in Colchester, covering %s and the villages around it." % BIZ["region"]),
        pin=icon("mappin"), region=BIZ["region"], areas=C.area_pill_row())

    faqs = C.faq_section(FAQ_GENERAL)

    body = hero + C.trust_strip() + services + who + gallery + why + reviews + cover + faqs
    jsonld = [C.local_business_ld(), C.faq_ld(FAQ_GENERAL)]
    return C.document(
        title="Painting &amp; Decorating Colchester | GBT Painting &amp; Decorating",
        description="Trusted painting, decorating &amp; tiling in Colchester &amp; Essex since 2008. Interior &amp; exterior painting, wallpapering, tiling. Fully insured. Free quotes — call 07547 187787.",
        canonical="/", body=body, jsonld=jsonld,
    )


# =========================================================================
# SERVICE PAGE
# =========================================================================
def _service_faqs(s):
    base = [
        ("How much does %s cost in Colchester?" % s["name"].lower(),
         "I price every job individually after seeing it, so you get a fair, accurate quote — guide prices for this service start from around %s. Quotes are always free and in writing." % _price_str(s)),
        ("How soon can you start?",
         "It depends on the season, but I can usually book you in within a week or two — and I'll always give you an honest lead time up front. For urgent work like end-of-tenancy, get in touch and I'll do my best to fit you in."),
        ("Do you cover my area?",
         "Yes — I cover Colchester and the surrounding Essex villages including Stanway, Highwoods, Wivenhoe, the Mersea Island villages, West Bergholt, Copford, Tiptree and Dedham."),
        ("Are you insured?",
         "Fully insured, and decorating locally since 2008. You're in safe, experienced hands."),
    ]
    return base


def service_page(s):
    url = C.svc_url(s)
    trail = [("Home", "/"), ("Services", "/#services"), (s["name"], url)]
    crumb = ('<div class="crumb"><a href="/">Home</a> {c} <a href="/">Services</a> {c} <span>{n}</span></div>'
             .format(c=icon("chev-right"), n=s["name"]))

    hero = """<section class="sv-hero hero"><div class="sv-hero-inner hero-inner">
<div class="hero-copy">
{crumb}
<h1><span class="hl">{name}</span> in Colchester</h1>
<p class="hero-intro">{intro}</p>
{ticks}
<div class="hero-actions">
<a class="btn btn-gold btn-lg" href="{tel}" data-track="svc-call">{ph} Call {phone}</a>
{price}
</div>
</div>
<div>{form}</div>
</div></section>""".format(
        crumb=crumb, name=s["name"], intro=s["intro"], ticks=C.hero_ticks(),
        tel=C.TEL, ph=icon("phone"), phone=BIZ["phone_display"],
        price=C.hero_price("%s from" % s["name"], _price_str(s), s["price_unit"]),
        form=C.quote_form(on_dark=True, heading="Free %s Quote" % s["name"], source=s["name"]))

    included = "".join("<li>%s</li>" % i for i in s["included"])
    steps = "".join(
        '<div class="step"><span class="step-num">%d</span><div><h4>%s</h4><p>%s</p></div></div>' % (i + 1, t, d)
        for i, (t, d) in enumerate(s["steps"]))

    main = """<section class="section"><div class="container two-col">
<div class="prose">
<h2>{name} — {benefit}</h2>
<p>{intro} Whether it's a single room or a whole property, you get the same careful preparation, quality materials and tidy workmanship that GBT has built its reputation on since 2008.</p>
<h3>What's included</h3>
<ul>{included}</ul>
<h3>How it works</h3>
<div class="steps">{steps}</div>
<h3>Guide pricing</h3>
<p>Every job is different, so I give a free written quote after seeing the work — but as a guide, {namelower} starts from <strong>{price} {unit}</strong>. You'll always know the price before I lift a brush.</p>
</div>
<aside class="sidebar-sticky">
{info}
<div class="card"><h3>Popular with</h3><p style="font-size:.95rem">Homeowners, landlords, letting agents and end-of-tenancy turnarounds across Colchester &amp; Essex.</p>
<a class="card-link" href="/contact/">Request a quote {ar}</a></div>
</aside>
</div></section>""".format(
        name=s["name"], benefit=s["benefit"], intro=s["intro"], included=included, steps=steps,
        namelower=s["name"].lower(), price=_price_str(s), unit=s["price_unit"],
        info=C.info_card(), ar=icon("arrow-right"))

    gallery = """<section class="section section--alt"><div class="container">
{head}
{g}
</div></section>""".format(
        head=C.sec_head("Recent %s Work" % s["name"]),
        g=C.gallery(s["gallery"]))

    related = """<section class="section"><div class="container">
{head}
{pills}
<div class="sec-head" style="margin:44px auto 24px"><h3>Areas I cover</h3></div>
{areas}
</div></section>""".format(
        head=C.sec_head("Other Services", "Need something else? I do the lot."),
        pills=C.service_pill_row(current_slug=s["slug"]),
        areas=C.area_pill_row())

    faqs = _service_faqs(s)
    faq = C.faq_section(faqs, heading="%s — Your Questions" % s["name"])
    reviews = C.reviews_section(REVIEWS[:3], dark=True)

    body = hero + C.trust_strip() + main + gallery + reviews + related + faq

    service_ld = {
        "@context": "https://schema.org", "@type": "Service",
        "serviceType": s["name"], "provider": {"@id": BIZ["domain"] + "/#business"},
        "areaServed": {"@type": "City", "name": BIZ["city"]},
        "description": s["intro"],
        "offers": {"@type": "Offer", "price": str(s["price_from"]), "priceCurrency": "GBP",
                   "description": "%s from £%d %s" % (s["name"], s["price_from"], s["price_unit"])},
    }
    jsonld = [C.local_business_ld(), service_ld, C.breadcrumb_ld(trail), C.faq_ld(faqs)]

    title = "%s Colchester | %s | %s" % (s["name"], s["meta_kw"], BIZ["short"])
    desc = ("%s in Colchester &amp; Essex by GBT — %s. Fully insured, established 2008. Free quotes from %s %s. Call %s."
            % (s["name"], s["benefit"].lower(), _price_str(s), s["price_unit"], BIZ["phone_display"]))
    return C.document(title=title, description=desc, canonical=url, body=body, jsonld=jsonld,
                      og_type="website", og_image="/assets/images/%s.svg" % s["gallery"][0])


# =========================================================================
# AREA PAGE
# =========================================================================
def _area_faqs(a):
    return [
        ("Do you cover %s?" % a["name"],
         "Yes — %s is right in my patch. I regularly work across %s (%s) and the surrounding area, so I can usually get to you quickly for a quote." % (a["name"], a["name"], a["postcode"])),
        ("How much does painting and decorating cost in %s?" % a["name"],
         "Every %s property is different, so I give a free written quote after a quick look. As a guide, interior rooms start from around £180 and exterior jobs are priced individually." % a["name"]),
        ("Can you work around us / our tenants?",
         "Of course. Whether you live in the property or it's a rental in %s, I plan the work around you — dust sheets down, low-odour paints, and the place left clean each day." % a["name"]),
        ("How do I get a quote?",
         "Call %s, email me, or send a few photos on WhatsApp for a fast ballpark — I reply in around 10 minutes during working hours." % BIZ["phone_display"]),
    ]


def area_page(a):
    url = C.area_url(a)
    trail = [("Home", "/"), ("Areas", "/" + REGION["slug"] + "/"), (a["name"], url)]
    crumb = ('<div class="crumb"><a href="/">Home</a> {c} <a href="/{hub}/">Areas</a> {c} <span>{n}</span></div>'
             .format(c=icon("chev-right"), hub=REGION["slug"], n=a["name"]))

    hero = """<section class="area-hero hero"><div class="area-hero-inner hero-inner">
<div class="hero-copy">
{crumb}
<h1><span class="hl">{name}</span> Painting &amp; Decorating</h1>
<p class="hero-intro">{blurb} A reliable local decorator for {name} homeowners, landlords and letting agents — trusted across {region} since 2008.</p>
{ticks}
<div class="hero-actions">
<a class="btn btn-gold btn-lg" href="{tel}" data-track="area-call">{ph} Call {phone}</a>
{price}
</div>
</div>
<div>{form}</div>
</div></section>""".format(
        crumb=crumb, name=a["name"], blurb=a["blurb"], region=BIZ["region"], ticks=C.hero_ticks(),
        tel=C.TEL, ph=icon("phone"), phone=BIZ["phone_display"],
        price=C.hero_price("Rooms from", "£180", "· free quotes"),
        form=C.quote_form(on_dark=True, heading="Free %s Quote" % a["name"], source="Area: " + a["name"]))

    gallery1 = """<section class="section"><div class="container">
{head}{g}</div></section>""".format(
        head=C.sec_head("Recent Work Near %s" % a["name"]),
        g=C.gallery(["interior", "exterior", "wallpaper"]))

    pills = """<section class="section section--alt"><div class="container">
{head}{p}</div></section>""".format(
        head=C.sec_head("How I Can Help in %s" % a["name"], "Every service, on your doorstep."),
        p=C.service_pill_row())

    local_paras = "".join("<h3>%s</h3><p>%s</p>" % (t, p) for t, p in a["paras"])
    local = """<section class="section"><div class="container two-col">
<div class="prose">
<h2>Painting &amp; Decorating in {name} — {region} Homes Deserve the Best</h2>
{paras}
</div>
<aside class="sidebar-sticky">
{rev}
<div class="info-card"><h3>Why {name} chooses GBT</h3>
<ul>
<li>{ck}<span>Local, reliable and fully insured</span></li>
<li>{ck}<span>Careful prep &amp; a clean, tidy finish</span></li>
<li>{ck}<span>Honest written quotes, no surprises</span></li>
<li>{ck}<span>Decorating {region} since 2008</span></li>
</ul>
<a class="btn btn-gold btn-block" href="{tel}" style="margin-top:16px">{ph} {phone}</a>
</div>
</aside>
</div></section>""".format(
        name=a["name"], region=BIZ["region"], paras=local_paras,
        rev=C.review_card(_pick_area_review(a)), ck=icon("check"),
        tel=C.TEL, ph=icon("phone"), phone=BIZ["phone_display"])

    gallery2 = """<section class="section section--alt"><div class="container">
{head}{g}</div></section>""".format(
        head=C.sec_head("More Local Transformations"),
        g=C.gallery(["frontdoor", "tile", "feature"]))

    faqs = _area_faqs(a)
    faq = C.faq_section(faqs, heading="%s — Common Questions" % a["name"], alt=False)
    reviews = C.reviews_section(REVIEWS[:3], dark=True, heading="Reviews from %s &amp; Nearby" % a["name"])

    body = hero + C.trust_strip() + gallery1 + pills + local + gallery2 + reviews + faq

    place_ld = {
        "@context": "https://schema.org", "@type": "Service",
        "serviceType": "Painting and Decorating",
        "provider": {"@id": BIZ["domain"] + "/#business"},
        "areaServed": {"@type": "City", "name": a["name"],
                       "address": {"@type": "PostalAddress", "addressLocality": a["name"],
                                   "postalCode": a["postcode"], "addressRegion": BIZ["region"],
                                   "addressCountry": "GB"}},
        "description": "Painting, decorating and tiling in %s, %s by GBT Painting & Decorating." % (a["name"], BIZ["region"]),
    }
    jsonld = [C.local_business_ld(), place_ld, C.breadcrumb_ld(trail), C.faq_ld(faqs)]

    title = "Painting &amp; Decorating %s | Decorator %s (%s)" % (a["name"], a["name"], a["postcode"])
    desc = ("Painting &amp; decorating in %s by GBT — %s Fully insured local decorator, established 2008. Free quotes. Call %s."
            % (a["name"], a["blurb"], BIZ["phone_display"]))
    return C.document(title=title, description=desc, canonical=url, body=body, jsonld=jsonld,
                      og_image="/assets/images/exterior.svg")


def _pick_area_review(a):
    for r in REVIEWS:
        if r[1] == a["name"]:
            return r
    return REVIEWS[0]


# =========================================================================
# REGION HUB
# =========================================================================
def region_hub():
    url = "/%s/" % REGION["slug"]
    cards = ""
    for a in AREAS:
        cards += """<article class="card">
<div class="svc-icon">{pin}</div>
<h3>{name}</h3><p>{blurb}</p>
<a class="card-link" href="{url}">{name} decorating {ar}</a>
</article>""".format(pin=icon("mappin"), name=a["name"], blurb=a["blurb"],
                     url=C.area_url(a), ar=icon("arrow-right"))

    hero = """<section class="hero"><div class="container" style="padding:64px 24px 20px;position:relative;z-index:2">
<div class="crumb"><a href="/">Home</a> {c} <span>Essex</span></div>
<h1 style="max-width:800px"><span class="hl">Essex</span> Painting &amp; Decorating Services</h1>
<p class="hero-intro" style="max-width:760px">{blurb}</p>
<div class="hero-actions"><a class="btn btn-gold btn-lg" href="{tel}">{ph} Call {phone}</a>
<a class="btn btn-navy-outline btn-lg" href="/contact/">Get a free quote</a></div>
</div></section>""".format(c=icon("chev-right"), blurb=REGION["blurb"],
                           tel=C.TEL, ph=icon("phone"), phone=BIZ["phone_display"])

    body = hero + C.trust_strip() + """<section class="section"><div class="container">
{head}
<div class="grid grid-3">{cards}</div>
</div></section>""".format(
        head=C.sec_head("Towns &amp; Villages I Cover", "Tap your area for local painting &amp; decorating."),
        cards=cards) + C.reviews_section(REVIEWS[:6], dark=True) + C.faq_section(FAQ_GENERAL)

    jsonld = [C.local_business_ld(), C.breadcrumb_ld([("Home", "/"), ("Essex", url)])]
    title = "Painting &amp; Decorating Essex | Areas Covered | %s" % BIZ["short"]
    desc = "GBT Painting & Decorating covers Colchester and villages across Essex — Stanway, Wivenhoe, Mersea, Tiptree, Dedham and more. Fully insured. Free quotes: 07547 187787."
    return C.document(title=title, description=desc, canonical=url, body=body, jsonld=jsonld)


# =========================================================================
# CONTACT
# =========================================================================
def contact():
    url = "/contact/"
    details = """<div class="prose">
<h2>Get in touch</h2>
<p>The quickest way to a price is to send a few photos on WhatsApp — I usually reply within about 10 minutes during working hours. Prefer to talk? Give me a call. Every quote is free and with no obligation.</p>
<div class="info-card" style="margin-top:24px">
<h3>Contact details</h3>
<ul>
<li>{ph}<span><strong>Mobile:</strong> <a href="{tel}" style="color:#fff">{phone}</a></span></li>
<li>{ph}<span><strong>Landline:</strong> <a href="{tell}" style="color:#fff">{land}</a></span></li>
<li>{mail}<span><strong>Email:</strong> <a href="mailto:{email}" style="color:#fff">{email}</a></span></li>
<li>{clock}<span><strong>Hours:</strong> {hours}</span></li>
<li>{pin}<span><strong>Area:</strong> Colchester &amp; {region} villages</span></li>
</ul>
<div style="display:grid;gap:10px;margin-top:18px">
<a class="btn btn-wa btn-block" href="{wa}" target="_blank" rel="noopener">{wapp} WhatsApp a photo</a>
</div>
</div>
<div class="badge-row" style="margin-top:22px">
<span class="badge">{v} Established 2008</span>
<span class="badge">{s} Fully insured</span>
<span class="badge">{st} 5.0 Google rating</span>
</div>
</div>""".format(
        ph=icon("phone"), tel=C.TEL, phone=BIZ["phone_display"], tell=C.TEL_LAND, land=BIZ["landline_display"],
        mail=icon("mail"), email=BIZ["email"], clock=icon("clock"), hours=BIZ["hours"],
        pin=icon("mappin"), region=BIZ["region"], wa=C.wa_link(), wapp=icon("whatsapp"),
        v=icon("verified"), s=icon("shield"), st=icon("star"))

    hero = """<section class="hero"><div class="container" style="padding:56px 24px 18px;position:relative;z-index:2">
<div class="crumb"><a href="/">Home</a> {c} <span>Contact</span></div>
<h1><span class="hl">Contact</span> GBT Painting &amp; Decorating</h1>
<p class="hero-intro" style="max-width:680px">Free, no-obligation quotes across Colchester &amp; Essex. Call, email or send a photo — I'll do the rest.</p>
</div></section>""".format(c=icon("chev-right"))

    body = hero + C.trust_strip() + """<section class="section"><div class="container two-col">
{details}
<aside>{form}</aside>
</div></section>""".format(details=details, form=C.quote_form(heading="Request a Free Quote", source="Contact page"))

    jsonld = [C.local_business_ld(), C.breadcrumb_ld([("Home", "/"), ("Contact", url)])]
    return C.document(
        title="Contact | Painting &amp; Decorating Colchester | %s" % BIZ["short"],
        description="Contact GBT Painting & Decorating in Colchester. Call 07547 187787, email or WhatsApp a photo for a fast free quote. Fully insured, established 2008.",
        canonical=url, body=body, jsonld=jsonld)


# =========================================================================
# TESTIMONIALS
# =========================================================================
def testimonials():
    url = "/testimonials/"
    cards = "".join(C.review_card(r) for r in REVIEWS)
    hero = """<section class="hero"><div class="container" style="padding:56px 24px 18px;position:relative;z-index:2">
<div class="crumb"><a href="/">Home</a> {c} <span>Reviews</span></div>
{pill}
<h1><span class="hl">Reviews</span> &amp; Recent Work</h1>
<p class="hero-intro" style="max-width:700px">Don't just take my word for it — here's what homeowners, landlords and letting agents across Colchester &amp; Essex say about GBT.</p>
</div></section>""".format(c=icon("chev-right"), pill=C.hero_pill())

    body = hero + C.trust_strip() + """<section class="section"><div class="container">
{head}<div class="grid grid-3">{cards}</div>
<div class="rev-cta"><a class="btn btn-gold btn-lg" href="{g}" target="_blank" rel="noopener">{star} Read all reviews on Google</a></div>
</div></section>""".format(head=C.sec_head("What Customers Say"), cards=cards,
                           g=BIZ["google_reviews_url"], star=icon("star")) + \
        """<section class="section section--alt"><div class="container">
{head}{g}</div></section>""".format(
            head=C.sec_head("A Look at the Work",
                            "Painting, wallpapering, murals and tiling across the area."),
            g=C.gallery(["interior", "exterior", "wallpaper", "mural", "tile", "frontdoor",
                         "hallway", "render", "feature"]))

    jsonld = [C.local_business_ld()]
    return C.document(
        title="Reviews &amp; Testimonials | Painting Colchester | %s" % BIZ["short"],
        description="Read reviews of GBT Painting & Decorating from customers across Colchester & Essex. 5.0 rated, established 2008. Fully insured painter & decorator.",
        canonical=url, body=body, jsonld=jsonld)


# =========================================================================
# THANK YOU
# =========================================================================
def thank_you():
    url = "/thank-you/"
    body = """<section class="section"><div class="ty-wrap">
<div class="ty-check">{ck}</div>
<h1>Thank you — message received!</h1>
<p style="font-size:1.12rem">Thanks for getting in touch with GBT Painting &amp; Decorating. I've received your details and will get back to you as soon as I can, usually within a few hours during working hours.</p>
<p>Need a faster answer? Send a few photos straight to my WhatsApp and I'll reply in around 10 minutes.</p>
<div class="cta-actions" style="justify-content:center;margin-top:28px">
<a class="btn btn-wa btn-lg" href="{wa}" target="_blank" rel="noopener">{wapp} WhatsApp a photo</a>
<a class="btn btn-navy btn-lg" href="{tel}">{ph} Call {phone}</a>
<a class="btn btn-navy-outline btn-lg" href="/" style="color:var(--navy);border-color:var(--navy)">Back to home</a>
</div>
</div></section>""".format(ck=icon("check"), wa=C.wa_link(), wapp=icon("whatsapp"),
                           tel=C.TEL, ph=icon("phone"), phone=BIZ["phone_display"])
    return C.document(
        title="Thank You | %s" % BIZ["short"],
        description="Thank you for contacting GBT Painting & Decorating. We'll be in touch shortly.",
        canonical=url, body=body, jsonld=[], og_type="website")


# =========================================================================
# LEGAL
# =========================================================================
def legal(kind):
    if kind == "privacy":
        url = "/privacy-policy/"
        title = "Privacy Policy | %s" % BIZ["short"]
        h1 = "Privacy Policy"
        content = """
<p>GBT Painting &amp; Decorating ("we", "I") respects your privacy. This policy explains what we collect and how we use it. <em>This is a demo page — replace with your finalised policy before going live.</em></p>
<h2>What we collect</h2>
<p>When you submit the quote form or contact us, we collect your name, phone number, email address and any details you provide about your project. We do not collect payment details through this website.</p>
<h2>How we use it</h2>
<ul><li>To respond to your enquiry and provide a quote</li><li>To carry out work you ask us to do</li><li>To keep records for accounting and legal purposes</li></ul>
<h2>Sharing</h2>
<p>We do not sell your data. Form submissions are delivered to us by email via FormSubmit. We only share information where required by law.</p>
<h2>Your rights</h2>
<p>You can ask us to see, correct or delete the personal data we hold about you. Contact us at <a href="mailto:{email}">{email}</a>.</p>
<h2>Cookies</h2>
<p>This site uses minimal cookies. Third-party fonts are loaded from Google Fonts.</p>
""".format(email=BIZ["email"])
    else:
        url = "/terms-of-service/"
        title = "Terms of Service | %s" % BIZ["short"]
        h1 = "Terms of Service"
        content = """
<p><em>This is a demo page — replace with your finalised terms before going live.</em></p>
<h2>Quotes</h2>
<p>All quotes are free and valid for 30 days unless stated otherwise. Prices may change if the scope of work changes or if additional preparation is needed once work begins.</p>
<h2>Bookings &amp; payment</h2>
<p>Dates are confirmed in writing. Payment terms are agreed before work starts. For larger jobs a deposit may be requested to cover materials.</p>
<h2>Workmanship</h2>
<p>We take pride in our work and aim to leave every job clean and tidy. If you're not happy with any aspect, tell us and we'll put it right.</p>
<h2>Liability</h2>
<p>GBT Painting &amp; Decorating is fully insured. Nothing in these terms limits liability where it cannot lawfully be limited.</p>
<h2>Contact</h2>
<p>Questions about these terms? Email <a href="mailto:{email}">{email}</a> or call {phone}.</p>
""".format(email=BIZ["email"], phone=BIZ["phone_display"])

    hero = """<section class="hero"><div class="container" style="padding:52px 24px 18px;position:relative;z-index:2">
<div class="crumb"><a href="/">Home</a> {c} <span>{h1}</span></div>
<h1>{h1}</h1></div></section>""".format(c=icon("chev-right"), h1=h1)
    body = hero + '<section class="section"><div class="container legal">%s</div></section>' % content
    return C.document(title=title, description="%s for GBT Painting & Decorating, Colchester." % h1,
                      canonical=url, body=body, jsonld=[])
