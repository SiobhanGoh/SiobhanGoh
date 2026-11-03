"""Builds the three 'Projects at a glance' cards in assets/cards/.

Run: python scripts/make_project_cards.py
Every figure on a card comes from that project's own README or evaluation files.
The cards are portrait and use large type because GitHub shows them three across,
at roughly 270 px wide each.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets" / "cards"
W, H, X = 360, 492, 26
FONT = "Arial,'DejaVu Sans',sans-serif"

CARDS = [
    {
        "file": "retailai.svg",
        "tag": "RETAIL ANALYTICS",
        "title": ["RetailAI"],
        "pitch": ["Drop in a sales file and get", "trends, forecasts, customer", "segments and product pairings."],
        "big": "4", "big_label": "forecast models with error bands",
        "facts": ["3 sample stores, incl. RM grocer", "Rule-based parts labelled honestly", "Your file never leaves the tab"],
        "chips": ["TypeScript", "React", "Forecasting"],
        "accent": "#E8B067", "accent2": "#D88BA7", "motif": "bars",
    },
    {
        "file": "sentiment.svg",
        "tag": "MULTILINGUAL NLP",
        "title": ["Rojak Sentiment"],
        "pitch": ["Reads Malay, English and", "code-switched comments as", "negative, neutral or positive."],
        "big": "76.04%", "big_label": "test accuracy, corrected split",
        "facts": ["Fine-tuned multilingual BERT", "Runs privately in the browser", "YouTube comment dashboards"],
        "chips": ["PyTorch", "Transformers", "ONNX"],
        "accent": "#F1A7C4", "accent2": "#AE92BA", "motif": "bubbles",
    },
    {
        "file": "blood-dashboard.svg",
        "tag": "FORECASTING IN R",
        "title": ["Blood Donation", "Forecasts"],
        "pitch": ["Klang Valley donations by", "ABO group, refreshed every", "morning from official data."],
        "big": "Daily", "big_label": "automated refresh and tests",
        "facts": ["4 forecasting methods compared", "Matches the original report", "Blood 101 guide for donors"],
        "chips": ["R Shiny", "Shinylive", "Actions"],
        "accent": "#E2667E", "accent2": "#D88BA7", "motif": "drop",
    },
]


def motif(kind, a, b):
    """Drawn in a 70 x 70 box with its top-left corner at (0, 0)."""
    if kind == "bars":
        hs = [26, 38, 31, 50, 44, 62]
        parts = [f'<rect x="{i * 11}" y="{68 - h}" width="7" height="{h}" rx="2" fill="{a}" opacity="{0.45 + i * 0.09:.2f}"/>'
                 for i, h in enumerate(hs)]
        parts.append(f'<path d="M-2 36 L22 24 L42 30 L68 4" stroke="{b}" stroke-width="2.4" fill="none" stroke-dasharray="4 3"/>')
        return "".join(parts)
    if kind == "bubbles":
        return (
            f'<rect x="0" y="0" width="52" height="34" rx="12" fill="{a}" opacity=".85"/>'
            f'<path d="M12 34 l-6 10 l14 -10z" fill="{a}" opacity=".85"/>'
            f'<rect x="22" y="30" width="48" height="30" rx="11" fill="{b}" opacity=".7"/>'
            f'<path d="M58 60 l6 9 l-14 -9z" fill="{b}" opacity=".7"/>'
            '<circle cx="14" cy="17" r="3.2" fill="#1E2433"/><circle cx="26" cy="17" r="3.2" fill="#1E2433"/><circle cx="38" cy="17" r="3.2" fill="#1E2433"/>'
        )
    return (  # blood drop with a pulse line
        f'<path d="M35 0 C41 18 63 34 63 50 A28 28 0 0 1 7 50 C7 34 29 18 35 0Z" fill="{a}" opacity=".9"/>'
        '<path d="M19 54 L28 54 L32 44 L38 64 L43 52 L51 52" stroke="#F9F7FA" stroke-width="2.4" fill="none" stroke-linejoin="round"/>'
    )


def chip_row(chips, x, y, accent):
    parts, cx = [], x
    for c in chips:
        w = 22 + sum(9.6 if ch.isupper() else 7.9 for ch in c)
        parts.append(f'<rect x="{cx:.0f}" y="{y}" width="{w:.0f}" height="30" rx="15" fill="{accent}" fill-opacity=".14" stroke="{accent}" stroke-opacity=".6"/>')
        parts.append(f'<text x="{cx + w / 2:.0f}" y="{y + 20}" text-anchor="middle" class="chip">{escape(c)}</text>')
        cx += w + 8
    assert cx - 8 <= W - X, f"chips too wide: {chips}"
    return "".join(parts)


def card(c):
    a, b = c["accent"], c["accent2"]
    out, y = [], 0

    y = 92
    for t in c["title"]:
        out.append(f'<text x="{X}" y="{y}" class="title">{escape(t)}</text>')
        y += 34
    y += 4
    for t in c["pitch"]:
        out.append(f'<text x="{X}" y="{y}" class="pitch">{escape(t)}</text>')
        y += 23
    y += 4
    out.append(f'<line x1="{X}" y1="{y}" x2="{W - X}" y2="{y}" stroke="#F9F7FA" stroke-opacity=".12"/>')
    y += 52
    out.append(f'<text x="{X}" y="{y}" class="big">{escape(c["big"])}</text>')
    y += 24
    out.append(f'<text x="{X}" y="{y}" class="biglab">{escape(c["big_label"])}</text>')
    y += 34
    for t in c["facts"]:
        out.append(f'<circle cx="{X + 4}" cy="{y - 5}" r="3.5" fill="{a}"/><text x="{X + 16}" y="{y}" class="fact">{escape(t)}</text>')
        y += 25
    assert y <= H - 60, f"content too tall for {c['file']}: {y}"

    title = escape(" ".join(c["title"]))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{title}: {escape(' '.join(c['pitch']))}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#111622"/><stop offset="70%" stop-color="#1E2433"/><stop offset="100%" stop-color="#312536"/></linearGradient>
    <linearGradient id="acc" x1="0" y1="0" x2="1" y2="0"><stop stop-color="{a}"/><stop offset="100%" stop-color="{b}"/></linearGradient>
    <radialGradient id="halo"><stop stop-color="{a}" stop-opacity="0.22"/><stop offset="100%" stop-color="{a}" stop-opacity="0"/></radialGradient>
    <style>
      text{{font-family:{FONT}}}
      .tag{{font-size:13px;fill:{a};letter-spacing:2.4px;font-weight:700}}
      .title{{font-size:30px;font-weight:700;fill:#F9F7FA}}
      .pitch{{font-size:17px;fill:#D4D3DD}}
      .big{{font-size:50px;font-weight:700;fill:url(#acc)}}
      .biglab{{font-size:15px;fill:#C3C1CF}}
      .fact{{font-size:16px;fill:#E8E6EE}}
      .chip{{font-size:14px;fill:#F3F0F6}}
    </style>
  </defs>
  <rect width="{W}" height="{H}" rx="22" fill="url(#bg)"/>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="21.5" fill="none" stroke="{a}" stroke-opacity=".3"/>
  <circle cx="{W - 60}" cy="62" r="105" fill="url(#halo)"/>
  <g transform="translate({W - 26 - 62} 22) scale(.88)">{motif(c["motif"], a, b)}</g>
  <rect x="{X}" y="32" width="28" height="4" rx="2" fill="url(#acc)"/>
  <text x="{X}" y="58" class="tag">{escape(c["tag"])}</text>
  {"".join(out)}
  {chip_row(c["chips"], X, H - 26 - 30, a)}
</svg>
'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for c in CARDS:
        (OUT / c["file"]).write_text(card(c), encoding="utf-8")
        print("wrote", OUT / c["file"])


if __name__ == "__main__":
    main()
