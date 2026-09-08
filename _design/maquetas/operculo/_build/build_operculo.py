# -*- coding: utf-8 -*-
"""Construye la maqueta de rats.cl/operculo-toracico (hub + 4 subpáginas) en _design/maquetas/operculo/."""
import json, re, html as H, sys
sys.path.insert(0, '/tmp/claude-0/-home-claude/7e55ec31-f280-5494-b928-ae7e5af92107/scratchpad')
from parts import PHYS, CSS, CTA, SCRIPTS

SRC = open('/home/claude/lazoweb/_design/maquetas/operculo/_build/v1-descartada.html', encoding='utf-8').read()
GA4 = re.search(r'<!-- Google Analytics 4.*?\}, true\);\n  </script>\n', SRC, re.S).group(0)
OUT = '/home/claude/lazoweb/_design/maquetas/operculo/'
BASE = 'https://rats.cl/operculo-toracico'
IMG = 'https://rats.cl/imgs/'
TODAY = '2026-09-08'
MAQUETA = True

EXTRA_CSS = '''  <style>
    /* ── Sección opérculo torácico: subnavegación y bloques propios ── */
    .subnav { display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:1.75rem; }
    .subnav a { font-size:0.8rem; font-weight:600; color:rgba(255,255,255,0.8); text-decoration:none; border:1px solid rgba(255,255,255,0.25); border-radius:999px; padding:0.4rem 0.95rem; transition:all .2s; }
    .subnav a:hover, .subnav a.on { background:var(--teal); border-color:var(--teal); color:#fff; }
    .hero.hero-sub { min-height:62vh; }
    .robot-box { background:var(--navy); border-radius:18px; padding:2.25rem 2.5rem; color:#fff; margin-top:2.5rem; display:grid; grid-template-columns:auto 1fr; gap:1.75rem; align-items:start; }
    .robot-box .rb-ico { width:52px; height:52px; border-radius:14px; background:rgba(34,211,238,0.12); display:flex; align-items:center; justify-content:center; color:var(--teal-lt); flex:none; }
    .robot-box h3 { font-family:var(--serif); font-size:1.6rem; letter-spacing:-0.02em; margin-bottom:0.6rem; color:#fff; }
    .robot-box p { color:rgba(255,255,255,0.72); font-size:0.93rem; line-height:1.75; }
    .robot-box p + p { margin-top:0.75rem; }
    .robot-box a { color:var(--teal-lt); font-weight:600; }
    .stat-strip { display:grid; grid-template-columns:repeat(4,1fr); gap:1rem; margin-top:2rem; }
    .stat-strip .st { background:var(--bg); border:1px solid var(--border); border-radius:12px; padding:1.1rem; }
    .stat-strip .st b { display:block; font-size:1.6rem; font-weight:800; color:var(--teal); letter-spacing:-0.03em; }
    .stat-strip .st span { font-size:0.78rem; color:var(--muted); line-height:1.4; }
    .stat-strip .st small { display:block; font-size:0.68rem; color:var(--muted); margin-top:0.35rem; }
    .fig { border-radius:16px; overflow:hidden; border:1px solid var(--border); background:var(--bg-alt); }
    .fig img { width:100%; display:block; }
    .fig figcaption { font-size:0.78rem; color:var(--muted); padding:0.75rem 1rem; line-height:1.5; }
    .two-col { display:grid; grid-template-columns:1.15fr 1fr; gap:3rem; align-items:center; margin-top:2.5rem; }
    .video-slot { position:relative; border-radius:18px; overflow:hidden; background:var(--navy2); aspect-ratio:16/9; display:flex; align-items:center; justify-content:center; color:rgba(255,255,255,0.7); text-align:center; padding:2rem; border:2px dashed rgba(34,211,238,0.35); }
    .video-slot strong { display:block; color:#fff; font-size:1.05rem; margin-bottom:0.4rem; }
    .video-slot small { font-size:0.8rem; }
    .cards-4 { display:grid; grid-template-columns:repeat(4,1fr); gap:1.25rem; margin-top:2.5rem; }
    .card-link { display:block; text-decoration:none; background:var(--bg); border:1px solid var(--border); border-radius:14px; padding:1.5rem; transition:border-color .2s, transform .2s, box-shadow .2s; }
    .card-link:hover { border-color:var(--teal); transform:translateY(-3px); box-shadow:0 12px 30px rgba(12,21,38,0.08); }
    .card-link .cl-num { font-size:0.7rem; font-weight:700; letter-spacing:0.08em; color:var(--teal); margin-bottom:0.5rem; }
    .card-link h3 { font-size:1.05rem; color:var(--navy); margin-bottom:0.45rem; }
    .card-link p { font-size:0.85rem; color:var(--slate); line-height:1.6; }
    .card-link .cl-go { display:inline-block; margin-top:0.85rem; font-size:0.82rem; font-weight:700; color:var(--teal-dark); }
    .defs { display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; margin-top:2.5rem; }
    .def { background:var(--bg-alt); border:1px solid var(--border); border-radius:14px; padding:1.5rem; }
    .def .d-tag { display:inline-block; font-size:0.68rem; font-weight:700; letter-spacing:0.06em; text-transform:uppercase; color:var(--teal-dark); background:var(--teal-mid); border-radius:6px; padding:0.2rem 0.5rem; margin-bottom:0.7rem; }
    .def h3 { font-size:1rem; color:var(--navy); margin-bottom:0.5rem; }
    .def p, .def li { font-size:0.86rem; color:var(--slate); line-height:1.65; }
    .def ul { padding-left:1.1rem; margin-top:0.4rem; }
    .def ul li { margin-bottom:0.25rem; }
    .list-check { list-style:none; display:grid; grid-template-columns:1fr 1fr; gap:0.6rem 2rem; margin-top:1.5rem; }
    .list-check li { position:relative; padding-left:1.5rem; font-size:0.9rem; color:var(--slate); line-height:1.6; }
    .list-check li::before { content:''; position:absolute; left:0; top:0.55em; width:9px; height:9px; border-radius:50%; background:var(--teal); }
    .refs { margin-top:1.5rem; }
    .refs ol { padding-left:1.3rem; }
    .refs li { font-size:0.8rem; color:var(--slate); line-height:1.6; margin-bottom:0.45rem; }
    .refs a { color:var(--teal-dark); }
    .refs-title { font-size:0.95rem; font-weight:700; color:var(--navy); margin-bottom:0.5rem; }
    .pager { display:flex; justify-content:space-between; gap:1rem; margin-top:3rem; flex-wrap:wrap; }
    .pager a { text-decoration:none; font-weight:700; font-size:0.9rem; color:var(--teal-dark); border:1px solid var(--border); border-radius:10px; padding:0.8rem 1.1rem; background:var(--bg); }
    .pager a:hover { border-color:var(--teal); }
    .cmp-wrap { overflow-x:auto; margin-top:2.5rem; border:1px solid var(--border); border-radius:14px; background:var(--bg); }
    .cmp-table { width:100%; border-collapse:collapse; font-size:0.86rem; min-width:720px; }
    .cmp-table th, .cmp-table td { padding:0.95rem 1.1rem; text-align:left; vertical-align:top; border-bottom:1px solid var(--border); line-height:1.55; }
    .cmp-table th { background:var(--navy); color:#fff; font-size:0.72rem; letter-spacing:0.06em; text-transform:uppercase; font-weight:700; }
    .cmp-table tbody tr:last-child td { border-bottom:none; }
    .cmp-table td { color:var(--slate); }
    .cmp-table td strong { color:var(--navy); }
    .cmp-table tr.cmp-hl td { background:var(--teal-pale); }
    .crumbs { font-size:0.78rem; color:rgba(255,255,255,0.55); margin-bottom:1.25rem; display:flex; gap:0.5rem; align-items:center; flex-wrap:wrap; }
    .crumbs a { color:rgba(255,255,255,0.75); text-decoration:none; }
    .fi-num { display:inline-flex; width:100%; height:100%; align-items:center; justify-content:center; font-weight:800; font-size:0.95rem; color:var(--teal-lt); }
    .ref-label { font-size:0.8rem; font-weight:600; color:var(--teal-lt); margin-bottom:0.75rem; }
    .ref-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:1.25rem; margin-top:2.5rem; }
    .ref-card { background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.1); border-radius:14px; padding:1.6rem; }
    .ref-card h3 { color:#fff; font-size:1rem; font-weight:700; margin-bottom:0.9rem; }
    .ref-card ul { list-style:none; display:flex; flex-direction:column; gap:0.6rem; }
    .ref-card li { font-size:0.85rem; color:rgba(255,255,255,0.72); line-height:1.6; padding-left:1rem; position:relative; }
    .ref-card li::before { content:''; position:absolute; left:0; top:0.62em; width:5px; height:5px; border-radius:50%; background:var(--teal-lt); }
    .ref-card a { color:var(--teal-lt); font-weight:600; }
    .maqueta-banner { position:fixed; bottom:12px; left:12px; z-index:999; background:#b45309; color:#fff; font-size:0.72rem; font-weight:700; padding:0.4rem 0.7rem; border-radius:8px; opacity:0.9; }
    @media (max-width:960px) { .cards-4, .defs, .stat-strip, .ref-grid { grid-template-columns:1fr 1fr; } .two-col { grid-template-columns:1fr; } .robot-box { grid-template-columns:1fr; padding:1.75rem; } }
    @media (max-width:640px) { .cards-4, .defs, .stat-strip, .list-check, .ref-grid { grid-template-columns:1fr; } .hero.hero-sub { min-height:70vh !important; } }
  </style>
'''

# Referencias verificadas en PubMed (8-sep-2026): título, revista, año, DOI.
REFS = {
 'hussain': ('Hussain MA, Aljabri B, Al-Omran M.', 'Vascular Thoracic Outlet Syndrome.', 'Semin Thorac Cardiovasc Surg. 2016;28(1):151-7.', '10.1053/j.semtcvs.2015.10.008'),
 'connolly': ('Connolly MR, Auchincloss HG.', 'Anatomy and Embryology of the Thoracic Outlet.', 'Thorac Surg Clin. 2021;31(1):1-10.', '10.1016/j.thorsurg.2020.09.007'),
 'roos': ('Roos DB.', 'Congenital anomalies associated with thoracic outlet syndrome. Anatomy, symptoms, diagnosis, and treatment.', 'Am J Surg. 1976;132(6):771-8.', '10.1016/0002-9610(76)90456-6'),
 'martinez': ('Martinez BD, et al.', 'Computer-assisted instrumentation during endoscopic transaxillary first rib resection for thoracic outlet syndrome: a safe alternate approach.', 'Vascular. 2005;13(6):327-35.', '10.1258/rsmvasc.13.6.327'),
 'cook': ('Cook JR, Thompson RW.', 'Evaluation and Management of Venous Thoracic Outlet Syndrome.', 'Thorac Surg Clin. 2021;31(1):27-44.', '10.1016/j.thorsurg.2020.08.012'),
 'nguyen': ('Nguyen LL, Soo Hoo AJ.', 'Evaluation and Management of Arterial Thoracic Outlet Syndrome.', 'Thorac Surg Clin. 2021;31(1):45-54.', '10.1016/j.thorsurg.2020.09.006'),
 'kok': ('Kök M, et al.', 'Systematic Review on Botulinum Toxin Injections as Diagnostic or Therapeutic Tool in Thoracic Outlet Syndrome.', 'Ann Vasc Surg. 2023;96:347-356.', '10.1016/j.avsg.2023.05.009'),
 'burt2018': ('Burt BM.', 'Thoracic outlet syndrome for thoracic surgeons.', 'J Thorac Cardiovasc Surg. 2018;156(3):1318-1323.e1.', '10.1016/j.jtcvs.2018.02.096'),
 'burt2020': ('Burt BM, Palivela N, Goodman MB.', 'Transthoracic Robotic First Rib Resection: Technique Crystallized.', 'Ann Thorac Surg. 2020;110(1):e71-e73.', '10.1016/j.athoracsur.2019.12.086'),
 'kara': ('Kara HV, Balderson SS, Tong BC, D\'Amico TA.', 'Video assisted transaxillary first rib resection in treatment of thoracic outlet syndrome (TOS).', 'Ann Cardiothorac Surg. 2016;5(1):67-9.', '10.3978/j.issn.2225-319X.2015.08.09'),
 'ghara2019': ('Gharagozloo F, Meyer M, Tempesta B, Gruessner S.', 'Robotic transthoracic first-rib resection for Paget-Schroetter syndrome.', 'Eur J Cardiothorac Surg. 2019;55(3):434-439.', '10.1093/ejcts/ezy275'),
 'costantino': ('Costantino CL, Schumacher LY.', 'Surgical Technique: Minimally Invasive First-Rib Resection.', 'Thorac Surg Clin. 2021;31(1):81-87.', '10.1016/j.thorsurg.2020.09.004'),
}
def refs_html(keys):
    lis = ''.join(f'<li>{a} {t} <em>{j}</em> <a href="https://doi.org/{d}" target="_blank" rel="noopener">doi:{d}</a></li>' for a,t,j,d in (REFS[k] for k in keys))
    return f'<div class="refs"><p class="refs-title">Fuentes</p><ol>{lis}</ol></div>'

NAV_ITEMS = [('causas','Causas'),('clinica','Clínica'),('estudio','Estudio'),('tratamiento','Tratamiento')]
def subnav(active):
    ON = ' class="on"'
    items = ''.join(f'<a href="{BASE}/{k}"{ON if k==active else ""}>{v}</a>' for k,v in NAV_ITEMS)
    return f'<div class="subnav"><a href="{BASE}"{ON if active=="index" else ""}>Visión general</a>{items}</div>'

def crumbs(name=None):
    c = f'<a href="https://rats.cl">Cirugía torácica robótica</a><span>›</span>'
    if name: c += f'<a href="{BASE}">Opérculo torácico</a><span>›</span><span aria-current="page">{name}</span>'
    else: c += '<span aria-current="page">Opérculo torácico</span>'
    return f'<p class="crumbs">{c}</p>'

def topbar_nav():
    return '''    <div class="topbar">
      <a href="https://rats.cl">Robótica</a><span>·</span>
      <a href="https://cancerpulmonar.cl">Cáncer Pulmonar</a><span>·</span>
      <a href="https://broncoscopia.cl">Broncoscopía</a><span>·</span>
      <a href="https://videotoracoscopia.cl">Videotoracoscopía</a><span>·</span>
      <a href="https://hiperhidrosis.cl">Hiperhidrosis</a>
    </div>
  <header>
  <nav id="main-nav">
    <a class="nav-logo" href="https://rats.cl">
      <div class="nav-logo-mark"><svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round"><path d="M12 2C7 6 4 10 4 14a8 8 0 0016 0c0-4-3-8-8-12z"/><path d="M12 8v8M9 13l3 3 3-3"/></svg></div>
      <span class="nav-logo-text"><span>RATS</span> · Dr. Lazo</span>
    </a>
    <ul class="nav-links">
      <li><a href="''' + BASE + '''">Opérculo torácico</a></li>
      <li><a href="''' + BASE + '''/causas">Causas</a></li>
      <li><a href="''' + BASE + '''/clinica">Clínica</a></li>
      <li><a href="''' + BASE + '''/estudio">Estudio</a></li>
      <li><a href="''' + BASE + '''/tratamiento">Tratamiento</a></li>
    </ul>
    <a class="nav-cta" href="#contacto">Agendar consulta →</a>
    <button class="nav-hamburger" aria-label="Abrir menú" onclick="this.closest('nav').classList.toggle('nav-open')"><span></span><span></span><span></span></button>
  </nav>
  </header>
'''

def robot_box(title, paras):
    ps = ''.join(f'<p>{p}</p>' for p in paras)
    return f'''<div class="robot-box">
        <div class="rb-ico"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="7" width="16" height="12" rx="3"/><path d="M12 3v4M8 12h.01M16 12h.01M9 16h6"/></svg></div>
        <div><h3>{title}</h3>{ps}</div>
      </div>'''

def faq_html(faqs, h2):
    items = ''.join(f'''        <div class="faq-item">
          <button class="faq-q">{q}<div class="faq-arrow">+</div></button>
          <div class="faq-a">{a}</div>
        </div>
''' for q,a in faqs)
    return f'''    <section class="section section-alt" id="faq">
      <div class="inner">
        <h2 class="faq-h2">{h2}</h2>
        <div class="faq-list">
{items}        </div>
      </div>
    </section>
'''

def faq_ld(url, faqs):
    return {"@context":"https://schema.org","@type":"FAQPage","@id":url+"#faq","mainEntity":[{"@type":"Question","name":H.unescape(re.sub('<[^>]+>','',q)),"acceptedAnswer":{"@type":"Answer","text":H.unescape(re.sub('<[^>]+>','',a))}} for q,a in faqs]}

def ld(o): return '  <script type="application/ld+json">\n'+json.dumps(o,ensure_ascii=False,indent=2)+'\n  </script>\n'

def pager(prev, nxt):
    a = f'<a href="{BASE}/{prev[0]}">← {prev[1]}</a>' if prev else f'<a href="{BASE}">← Visión general</a>'
    b = f'<a href="{BASE}/{nxt[0]}">{nxt[1]} →</a>' if nxt else f'<a href="{BASE}#contacto">Agendar consulta →</a>'
    return f'<div class="pager">{a}{b}</div>'

def page(fname, url, title, desc, name, crumb_name, active, hero_h1, hero_lead, body, faqs, faq_h2, crumbs_ld, extra_ld=None, og_type='article'):
    assert len(title) <= 60, (fname, len(title))
    assert 120 <= len(desc) <= 158, (fname, len(desc))
    web = {"@context":"https://schema.org","@type":"MedicalWebPage","@id":url+"#webpage","url":url,"name":name,"inLanguage":"es-CL",
      "about":{"@type":"MedicalCondition","name":"Síndrome del opérculo torácico","alternateName":["Thoracic outlet syndrome","TOS","SOT"]},
      "author":{"@id":"https://cirugiatoracica.cl/#david-lazo"},"reviewedBy":{"@id":"https://cirugiatoracica.cl/#david-lazo"},
      "lastReviewed":TODAY,"dateModified":TODAY,"specialty":"https://schema.org/Surgical",
      "isPartOf":{"@type":"WebSite","@id":"https://rats.cl/#website","url":"https://rats.cl/","name":"RATS.cl","inLanguage":"es-CL"},
      "breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":n,"item":u} for i,(n,u) in enumerate(crumbs_ld)]},
      "description":desc}
    if extra_ld: web.update(extra_ld)
    head = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:site_name" content="Cirugía Robótica RATS · Dr. David Lazo Pérez" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="https://rats.cl/imgs/hero-davinci.jpg" />
  <meta property="og:locale" content="es_CL" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="author" content="Dr. David Lazo Pérez" />
  <link rel="canonical" href="{url}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<!-- MAQUETA · no publicada · {TODAY} · pendiente de revisión de David -->
'''
    hero = f'''  <main id="main-content">
  <section class="hero hero-sub" id="inicio">
    <div class="hero-bg"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      {crumbs(crumb_name)}
      <div class="hero-badge"><div class="hero-badge-dot"></div>Sistema Da Vinci · Clínica Las Condes · Santiago</div>
      <h1>{hero_h1}</h1>
      <p class="hero-lead">{hero_lead}</p>
      {subnav(active)}
    </div>
  </section>
'''
    doc = head + PHYS + CSS + EXTRA_CSS + ld(faq_ld(url, faqs)) + ld(web) + GA4 + '</head>\n<body>\n' + topbar_nav() + hero + body + faq_html(faqs, faq_h2) + CTA + '''  </main>
  <footer>
    <p>© 2026 · Dr. David Lazo Pérez · Cirujano Torácico · Santiago, Chile</p>
    <div class="footer-links">
      <a href="https://cirugiatoracica.cl">cirugiatoracica.cl</a>
      <a href="https://cancerpulmonar.cl">cancerpulmonar.cl</a>
      <a href="https://broncoscopia.cl">broncoscopia.cl</a>
      <a href="https://videotoracoscopia.cl">videotoracoscopia.cl</a>
      <a href="https://hiperhidrosis.cl">hiperhidrosis.cl</a>
    </div>
  </footer>
  <div class="maqueta-banner">MAQUETA · no publicada</div>
''' + SCRIPTS + '</body>\n</html>\n'
    doc = doc.replace("url('imgs/", "url('"+IMG).replace('src="imgs/', 'src="'+IMG).replace('poster="imgs/', 'poster="'+IMG).replace('data-src="imgs/', 'data-src="'+IMG)
    doc = doc.replace('local-imgs/', 'imgs/')
    if MAQUETA:  # enlaces relativos .html para revisar en local; en producción (cleanUrls) van sin extensión
        for k,_ in NAV_ITEMS:
            doc = doc.replace(f'href="{BASE}/{k}"', f'href="{k}.html"')
        doc = doc.replace(f'href="{BASE}#', 'href="index.html#').replace(f'href="{BASE}"', 'href="index.html"')
    open(OUT + fname, 'w', encoding='utf-8').write(doc)
    words = len(re.sub(r'<[^>]+>', ' ', re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', doc, flags=re.S)).split())
    print(fname, len(doc), 'bytes', words, 'palabras')

exec(open('/tmp/claude-0/-home-claude/7e55ec31-f280-5494-b928-ae7e5af92107/scratchpad/content_operculo.py', encoding='utf-8').read())
