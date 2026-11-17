import math

def _axes(W, H, ox, oy, tx, ty, tmax, smax, tstep, sstep, tlab, slab, grid=True):
    """returns (svg_str, X(t), Y(s))"""
    X = lambda t: ox + t / tmax * tx
    Y = lambda s: oy - s / smax * ty
    g = ''
    n = round(tmax / tstep)
    for i in range(n + 1):
        t = i * tstep
        if grid: g += f'<line x1="{X(t):.1f}" y1="{Y(smax):.1f}" x2="{X(t):.1f}" y2="{oy}" stroke="#e2e8f0"/>'
        g += f'<text x="{X(t):.1f}" y="{oy+14}" font-size="10" text-anchor="middle" fill="#334155">{("%g" % t).replace(".", ",")}</text>'
    m = round(smax / sstep)
    for j in range(m + 1):
        s = j * sstep
        if grid: g += f'<line x1="{ox}" y1="{Y(s):.1f}" x2="{X(tmax):.1f}" y2="{Y(s):.1f}" stroke="#e2e8f0"/>'
        g += f'<text x="{ox-5}" y="{Y(s)+3.5:.1f}" font-size="10" text-anchor="end" fill="#334155">{("%g" % s).replace(".", ",")}</text>'
    g += (f'<line x1="{ox}" y1="{oy}" x2="{X(tmax)+14}" y2="{oy}" stroke="#1e293b" stroke-width="1.5"/><polygon points="{X(tmax)+18},{oy} {X(tmax)+10},{oy-4} {X(tmax)+10},{oy+4}" fill="#1e293b"/>'
          f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{Y(smax)-14}" stroke="#1e293b" stroke-width="1.5"/><polygon points="{ox},{Y(smax)-18} {ox-4},{Y(smax)-10} {ox+4},{Y(smax)-10}" fill="#1e293b"/>'
          f'<text x="{X(tmax)+14}" y="{oy+16}" font-size="11" font-weight="700" text-anchor="end">{tlab}</text>'
          f'<text x="{ox+6}" y="{Y(smax)-8}" font-size="11" font-weight="700">{slab}</text>')
    return g, X, Y

def st_graph():
    g, X, Y = _axes(340, 220, 40, 190, 260, 160, 3, 120, 0.5, 20, 't (h)', 's (km)')
    A = [(0, 0), (3, 120)]
    B = [(0, 0), (1, 60), (1.5, 60), (2.5, 120)]
    pa = ' '.join(f'{X(t):.1f},{Y(s):.1f}' for t, s in A)
    pb = ' '.join(f'{X(t):.1f},{Y(s):.1f}' for t, s in B)
    g += f'<polyline points="{pa}" fill="none" stroke="#2563eb" stroke-width="2.6"/><polyline points="{pb}" fill="none" stroke="#e11d48" stroke-width="2.6"/>'
    g += f'<text x="{X(2.75):.1f}" y="{Y(98):.1f}" font-size="12" font-weight="800" fill="#2563eb">Xe A</text><text x="{X(2.05):.1f}" y="{Y(112):.1f}" font-size="12" font-weight="800" fill="#e11d48">Xe B</text>'
    return f'<svg viewBox="0 0 340 215" width="330" height="208" font-family="Inter">{g}</svg>'

def blank_graph():
    g, X, Y = _axes(340, 220, 40, 190, 260, 160, 2, 24, 0.5, 4, 't (h)', 's (km)')
    return f'<svg viewBox="0 0 340 215" width="300" height="190" font-family="Inter">{g}</svg>'

def waves_svg():
    def wave(x0, amp, cycles, color):
        pts = ' '.join(f'{x0 + i:.1f},{55 - amp * math.sin(2 * math.pi * cycles * i / 200):.1f}' for i in range(0, 201, 2))
        return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2.2"/>'
    out = ''
    for x0, amp, cyc, lab, col in [(20, 38, 2, 'Âm A', '#e11d48'), (290, 16, 5, 'Âm B', '#2563eb')]:
        out += f'<rect x="{x0-10}" y="8" width="220" height="94" rx="8" fill="#0f172a"/>'
        out += ''.join(f'<line x1="{x0-10}" y1="{y}" x2="{x0+210}" y2="{y}" stroke="#1e3a5f"/>' for y in (17, 36, 55, 74, 93))
        out += wave(x0, amp, cyc, '#4ade80') + f'<text x="{x0+100}" y="118" font-size="12" font-weight="800" text-anchor="middle" fill="{col}">{lab}</text>'
    return f'<svg viewBox="0 0 520 124" width="440" height="106" font-family="Inter">{out}</svg><div class="cap">Đồ thị dao động của hai âm trên màn hình dao động kí (cùng một khoảng thời gian)</div>'

def mirror_svg(angle_with_mirror=30):
    # mirror horizontal at y=110, point I at (170,110)
    ix, iy = 170, 110
    a = math.radians(angle_with_mirror)
    L = 120
    sx, sy = ix - L * math.cos(a), iy - L * math.sin(a)
    hatch = ''.join(f'<line x1="{x}" y1="{iy}" x2="{x-8}" y2="{iy+9}" stroke="#64748b"/>' for x in range(40, 310, 12))
    mx, my = (sx + ix) / 2, (sy + iy) / 2
    arc = f'<path d="M {ix-40},{iy} A 40 40 0 0 1 {ix-40*math.cos(a):.1f},{iy-40*math.sin(a):.1f}" fill="none" stroke="#f59e0b" stroke-width="1.6"/>'
    return f'''<svg viewBox="0 0 330 135" width="250" height="102" font-family="Inter">
<line x1="30" y1="{iy}" x2="310" y2="{iy}" stroke="#1e293b" stroke-width="3"/>{hatch}
<line x1="{ix}" y1="{iy}" x2="{ix}" y2="10" stroke="#64748b" stroke-dasharray="5 4"/><text x="{ix+5}" y="20" font-size="11" fill="#64748b">N</text>
<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{ix}" y2="{iy}" stroke="#e11d48" stroke-width="2.6"/>
<polygon points="{mx:.1f},{my:.1f} {mx-12:.1f},{my-2:.1f} {mx-7:.1f},{my-9:.1f}" fill="#e11d48" transform="rotate({angle_with_mirror-35} {mx:.1f} {my:.1f})"/>
<text x="{sx-14:.1f}" y="{sy+4:.1f}" font-size="12" font-weight="700" fill="#e11d48">S</text><text x="{ix-4}" y="{iy+24}" font-size="12" font-weight="700">I</text>
{arc}<text x="{ix-70}" y="{iy-8}" font-size="12" font-weight="700" fill="#b45309">{angle_with_mirror}°</text>
<text x="290" y="{iy-6}" font-size="10" fill="#334155" text-anchor="end">gương phẳng</text></svg>'''

def magnet_svg():
    cx, cy = 280, 85
    lines = ''
    for k in (28, 48, 70):
        lines += f'<path d="M {cx-70},{cy-6} C {cx-70-k*0.8},{cy-30-k*1.3} {cx+70+k*0.8},{cy-30-k*1.3} {cx+70},{cy-6}" fill="none" stroke="#64748b" stroke-width="1.4"/>'
        lines += f'<path d="M {cx-70},{cy+6} C {cx-70-k*0.8},{cy+30+k*1.3} {cx+70+k*0.8},{cy+30+k*1.3} {cx+70},{cy+6}" fill="none" stroke="#64748b" stroke-width="1.4"/>'
    arrows = ''
    for k in (28, 48, 70):
        ytop = cy - 6 - 0.75 * (24 + k * 1.3)
        ybot = cy + 6 + 0.75 * (24 + k * 1.3)
        arrows += f'<polygon points="{cx+6},{ytop:.1f} {cx-4},{ytop-5:.1f} {cx-4},{ytop+5:.1f}" fill="#334155"/>'
        arrows += f'<polygon points="{cx+6},{ybot:.1f} {cx-4},{ybot-5:.1f} {cx-4},{ybot+5:.1f}" fill="#334155"/>'
    side = (f'<line x1="{cx-70}" y1="{cy}" x2="{cx-170}" y2="{cy}" stroke="#64748b" stroke-width="1.4"/><polygon points="{cx-140},{cy} {cx-130},{cy-5} {cx-130},{cy+5}" fill="#334155"/>'
            f'<line x1="{cx+70}" y1="{cy}" x2="{cx+170}" y2="{cy}" stroke="#64748b" stroke-width="1.4"/><polygon points="{cx+120},{cy} {cx+130},{cy-5} {cx+130},{cy+5}" fill="#334155"/>')
    mag = (f'<rect x="{cx-70}" y="{cy-14}" width="70" height="28" fill="#dc2626"/><rect x="{cx}" y="{cy-14}" width="70" height="28" fill="#2563eb"/>'
           f'<text x="{cx-35}" y="{cy+6}" font-size="16" font-weight="800" fill="#fff" text-anchor="middle">N</text><text x="{cx+35}" y="{cy+6}" font-size="16" font-weight="800" fill="#fff" text-anchor="middle">S</text>')
    return f'<svg viewBox="0 0 560 170" width="440" height="134" font-family="Inter">{lines}{arrows}{side}{mag}</svg><div class="cap">Đường sức từ của nam châm thẳng: bên ngoài nam châm, đi ra từ cực Bắc (N), đi vào cực Nam (S)</div>'

def speed_sign(n=50):
    return f'<svg viewBox="0 0 60 60" width="40" height="40"><circle cx="30" cy="30" r="27" fill="#fff" stroke="#dc2626" stroke-width="7"/><text x="30" y="38" font-size="22" font-weight="800" text-anchor="middle" font-family="Inter">{n}</text></svg>'
