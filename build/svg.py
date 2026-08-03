# -*- coding: utf-8 -*-
"""Inline SVG icons and generated placeholder gallery images."""

# --- Icon library (Material-style, 24x24) ---------------------------------
_ICONS = {
    "phone": "M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z",
    "check": "M9 16.17 4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z",
    "star": "M12 17.27 18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z",
    "chev-down": "M7.41 8.59 12 13.17l4.59-4.58L18 10l-6 6-6-6z",
    "chev-right": "M8.59 16.59 13.17 12 8.59 7.41 10 6l6 6-6 6z",
    "arrow-right": "M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z",
    "plus": "M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6z",
    "menu": "M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z",
    "close": "M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z",
    "mappin": "M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z",
    "clock": "M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z",
    "mail": "M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z",
    "shield": "M12 1 3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-1 15-4-4 1.41-1.41L11 13.17l5.59-5.59L18 9l-7 7z",
    "search": "M15.5 14h-.79l-.28-.27a6.5 6.5 0 10-.7.7l.27.28v.79l5 5 1.5-1.5-5-5zm-6 0A4.5 4.5 0 1114 9.5 4.5 4.5 0 019.5 14z",
    "pound": "M6 20v-2h1.5c.83 0 1.5-.67 1.5-1.5V13H6v-2h3V8.5A4.5 4.5 0 0113.5 4c1.9 0 3.6 1.2 4.24 2.96l-1.88.68A2.5 2.5 0 0013.5 6 2.5 2.5 0 0011 8.5V11h4v2h-4v3.5c0 .53-.15 1.03-.4 1.5H18v2H6z",
    "leaf": "M6.05 8.05c-2.73 2.73-2.73 7.15-.02 9.88 1.47-3.4 4.09-6.24 7.36-7.93-2.77 2.34-4.71 5.61-5.39 9.32 2.6 1.23 5.8.78 7.95-1.37C19.43 14.47 20 4 20 4S9.53 4.57 6.05 8.05z",
    "thumb": "M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-2z",
    "calendar": "M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11z",
    "verified": "M23 12l-2.44-2.79.34-3.69-3.61-.82-1.89-3.2L12 2.96 8.6 1.5 6.71 4.69 3.1 5.5l.34 3.7L1 12l2.44 2.79-.34 3.7 3.61.82L8.6 22.5l3.4-1.47 3.4 1.46 1.89-3.19 3.61-.82-.34-3.69L23 12zm-12.91 4.72-3.8-3.81 1.48-1.48 2.32 2.33 5.85-5.87 1.48 1.48-7.33 7.35z",
    "facebook": "M22 12c0-5.52-4.48-10-10-10S2 6.48 2 12c0 4.84 3.44 8.87 8 9.8V15H8v-3h2V9.5C10 7.57 11.57 6 13.5 6H16v3h-2c-.55 0-1 .45-1 1v2h3v3h-3v6.95c5.05-.5 9-4.76 9-9.95z",
    "whatsapp": "M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.148-.669-1.612-.916-2.207-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.71.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413",
    # service icons
    "roller": "M18 4V3c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1v4c0 .55.45 1 1 1h12c.55 0 1-.45 1-1V6h1v4H9v11c0 .55.45 1 1 1h2c.55 0 1-.45 1-1v-9h8V4h-4z",
    "brush": "M7 14c-1.66 0-3 1.34-3 3 0 1.31-1.16 2-2 2 .92 1.22 2.49 2 4 2 2.21 0 4-1.79 4-4 0-1.66-1.34-3-3-3zm13.71-9.37-1.34-1.34a.9959.9959 0 00-1.41 0L9 12.25 11.75 15l8.96-8.96a.9959.9959 0 000-1.41z",
    "house": "M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z",
    "wallpaper": "M4 4h7V2H4c-1.1 0-2 .9-2 2v7h2V4zm6 9-4 5h12l-3-4-2.03 2.71L10 13zm7-4.5c0-.83-.67-1.5-1.5-1.5S14 7.67 14 8.5s.67 1.5 1.5 1.5S17 9.33 17 8.5zM20 2h-7v2h7v7h2V4c0-1.1-.9-2-2-2zm0 18h-7v2h7c1.1 0 2-.9 2-2v-7h-2v7zM4 13H2v7c0 1.1.9 2 2 2h7v-2H4v-7z",
    "tile": "M10 4v4h4V4h-4zm-6 6v4h4v-4H4zm6 0v4h4v-4h-4zm6 0v4h4v-4h-4zM4 4v4h4V4H4zm12 0v4h4V4h-4zM4 16v4h4v-4H4zm6 0v4h4v-4h-4zm6 0v4h4v-4h-4z",
    "gutter": "M2 10 12 3l10 7v2H2v-2zm2 4h16v6H4v-6zm2 2v2h2v-2H6zm5 0v2h2v-2h-2zm5 0v2h2v-2h-2z",
    "keys": "M12.65 10A5.99 5.99 0 006.99 4C3.68 4 1 6.68 1 10s2.68 6 5.99 6c2.61 0 4.83-1.67 5.65-4H17v4h4v-4h2v-4H12.65zM7 13c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3z",
}


def icon(name, cls="", size=None):
    """Return an inline <svg> for the named icon.

    Always carries a baseline width/height so a bare icon never renders at the
    SVG default (300x150). CSS class rules override these presentation attrs.
    """
    path = _ICONS.get(name, "")
    dims = '%s' % size if size else "1em"
    attrs = 'fill="currentColor" viewBox="0 0 24 24" aria-hidden="true" width="%s" height="%s"' % (dims, dims)
    if cls:
        attrs += ' class="%s"' % cls
    return '<svg %s><path d="%s"/></svg>' % (attrs, path)


def google_logo(cls="rev-g"):
    """Multi-colour Google 'G'."""
    return (
        '<svg class="%s" viewBox="0 0 48 48" aria-hidden="true">'
        '<path fill="#4285F4" d="M45.12 24.5c0-1.56-.14-3.06-.4-4.5H24v8.51h11.84c-.51 2.75-2.06 5.08-4.39 6.64v5.52h7.11c4.16-3.83 6.56-9.47 6.56-16.17z"/>'
        '<path fill="#34A853" d="M24 46c5.94 0 10.92-1.97 14.56-5.33l-7.11-5.52c-1.97 1.32-4.49 2.1-7.45 2.1-5.73 0-10.58-3.87-12.31-9.07H4.34v5.7C7.96 41.07 15.4 46 24 46z"/>'
        '<path fill="#FBBC05" d="M11.69 28.18C11.25 26.86 11 25.45 11 24s.25-2.86.69-4.18v-5.7H4.34A21.99 21.99 0 002 24c0 3.55.85 6.91 2.34 9.88l7.35-5.7z"/>'
        '<path fill="#EA4335" d="M24 10.75c3.23 0 6.13 1.11 8.41 3.29l6.31-6.31C34.91 4.18 29.93 2 24 2 15.4 2 7.96 6.93 4.34 14.12l7.35 5.7c1.73-5.2 6.58-9.07 12.31-9.07z"/>'
        "</svg>"
    ) % cls


# --- Placeholder gallery images (generated SVG scenes) --------------------
# Each theme paints an on-brand abstract scene so the demo looks intentional
# rather than showing broken images. Real photos drop straight in later.

_PALETTES = {
    "interior": ["#EAD9C0", "#C98A5E", "#F4EDE2", "#8A5A3B"],
    "woodwork": ["#DCE7EE", "#2C5F86", "#F1F5F8", "#12385f"],
    "hallway": ["#E7E0D2", "#7A8B6F", "#F5F1E8", "#4A5A3E"],
    "exterior": ["#BFD3E6", "#D9A441", "#8FB0CE", "#7A4B2A"],
    "render": ["#CFE0EC", "#E8E2D5", "#A9C0D6", "#B0693C"],
    "frontdoor": ["#D7E2EA", "#20527E", "#EFE9DC", "#123a5c"],
    "wallpaper": ["#EFE3D0", "#2E6B6B", "#F6EFE2", "#1c4f4f"],
    "feature": ["#E7DDEA", "#5B4B8A", "#F3EEF6", "#3d2f66"],
    "mural": ["#FCE9D0", "#4FA3C7", "#F7C9A0", "#E56B4E"],
    "tile": ["#DFEAF0", "#3E7CA8", "#F2F6F9", "#2a5a7d"],
    "bathroom": ["#DDEBEA", "#4C9C9C", "#F0F6F5", "#2f6e6e"],
    "kitchen": ["#E9E2D6", "#B4854E", "#F5F0E7", "#7A5630"],
}


def gallery_svg(theme):
    """Build a 800x600 stylised scene for the given theme."""
    p = _PALETTES.get(theme, _PALETTES["interior"])
    bg, accent, light, dark = p[0], p[1], p[2], p[3]
    W, H = 800, 600
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">' % (W, H, W, H)]
    parts.append('<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1">'
                 '<stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>' % (light, bg))
    parts.append('<rect width="%d" height="%d" fill="url(#g)"/>' % (W, H))

    if theme in ("exterior", "render", "frontdoor"):
        # house facade
        parts.append('<rect x="120" y="180" width="560" height="360" fill="%s"/>' % light)
        parts.append('<polygon points="90,190 400,60 710,190" fill="%s"/>' % dark)
        # door
        parts.append('<rect x="360" y="360" width="90" height="180" rx="4" fill="%s"/>' % accent)
        # windows
        for x in (170, 500):
            parts.append('<rect x="%d" y="250" width="120" height="90" fill="%s" stroke="%s" stroke-width="6"/>' % (x, bg, dark))
        parts.append('<rect x="170" y="380" width="120" height="90" fill="%s" stroke="%s" stroke-width="6"/>' % (bg, dark))
    elif theme in ("tile", "bathroom", "kitchen"):
        # tiled grid
        parts.append('<rect x="80" y="80" width="640" height="440" fill="%s"/>' % light)
        gap = 8
        cols, rows = 8, 5
        tw = (640 - gap * (cols + 1)) / cols
        th = (440 - gap * (rows + 1)) / rows
        for r in range(rows):
            for c in range(cols):
                col = accent if (r + c) % 3 == 0 else bg
                x = 80 + gap + c * (tw + gap)
                y = 80 + gap + r * (th + gap)
                parts.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s"/>' % (x, y, tw, th, col))
    elif theme in ("wallpaper", "feature"):
        parts.append('<rect x="90" y="90" width="620" height="420" fill="%s"/>' % light)
        # repeating motif
        for r in range(4):
            for c in range(6):
                cx = 150 + c * 100
                cy = 150 + r * 95
                col = accent if (r + c) % 2 == 0 else dark
                parts.append('<circle cx="%d" cy="%d" r="26" fill="%s" opacity="0.85"/>' % (cx, cy, col))
        parts.append('<rect x="90" y="90" width="620" height="420" fill="none" stroke="%s" stroke-width="10"/>' % dark)
    elif theme == "mural":
        parts.append('<rect x="90" y="90" width="620" height="420" fill="%s"/>' % light)
        parts.append('<circle cx="250" cy="230" r="70" fill="%s"/>' % accent)
        parts.append('<polygon points="430,320 540,150 650,320" fill="%s"/>' % dark)
        parts.append('<path d="M120 470 Q300 380 380 460 T700 440" stroke="%s" stroke-width="18" fill="none" stroke-linecap="round"/>' % accent)
        for i, cx in enumerate((180, 560, 620)):
            parts.append('<circle cx="%d" cy="%d" r="18" fill="%s"/>' % (cx, 160 + i * 30, dark))
    else:
        # interior room: two-tone wall, skirting, window
        parts.append('<rect x="0" y="0" width="%d" height="420" fill="%s"/>' % (W, light))
        parts.append('<rect x="0" y="300" width="%d" height="120" fill="%s"/>' % (W, accent))
        parts.append('<rect x="0" y="420" width="%d" height="30" fill="%s"/>' % (W, bg))  # skirting
        parts.append('<rect x="0" y="450" width="%d" height="150" fill="%s"/>' % (W, dark))  # floor
        # window
        parts.append('<rect x="470" y="120" width="220" height="170" fill="%s" stroke="%s" stroke-width="10"/>' % (bg, dark))
        parts.append('<line x1="580" y1="120" x2="580" y2="290" stroke="%s" stroke-width="8"/>' % dark)
        parts.append('<line x1="470" y1="205" x2="690" y2="205" stroke="%s" stroke-width="8"/>' % dark)
        # roller motif
        parts.append('<rect x="120" y="180" width="70" height="26" rx="6" fill="%s"/>' % dark)
        parts.append('<rect x="150" y="206" width="10" height="90" fill="%s"/>' % dark)

    # subtle paint swatch strip bottom-left for brand feel
    sw = ["#F4A62A", "#2563EB", "#25D366", dark]
    for i, c in enumerate(sw):
        parts.append('<rect x="%d" y="548" width="34" height="34" rx="5" fill="%s" opacity="0.9"/>' % (30 + i * 40, c))
    parts.append("</svg>")
    return "".join(parts)


def logo_mark():
    """Brand mark: paint roller in a rounded navy square."""
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48">'
        '<rect width="48" height="48" rx="11" fill="#102741"/>'
        '<path fill="#F4A62A" d="M32 14v-1.5c0-.8-.7-1.5-1.5-1.5h-14c-.8 0-1.5.7-1.5 1.5v6c0 .8.7 1.5 1.5 1.5h14c.8 0 1.5-.7 1.5-1.5V18h1.5v5H21v14c0 .8.7 1.5 1.5 1.5h2c.8 0 1.5-.7 1.5-1.5V26h11V14h-5.5z"/>'
        "</svg>"
    )


def favicon_svg():
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">'
        '<rect width="48" height="48" rx="10" fill="#102741"/>'
        '<path fill="#F4A62A" d="M32 14v-1.5c0-.8-.7-1.5-1.5-1.5h-14c-.8 0-1.5.7-1.5 1.5v6c0 .8.7 1.5 1.5 1.5h14c.8 0 1.5-.7 1.5-1.5V18h1.5v5H21v14c0 .8.7 1.5 1.5 1.5h2c.8 0 1.5-.7 1.5-1.5V26h11V14h-5.5z"/>'
        "</svg>"
    )
