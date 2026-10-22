# Draws the numbered callouts on docs/after.jpg.
# Usage: python3 docs/annotate.py docs/after.jpg out.svg && rsvg-convert out.svg -o out.png

import base64, sys
src, out = sys.argv[1], sys.argv[2]
W, H = 1512, 790
LEG = 132
img = base64.b64encode(open(src, 'rb').read()).decode()
# (number, badge x, badge y, target x or None, target y)
marks = [
    (1, 36, 590, None, None),
    (2, 214, 260, 121, 269),
    (3, 170, 470, 74, 470),
    (4, 1242, 140, 1201, 140),
    (5, 790, 758, 822, 758),
    (6, 1112, 758, 1068, 758),
    (7, 1205, 64, 1238, 40),
]
labels = [
    "Full-height, narrower icon bar",
    "Moderators: round avatar, gold crown",
    "Panel flush with the bar, less padding",
    "Cameras fill the tile, clear name tags",
    "Red when mic or camera is off",
    "Larger, clearer icons, easy to read",
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
