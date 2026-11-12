#!/usr/bin/env python3
"""Render the README preview cards (previews/*.svg) for each case study.

Stdlib only. Fonts are subset WOFF2 files (SIL Open Font License) in fonts/,
embedded as base64 so the cards look the same everywhere GitHub shows them.
Run:  python3 scripts/render_previews.py        (set STATIC=1 to drop the animation)
"""
import base64
import html
import json
import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "previews"
STATIC = os.environ.get("STATIC") == "1"

PAPER, INK, INK2, GREY, RULE = "#f3f3f1", "#111111", "#3a3a3c", "#6e6e73", "#dcdcd7"
BLUE, RED, YELLOW = "#2f55ff", "#ef3b2d", "#ffc81a"
FACES = {
    "serif-400": ("Instrument Serif", "normal", 400),
    "serif-italic": ("Instrument Serif", "italic", 400),
    "geist-400": ("Geist", "normal", 400),
    "geist-600": ("Geist", "normal", 600),
    "geistmono-400": ("Geist Mono", "normal", 400),
}
METRICS = json.loads((ROOT / "fonts" / "metrics.json").read_text())
CSS = (
    ".sr{font-family:'Instrument Serif',Georgia,serif}.it{font-style:italic}"
    ".ss{font-family:Geist,system-ui,-apple-system,sans-serif}.b6{font-weight:600}"
    ".mo{font-family:'Geist Mono',ui-monospace,Menlo,monospace}"
)
KEYFRAMES = (
    "@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}"
    "@keyframes nudge{0%,100%{transform:translateX(0)}50%{transform:translateX(4px)}}"
    "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
)

W, H = 440, 300

# slug, eyebrow, title, [(number, label)], footer, accent
CARDS = [
    ("price-catalogue-electronics-retail", "REQUIREMENTS → RELEASE",
     "From one client meeting to a 3,104-product price catalogue",
     [("15", "requirements traced"), ("22", "live UAT checks"), ("4", "releases in 5 days")],
     "Electronics retail · 2026", BLUE),
    ("advance-washing-zero-to-one", "ZERO TO ONE",
     "A laundry service, from idea to both app stores",
     [("2", "app stores live"), ("80%", "customers via WhatsApp"), ("144", "sign-ups in a month")],
     "The Business Wings · 2025–now", RED),
    ("enorbit-whatsapp-platform", "PLATFORM OPERATIONS",
     "Running a multi-tenant WhatsApp automation platform",
     [("~13", "client businesses"), ("8", "safeguards shipped"), ("2,840", "contacts relaunched")],
     "EnOrbit · 2026–now", YELLOW),
    ("agency-portfolio-20-websites", "PORTFOLIO DELIVERY",
     "About 20 client websites in one year, for a digital agency",
     [("~20", "sites and pages"), ("7", "pages, one client"), ("1", "shared tracker")],
     "Digital agency · 2026", BLUE),
    ("alankara-ai-virtual-try-on", "TEAM LEADERSHIP",
     "Leading a team of 4–5 to ship a virtual jewellery try-on",
     [("4–5", "people led"), ("3", "surfaces: web, tablet, kiosk"), ("1", "product, end to end")],
     "AISMARTLIVE · 2022–2025", RED),
    ("one-client-two-platforms", "CLIENT RELATIONSHIP",
     "One client, two platforms: training and laundry operations",
     [("2", "platforms delivered"), ("3", "role dashboards"), ("1", "WhatsApp ordering flow")],
     "Hyderabad · 2025–2026", YELLOW),
    ("jewellery-retailer-sketch-to-whatsapp-flow", "REQUIREMENTS FROM A SKETCH",
     "From a hand-drawn sketch to a live WhatsApp flow",
     [("1", "sketch as the brief"), ("2", "systems delivered"), ("1", "rollback path ready")],
     "Jewellery retail · 2026", BLUE),
    ("support-crm-retired", "LESSONS LEARNED",
     "A CRM 15 people used every day, and why it was switched off",
     [("~15", "daily users"), ("6", "modules"), ("1", "pivot that retired it")],
     "The Business Wings · 2025", RED),
]


def esc(s):
    return html.escape(s, quote=True)


def width(text, face, size):
    m = METRICS[face]
    return sum(m.get(c, 0.55) for c in text) * size


def wrap(text, face, size, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if cur and width(trial, face, size) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + ([cur] if cur else [])


def anim(name, dur, delay, loop=False):
    if STATIC:
        return ""
    rep = "infinite" if loop else "both"
    return f' style="animation:{name} {dur}s cubic-bezier(.2,.8,.2,1) {delay:.2f}s {rep}"'


def svg(w, h, title, body, faces):
    css = []
    for key in faces:
        family, style, weight = FACES[key]
        b64 = base64.b64encode((ROOT / "fonts" / f"{key}.woff2").read_bytes()).decode()
        css.append(f"@font-face{{font-family:'{family}';font-style:{style};font-weight:{weight};"
                   f"src:url(data:font/woff2;base64,{b64}) format('woff2')}}")
    style = "".join(css) + CSS + ("" if STATIC else KEYFRAMES)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-labelledby="t"><title id="t">{esc(title)}</title><style>{style}</style>{body}</svg>\n')


def card(i, eyebrow, title, stats, footer, accent):
    pad, d = 28, 0.12 * (i % 2)
    body = [f'<rect x="4" y="4" width="{W - 8}" height="{H - 8}" rx="16" fill="{PAPER}"/>',
            f'<g{anim("rise", 0.7, d)}>',
            f'<rect x="{pad}" y="32" width="9" height="9" rx="2" fill="{accent}"/>',
            f'<text class="mo" x="{pad + 17}" y="41" font-size="11" letter-spacing="1" fill="{GREY}">{esc(eyebrow)}</text>']
    lines = wrap(title, "serif-400", 29, W - 2 * pad)[:3]
    for k, t in enumerate(lines):
        body.append(f'<text class="sr" x="{pad}" y="{84 + k * 31}" font-size="29" fill="{INK}">{esc(t)}</text>')
    top = 84 + len(lines) * 31 + 6
    if accent == YELLOW:
        body.append(f'<rect x="{pad}" y="{top - 1.5}" width="{W - 2 * pad}" height="3" rx="1.5" fill="{YELLOW}"/>')
    else:
        body.append(f'<line x1="{pad}" y1="{top}" x2="{W - pad}" y2="{top}" stroke="{RULE}"/>')
    col = (W - 2 * pad) / 3
    for k, (num, label) in enumerate(stats):
        x = pad + k * col
        body.append(f'<text class="sr" x="{x}" y="{top + 40}" font-size="34" fill="{accent if accent != YELLOW else INK}">{esc(num)}</text>')
        for j, t in enumerate(wrap(label, "geist-400", 11.5, col - 12)[:2]):
            body.append(f'<text class="ss" x="{x}" y="{top + 60 + j * 15}" font-size="11.5" fill="{INK2}">{esc(t)}</text>')
    body.append(f'<text class="mo" x="{pad}" y="{H - 30}" font-size="11" fill="{GREY}">{esc(footer)}</text>')
    body.append(f'<g{anim("nudge", 1.6, 1.2, loop=True)}><text class="ss b6" x="{W - pad}" y="{H - 30}" '
                f'font-size="12.5" text-anchor="end" fill="{INK}">Read the case study →</text></g>')
    body.append("</g>")
    return svg(W, H, f"{title}. {' · '.join(n + ' ' + l for n, l in stats)}", "".join(body),
               ["serif-400", "geist-400", "geist-600", "geistmono-400"])


def header(n_cases, n_templates):
    w, h, pad = 880, 210, 36
    body = [f'<rect x="4" y="4" width="{w - 8}" height="{h - 8}" rx="16" fill="{PAPER}"/>',
            f'<g{anim("rise", 0.7, 0)}>',
            f'<text class="mo" x="{pad}" y="50" font-size="12" letter-spacing="1.2" fill="{GREY}">KRISHNA CHAITANYA DOPPA · TECHNICAL PROJECT MANAGER</text>',
            f'<text class="sr" x="{pad}" y="112" font-size="56" fill="{INK}">Case studies</text>',
            f'<text class="sr it" x="{pad + width("Case studies ", "serif-400", 56)}" y="112" font-size="56" fill="{BLUE}">and templates</text>',
            f'<text class="ss" x="{pad}" y="150" font-size="15" fill="{INK2}">How I take a requirement from a founder or CEO to a tested, live release.</text>',
            f'<text class="ss" x="{pad}" y="172" font-size="15" fill="{INK2}">Real projects, written up. No client code.</text>']
    for k, (num, label, color) in enumerate([(str(n_cases), "case studies", BLUE),
                                             (str(n_templates), "templates", RED),
                                             ("30+", "projects since 2021", INK)]):
        y = 70 + k * 48
        body.append(f'<text class="sr" x="{w - pad - 150}" y="{y + 18}" font-size="34" text-anchor="end" fill="{color}">{num}</text>')
        body.append(f'<text class="ss" x="{w - pad - 140}" y="{y + 12}" font-size="13" fill="{INK2}">{label}</text>')
    body.append("</g>")
    return svg(w, h, f"Case studies and templates: {n_cases} case studies, {n_templates} templates",
               "".join(body), ["serif-400", "serif-italic", "geist-400", "geistmono-400"])


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / "header.svg").write_text(header(len(CARDS), 4))
    for i, (slug, *args) in enumerate(CARDS):
        (OUT / f"{slug}.svg").write_text(card(i, *args))
    print(f"wrote {len(CARDS) + 1} cards to {OUT}")


if __name__ == "__main__":
    main()
