# Draws the numbered callouts on docs/after.jpg.
# Usage: python3 docs/annotate.py docs/after.jpg out.svg && rsvg-convert out.svg -o out.png

import base64, sys
src, out = sys.argv[1], sys.argv[2]
W, H = 1512, 790
LEG = 182
img = base64.b64encode(open(src, 'rb').read()).decode()
# (number, badge x, badge y, target x or None, target y)
marks = [
    (1, 36, 610, None, None),
    (2, 560, 246, 452, 272),
    (3, 394, 560, None, None),
    (4, 232, 645, 232, 602),
    (5, 1390, 150, 1356, 150),
    (6, 545, 600, 545, 646),
    (7, 930, 758, 975, 758),
    (8, 1272, 758, 1218, 758),
    (9, 852, 624, 903, 624),
    (10, 1205, 72, 1238, 44),
]
labels = [
    "Full-height icon bar, names under icons",
    "Round avatars, crown, presenter badge",
    "Both side panels flush and full height",
    "Chat bubbles, yours in light blue",
    "Cameras fill the tile, ring on speaker",
    "One action per row, nothing cut",
    "Red when mic or camera is off",
    "Clear icons, you can tell what each does",
    "Media panel: wide tiles, labels fit",
    "Same corner radius on every button",
]
ACC = "#F25C3B"
s = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H+LEG}" viewBox="0 0 {W} {H+LEG}">',
     '<defs><filter id="sh" x="-50%" y="-50%" width="200%" height="200%"><feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#000" flood-opacity=".45"/></filter></defs>',
     f'<image x="0" y="0" width="{W}" height="{H}" xlink:href="data:image/jpeg;base64,{img}"/>']
for n, bx, by, tx, ty in marks:
    if tx is not None:
        s.append(f'<line x1="{bx}" y1="{by}" x2="{tx}" y2="{ty}" stroke="{ACC}" stroke-width="2.5" stroke-linecap="round"/>')
    s.append(f'<circle cx="{bx}" cy="{by}" r="14" fill="{ACC}" stroke="#fff" stroke-width="2.5" filter="url(#sh)"/>')
    s.append(f'<text x="{bx}" y="{by+5.5}" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="15" font-weight="700" fill="#fff">{n}</text>')
# legend
s.append(f'<rect x="0" y="{H}" width="{W}" height="{LEG}" fill="#F4F6FA"/>')
s.append(f'<rect x="0" y="{H}" width="{W}" height="1" fill="#E3E4E8"/>')
cols, colw, x0, y0, rowh = 4, 368, 40, H + 44, 50
for i, t in enumerate(labels):
    cx = x0 + (i % cols) * colw
    cy = y0 + (i // cols) * rowh
    s.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="{ACC}"/>')
    s.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="14" font-weight="700" fill="#fff">{i+1}</text>')
    s.append(f'<text x="{cx+24}" y="{cy+6}" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="16" fill="#1f2329">{t}</text>')
s.append('</svg>')
open(out, 'w').write('\n'.join(s))
