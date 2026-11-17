from _axes_src import _axes

def lens_svg():
    ax = 95; sx = 6; sy = 20   # px per cm horizontally / vertically (affine scaling keeps rays straight)
    Ox = 300
    X = lambda cm: Ox + cm * sx
    Y = lambda cm: ax - cm * sy
    g = f'<line x1="40" y1="{ax}" x2="540" y2="{ax}" stroke="#334155" stroke-width="1.3"/>'
    g += f'<line x1="{Ox}" y1="{ax-70}" x2="{Ox}" y2="{ax+70}" stroke="#2563eb" stroke-width="3"/><polygon points="{Ox},{ax-76} {Ox-6},{ax-64} {Ox+6},{ax-64}" fill="#2563eb"/><polygon points="{Ox},{ax+76} {Ox-6},{ax+64} {Ox+6},{ax+64}" fill="#2563eb"/>'
    for cm, lab in [(-10, 'F'), (10, "F'")]:
        g += f'<circle cx="{X(cm)}" cy="{ax}" r="3" fill="#1e293b"/><text x="{X(cm)-4}" y="{ax+16}" font-size="12" font-weight="700">{lab}</text>'
    g += f'<text x="{Ox+5}" y="{ax+16}" font-size="12" font-weight="700">O</text>'
    # object AB (d = 30 cm, h = 2 cm) and image A'B' (d' = 15 cm, h' = 1 cm)
    g += f'<line x1="{X(-30)}" y1="{ax}" x2="{X(-30)}" y2="{Y(2)+6}" stroke="#16a34a" stroke-width="3"/><polygon points="{X(-30)},{Y(2)} {X(-30)-6},{Y(2)+10} {X(-30)+6},{Y(2)+10}" fill="#16a34a"/>'
    g += f'<text x="{X(-30)-6}" y="{ax+16}" font-size="12" font-weight="700">A</text><text x="{X(-30)-16}" y="{Y(2)+4}" font-size="12" font-weight="700">B</text>'
    g += f'<line x1="{X(15)}" y1="{ax}" x2="{X(15)}" y2="{Y(-1)-6}" stroke="#e11d48" stroke-width="3"/><polygon points="{X(15)},{Y(-1)} {X(15)-6},{Y(-1)-10} {X(15)+6},{Y(-1)-10}" fill="#e11d48"/>'
    g += f'<text x="{X(15)+5}" y="{ax-6}" font-size="12" font-weight="700">A\'</text><text x="{X(15)+6}" y="{Y(-1)+12}" font-size="12" font-weight="700">B\'</text>'
    # rays
    g += f'<polyline points="{X(-30)},{Y(2)} {Ox},{Y(2)} {X(15)},{Y(-1)}" fill="none" stroke="#f59e0b" stroke-width="1.8"/>'
    g += f'<line x1="{X(-30)}" y1="{Y(2)}" x2="{X(15)}" y2="{Y(-1)}" stroke="#f59e0b" stroke-width="1.8"/>'
    g += f'<text x="44" y="18" font-size="10" fill="#64748b">f = 10 cm; AB = 2 cm; OA = 30 cm (hình không theo tỉ lệ chiều cao)</text>'
    return f'<svg viewBox="0 0 560 175" width="440" height="138" font-family="Inter">{g}</svg>'

def prism_svg():
    g = '<polygon points="200,20 120,150 280,150" fill="#e0f2fe" stroke="#0369a1" stroke-width="2"/>'
    g += '<line x1="20" y1="70" x2="168" y2="75" stroke="#f8fafc" stroke-width="5"/><line x1="20" y1="70" x2="168" y2="75" stroke="#94a3b8" stroke-width="1"/>'
    g += '<text x="22" y="62" font-size="11" font-weight="700" fill="#334155">ánh sáng trắng</text>'
    cols = ['#dc2626', '#f97316', '#eab308', '#16a34a', '#0ea5e9', '#4338ca', '#7e22ce']
    for i, c in enumerate(cols):
        y1 = 82 + i * 2.2
        g += f'<line x1="168" y1="75" x2="228" y2="{y1:.1f}" stroke="{c}" stroke-width="1.6"/>'
        g += f'<line x1="228" y1="{y1:.1f}" x2="420" y2="{100 + i * 11}" stroke="{c}" stroke-width="2.4"/>'
    g += '<rect x="420" y="92" width="10" height="82" fill="#334155"/><text x="436" y="104" font-size="10" fill="#dc2626">đỏ</text><text x="436" y="172" font-size="10" fill="#7e22ce">tím</text>'
    g += '<text x="160" y="168" font-size="11" fill="#0369a1">đáy lăng kính</text>'
    return f'<svg viewBox="0 0 480 180" width="360" height="135" font-family="Inter"><rect width="480" height="180" rx="8" fill="#0f172a"/>{g}</svg>'

def fiber_svg():
    g = '<rect x="20" y="20" width="440" height="70" rx="35" fill="#cffafe" stroke="#0891b2" stroke-width="2"/><rect x="20" y="38" width="440" height="34" fill="#a5f3fc"/>'
    pts = '30,55 90,38 150,72 210,38 270,72 330,38 390,72 450,48'
    g += f'<polyline points="{pts}" fill="none" stroke="#e11d48" stroke-width="2.4"/>'
    g += '<text x="24" y="108" font-size="11" fill="#334155">Lõi (chiết suất lớn) – vỏ (chiết suất nhỏ hơn): ánh sáng phản xạ toàn phần liên tiếp và đi theo sợi quang</text>'
    return f'<svg viewBox="0 0 480 115" width="380" height="92" font-family="Inter">{g}</svg>'

def iu_graph():
    g, X, Y = _axes(340, 220, 44, 190, 250, 160, 6, 0.6, 1, 0.1, 'U (V)', 'I (A)')
    g += f'<line x1="{X(0)}" y1="{Y(0)}" x2="{X(6)}" y2="{Y(0.6)}" stroke="#2563eb" stroke-width="2.6"/><line x1="{X(0)}" y1="{Y(0)}" x2="{X(6)}" y2="{Y(0.3)}" stroke="#e11d48" stroke-width="2.6"/>'
    g += f'<text x="{X(4.6)}" y="{Y(0.52)}" font-size="12" font-weight="800" fill="#2563eb">R₁</text><text x="{X(5.2)}" y="{Y(0.22)}" font-size="12" font-weight="800" fill="#e11d48">R₂</text>'
    return f'<svg viewBox="0 0 340 215" width="260" height="164" font-family="Inter">{g}</svg>'

def _res(x, y, lab, vertical=False):
    if vertical:
        return f'<rect x="{x-8}" y="{y-20}" width="16" height="40" fill="#fff" stroke="#1e293b" stroke-width="2"/><text x="{x+12}" y="{y+4}" font-size="12" font-weight="700">{lab}</text>'
    return f'<rect x="{x-20}" y="{y-8}" width="40" height="16" fill="#fff" stroke="#1e293b" stroke-width="2"/><text x="{x-8}" y="{y-12}" font-size="12" font-weight="700">{lab}</text>'

def _batt(x, y):
    return (f'<rect x="{x-12}" y="{y-16}" width="24" height="32" fill="#fff"/><line x1="{x-6}" y1="{y-16}" x2="{x-6}" y2="{y+16}" stroke="#1e293b" stroke-width="2"/>'
            f'<line x1="{x+6}" y1="{y-8}" x2="{x+6}" y2="{y+8}" stroke="#1e293b" stroke-width="5"/>'
            f'<text x="{x-16}" y="{y-18}" font-size="12" font-weight="800" fill="#dc2626">+</text><text x="{x+10}" y="{y-14}" font-size="13" font-weight="800">−</text>')

def circuits_svg():
    # series
    g = '<rect x="20" y="30" width="200" height="100" fill="none" stroke="#1e293b" stroke-width="2"/>' + _batt(120, 30) + _res(80, 130, 'R₁') + _res(160, 130, 'R₂')
    g += '<text x="80" y="168" font-size="12" font-weight="800" fill="#4338ca">a) Mắc nối tiếp</text>'
    # parallel
    g += '<rect x="290" y="30" width="200" height="100" fill="none" stroke="#1e293b" stroke-width="2"/>' + _batt(390, 30)
    g += '<line x1="340" y1="130" x2="340" y2="90" stroke="#1e293b" stroke-width="2"/><line x1="440" y1="130" x2="440" y2="90" stroke="#1e293b" stroke-width="2"/>'
    g += '<line x1="340" y1="90" x2="440" y2="90" stroke="#1e293b" stroke-width="2"/>' + _res(390, 90, 'R₁') + _res(390, 130, 'R₂')
    g += '<circle cx="340" cy="130" r="3" fill="#1e293b"/><circle cx="440" cy="130" r="3" fill="#1e293b"/>'
    g += '<text x="345" y="168" font-size="12" font-weight="800" fill="#4338ca">b) Mắc song song</text>'
    return f'<svg viewBox="0 0 510 175" width="400" height="137" font-family="Inter">{g}</svg>'
