# Rediseño F2 (Índigo + coral) de las páginas existentes de cancerpulmonar.cl
# Regla: no cambia ningún texto. Solo estructura visual, fuentes y colores.
import re, json, sys, os
from bs4 import BeautifulSoup

SRC = sys.argv[1]   # dist/cancerpulmonar original
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

FONTS = '''  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=DM+Sans:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/estilo.css" />'''

NAV = [('/que-es', '¿Qué es?'), ('/causas', 'Causas'), ('/diagnostico', 'Diagnóstico'),
       ('/nodulo-pulmonar', 'Nódulo pulmonar'), ('/etapificacion', 'Etapificación'),
       ('/tratamiento', 'Tratamiento'), ('/sobrevida', 'Sobrevida')]

# ---------- colores: teal antiguo -> índigo/coral ----------
HEX = {
    '#0c1526': '#1A1950', '#0c4a6e': '#2B2A6B', '#0891b2': '#2B2A6B', '#0e7490': '#2B2A6B',
    '#22d3ee': '#F28A6E', '#ecfeff': '#F2F1FB', '#cffafe': '#FFE3D9', '#0369a1': '#2B2A6B',
    '#f4f8fb': '#F2F1FB', '#edf2f7': '#ECEAF8', '#dce8f0': '#E2E0F3', '#1a2b3c': '#1A1950',
    '#3a5068': '#4D4C80', '#607d93': '#5E5D8C', '#06b6d4': '#2B2A6B',
}
RGBA = {
    r'rgba\(\s*8\s*,\s*145\s*,\s*178\s*,': 'rgba(43,42,107,',
    r'rgba\(\s*6\s*,\s*182\s*,\s*212\s*,': 'rgba(43,42,107,',
    r'rgba\(\s*34\s*,\s*211\s*,\s*238\s*,': 'rgba(242,138,110,',
    r'rgba\(\s*12\s*,\s*21\s*,\s*38\s*,': 'rgba(26,25,80,',
    r'rgba\(\s*143\s*,\s*163\s*,\s*188\s*,': 'rgba(77,76,128,',
    r'rgba\(\s*12\s*,\s*74\s*,\s*110\s*,': 'rgba(43,42,107,',
}
COLORTXT = {'#fcd34d':'#7A5200','#fde68a':'#7A5200','#86efac':'#1D6B45','#fca5a5':'#B23A22','#34d399':'#1D6B45','#6ee7b7':'#1D6B45','#10b981':'#1D6B45','#059669':'#1D6B45','#fbbf24':'#7A5200','#f59e0b':'#7A5200','#f87171':'#B23A22','#ef4444':'#B23A22','#dc2626':'#B23A22','#a78bfa':'#5B3FB0','#c4b5fd':'#5B3FB0','#f472b6':'#A3245E','#67e8f9':'#2B2A6B'}
def recolor(t):
    for k, v in HEX.items():
        t = re.sub(re.escape(k) + r'\b', v, t, flags=re.I)
    for k, v in RGBA.items():
        t = re.sub(k, v, t)
    def _c(m):
        v = m.group(2).lower()
        return m.group(1) + COLORTXT.get(v, m.group(2))
    t = re.sub(r'((?<![-\w])color\s*:\s*)(#[0-9a-fA-F]{6})\b', _c, t)
    t = t.replace("'DM Serif Display',serif", "var(--display)").replace("'DM Serif Display', serif", "var(--display)")
    return t

LEGACY_VARS = '''.lg{--navy:#1A1950;--teal-deep:#2B2A6B;--teal:#2B2A6B;--teal-dark:#2B2A6B;--teal-lt:#F28A6E;
--teal-pale:#F2F1FB;--teal-mid:#FFE3D9;--bg:#fff;--bg2:#F2F1FB;--bg3:#ECEAF8;--bg4:#E2E0F3;--text:#1A1950;
--slate:#4D4C80;--muted:#5E5D8C;--text-muted:#4D4C80;--border:#E2E0F3;--accent:#2B2A6B;--accent2:#B23A22;
--accent-lt:#F28A6E;--radius:22px;--serif:var(--display);--sans:'DM Sans',system-ui,sans-serif;
font-family:var(--sans);color:var(--ink);line-height:1.65}'''

# ---------- CSS: acotar todo el CSS antiguo a .lg ----------
def strip_comments(c):
    return re.sub(r'/\*.*?\*/', '', c, flags=re.S)

def parse_blocks(c):
    """Devuelve lista de (prelude, body) a nivel superior."""
    out, i, n = [], 0, len(c)
    while i < n:
        j = c.find('{', i)
        if j < 0: break
        pre = c[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if c[k] == '{': depth += 1
            elif c[k] == '}': depth -= 1
            k += 1
        out.append((pre, c[j + 1:k - 1]))
        i = k
    return out

def scope_sel(sel):
    res = []
    for s in sel.split(','):
        s = s.strip()
        if not s: continue
        if s.startswith(':root'):
            continue                      # variables: se reemplazan por LEGACY_VARS
        if re.match(r'^(html|body)\b', s):
            continue                      # globales: los maneja estilo.css
        res.append('.lg ' + s)
    return ', '.join(res)

def scope_css(c):
    out = []
    for pre, body in parse_blocks(c):
        if pre.startswith('@media') or pre.startswith('@supports'):
            inner = scope_css(body)
            if inner.strip(): out.append(pre + '{' + inner + '}')
        elif pre.startswith('@'):
            out.append(pre + '{' + body + '}')
        else:
            s = scope_sel(pre)
            if s: out.append(s + '{' + body.strip() + '}')
    return '\n'.join(out)

SKIN = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skin.css'), encoding='utf-8').read()

# ---------- piezas del shell ----------
def topbar(b):
    m = re.search(r'<div class="topbar">(.*?)</div>\s*(?=<header|<nav)', b, re.S)
    soup = BeautifulSoup(m.group(1), 'html.parser')
    left = soup.find(class_='topbar-left')
    links = soup.find(class_='topbar-links')
    left_html = left.decode_contents().strip() if left else ''
    links_html = links.decode_contents().strip() if links else ''
    return ('<div class="topbar"><div class="wrap">\n  <span>' + left_html + '</span>\n  <div class="topbar-links">\n    '
            + links_html + '\n  </div>\n</div></div>\n')

def header(active, cta='https://cirugiatoracica.cl/#contacto', ctatxt='Consultar al especialista', logo='/'):
    lis = []
    for href, txt in NAV:
        a = ' class="active"' if href == active else ''
        lis.append(f'    <li><a href="{href}"{a}>{txt}</a></li>')
    return (f'<header class="site-header">\n<nav>\n  <a href="{logo}" class="logo">Cáncer <span>Pulmonar</span></a>\n'
            '  <button class="nav-toggle" aria-label="Abrir menú" onclick="this.closest(\'nav\').classList.toggle(\'nav-open\')"><span></span><span></span><span></span></button>\n'
            '  <ul class="nav-links">\n' + '\n'.join(lis) + '\n  </ul>\n'
            f'  <a href="{cta}" class="nav-cta">{ctatxt}</a>\n</nav>\n</header>\n')

def crumbs(h):
    soup = BeautifulSoup(h, 'html.parser')
    inner = soup.find(class_='breadcrumb-inner')
    parts = []
    for el in inner.children:
        if getattr(el, 'name', None) == 'a':
            parts.append(str(el))
        elif getattr(el, 'name', None) == 'span' and 'breadcrumb-current' in (el.get('class') or []):
            parts.append('<span class="current">' + el.decode_contents() + '</span>')
    return '<div class="wrap"><div class="crumbs">' + ' › '.join(parts) + '</div></div>\n'

def hero(h):
    soup = BeautifulSoup(h, 'html.parser')
    tag = soup.find(class_='page-hero-tag').decode_contents()
    h1 = soup.find('h1').decode_contents()
    lead = soup.find(class_='page-hero-lead').decode_contents()
    return ('<div class="wrap">\n  <div class="hero">\n    <div class="hero-tag">' + tag + '</div>\n    <h1>' + h1
            + '</h1>\n    <p>' + lead + '</p>\n  </div>\n</div>\n')

def pager(h):
    soup = BeautifulSoup(h, 'html.parser')
    out = []
    for a in soup.find_all('a', class_='page-nav-link'):
        cls = ' class="next"' if 'next' in a.get('class') else ''
        k = a.find(class_='pnl-label').decode_contents().strip()
        t = a.find(class_='pnl-title').decode_contents().strip()
        out.append(f'    <a href="{a["href"]}"{cls}><div class="k">{k}</div><div class="t">{t}</div></a>')
    return '<section class="section"><div class="wrap">\n  <div class="pager">\n' + '\n'.join(out) + '\n  </div>\n</div></section>\n'

def clean_inline(el):
    for t in el.find_all(True):
        if t.has_attr('style'): del t['style']
    return el

def bio(h):
    soup = BeautifulSoup(h, 'html.parser')
    img = soup.find('img')
    img_html = str(img)
    col = soup.find(class_='bio-photo').find_next_sibling('div')
    ps = col.find_all('p', recursive=False)
    eyebrow, name, role = ps[0].decode_contents(), col.find('h2').decode_contents(), ps[1].decode_contents()
    txts = []
    for p in ps[2:]:
        clean_inline(p)
        txts.append('      <p class="txt">' + p.decode_contents() + '</p>')
    sol = None
    for a in col.find_all('a'):
        if 'Solicitar hora' in a.get_text():
            sol = a
    perfil = col.find('a', class_='perfil-box')
    acts = []
    if sol is not None:
        acts.append(f'        <a class="btn" href="{sol["href"]}">{sol.get_text().strip()}</a>')
    if perfil is not None:
        t = perfil.find(class_='perfil-box-t').decode_contents()
        s = perfil.find(class_='perfil-box-s').decode_contents()
        acts.append(f'        <a class="perfil" href="{perfil["href"]}"><b>{t}</b><span>{s}</span></a>')
    # cifras (+5.700 / +3.200 / 19 años): eliminadas a pedido de David (17-oct-2026)
    return ('\n<section class="section" id="dr-lazo"><div class="wrap">\n  <div class="bio">\n    ' + img_html + '\n    <div>\n'
            '      <p class="eyebrow">' + eyebrow + '</p>\n      <h2>' + name + '</h2>\n      <p class="role">' + role + '</p>\n'
            + '\n'.join(txts) + '\n      <div class="actions">\n' + '\n'.join(acts) + '\n      </div>\n    </div>\n  </div>\n</div></section>\n')

def faq(h):
    soup = BeautifulSoup(h, 'html.parser')
    h2 = soup.find(class_='faq-h2').decode_contents()
    items = []
    for it in soup.find_all(class_='faq-item'):
        q = it.find(class_='faq-q')
        arr = q.find(class_='faq-arrow')
        if arr: arr.decompose()
        a = it.find(class_='faq-a')
        items.append('    <details><summary>' + q.decode_contents().strip() + '</summary><p>' + a.decode_contents().strip() + '</p></details>')
    return ('\n<section class="section" id="faq"><div class="wrap">\n  <h2 class="h2">' + h2 + '</h2>\n  <div class="faq">\n'
            + '\n'.join(items) + '\n  </div>\n</div></section>\n')

CTA = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cta.html'), encoding='utf-8').read()

def footer(h):
    soup = BeautifulSoup(h, 'html.parser')
    brand = soup.find(class_='footer-brand').decode_contents()
    links = soup.find(class_='footer-links')
    disc = soup.find(class_='footer-disclaimer').decode_contents().strip()
    return ('<footer class="site-footer"><div class="wrap">\n  <div class="footer-top">\n    <div class="footer-brand">' + brand
            + '</div>\n    <div class="footer-links">\n      ' + links.decode_contents().strip() + '\n    </div>\n  </div>\n'
            '  <div class="footer-disclaimer">' + disc + '</div>\n</div></footer>\n')

def grab(pat, s):
    m = re.search(pat, s, re.S)
    if not m: raise SystemExit('no encontrado: ' + pat)
    return m.group(0)

# Cambios de texto pedidos explícitamente por David
EDITS = {
    'causas.html': [('<h4>Importante: no todos los fumadores desarrollan cáncer</h4>', '<h4>Importante: no sólo los fumadores desarrollan cáncer</h4>'),
                    ('Fumar es el principal factor de riesgo, pero no el único, y no todos los fumadores enferman.', 'Fumar es el principal factor de riesgo, pero no el único.'),
                    ('El TAC de baja dosis detecta nódulos pulmonares pequeños', 'El TAC de baja dosis detecta <a href="/nodulo-pulmonar">nódulos pulmonares</a> pequeños')],
    'index.html': [('<div class="faq-a">La mayoría de los nódulos pulmonares no son cáncer.', '<div class="faq-a">La mayoría de los <a href="/nodulo-pulmonar">nódulos pulmonares</a> no son cáncer.')],  # 17-oct-2026
}

def build(fname):
    s = open(os.path.join(SRC, fname), encoding='utf-8').read()
    for a, b in EDITS.get(fname, []):
        assert s.count(a) == 1, a
        s = s.replace(a, b)
    head, body = s[:s.index('<body')], s[s.index('<body'):]
    # head
    css_old = re.search(r'<style>(.*?)</style>', head, re.S).group(1)
    head = re.sub(r'\s*<link rel="preconnect"[^>]*>', '', head)
    head = re.sub(r'\s*<link href="https://fonts.googleapis.com[^>]*>', '', head)
    legacy = recolor(scope_css(strip_comments(css_old)))
    newstyle = '<style>\n' + LEGACY_VARS + '\n' + legacy + '\n/* --- capa F2 sobre el contenido --- */\n' + SKIN + '\n</style>'
    head = re.sub(r'<style>.*?</style>', lambda m: FONTS.strip() + '\n  ' + newstyle, head, count=1, flags=re.S)
    # body
    active = '/' + fname.replace('.html', '')
    main = grab(r'<main[^>]*>.*?</main>', body)
    bc = grab(r'<div class="breadcrumb">.*?</div>\s*</div>', main)
    hr = grab(r'<div class="page-hero">.*?</div>\s*</div>', main)
    pn = grab(r'<div class="page-nav">.*?</a>\s*<a.*?</a>\s*</div>', main)
    i0 = main.index(hr) + len(hr)
    i1 = main.index(pn)
    content = label_tables(recolor_inline(main[i0:i1].strip()))
    mtag = re.match(r'<main[^>]*>', main).group(0)
    newmain = (mtag + '\n' + crumbs(bc) + hero(hr) + '<section class="section"><div class="wrap lg">\n' + content
               + '\n</div></section>\n' + pager(pn) + '</main>\n')
    rest = body[body.index(pn) + len(pn):]
    biosec = grab(r'<section class="bio-section-light" id="dr-lazo">.*?</section>', rest)
    faqsec = grab(r'<section[^>]*id="faq">.*?</section>', rest)
    ctasec = grab(r'<section class="cta-unified" id="contacto">.*?</section>', rest)
    foot = grab(r'<footer>.*?</footer>', rest)
    lds = re.findall(r'<script type="application/ld\+json">.*?</script>', body, re.S)
    for x in lds: json.loads(re.search(r'>(.*)</script>', x, re.S).group(1))
    # orden original de bio/faq
    order = sorted([(rest.index(biosec), bio(biosec)), (rest.index(faqsec), faq(faqsec))])
    newbody = ('<body>\n\n' + topbar(body) + '\n' + header(active, re.search(r'<a href="([^"]+)" class="nav-cta"', body).group(1)) + '\n' + newmain + ''.join(x for _, x in order)
               + '\n' + CTA + '\n' + footer(foot) + '\n  ' + '\n  '.join(lds) + '\n</body>\n</html>\n')
    out = head + newbody
    open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(out)
    return out


def label_tables(h):
    """Marca tablas para apilarlas en móvil: data-l (encabezado) y data-c (columna), respetando rowspan."""
    def tb(m):
        t = m.group(0)
        th = [' '.join(re.sub('<[^>]+>', '', x).split()) for x in re.findall(r'<th[^>]*>(.*?)</th>', t, re.S)]
        if not th: return t
        pend = {}   # col -> filas restantes ocupadas
        def tr(r):
            if '<th' in r.group(0): return r.group(0)
            occ = {c for c, n in pend.items() if n > 0}
            for c in list(pend): pend[c] -= 1
            col = [0]
            def td(c):
                while col[0] in occ: col[0] += 1
                a = c.group(1)
                rs = re.search(r'rowspan="(\d+)"', a); cs = re.search(r'colspan="(\d+)"', a)
                n = int(cs.group(1)) if cs else 1
                i = col[0]
                if rs: pend[i] = int(rs.group(1)) - 1
                lab = ' · '.join(th[i:i + n]); col[0] += n
                return '<td' + a + ' data-c="' + str(i) + '" data-l="' + lab.replace('"', '&quot;') + '">'
            return re.sub(r'<td([^>]*)>', td, r.group(0))
        t = re.sub(r'<tr[^>]*>.*?</tr>', tr, t, flags=re.S)
        t = re.sub(r'<table( class="([^"]*)")?', lambda mm: '<table class="' + ((mm.group(2) + ' ') if mm.group(2) else '') + 'stk"', t, count=1)
        return t
    return re.sub(r'<table[^>]*>.*?</table>', tb, h, flags=re.S)

def recolor_inline(h):
    return re.sub(r'style="([^"]*)"', lambda m: 'style="' + recolor(m.group(1)) + '"', h)


def build_index(fname='index.html'):
    s = open(os.path.join(SRC, fname), encoding='utf-8').read()
    for a, b in EDITS.get(fname, []):
        assert s.count(a) == 1, a
        s = s.replace(a, b)
    head, body = s[:s.index('<body')], s[s.index('<body'):]
    css_old = re.search(r'<style>(.*?)</style>', head, re.S).group(1)
    head = re.sub(r'\s*<link rel="preconnect"[^>]*>', '', head)
    head = re.sub(r'\s*<link href="https://fonts.googleapis.com[^>]*>', '', head)
    legacy = recolor(scope_css(strip_comments(css_old)))
    newstyle = '<style>\n' + LEGACY_VARS + '\n' + legacy + '\n/* --- capa F2 sobre el contenido --- */\n' + SKIN + '\n</style>'
    head = re.sub(r'<style>.*?</style>', lambda m: FONTS.strip() + '\n  ' + newstyle, head, count=1, flags=re.S)
    # topbar
    tb = BeautifulSoup(grab(r'<div class="topbar">.*?</div>', body), 'html.parser').find(class_='topbar')
    top = '<div class="topbar"><div class="wrap">\n  <span></span>\n  <div class="topbar-links">\n    ' + tb.decode_contents().strip() + '\n  </div>\n</div></div>\n'
    navm = re.search(r'<a href="([^"]+)" class="nav-cta">([^<]+)</a>', body)
    logo = re.search(r'<a class="nav-logo" href="([^"]+)"', body).group(1)
    hdr = header(None, navm.group(1), navm.group(2), logo)
    # hero
    hs = BeautifulSoup(grab(r'<section class="hero" id="inicio">.*?</section>', body), 'html.parser')
    badge = hs.find(class_='hero-badge'); badge.find(class_='hero-badge-dot').decompose()
    h1 = hs.find('h1').decode_contents(); lead = hs.find(class_='hero-lead').decode_contents()
    cta = hs.find(class_='hero-ctas').find('a')
    hero_html = ('<div class="wrap">\n  <div class="hero has-img" id="inicio">\n    <div class="hero-txt">\n    <div class="hero-tag">' + badge.decode_contents().strip()
                 + '</div>\n    <h1>' + h1 + '</h1>\n    <p>' + lead + '</p>\n    <div class="hero-actions"><a class="btn" href="' + cta['href'] + '">' + cta.decode_contents() + '</a></div>\n    </div>\n'
                 '    <img class="hero-img hero-photo" src="imgs/hero-petct.webp" alt="" width="1408" height="768" decoding="async" fetchpriority="high" />\n  </div>\n</div>\n')
    main = grab(r'<main[^>]*>.*?</main>', body)
    alert = grab(r'<div class="alert-wrap">.*?</div>\s*</div>\s*</div>\s*</div>', main)
    cards = grab(r'<section class="section section-alt" style="padding-top:2rem;">.*?</section>', main)
    cards = cards.replace('<section class="section section-alt" style="padding-top:2rem;">', '<div class="home-cards">').rsplit('</section>', 1)[0] + '</div>'
    biosec = grab(r'<section class="section" id="dr-lazo".*?</section>', main)
    mtag = re.match(r'<main[^>]*>', main).group(0)
    newmain = (mtag + '\n' + hero_html + '<section class="section"><div class="wrap lg">\n' + recolor_inline(alert) + '\n' + recolor_inline(cards)
               + '\n</div></section>\n' + bio_index(biosec) + '</main>\n')
    rest = body[body.index('</main>') + 7:]
    pubsec = grab(r'<section class="section section-alt" id="publicaciones">.*?</section>', rest)
    faqsec = grab(r'<section[^>]*id="faq">.*?</section>', rest)
    foot = grab(r'<footer>.*?</footer>', rest)
    lds = re.findall(r'<script type="application/ld\+json">.*?</script>', body, re.S)
    for x in lds: json.loads(re.search(r'>(.*)</script>', x, re.S).group(1))
    ft = footer(foot).replace('<a href="/diagnostico">Diagnóstico</a>', '<a href="/diagnostico">Diagnóstico</a>\n        <a href="/nodulo-pulmonar">Nódulo pulmonar</a>', 1)
    newbody = ('<body>\n\n' + top + '\n' + hdr + '\n' + newmain + pubs_index(pubsec) + '\n' + CTA + faq(faqsec) + '\n' + ft
               + '\n  ' + '\n  '.join(lds) + '\n</body>\n</html>\n')
    open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(head + newbody)

def bio_index(h):
    soup = BeautifulSoup(h, 'html.parser')
    img = str(soup.find('img'))
    eb = soup.find(class_='bio-eyebrow').decode_contents()
    nm = soup.find(class_='bio-name').decode_contents()
    rl = soup.find(class_='bio-role').decode_contents()
    txts = ['      <p class="txt">' + ' '.join(p.decode_contents().split()) + '</p>' for p in soup.find_all(class_='bio-text')]
    src = soup.find(class_='bio-src')
    if src: txts.append('      <p class="txt src">' + src.decode_contents().strip() + '</p>')
    perfil = soup.find('a', class_='perfil-box')
    t = perfil.find(class_='perfil-box-t').decode_contents(); s_ = perfil.find(class_='perfil-box-s').decode_contents()
    # cifras (bio-creds) eliminadas a pedido de David (17-oct-2026)
    return ('\n<section class="section" id="dr-lazo"><div class="wrap">\n  <div class="bio">\n    ' + img + '\n    <div>\n'
            '      <p class="eyebrow">' + eb + '</p>\n      <h2>' + nm + '</h2>\n      <p class="role">' + rl + '</p>\n' + '\n'.join(txts)
            + '\n      <div class="actions">\n        <a class="perfil" href="' + perfil['href'] + '"><b>' + t + '</b><span>' + s_ + '</span></a>\n      </div>\n    </div>\n  </div>\n</div></section>\n')

def pubs_index(h):
    soup = BeautifulSoup(h, 'html.parser')
    title = soup.find(class_='section-title').decode_contents()
    intro = soup.find(class_='pubs-intro').decode_contents()
    items = []
    for it in soup.find_all(class_='pubs-item'):
        items.append('    <div class="pub">\n      <div class="pub-t">' + it.find(class_='pubs-title').decode_contents() + '</div>\n      <div class="pub-a">'
                     + it.find(class_='pubs-authors').decode_contents() + '</div>\n      <div class="pub-m">' + it.find(class_='pubs-meta').decode_contents() + '</div>\n    </div>')
    al = soup.find(class_='pubs-all')
    more = ('\n  <a class="more" href="' + al['href'] + '">' + al.decode_contents() + '</a>') if al else ''
    return ('\n<section class="section" id="publicaciones"><div class="wrap">\n  <h2 class="h2">' + title + '</h2>\n  <p class="pubs-intro">' + intro
            + '</p>\n  <div class="pubs">\n' + '\n'.join(items) + '\n  </div>' + more + '\n</div></section>\n')

if __name__ == '__main__':
    for f in sys.argv[3:]:
        build_index(f) if f == 'index.html' else build(f)
        print('ok', f)
