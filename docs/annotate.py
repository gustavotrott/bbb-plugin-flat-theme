# Draws the numbered callouts on docs/after.jpg.
# Usage: python3 docs/annotate.py docs/after.jpg out.svg && rsvg-convert out.svg -o out.png

import base64, sys
src, out = sys.argv[1], sys.argv[2]
W, H = 1512, 792
LEG = 132
img = base64.b64encode(open(src, 'rb').read()).decode()
# (number, badge x, badge y, target x or None, target y)
marks = [
    (1, 31, 565, None, None),
    (2, 182, 211, 111, 221),
    (3, 170, 470, 68, 470),
    (4, 1242, 140, 1207, 140),
    (5, 790, 763, 828, 763),
    (6, 1205, 64, 1238, 40),
]
labels = [
    "Full-height icon bar, narrower, clearer icons",
    "Moderators: round avatar with a gold crown",
    "Side panel flush with the bar, less padding",
    "Cameras fill the tile, readable name tags",
    "Red when mic or camera is off, 40px controls",
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
cols, colw, x0, y0, rowh = 3, 470, 48, H + 44, 50
for i, t in enumerate(labels):
    cx = x0 + (i % cols) * colw
    cy = y0 + (i // cols) * rowh
    s.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="{ACC}"/>')
    s.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="14" font-weight="700" fill="#fff">{i+1}</text>')
    s.append(f'<text x="{cx+24}" y="{cy+6}" font-family="Helvetica Neue, Helvetica, Arial, sans-serif" font-size="17" fill="#1f2329">{t}</text>')
s.append('</svg>')
open(out, 'w').write('\n'.join(s))
