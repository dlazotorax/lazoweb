# -*- coding: utf-8 -*-
"""Convierte el lienzo de Claude Design (lienzo-design-v2.dc.html) en 5 páginas estáticas.
Uso, desde la raíz del repo:
  python3 _design/maquetas/operculo/_build/convert_dc.py            # maqueta → _design/maquetas/operculo/
  python3 _design/maquetas/operculo/_build/convert_dc.py --publicar # sitio   → dist/rats/operculo-toracico/
La fuente de verdad es el lienzo; no editar los HTML generados a mano."""
import re, json, html as H, sys, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, HERE)
from parts import PHYS

MAQUETA = '--publicar' not in sys.argv
DC = open(os.path.join(HERE, 'lienzo-design-v2.dc.html'), encoding='utf-8').read()
V1 = open(os.path.join(HERE, 'v1-descartada.html'), encoding='utf-8').read()
GA4 = re.search(r'<!-- Google Analytics 4.*?\}, true\);\n  </script>\n', V1, re.S).group(0)
OUT = os.path.join(ROOT, '_design/maquetas/operculo/') if MAQUETA else os.path.join(ROOT, 'dist/rats/operculo-toracico/')
BASE = 'https://rats.cl/operculo-toracico'
TODAY = '2026-09-13'
ACCENT = '#C4500E'   # naranjo levemente oscuro (David, 8-sep); el lienzo trae #0047FF
DC = DC.replace('#0047FF', ACCENT).replace('#0047ff', ACCENT)

PAGES = {  # key: (archivo, url, title, description, name, migas)
 'index': ('index.html', BASE, 'Opérculo torácico: cirugía robótica · Dr. David Lazo',
   'Síndrome del opérculo torácico neurogénico, venoso y arterial: causas, clínica, estudio y resección robótica de la primera costilla. Dr. David Lazo, Santiago.',
   'Síndrome del opérculo torácico: resolución robótica', None),
 'causas': ('causas.html', BASE+'/causas', 'Opérculo torácico: causas · Dr. David Lazo',
   'Causas del síndrome del opérculo torácico: costilla cervical, primera costilla anómala, bandas de Roos, anomalías musculares y trauma. Dr. David Lazo.',
   'Causas del síndrome del opérculo torácico', 'Causas'),
 'clinica': ('clinica.html', BASE+'/clinica', 'Opérculo torácico: síntomas y clínica · Dr. David Lazo',
   'Clínica del opérculo torácico neurogénico, venoso (Paget-Schroetter) y arterial: síntomas, signos y diagnóstico diferencial. Dr. David Lazo, Santiago.',
   'Clínica del síndrome del opérculo torácico', 'Clínica'),
 'estudio': ('estudio.html', BASE+'/estudio', 'Opérculo torácico: estudio y diagnóstico · Dr. David Lazo',
   'Estudio del opérculo torácico: radiografía, EMG, PVR, Doppler, angioTC o angioRM con maniobras y bloqueo con toxina botulínica. Dr. David Lazo, Santiago.',
   'Estudio del síndrome del opérculo torácico', 'Estudio'),
 'tratamiento': ('tratamiento.html', BASE+'/tratamiento', 'Opérculo torácico: tratamiento robótico · Dr. David Lazo',
   'Tratamiento del opérculo torácico: terapia física, vías supraclavicular y transaxilar, y resección robótica de la primera costilla. Dr. David Lazo, Santiago.',
   'Tratamiento del síndrome del opérculo torácico', 'Tratamiento'),
}
GO = {'goIndex':'index','goCausas':'causas','goClinica':'clinica','goEstudio':'estudio','goTratamiento':'tratamiento'}

# H1 por página (13-sep-2026): cada URL con su propia consulta; la portada conserva el masthead original.
H1S = {'index': 'Opérculo torácico', 'causas': 'Causas del opérculo torácico',
       'clinica': 'Síntomas del opérculo torácico', 'estudio': 'Estudio del opérculo torácico',
       'tratamiento': 'Tratamiento del opérculo torácico'}

# Sinónimos en español, visibles en el texto de la portada (§2); por la regla
# schema-visible solo se declaran en el alternateName de la portada.
SINONIMOS_ES = ['Síndrome de la salida torácica', 'Síndrome del desfiladero torácico']
def href(key):
    if MAQUETA: return PAGES[key][0]
    return PAGES[key][1]

# ── piezas comunes ──
helmet_css = re.search(r'<helmet>.*?<style>(.*?)</style>', DC, re.S).group(1)
fonts = re.search(r'<helmet>(.*?)<style>', DC, re.S).group(1).strip()
body_all = re.search(r'<div style="background:#F6F5F1">(.*)</div>\s*</x-dc>', DC, re.S).group(1)
strip_hdr = body_all[:body_all.index('<nav ')]
nav = body_all[body_all.index('<nav '):body_all.index('</nav>')+6]
tail = body_all[body_all.index('<section id="contacto"'):]
mains = {}
for m in re.finditer(r'<sc-if value="\{\{ is(\w+) \}\}"[^>]*>\s*(<main.*?</main>)\s*</sc-if>', body_all, re.S):
    mains[m.group(1).lower()] = m.group(2)
assert set(mains) == set(PAGES), mains.keys()

# ── conversión de bindings ──
hover_classes = {}
def hoverize(s):
    def rep(m):
        css = m.group(1)
        if css not in hover_classes: hover_classes[css] = f'hv{len(hover_classes)+1}'
        return f'class="{hover_classes[css]}"'
    return re.sub(r'style-hover="([^"]*)"', rep, s)

def buttons_to_links(s):
    # <button onClick="{{ goX }}" style="..."> ... </button>  →  <a href=".." style="...;display:block;text-decoration:none">
    def rep(m):
        key, attrs, inner = GO[m.group(1)], m.group(2), m.group(3)
        attrs = attrs.replace('cursor:pointer;', '').replace('border:none;', 'border:0;')
        attrs = re.sub(r'style="([^"]*)"', lambda mm: f'style="{mm.group(1).rstrip(";")};display:block;text-decoration:none{"" if "color:" in mm.group(1) else ";color:#0B0B0B"}"', attrs, count=1)
        return f'<a href="{href(key)}"{attrs}>{inner}</a>'
    return re.sub(r'<button onClick="\{\{ (go\w+) \}\}"([^>]*)>(.*?)</button>', rep, s, flags=re.S)

def nav_for(active):
    n = nav
    for k in PAGES:
        cap = k.capitalize()
        pat = re.compile(r'<sc-if value="\{\{ is'+cap+r' \}\}"[^>]*>(.*?)</sc-if>', re.S)
        n = pat.sub((lambda m: m.group(1)) if k == active else '', n)
    n = buttons_to_links(hoverize(n))
    n = n.replace('<nav ', '<nav aria-label="Sección opérculo torácico" ', 1)
    return n

def convert_main(s):
    s = buttons_to_links(hoverize(s))
    # En el sitio publicado la ruta debe ser absoluta: con cleanUrls la portada
    # se sirve en /operculo-toracico SIN barra final, y un src relativo 'imgs/'
    # resuelve contra la raiz del dominio (404). En la maqueta local se mantiene
    # relativo para poder abrirla como archivo.
    s = s.replace('uploads/operculo/imgs/', 'imgs/' if MAQUETA else '/operculo-toracico/imgs/')
    return s

def faqs_from(main_html):
    return [(H.unescape(re.sub('<[^>]+>','',q)).strip(), H.unescape(re.sub('<[^>]+>','',a)).strip())
            for q,a in re.findall(r'<summary[^>]*>(.*?)</summary>\s*<p[^>]*>(.*?)</p>', main_html, re.S)]

def ld(o): return '  <script type="application/ld+json">\n'+json.dumps(o,ensure_ascii=False,indent=2)+'\n  </script>\n'

def build(key):
    fname, url, title, desc, name, crumb = PAGES[key]
    assert len(title) <= 60 and 120 <= len(desc) <= 158, (fname, len(title), len(desc))
    main_html = convert_main(mains[key])
    nav_html = nav_for(key)
    tail_html = hoverize(tail)
    strip_html = hoverize(strip_hdr)
    if not MAQUETA:
        # El rotulo 'Maqueta de rediseno · no publicada' solo tiene sentido en la maqueta.
        strip_html = re.sub(r'<span style="color:#8F8F8F">Maqueta de rediseño · no publicada</span>\s*', '', strip_html)
        assert 'Maqueta de rediseño' not in strip_html
    if H1S[key] != 'Opérculo torácico':
        assert strip_html.count('>Opérculo torácico</h1>') == 1
        strip_html = strip_html.replace('>Opérculo torácico</h1>', f'>{H1S[key]}</h1>')
    faqs = faqs_from(main_html)
    assert faqs, key
    crumbs = [('Cirugía torácica robótica','https://rats.cl/'),('Opérculo torácico',BASE)] + ([(crumb,url)] if crumb else [])
    web = {"@context":"https://schema.org","@type":"MedicalWebPage","@id":url+"#webpage","url":url,"name":name,"inLanguage":"es-CL",
      "about":{"@type":"MedicalCondition","name":"Síndrome del opérculo torácico","alternateName":["Thoracic outlet syndrome","TOS","SOT"],
               "possibleTreatment":{"@type":"MedicalProcedure","name":"Resección robótica de la primera costilla","procedureType":"https://schema.org/SurgicalProcedure"}},
      "author":{"@id":"https://cirugiatoracica.cl/#david-lazo"},"reviewedBy":{"@id":"https://cirugiatoracica.cl/#david-lazo"},
      "lastReviewed":TODAY,"dateModified":TODAY,"specialty":"https://schema.org/Surgical",
      "isPartOf":{"@type":"WebSite","@id":"https://rats.cl/#website","url":"https://rats.cl/","name":"RATS.cl","inLanguage":"es-CL"},
      "breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate(crumbs)]},
      "description":desc}
    if key == 'index':
        assert all(s.lower() in re.sub(r'<[^>]+>','',main_html).lower() for s in SINONIMOS_ES), 'sinónimos no visibles en la portada'
        web['about']['alternateName'] += SINONIMOS_ES
    faq = {"@context":"https://schema.org","@type":"FAQPage","@id":url+"#faq","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]}
    hover_css = '\n'.join(f'  .{c}:hover{{{css}}}' for css,c in hover_classes.items())
    head = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Cirugía Robótica RATS · Dr. David Lazo Pérez" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="https://rats.cl/imgs/hero-davinci.jpg" />
  <meta property="og:locale" content="es_CL" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="author" content="Dr. David Lazo Pérez" />
  <link rel="canonical" href="{url}" />
  {fonts}
{'<!-- MAQUETA · no publicada · '+TODAY+' · pendiente de revisión de David -->' if MAQUETA else ''}
  <style>
{helmet_css.strip()}
  img {{ height: auto; max-width: 100%; }}
  nav a {{ color: #F6F5F1; }}
  nav a:hover {{ text-decoration: none; }}
{hover_css}
  </style>
'''
    doc = head + PHYS + ld(faq) + ld(web) + GA4 + '</head>\n<body>\n<div style="background:#F6F5F1">\n' + strip_html + nav_html + '\n' + main_html + '\n' + tail_html + '\n</div>\n</body>\n</html>\n'
    assert '{{' not in doc and 'sc-if' not in doc and 'onClick' not in doc and 'style-hover' not in doc, key
    os.makedirs(OUT, exist_ok=True)
    open(OUT + fname, 'w', encoding='utf-8').write(doc)
    words = len(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', doc, flags=re.S)).split())
    print(fname, len(doc), 'bytes', words, 'palabras', len(faqs), 'FAQ')

# primera pasada para poblar hover_classes en todas las piezas, luego escribir
for k in PAGES: hoverize(mains[k]);
hoverize(nav); hoverize(tail); hoverize(strip_hdr)
for k in PAGES: build(k)
# imágenes: se copian junto a las páginas (en la maqueta ya están ahí)
src = os.path.join(ROOT, '_design/maquetas/operculo/imgs'); dst = os.path.join(OUT, 'imgs')
if os.path.abspath(src) != os.path.abspath(dst):
    os.makedirs(dst, exist_ok=True)
    for f in os.listdir(src):
        if f.endswith('.webp'): shutil.copy2(os.path.join(src, f), dst)
    print('imgs copiadas a', dst)
