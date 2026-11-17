def lever_svg():
    O, O1, O2, y = 170, 70, 470, 60   # 200 px per metre: d1 = 0,5 m, d2 = 1,5 m
    return f'''<svg viewBox="0 0 560 150" width="400" height="108" font-family="Inter">
<rect x="40" y="{y-6}" width="460" height="12" rx="3" fill="#a16207"/>
<polygon points="{O},{y+6} {O-18},{y+40} {O+18},{y+40}" fill="#64748b"/><line x1="{O-40}" y1="{y+40}" x2="{O+40}" y2="{y+40}" stroke="#334155" stroke-width="3"/>
<text x="{O-4}" y="{y+56}" font-size="13" font-weight="800">O</text>
<rect x="{O1-26}" y="{y+6}" width="52" height="40" fill="#94a3b8" stroke="#334155"/><text x="{O1}" y="{y+31}" font-size="12" font-weight="800" text-anchor="middle" fill="#fff">600 N</text>
<text x="{O1-8}" y="{y-12}" font-size="12" font-weight="700">O₁</text>
<line x1="{O2}" y1="{y-50}" x2="{O2}" y2="{y-10}" stroke="#e11d48" stroke-width="3"/><polygon points="{O2},{y-6} {O2-6},{y-18} {O2+6},{y-18}" fill="#e11d48"/>
<text x="{O2+8}" y="{y-34}" font-size="13" font-weight="800" fill="#e11d48">F₂ = ?</text><text x="{O2-8}" y="{y+24}" font-size="12" font-weight="700">O₂</text>
<line x1="{O1}" y1="{y+70}" x2="{O}" y2="{y+70}" stroke="#2563eb" stroke-width="1.5"/><text x="{(O1+O)//2}" y="{y+86}" font-size="11" text-anchor="middle" fill="#2563eb">d₁ = 0,5 m</text>
<line x1="{O}" y1="{y+70}" x2="{O2}" y2="{y+70}" stroke="#15803d" stroke-width="1.5"/><text x="{(O+O2)//2}" y="{y+86}" font-size="11" text-anchor="middle" fill="#15803d">d₂ = 1,5 m</text>
<line x1="{O1}" y1="{y+64}" x2="{O1}" y2="{y+76}" stroke="#334155"/><line x1="{O}" y1="{y+64}" x2="{O}" y2="{y+76}" stroke="#334155"/><line x1="{O2}" y1="{y+64}" x2="{O2}" y2="{y+76}" stroke="#334155"/>
</svg>'''

def _batt(x, y):  # horizontal battery centred at x on a horizontal wire at y; long plate (+) on the left
    return (f'<rect x="{x-12}" y="{y-16}" width="24" height="32" fill="#fff"/>'
            f'<line x1="{x-6}" y1="{y-16}" x2="{x-6}" y2="{y+16}" stroke="#1e293b" stroke-width="2"/>'
            f'<line x1="{x+6}" y1="{y-8}" x2="{x+6}" y2="{y+8}" stroke="#1e293b" stroke-width="5"/>'
            f'<text x="{x-16}" y="{y-18}" font-size="12" font-weight="800" fill="#dc2626">+</text><text x="{x+10}" y="{y-14}" font-size="13" font-weight="800">−</text>')

def _lamp(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="13" fill="#fff" stroke="#1e293b" stroke-width="2"/>'
            f'<line x1="{x-9}" y1="{y-9}" x2="{x+9}" y2="{y+9}" stroke="#1e293b" stroke-width="2"/><line x1="{x-9}" y1="{y+9}" x2="{x+9}" y2="{y-9}" stroke="#1e293b" stroke-width="2"/>')

def _meter(x, y, t):
    return f'<circle cx="{x}" cy="{y}" r="13" fill="#fff" stroke="#1e293b" stroke-width="2"/><text x="{x}" y="{y+5}" font-size="14" font-weight="800" text-anchor="middle">{t}</text>'

def _switch_v(x, y, closed=True):  # vertical switch on a vertical wire at x, centred at y
    if closed:
        return (f'<rect x="{x-6}" y="{y-16}" width="12" height="32" fill="#fff"/><circle cx="{x}" cy="{y-14}" r="3" fill="#1e293b"/><circle cx="{x}" cy="{y+14}" r="3" fill="#1e293b"/>'
                f'<line x1="{x}" y1="{y+14}" x2="{x}" y2="{y-14}" stroke="#1e293b" stroke-width="2"/>')
    return (f'<rect x="{x-6}" y="{y-16}" width="22" height="32" fill="#fff"/><circle cx="{x}" cy="{y-14}" r="3" fill="#1e293b"/><circle cx="{x}" cy="{y+14}" r="3" fill="#1e293b"/>'
            f'<line x1="{x}" y1="{y+14}" x2="{x+14}" y2="{y-10}" stroke="#1e293b" stroke-width="2"/>')

def _arrow(x, y, d):
    pts = {'down': f'{x},{y+6} {x-5},{y-4} {x+5},{y-4}', 'up': f'{x},{y-6} {x-5},{y+4} {x+5},{y+4}',
           'right': f'{x+6},{y} {x-4},{y-5} {x-4},{y+5}', 'left': f'{x-6},{y} {x+4},{y-5} {x+4},{y+5}'}[d]
    return f'<polygon points="{pts}" fill="#e11d48"/>'

def symbols_svg():
    items = []
    y = 34
    def lbl(x, t): return f'<text x="{x}" y="{y+40}" font-size="10" text-anchor="middle" fill="#334155">{t}</text>'
    g = ''
    xs = [40, 115, 190, 265, 340, 415, 490]
    # wire stubs
    for x in xs:
        g += f'<line x1="{x-28}" y1="{y}" x2="{x+28}" y2="{y}" stroke="#1e293b" stroke-width="2"/>'
    g += _batt(xs[0], y) + lbl(xs[0], 'Nguồn (pin)')
    g += (f'<rect x="{xs[1]-14}" y="{y-10}" width="28" height="12" fill="#fff"/><circle cx="{xs[1]-12}" cy="{y}" r="3"/><circle cx="{xs[1]+12}" cy="{y}" r="3"/>'
          f'<line x1="{xs[1]-12}" y1="{y}" x2="{xs[1]+12}" y2="{y}" stroke="#1e293b" stroke-width="2"/>') + lbl(xs[1], 'Công tắc đóng')
    g += (f'<rect x="{xs[2]-14}" y="{y-16}" width="28" height="14" fill="#fff"/><rect x="{xs[2]-14}" y="{y-2}" width="28" height="4" fill="#fff"/><circle cx="{xs[2]-12}" cy="{y}" r="3"/><circle cx="{xs[2]+12}" cy="{y}" r="3"/>'
          f'<line x1="{xs[2]-12}" y1="{y}" x2="{xs[2]+10}" y2="{y-13}" stroke="#1e293b" stroke-width="2"/>') + lbl(xs[2], 'Công tắc mở')
    g += _lamp(xs[3], y) + lbl(xs[3], 'Bóng đèn')
    g += _meter(xs[4], y, 'A') + lbl(xs[4], 'Ampe kế')
    g += _meter(xs[5], y, 'V') + lbl(xs[5], 'Vôn kế')
    g += f'<rect x="{xs[6]-16}" y="{y-7}" width="32" height="14" fill="#fff" stroke="#1e293b" stroke-width="2"/><line x1="{xs[6]-16}" y1="{y}" x2="{xs[6]+16}" y2="{y}" stroke="#1e293b" stroke-width="1.5"/>' + lbl(xs[6], 'Cầu chì')
    return f'<svg viewBox="0 0 530 84" width="100%" height="84" font-family="Inter">{g}</svg>'

def circuit_svg():
    L, R, T, B = 60, 260, 30, 150
    g = f'<rect x="{L}" y="{T}" width="{R-L}" height="{B-T}" fill="none" stroke="#1e293b" stroke-width="2"/>'
    g += _batt((L + R) // 2, T) + _lamp((L + R) // 2, B) + _switch_v(R, (T + B) // 2, True)
    g += _arrow(L, (T + B) // 2, 'down') + _arrow((L + R) // 2 - 45, B, 'right') + _arrow(R, (T + B) // 2 + 34, 'up') + _arrow((L + R) // 2 - 45, T, 'left')
    g += f'<text x="{R+12}" y="{(T+B)//2+4}" font-size="11">K</text><text x="{(L+R)//2-6}" y="{B+30}" font-size="11">Đ</text>'
    return f'<svg viewBox="0 0 320 190" width="230" height="136" font-family="Inter">{g}</svg>'

def meters_svg():
    L, R, T, B = 50, 330, 30, 130
    g = f'<rect x="{L}" y="{T}" width="{R-L}" height="{B-T}" fill="none" stroke="#1e293b" stroke-width="2"/>'
    lx = 240
    g += _batt((L + R) // 2, T) + _switch_v(L, (T + B) // 2, True) + _meter(130, B, 'A') + _lamp(lx, B)
    # voltmeter branch across the lamp
    g += (f'<line x1="{lx-40}" y1="{B}" x2="{lx-40}" y2="{B+44}" stroke="#1e293b" stroke-width="2"/><line x1="{lx+40}" y1="{B}" x2="{lx+40}" y2="{B+44}" stroke="#1e293b" stroke-width="2"/>'
          f'<line x1="{lx-40}" y1="{B+44}" x2="{lx+40}" y2="{B+44}" stroke="#1e293b" stroke-width="2"/>' + _meter(lx, B + 44, 'V')
          + f'<circle cx="{lx-40}" cy="{B}" r="3" fill="#1e293b"/><circle cx="{lx+40}" cy="{B}" r="3" fill="#1e293b"/>')
    g += f'<text x="{L-16}" y="{(T+B)//2+4}" font-size="11">K</text><text x="{lx+16}" y="{B-16}" font-size="11">Đ</text>'
    g += f'<text x="{112}" y="{B-18}" font-size="10" fill="#dc2626">+</text><text x="{142}" y="{B-18}" font-size="11">−</text>'
    g += f'<text x="{lx-30}" y="{B+38}" font-size="10" fill="#dc2626">+</text><text x="{lx+24}" y="{B+38}" font-size="11">−</text>'
    return f'<svg viewBox="0 0 380 190" width="260" height="130" font-family="Inter">{g}</svg>'
