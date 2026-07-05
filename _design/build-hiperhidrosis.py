#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador estático de hiperhidrosis.cl (design system v2).

Regenera dist/hiperhidrosis/ completo: 16 páginas (slugs idénticos al sitio
WordPress original), sitemap.xml y robots.txt. El contenido médico proviene
del sitio en producción; el diseño, de la maqueta Claude Design
(_design/hiperhidrosis-home-v2.html).

Uso:  python3 _design/build-hiperhidrosis.py
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "hiperhidrosis"
BASE = "https://hiperhidrosis.cl"

# ---- Datos de contacto de la red -------------------------------------------------
CLC_URL = "https://reserva.clinicalascondes.cl/AgendaWeb/reserva-horas?nombre=DAVID%20RENE&apellidoPat=LAZO&apellidoMat=PEREZ"
ENCUADRADO_URL = "https://encuadrado.com/p/david-lazo-perez/"
INSTAGRAM = "https://www.instagram.com/hiperhidrosis.cl/"
FACEBOOK = "https://www.facebook.com/hiperhidrosis.cl/"
CIRUGIATORACICA = "https://cirugiatoracica.cl"

# ---- JSON-LD compartido -----------------------------------------------------------
PHYSICIAN = {
    "@type": "Physician",
    "@id": f"{BASE}/#physician",
    "name": "Dr. David Lazo",
    "image": f"{BASE}/assets/foto-dr-lazo-bio.jpg",
    "medicalSpecialty": "https://schema.org/Surgical",
    "description": "Cirujano torácico especialista en hiperhidrosis y rubor facial patológico (eritrofobia). Médico-Cirujano de la Pontificia Universidad Católica de Chile, especialista en Cirugía General y Cirugía Torácica de la Universidad de Chile.",
    "affiliation": [
        {"@type": "MedicalOrganization", "name": "Clínica Las Condes"},
        {"@type": "MedicalOrganization", "name": "Hospital Clínico San Borja Arriarán"},
    ],
    "url": CIRUGIATORACICA,
    "sameAs": [CIRUGIATORACICA, ENCUADRADO_URL, INSTAGRAM, FACEBOOK,
               "https://www.linkedin.com/in/david-lazo-p%C3%A9rez-7b194748/",
               "https://www.instagram.com/dr.david.lazo.p/",
               "https://www.doctoralia.cl/david-rene-lazo-perez-3/cirujano-toracico-cirujano-general/santiago"],
}
ORG = {
    "@type": "Organization",
    "@id": f"{BASE}/#org",
    "name": "Hiperhidrosis.cl",
    "url": f"{BASE}/",
    "logo": {"@type": "ImageObject", "url": f"{BASE}/assets/logo-hd.png"},
}
WEBSITE = {
    "@type": "WebSite",
    "@id": f"{BASE}/#website",
    "name": "Hiperhidrosis.cl",
    "url": f"{BASE}/",
    "inLanguage": "es",
    "publisher": {"@id": f"{BASE}/#org"},
}
CONDITION = {
    "@type": "MedicalCondition",
    "@id": f"{BASE}/#hiperhidrosis",
    "name": "Hiperhidrosis",
    "alternateName": "Sudoración excesiva",
    "description": "Trastorno producido por la sobreestimulación del sistema nervioso simpático que provoca un aumento de la sudoración, especialmente en cara, axilas, manos y pies.",
}


def jsonld(*nodes):
    graph = [WEBSITE, ORG, PHYSICIAN, CONDITION] + list(nodes)
    doc = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">'
            + json.dumps(doc, ensure_ascii=False, separators=(",", ":"))
            + "</script>")


def medical_page(url, name, desc):
    return {
        "@type": "MedicalWebPage",
        "@id": url + "#webpage",
        "url": url,
        "name": name,
        "description": desc,
        "inLanguage": "es",
        "isPartOf": {"@id": f"{BASE}/#website"},
        "about": {"@id": f"{BASE}/#hiperhidrosis"},
        "reviewedBy": {"@id": f"{BASE}/#physician"},
    }


# ---- Chrome compartido -------------------------------------------------------------
def head(title, desc, path, ogimage="assets/logo-hd.png", ogtype="website", extra_jsonld=""):
    canonical = BASE + path
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canonical}">
  <meta property="og:locale" content="es_CL">
  <meta property="og:type" content="{ogtype}">
  <meta property="og:site_name" content="Hiperhidrosis.cl">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{BASE}/{ogimage}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{BASE}/{ogimage}">
  <link rel="icon" href="/assets/logo-footer.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/site.css">
  <script src="/assets/nav.js" defer></script>
  {extra_jsonld}
</head>
<body>
"""


TRATAMIENTOS_LINKS = """
        <li><a href="/hiperhidrosis-localizada-leve">Hiperhidrosis localizada leve</a></li>
        <li><a href="/hiperhidrosis-localizada-moderada">Hiperhidrosis localizada moderada</a></li>
        <li><a href="/hiperhidrosis-localizada-severa">Hiperhidrosis localizada severa</a></li>
        <li><a href="/rubor-facial-patologico">Rubor facial patológico</a></li>"""

NAV = f"""<nav class="site-nav">
  <a href="/" class="site-nav__logo" aria-label="Hiperhidrosis.cl — Inicio">
    <img src="/assets/logo-hd.png" alt="Hiperhidrosis.cl" width="333" height="201">
  </a>
  <div class="site-nav__links desk-nav">
    <a href="/sobre-la-hiperhidrosis" class="navlink-d">¿Qué es?</a>
    <div class="nav-drop">
      <button type="button" class="navlink-d nav-drop__btn" aria-haspopup="true" aria-expanded="false" aria-controls="drop-tratamientos">Tratamientos<span class="nav-drop__caret" aria-hidden="true">▾</span></button>
      <ul class="nav-drop__menu" id="drop-tratamientos">{TRATAMIENTOS_LINKS}
      </ul>
    </div>
    <a href="/cirugia-hiperhidrosis" class="navlink-d">Cirugía</a>
    <a href="/test-nivel-de-severidad" class="navlink-d">Test</a>
    <a href="/blog" class="navlink-d">Blog</a>
    <a href="#contacto" class="btn-pill cta-btn">Agendar hora<span class="arrow">→</span></a>
  </div>
  <button type="button" class="nav-burger" aria-haspopup="true" aria-expanded="false" aria-controls="mobile-nav" aria-label="Abrir menú">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="mobile-nav" id="mobile-nav" hidden>
  <a href="/sobre-la-hiperhidrosis">¿Qué es?</a>
  <div class="mnav-drop">
    <button type="button" class="mnav-drop__btn" aria-haspopup="true" aria-expanded="false" aria-controls="mdrop-tratamientos">Tratamientos<span class="nav-drop__caret" aria-hidden="true">▾</span></button>
    <ul class="mnav-drop__menu" id="mdrop-tratamientos" hidden>{TRATAMIENTOS_LINKS}
    </ul>
  </div>
  <a href="/cirugia-hiperhidrosis">Cirugía</a>
  <a href="/test-nivel-de-severidad">Test</a>
  <a href="/blog">Blog</a>
  <a href="#contacto" class="btn-pill cta-btn mobile-nav__cta">Agendar hora<span class="arrow">→</span></a>
</div>
"""

LINKEDIN = "https://www.linkedin.com/in/david-lazo-p%C3%A9rez-7b194748/"
INSTAGRAM_DR = "https://www.instagram.com/dr.david.lazo.p/"
DOCTORALIA = "https://www.doctoralia.cl/david-rene-lazo-perez-3/cirujano-toracico-cirujano-general/santiago"

# Bloque de contacto estándar de la red (estructura idéntica a dist/rats/ y
# dist/cirugiatoracica/), adaptado visualmente al design system de hiperhidrosis.
CONTACT = f"""<!-- ===== CONTACTO (bloque estándar de la red, ref: dist/rats/) ===== -->
<section class="cta-unified" id="contacto">
  <p class="cta-eyebrow">Primer paso</p>
  <h2 class="cta-title">Hable directamente<br>con el especialista</h2>
  <div class="cta-contact-grid">
    <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;gap:0.75rem;padding:1.5rem;">
      <img alt="Dr. David Lazo Pérez, Cirujano Torácico especialista en hiperhidrosis" loading="lazy" src="/assets/foto-dr-lazo-bio.jpg" width="800" height="800" style="width:120px;height:120px;border-radius:50%;object-fit:cover;object-position:center 10%;border:3px solid rgba(255,255,255,0.2);margin:0;">
      <div style="text-align:center;">
        <p style="font-size:0.88rem;font-weight:700;color:#fff;margin:0 0 0.2rem;">Dr. David Lazo Pérez</p>
        <p style="font-size:0.75rem;color:rgba(255,255,255,0.55);margin:0;">Cirujano Torácico</p>
      </div>
    </div>
    <div class="contact-card">
      <h4>🗓️ Agendar consulta</h4>
      <div class="ccontact-links">
        <a class="ccontact-link" href="{CLC_URL}" rel="noopener" target="_blank">
          <span class="ccontact-ico">🏥</span>
          <div><span class="ccontact-label">Clínica Las Condes</span><span class="ccontact-val">Reservar hora presencial →</span></div>
        </a>
        <a class="ccontact-link" href="{ENCUADRADO_URL}" rel="noopener" target="_blank">
          <span class="ccontact-ico">💻</span>
          <div><span class="ccontact-label">Telemedicina</span><span class="ccontact-val">Consulta online — todo Chile →</span></div>
        </a>
      </div>
    </div>
    <div class="contact-card">
      <h4>🌐 Redes sociales</h4>
      <div class="ccontact-links">
        <a class="ccontact-link" href="{LINKEDIN}" rel="noopener" target="_blank">
          <svg class="ccontact-ico" fill="currentColor" style="width:20px;height:20px;color:rgba(255,255,255,0.75);flex-shrink:0" viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect height="12" width="4" x="2" y="9"></rect><circle cx="4" cy="4" r="2"></circle></svg>
          <div><span class="ccontact-label">LinkedIn</span><span class="ccontact-val">Dr. David Lazo Pérez</span></div>
        </a>
        <a class="ccontact-link" href="{INSTAGRAM_DR}" rel="noopener" target="_blank">
          <svg class="ccontact-ico" fill="none" stroke="currentColor" stroke-width="2" style="width:20px;height:20px;color:rgba(255,255,255,0.75);flex-shrink:0" viewBox="0 0 24 24"><rect height="20" rx="5" ry="5" width="20" x="2" y="2"></rect><circle cx="12" cy="12" r="4"></circle><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line></svg>
          <div><span class="ccontact-label">Instagram</span><span class="ccontact-val">@dr.david.lazo.p</span></div>
        </a>
        <a class="ccontact-link" href="{DOCTORALIA}" rel="noopener" target="_blank">
          <svg class="ccontact-ico" fill="currentColor" style="width:20px;height:20px;color:rgba(255,255,255,0.75);flex-shrink:0" viewBox="0 0 24 24"><path d="M12 2a5 5 0 1 1 0 10A5 5 0 0 1 12 2zm0 12c5.523 0 10 2.239 10 5v1H2v-1c0-2.761 4.477-5 10-5z"></path></svg>
          <div><span class="ccontact-label">Doctoralia</span><span class="ccontact-val">Ver perfil y reseñas →</span></div>
        </a>
      </div>
    </div>
  </div>
</section>
"""

FOOTER = f"""<footer class="site-footer">
  <div class="footer-grid">
    <div>
      <img src="/assets/logo-footer.png" alt="Hiperhidrosis.cl" class="site-footer__logo" width="194" height="142" loading="lazy">
      <p class="site-footer__blurb">Portal de información sobre la sudoración excesiva y sus tratamientos en Chile. Dr. David Lazo, cirujano torácico — Clínica Las Condes.</p>
    </div>
    <div>
      <div class="footer-col__title">Navegación</div>
      <div class="footer-col__links">
        <a href="/sobre-la-hiperhidrosis" class="flink">¿Qué es la hiperhidrosis?</a>
        <a href="/#tratamientos" class="flink">Tratamientos</a>
        <a href="/cirugia-hiperhidrosis" class="flink">Cirugía</a>
        <a href="/rubor-facial-patologico" class="flink">Rubor facial patológico</a>
        <a href="/test-nivel-de-severidad" class="flink">Test de severidad</a>
        <a href="/blog" class="flink">Blog</a>
      </div>
    </div>
    <div>
      <div class="footer-col__title">Contacto</div>
      <div class="footer-col__links">
        <a href="{CLC_URL}" class="flink" target="_blank" rel="noopener">Agenda Clínica Las Condes</a>
        <a href="{ENCUADRADO_URL}" class="flink" target="_blank" rel="noopener">Agenda Encuadrado</a>
        <a href="{INSTAGRAM}" class="flink" target="_blank" rel="noopener">Instagram</a>
        <a href="{FACEBOOK}" class="flink" target="_blank" rel="noopener">Facebook</a>
      </div>
    </div>
  </div>
  <div class="site-footer__legal">© 2026 Hiperhidrosis.cl · Esta información es orientativa y no reemplaza una consulta médica. · Sitio del equipo: <a href="{CIRUGIATORACICA}" target="_blank" rel="noopener">cirugiatoracica.cl</a></div>
</footer>
"""


def subpage_hero(eyebrow, h1, lede="", meta=""):
    lede_html = f'\n    <p class="lede">{lede}</p>' if lede else ""
    meta_html = f'\n    <p class="meta">{meta}</p>' if meta else ""
    return f"""<header class="page-hero">
  <div class="page-hero__inner">
    <span class="eyebrow">{eyebrow}</span>
    <h1>{h1}</h1>{lede_html}{meta_html}
  </div>
</header>
"""


def write_page(path, html):
    """path: '' para home, 'slug' o '2020/08/30/slug' para el resto."""
    d = OUT / path if path else OUT
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(html, encoding="utf-8")
    print(f"  {('/' + path) if path else '/'}")


def page(path, title, desc, hero, body, ld_nodes, ogimage="assets/logo-hd.png",
         ogtype="website", scripts=""):
    url = BASE + ("/" + path if path else "/")
    html = (head(title, desc, ("/" + path if path else "/"), ogimage, ogtype, jsonld(*ld_nodes))
            + NAV + hero + body + CONTACT + FOOTER + scripts + "</body>\n</html>\n")
    write_page(path, html)
    return url


# =====================================================================================
# HOME
# =====================================================================================
def build_home():
    title = "Hiperhidrosis.cl — La sudoración excesiva tiene tratamiento"
    desc = ("Portal de información sobre la hiperhidrosis (sudoración excesiva) y sus tratamientos en Chile: "
            "antitranspirantes, Botox, iontoforesis y cirugía. Dr. David Lazo, cirujano torácico.")
    hero = """<!-- ===== HERO · Full-bleed dramático (maqueta 1a) ===== -->
<header id="top" class="hero-full">
""" + NAV + """
  <div class="hero-full__stage" data-slideshow>
    <div class="hero-slides">
      <img class="is-active" src="/assets/zona-palmar.jpg" alt="Sudoración palmar" width="1280" height="500" fetchpriority="high">
      <img src="/assets/zona-axilar.jpg" alt="Sudoración axilar" width="1280" height="500">
      <img src="/assets/zona-facial.jpg" alt="Sudoración craneofacial" width="1280" height="500">
    </div>
    <div class="hero-dots">
      <button class="is-active" type="button" aria-label="Sudoración palmar"></button>
      <button type="button" aria-label="Sudoración axilar"></button>
      <button type="button" aria-label="Sudoración craneofacial"></button>
    </div>
    <div class="hero-content">
      <div class="hero-copy">
        <div class="hero-copy__glow"></div>
        <h1>La Sudoración Excesiva<br><em><span>tiene tratamiento.</span></em></h1>
        <p>Manos, axilas, pies o rostro que transpiran sin control. Conoce las causas y las alternativas reales para recuperar tu vida diaria.</p>
        <div class="hero-copy__actions">
          <a href="#contacto" class="cta-btn">Agenda tu hora médica<span class="arrow">→</span></a>
        </div>
      </div>
    </div>
  </div>
</header>
"""
    body = """<!-- ===== ¿QUÉ ES? ===== -->
<section id="que-es" class="quees-section">
  <div class="quees">
    <div class="quees__media">
      <img src="/assets/localizada.jpg" alt="Hiperhidrosis localizada" width="1920" height="800" loading="lazy">
    </div>
    <div>
      <span class="eyebrow">Entender la condición</span>
      <h2>¿Qué es la hiperhidrosis?</h2>
      <p>Es un trastorno producido por la <strong>sobreestimulación del sistema nervioso simpático</strong>, parte del sistema nervioso autónomo que comanda las funciones no conscientes del organismo. Esto provoca un aumento de la sudoración, especialmente en <strong>cara, axilas, manos y pies</strong>.</p>
      <p>No depende del calor ni del esfuerzo físico, y puede afectar de forma importante la vida social, laboral y emocional de quien la padece. <a href="/sobre-la-hiperhidrosis" class="navlink" style="font-weight:600;color:#2C8C9E">Conoce más sobre la hiperhidrosis →</a></p>
      <div class="quees__facts">
        <div class="fact-card">
          <div class="fact-card__title">Primaria</div>
          <div class="fact-card__body">Localizada y sin causa aparente; suele iniciar en la infancia o adolescencia.</div>
        </div>
        <div class="fact-card">
          <div class="fact-card__title">Secundaria</div>
          <div class="fact-card__body">Asociada a otra condición o medicamento; puede afectar todo el cuerpo.</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ===== TEST DE SEVERIDAD ===== -->
<section id="test" class="test-section">
  <div class="test-band">
    <div class="test-band__copy">
      <span class="eyebrow">Autoevaluación</span>
      <h2>Test de nivel de severidad</h2>
      <p>Responde unas breves preguntas y conoce qué tan severa es tu sudoración. Una orientación inicial antes de tu consulta.</p>
    </div>
    <a href="/test-nivel-de-severidad" class="btn-navy cta-btn">Hacer el test<span class="arrow">→</span></a>
  </div>
</section>

<!-- ===== TRATAMIENTOS ===== -->
<section id="tratamientos" class="navy-section">
  <div class="navy-panel">
    <div class="navy-panel__head">
      <span class="eyebrow">Alternativas reales</span>
      <h2>Tratamientos disponibles</h2>
      <p>Existen numerosas alternativas, desde desodorantes especiales hasta la cirugía. La elección depende de la localización y la severidad de cada caso.</p>
    </div>
    <div class="sev-list">
      <!-- Leve -->
      <div class="sev-row">
        <div class="sev-label">
          <div class="sev-label__kicker">Hiperhidrosis</div>
          <div class="sev-label__level">Leve</div>
        </div>
        <svg class="sev-brace" viewBox="0 0 20 100" preserveAspectRatio="none" aria-hidden="true"><path d="M15 3 C7 3 11 28 3 50 C11 72 7 97 15 97" fill="none" stroke="rgba(127,208,220,.9)" stroke-width="2" vector-effect="non-scaling-stroke" stroke-linecap="round"></path></svg>
        <div class="sev-items">
          <a class="trat" href="/hiperhidrosis-localizada-leve">
            <h3>Antitranspirantes médicos</h3>
            <p>Soluciones tópicas de primera línea para casos leves.</p>
          </a>
        </div>
      </div>
      <!-- Moderada -->
      <div class="sev-row">
        <div class="sev-label">
          <div class="sev-label__kicker">Hiperhidrosis</div>
          <div class="sev-label__level">Moderada</div>
        </div>
        <svg class="sev-brace" viewBox="0 0 20 100" preserveAspectRatio="none" aria-hidden="true"><path d="M15 3 C7 3 11 28 3 50 C11 72 7 97 15 97" fill="none" stroke="rgba(127,208,220,.9)" stroke-width="2" vector-effect="non-scaling-stroke" stroke-linecap="round"></path></svg>
        <div class="trat-grid">
          <a class="trat" href="/hiperhidrosis-localizada-moderada">
            <h3>Toxina botulínica</h3>
            <p>Bloquea la señal que activa las glándulas; muy eficaz en axilas y manos.</p>
          </a>
          <a class="trat" href="/hiperhidrosis-localizada-moderada">
            <h3>Iontoforesis</h3>
            <p>Corriente suave a través del agua, ideal para manos y pies.</p>
          </a>
          <a class="trat" href="/hiperhidrosis-localizada-moderada">
            <h3>Medicación oral</h3>
            <p>Anticolinérgicos para casos generalizados, siempre supervisados.</p>
          </a>
        </div>
      </div>
      <!-- Severa -->
      <div class="sev-row">
        <div class="sev-label">
          <div class="sev-label__kicker">Hiperhidrosis</div>
          <div class="sev-label__level">Severa</div>
        </div>
        <svg class="sev-brace" viewBox="0 0 20 100" preserveAspectRatio="none" aria-hidden="true"><path d="M15 3 C7 3 11 28 3 50 C11 72 7 97 15 97" fill="none" stroke="rgba(127,208,220,.9)" stroke-width="2" vector-effect="non-scaling-stroke" stroke-linecap="round"></path></svg>
        <div class="sev-items">
          <a class="trat" href="/cirugia-hiperhidrosis">
            <h3>Cirugía · Simpatectomía</h3>
            <p>Opción definitiva para casos severos seleccionados.</p>
          </a>
        </div>
      </div>
      <a href="#contacto" class="trat trat-cta">
        <div>
          <h3>¿Cuál es para ti?</h3>
          <p>La severidad y la zona definen el tratamiento. Agenda una evaluación y definamos tu plan.</p>
        </div>
        <span class="trat-cta__go">Agendar →</span>
      </a>
    </div>
  </div>
</section>

<!-- ===== BLOG ===== -->
<section id="blog" class="blog-section">
  <div class="wrap">
    <div class="blog-head">
      <div>
        <span class="eyebrow">Recursos</span>
        <h2>Desde el blog</h2>
      </div>
      <a href="/blog" class="blog-head__all navlink">Ver todos los artículos →</a>
    </div>
    <div class="blog-grid">
      <a href="/2021/02/19/enfermedades-asociadas-a-la-hiperhidrosis" class="post">
        <div class="post__imgwrap"><img class="pimg" src="/assets/thumb-enfermedades.jpg" alt="Enfermedades asociadas a la hiperhidrosis" width="400" height="250" loading="lazy"></div>
        <div class="post__body"><span class="post__cat">Causas</span><h3 class="post__title">Enfermedades asociadas a la hiperhidrosis</h3></div>
      </a>
      <a href="/2021/01/18/hiperhidrosis-y-sus-consecuencias-en-la-salud-mental" class="post">
        <div class="post__imgwrap"><img class="pimg" src="/assets/thumb-salud-mental.jpg" alt="Hiperhidrosis y salud mental" width="400" height="250" loading="lazy"></div>
        <div class="post__body"><span class="post__cat">Salud mental</span><h3 class="post__title">Hiperhidrosis y sus consecuencias en la salud mental</h3></div>
      </a>
      <a href="/2021/01/12/por-que-me-sudan-tanto-los-pies" class="post">
        <div class="post__imgwrap"><img class="pimg" src="/assets/thumb-pies.jpg" alt="Hiperhidrosis plantar" width="400" height="250" loading="lazy"></div>
        <div class="post__body"><span class="post__cat">Pies</span><h3 class="post__title">¿Por qué me sudan tanto los pies?</h3></div>
      </a>
    </div>
  </div>
</section>
"""
    node = medical_page(BASE + "/", title, desc)
    url = BASE + "/"
    html = (head(title, desc, "/", "assets/zona-palmar.jpg", "website", jsonld(node))
            + hero + body + CONTACT + FOOTER
            + '<script src="/assets/home.js" defer></script>\n</body>\n</html>\n')
    write_page("", html)


# =====================================================================================
# SOBRE LA HIPERHIDROSIS
# =====================================================================================
def build_sobre():
    path = "sobre-la-hiperhidrosis"
    title = "¿Qué es la hiperhidrosis? Causas, tipos y consecuencias | Hiperhidrosis.cl"
    desc = ("La hiperhidrosis es la sudoración excesiva producida por la sobreestimulación del sistema nervioso "
            "simpático. Conoce por qué sudamos, sus consecuencias y los tipos: localizada (primaria) y generalizada (secundaria).")
    hero = subpage_hero("Entender la condición", "Sobre la hiperhidrosis",
                        "La hiperhidrosis es un trastorno producido por la sobreestimulación del sistema nervioso simpático (que junto al sistema parasimpático forman el sistema nervioso autónomo, que comanda todas las funciones no conscientes del organismo), produciéndose un aumento de la sudoración de todo el organismo, en especial de cara, axila, manos, y pies.")
    body = f"""<section class="prose-section">
  <div class="prose">
    <h2 id="por-que-sudamos">¿Por qué sudamos?</h2>
    <div class="media-split media-split--img-right">
      <div class="media-split__body">
        <p>El sudor es una de las formas que emplea el organismo para controlar su temperatura, proceso que se denomina <strong>termorregulación</strong> y que es controlado por la corteza cerebral y el hipotálamo, los cuales comandan todos los procesos ligados a la producción y eliminación del calor corporal.</p>
        <p>Normalmente, cuando aumenta la temperatura corporal, estas estructuras envían impulsos eléctricos a través de los nervios simpáticos hasta las glándulas sudoríparas para que produzcan sudor, el cual al evaporarse en la superficie de la piel, disminuye la temperatura del organismo. Para esto, el cuerpo humano posee entre <strong>2 a 4 millones de glándulas sudoríparas</strong>, las cuales se encuentran distribuidas de forma heterogénea, concentrándose principalmente en las palmas de las manos, cara, axilas y plantas de los pies.</p>
      </div>
      <figure class="img-card media-split__media">
        <img src="/assets/por-que-sudamos.jpg" alt="Persona con sudoración tras ejercicio físico — termorregulación corporal" width="900" height="682" loading="lazy">
      </figure>
    </div>

    <h2 id="consecuencias-hiperhidrosis">¿Cuáles son las consecuencias de la hiperhidrosis?</h2>
    <p>Este trastorno no solo produce las consecuencias propias de la hipersudoración, sino también:</p>
    <ul>
      <li><strong>Trastornos cutáneos:</strong> maceración de la piel, aumento en la frecuencia de infecciones bacterianas y por hongos, mal olor (bromhidrosis).</li>
      <li><strong>Trastornos psicológicos:</strong> las alteraciones sociales que conlleva el tener que cambiarse de camisa o blusa numerosas veces durante el día, la vergüenza de extender la mano, acariciar a otro con la mano húmeda, el humedecer los libros, papeles o billetes que se tocan, etc., producen un sinnúmero de alteraciones psicológicas que dificultan enormemente la vida emocional, laboral y familiar de la persona aquejada de hiperhidrosis.</li>
    </ul>
    <p>Puedes profundizar en este tema en nuestro artículo sobre <a href="/2021/01/18/hiperhidrosis-y-sus-consecuencias-en-la-salud-mental">hiperhidrosis y salud mental</a>.</p>

    <h2 id="tipos-hiperhidrosis">Tipos de hiperhidrosis</h2>

    <h3>Hiperhidrosis localizada o primaria</h3>
    <div class="media-split">
      <figure class="img-card media-split__media">
        <img src="/assets/foto-palmar.jpg" alt="Hiperhidrosis localizada: palma de la mano con sudoración excesiva" width="414" height="325" loading="lazy">
      </figure>
      <div class="media-split__body">
        <p>Es la forma más frecuentemente observada, afectando al <strong>2-3% de la población general</strong>, a hombres y mujeres por igual. Este trastorno no se debe a una enfermedad, sino a un trastorno “primario” (sin una causa aparente) de la regulación del sistema nervioso autónomo. Se cree que existe una sobreestimulación de las estructuras cerebrales que controlan la producción de sudor (corteza cerebral e hipotálamo), que a través de los nervios simpáticos, le ordenan a las glándulas sudoríparas aumentar la excreción de sudor <strong>hasta 40 veces lo normal</strong> para una persona.</p>
      </div>
    </div>
    <p>La hiperhidrosis primaria se presenta desde temprano en la infancia, aumentando severamente en la pubertad, para luego disminuir en la adultez tardía. Entre un 25-50% de los pacientes poseen historia familiar de hiperhidrosis. La hipersudoración ocurre en forma espontánea e intermitente y se acentúa en situaciones de estrés emocional y con altas temperaturas, a su vez que desaparece durante el sueño. El término “localizada” se emplea ya que habitualmente, este tipo de hiperhidrosis afecta zonas determinadas del cuerpo:</p>
    <ul>
      <li>Cara</li>
      <li>Axilas</li>
      <li>Palmas de las manos</li>
      <li>Plantas de los pies</li>
    </ul>
    <p>En este tipo de hiperhidrosis es en el cual se concentran los tratamientos, tanto dermatológicos como quirúrgicos, según su severidad: <a href="/hiperhidrosis-localizada-leve">leve</a>, <a href="/hiperhidrosis-localizada-moderada">moderada</a> o <a href="/hiperhidrosis-localizada-severa">severa</a>.</p>

    <h3>Hiperhidrosis generalizada o secundaria</h3>
    <figure class="img-card">
      <img src="/assets/tipos-secundaria.jpg" alt="Hiperhidrosis generalizada o secundaria" width="1920" height="800" loading="lazy">
    </figure>
    <p>En este tipo, la hipersudoración habitualmente no tiene una causa identificable, pero como su nombre lo dice, puede también ser consecuencia de una condición patológica, entre las que se cuentan:</p>
    <ul>
      <li>Infecciones</li>
      <li>Tumores</li>
      <li>Trastornos hormonales</li>
      <li>Trastornos neurológicos</li>
      <li>Enfermedades cardiovasculares y del aparato respiratorio</li>
      <li>Secundario a medicamentos</li>
    </ul>
    <p>El gran desafío de este tipo de hiperhidrosis consiste en descubrir cuál es su causa, para lo cual se debe consultar con un especialista para realizar toda la serie de estudios de laboratorio e imágenes necesarios. Obviamente su tratamiento corresponderá al de la enfermedad que lo produce. Revisa el listado de <a href="/2021/02/19/enfermedades-asociadas-a-la-hiperhidrosis">enfermedades asociadas a la hiperhidrosis</a>.</p>

  </div>
</section>

<section class="test-section" style="padding-bottom:40px">
  <div class="test-band">
    <div class="test-band__copy">
      <span class="eyebrow">Autoevaluación</span>
      <h2>¿Qué tan severa es tu sudoración?</h2>
      <p>Responde el test de severidad y orienta tu próxima consulta.</p>
    </div>
    <a href="/test-nivel-de-severidad" class="btn-navy cta-btn">Hacer el test<span class="arrow">→</span></a>
  </div>
</section>
"""
    url = BASE + "/" + path
    page(path, title, desc, hero, body,
         [medical_page(url, title, desc)], ogimage="assets/foto-palmar.jpg")


# =====================================================================================
# GRADOS DE SEVERIDAD (leve / moderada / severa)
# =====================================================================================
def build_leve():
    path = "hiperhidrosis-localizada-leve"
    title = "Hiperhidrosis localizada leve: antitranspirantes médicos | Hiperhidrosis.cl"
    desc = ("Tratamiento de la hiperhidrosis leve: desodorantes y cremas en base a cloruro de aluminio indicados "
            "por dermatólogo, con hasta un 98% de efectividad en este grado de severidad.")
    hero = subpage_hero("Grados de severidad", "Hiperhidrosis localizada leve")
    body = """<section class="prose-section">
  <div class="prose">
    <p>El tratamiento de la <strong>hiperhidrosis leve</strong> recae en el dermatólogo, quien luego de una minuciosa evaluación, habitualmente recomienda el uso de <strong>desodorantes y cremas especiales en base a cloruro de aluminio</strong>, los que se encuentran ampliamente en el mercado.</p>
    <p>Estos se supone que actúan a nivel de los conductos glandulares, obstruyéndolos y promoviendo la atrofia de las células secretoras. Requiere de aplicaciones seriadas nocturnas y tienen hasta un <strong>98% de efectividad</strong> a este grado de severidad de hiperhidrosis.</p>
    <p>Su principal efecto secundario es la <strong>irritación de la zona tratada</strong>, lo que habitualmente motiva la descontinuación de su uso.</p>
    <div class="img-row">
      <div class="prod"><img src="/assets/trat-xerac.jpg" alt="Solución antitranspirante Xerac AC 35 ml" width="1000" height="1000" loading="lazy"></div>
      <div class="prod"><img src="/assets/trat-antitranspirante.png" alt="Antitranspirante médico en base a cloruro de aluminio" width="1000" height="1100" loading="lazy"></div>
      <div class="prod"><img src="/assets/trat-drysol.jpg" alt="Drysol desodorante en spray 35 ml" width="1000" height="1000" loading="lazy"></div>
    </div>
    <p>Si los antitranspirantes médicos no logran controlar tu sudoración, revisa las alternativas para la <a href="/hiperhidrosis-localizada-moderada">hiperhidrosis moderada</a> o realiza nuestro <a href="/test-nivel-de-severidad">test de severidad</a>.</p>
  </div>
</section>
"""
    url = BASE + "/" + path
    therapy = {
        "@type": "MedicalTherapy",
        "name": "Antitranspirantes médicos (cloruro de aluminio)",
        "description": "Desodorantes y cremas en base a cloruro de aluminio para hiperhidrosis leve; aplicaciones seriadas nocturnas con hasta un 98% de efectividad.",
        "recognizingAuthority": {"@id": f"{BASE}/#physician"},
    }
    page(path, title, desc, hero, body,
         [medical_page(url, title, desc), therapy], ogimage="assets/trat-xerac.jpg")


def build_moderada():
    path = "hiperhidrosis-localizada-moderada"
    title = "Hiperhidrosis localizada moderada: iontoforesis, medicamentos y Botox | Hiperhidrosis.cl"
    desc = ("Tratamientos de la hiperhidrosis moderada indicados por dermatólogo: iontoforesis, medicamentos "
            "orales y toxina botulínica (Botox), según la localización de la hipersudoración.")
    hero = subpage_hero("Grados de severidad", "Hiperhidrosis localizada moderada",
                        "La hiperhidrosis moderada es resorte de tratamiento del dermatólogo, quien dependiendo de la localización de la hipersudoración, tiene a su disposición herramientas como las siguientes.")
    body = """<section class="prose-section">
  <div class="prose">
    <h2>Iontoforesis</h2>
    <p>Terapia consistente en la exposición de la superficie cutánea afectada a <strong>impulsos de corriente eléctrica de bajo voltaje</strong>. Se teoriza que su efecto se debe a la hiperqueratosis que se provoca a nivel del ducto ecrino y también al bloqueo del gradiente electroquímico glandular.</p>
    <p>Su aplicación es en sesiones en un inicio trisemanales, que se van espaciando en el tiempo dependiendo de la mejoría observada. Reduce hasta en un <strong>81% la sudoración palmar</strong> y sus principales efectos secundarios son eritema (enrojecimiento de la piel), dolor local y parestesias (sensación de hormigueo, entumecimiento, ardor o pérdida de la sensibilidad).</p>

    <h2>Medicamentos orales</h2>
    <p>Existen descritos en la literatura médica múltiples medicamentos que ayudan al tratamiento de la hiperhidrosis, entre los que se cuentan: <strong>anticolinérgicos, antidepresivos de varios tipos, ansiolíticos, betabloqueadores, bloqueadores de los canales de calcio</strong>, etc.</p>
    <p>Cualquiera de estos medicamentos debe ser indicado y controlado por un especialista, puesto que no están exentos de efectos secundarios y contraindicaciones, ya que son en su gran mayoría de uso de otras enfermedades que tienen efectos beneficiosos para los pacientes portadores de hiperhidrosis.</p>

    <h2>BOTOX (toxina botulínica)</h2>
    <p>Tratamiento consistente en la <strong>inyección subcutánea de toxina botulínica</strong> (ampliamente conocida por su uso en terapia cosmética), en las zonas con exceso de sudoración. Su uso se basa en el efecto de la toxina como bloqueador del estímulo nervioso que activa las glándulas sudoríparas.</p>
    <p>Tiene una <strong>efectividad del 90%</strong> en la reducción de un 50% de la sudoración axilar y una duración de <strong>3 a 7 meses</strong>, después de lo cual se debe repetir su inyección. <strong>No</strong> debe ser utilizada en niños ni embarazadas, y su uso en palmas y plantas es doloroso, por lo que se requiere generalmente de sedación durante el procedimiento.</p>

    <div class="img-row img-row--2">
      <div class="prod"><img src="/assets/trat-iontoforesis.jpg" alt="Equipo de iontoforesis para hiperhidrosis palmar y plantar" width="1500" height="1500" loading="lazy"></div>
      <div class="prod"><img src="/assets/trat-botox.jpg" alt="Toxina botulínica (Botox) para hiperhidrosis" width="700" height="525" loading="lazy"></div>
    </div>
    <p>Si estos tratamientos no logran resultados satisfactorios, conoce la alternativa para la <a href="/hiperhidrosis-localizada-severa">hiperhidrosis severa</a>: la <a href="/cirugia-hiperhidrosis">cirugía de la hiperhidrosis</a>.</p>
  </div>
</section>
"""
    url = BASE + "/" + path
    therapies = [
        {"@type": "MedicalTherapy", "name": "Iontoforesis",
         "description": "Exposición de la superficie cutánea afectada a impulsos de corriente eléctrica de bajo voltaje; reduce hasta en un 81% la sudoración palmar."},
        {"@type": "MedicalTherapy", "name": "Medicamentos orales",
         "description": "Anticolinérgicos, antidepresivos, ansiolíticos, betabloqueadores y bloqueadores de los canales de calcio, indicados y controlados por un especialista."},
        {"@type": "MedicalTherapy", "name": "Toxina botulínica (Botox)",
         "description": "Inyección subcutánea de toxina botulínica en las zonas con exceso de sudoración; efectividad del 90% en axilas, duración de 3 a 7 meses."},
    ]
    page(path, title, desc, hero, body,
         [medical_page(url, title, desc)] + therapies, ogimage="assets/trat-iontoforesis.jpg")


def build_severa():
    path = "hiperhidrosis-localizada-severa"
    title = "Hiperhidrosis localizada severa: tratamiento quirúrgico | Hiperhidrosis.cl"
    desc = ("La cirugía (simpatectomía por videotoracoscopía) es el tratamiento con mejores resultados para la "
            "hiperhidrosis severa: bloqueo permanente de los estímulos hacia las glándulas sudoríparas.")
    hero = subpage_hero("Grados de severidad", "Hiperhidrosis localizada severa")
    body = """<section class="prose-section">
  <div class="prose">
    <p>La <strong>cirugía es el tratamiento con mejores resultados</strong> disponible en la actualidad. Consiste en la <strong>simpatectomía o simpaticotomía</strong>, procedimiento en el que se seccionan las cadenas formadas por el nervio simpático por su paso a través del tórax con el fin de bloquear permanentemente los estímulos cerebrales hacia las glándulas sudoríparas.</p>
    <p>Esta técnica se realiza hoy en día por <strong>videotoracoscopía</strong> y su principal ventaja es la inmediata resolución de la hipersudoración. Conoce el detalle del procedimiento, sus resultados y efectos secundarios en <a href="/cirugia-hiperhidrosis">cirugía de la hiperhidrosis</a>.</p>
    <p>Para la <strong>hiperhidrosis plantar</strong> el tratamiento quirúrgico se encuentra en fase experimental y aún no disponible en nuestro país.</p>
  </div>
</section>
"""
    url = BASE + "/" + path
    proc = {
        "@type": "MedicalProcedure",
        "name": "Simpatectomía por videotoracoscopía",
        "procedureType": "https://schema.org/SurgicalProcedure",
        "description": "Sección de las cadenas del nervio simpático torácico para bloquear permanentemente los estímulos hacia las glándulas sudoríparas; indicada en hiperhidrosis severa.",
        "howPerformed": "Videotoracoscopía",
    }
    page(path, title, desc, hero, body,
         [medical_page(url, title, desc), proc])


# =====================================================================================
# CIRUGÍA
# =====================================================================================
def build_cirugia():
    path = "cirugia-hiperhidrosis"
    title = "Cirugía de la hiperhidrosis: simpatectomía por videotoracoscopía | Hiperhidrosis.cl"
    desc = ("Simpatectomía por videotoracoscopía: procedimiento, resultados (éxito superior al 95%), sudoración "
            "compensatoria, contraindicaciones, riesgos y complicaciones. Dr. David Lazo, cirujano torácico.")
    hero = subpage_hero("Tratamiento quirúrgico", "Cirugía de la hiperhidrosis",
                        "La cirugía de la hiperhidrosis consiste en la simpatectomía o simpaticotomía por videotoracoscopía.")
    body = f"""<section class="prose-section">
  <div class="prose">
    <h2>¿En qué consiste?</h2>
    <p>Este procedimiento consiste en la <strong>sección de las cadenas formadas por el nervio simpático torácico</strong>, entre los ganglios que éste posee sobre las 2ª a 4ª costillas (dependiendo de la zona afectada) y también de las posibles interconexiones nerviosas entre dichos ganglios, a ambos lados del tórax.</p>
    <p>Esta técnica es realizada por <a href="{CIRUGIATORACICA}" target="_blank" rel="noopener">nuestro equipo</a>, utilizando dos pequeñas incisiones a la altura de la axila: una de 3 mm y la otra de 3 ó 5 mm (dependiendo del tamaño del paciente). A través de estas pequeñas incisiones se introducen la cámara y los instrumentos quirúrgicos con los que se secciona la cadena simpática. Una vez seccionada la cadena simpática del lado derecho del paciente, se realiza la del lado izquierdo.</p>
    <p>La duración aproximada de la cirugía es de <strong>menos de una hora</strong>, requiere anestesia general y de <strong>un día de hospitalización</strong>. La reincorporación a la vida cotidiana es muy rápida y se lleva a cabo luego de 24 a 48 horas.</p>

    <figure class="img-card">
      <img src="/assets/cirugia.jpg" alt="Esquema de la simpatectomía por videotoracoscopía" width="600" height="1000" loading="lazy">
    </figure>

    <h2>Resultados</h2>
    <p>En general el éxito de esta operación es <strong>superior al 95%</strong>, dependiendo de la zona a tratar:</p>
    <ul>
      <li><strong>Hiperhidrosis palmar:</strong> 99%</li>
      <li><strong>Hiperhidrosis axilar y facial:</strong> 95-96%</li>
    </ul>

    <h2>Efectos secundarios</h2>
    <p>Su principal efecto secundario es la <a href="/2020/11/13/sudoracion-compensatoria-el-temido-efecto-secundario-de-la-simpatectomia"><strong>sudoración compensatoria</strong></a>, trastorno en el cual el organismo desvía el estímulo de la sudoración hacia zonas no intervenidas, como espalda, pecho, abdomen y piernas. Habitualmente se presenta como un aumento de la sudoración de las zonas antes mencionadas, que con el pasar de las semanas disminuye hasta pasar desapercibida.</p>
    <p>Este es un efecto que se observa frecuentemente de manera leve, sin embargo, esta puede ser severa en aproximadamente el <strong>1 al 8% de los casos</strong>. Es por este motivo que la indicación quirúrgica debe conversarse seria e informadamente entre cirujano y paciente, analizando los beneficios que otorga, versus el riesgo de la sudoración compensatoria.</p>

    <h2>Contraindicaciones de la cirugía</h2>
    <p>Estas son escasas y principalmente corresponden a pacientes que son portadores de: <strong>bradicardias extremas</strong> (ojo los deportistas de alto rendimiento), <strong>vagotonías y disautonomías con lipotimias frecuentes</strong>.</p>
    <p>Pese a que no es una contraindicación absoluta, los pacientes obesos deben tener en cuenta que tienen un alto riesgo de sudoración compensatoria, por lo que se sugiere fuertemente el posponer la intervención hasta lograr la mayor corrección de su IMC posible.</p>

    <h2>Riesgos y complicaciones</h2>
    <p>Como toda intervención quirúrgica, la simpatectomía por videotoracoscopía posee complicaciones, las cuales pese a ser extremadamente poco frecuentes, existen: <strong>hemorragia, infecciones, neumotórax, derrame pleural</strong> y muy rara vez <strong>Síndrome de Horner</strong> (caída transitoria y parcial de un párpado).</p>
  </div>
</section>
"""
    url = BASE + "/" + path
    proc = {
        "@type": "MedicalProcedure",
        "@id": url + "#procedure",
        "name": "Simpatectomía por videotoracoscopía",
        "procedureType": "https://schema.org/SurgicalProcedure",
        "description": desc,
        "howPerformed": "Dos incisiones de 3 y 5 mm a la altura de la axila por las que se introducen cámara e instrumentos para seccionar la cadena simpática torácica, a ambos lados del tórax. Duración menor a una hora, anestesia general y un día de hospitalización.",
        "followup": "Reincorporación a la vida cotidiana luego de 24 a 48 horas.",
        "seriousAdverseOutcome": {"@type": "MedicalEntity", "name": "Sudoración compensatoria"},
    }
    page(path, title, desc, hero, body,
         [medical_page(url, title, desc), proc], ogimage="assets/cirugia.jpg")


# =====================================================================================
# RUBOR FACIAL PATOLÓGICO
# =====================================================================================
RUBOR_FAQ = [
    ("¿Por qué se produce el rubor facial patológico?",
     "Este trastorno se origina por la sobreestimulación del sistema nervioso simpático (que junto al sistema parasimpático forman el sistema nervioso autónomo, que comanda todas las funciones no conscientes del organismo), que produce la dilatación de los vasos sanguíneos faciales y la estimulación de las glándulas sudoríparas de esta región."),
    ("¿Cómo se trata?",
     "El tratamiento recae en un equipo multidisciplinario que involucra a dermatólogos, psiquiatras y cirujanos torácicos. Dentro de las opciones terapéuticas se encuentran cremas y fármacos que atenúan los síntomas de esta enfermedad, tratamientos con antidepresivos, psicoterapia, terapia cognitivo-conductual y finalmente la cirugía."),
    ("¿En qué consiste la cirugía del rubor facial patológico?",
     "La cirugía del rubor facial patológico (reservada para casos que no responden a los tratamientos con fármacos) es similar a la de la hiperhidrosis y consiste en la simpatectomía videotoracoscópica, con la salvedad que el lugar de sección de la cadena simpática es más proximal (o más arriba), a nivel de la 2ª costilla (T2 o R2)."),
    ("¿Qué diferencias tiene la simpatectomía por videotoracoscopía de la hiperhidrosis con la que se realiza para el rubor facial patológico?",
     "La diferencia más importante entre estos dos procedimientos es que debido al ascenso en el nivel de corte en la cadena de los nervios simpáticos, existe una mayor probabilidad de que ocurran los efectos secundarios y complicaciones de la operación."),
]


def build_rubor():
    path = "rubor-facial-patologico"
    title = "Rubor facial patológico (eritrofobia): causas y tratamiento | Hiperhidrosis.cl"
    desc = ("El rubor facial patológico, eritrofobia o blushing es el enrojecimiento facial súbito frente a "
            "situaciones de estrés. Conoce por qué se produce, cómo se trata y en qué consiste su cirugía.")
    hero = subpage_hero("Otra cara de la condición", "Rubor facial patológico o eritrofobia",
                        "Se denomina rubor facial patológico, eritrofobia o blushing, al enrojecimiento facial súbito frente a situaciones de estrés, acompañado de la sensación de calor o bochorno, adormecimiento u hormigueo de la cara.")
    faq_html = "".join(
        f"""
    <h2>{q}</h2>
    <p>{a}</p>""" for q, a in RUBOR_FAQ)
    body = f"""<section class="prose-section">
  <div class="prose">
    <figure class="img-card">
      <img src="/assets/foto-rubor.jpg" alt="Rubor facial patológico o eritrofobia" width="1920" height="800" loading="lazy">
    </figure>
    <p>Esta afección se encuentra comúnmente en la población, siendo objeto de múltiples trastornos sociales para las personas que lo padecen, pudiendo llegar incluso a provocar cuadros psiquiátricos de difícil manejo, como alteraciones del ánimo, fobias y conductas aberrantes.</p>
    {faq_html}
    <p>¿Tu caso se acompaña de sudoración excesiva? Revisa también los <a href="/#tratamientos">tratamientos de la hiperhidrosis</a> y el detalle de la <a href="/cirugia-hiperhidrosis">cirugía</a>.</p>
  </div>
</section>
"""
    url = BASE + "/" + path
    faq_node = {
        "@type": "FAQPage",
        "@id": url + "#faq",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in RUBOR_FAQ
        ],
    }
    page(path, title, desc, hero, body,
         [medical_page(url, title, desc), faq_node], ogimage="assets/foto-rubor.jpg")


# =====================================================================================
# TEST DE SEVERIDAD
# =====================================================================================
QUIZ_QUESTIONS = [
    "Sensación de vergüenza asociada a la ropa o palmas húmedas.",
    "Necesidad de cambio de ropa dos o más veces al día.",
    "¿Evitas saludar con la mano?",
    "Frustración en las actividades diarias a causa de la sudoración.",
    "¿Evitas encuentros sociales con amigos o familia?",
    "Cambio en el tipo de actividades recreativas.",
    "Depresión y baja autoestima.",
    "Infecciones, bacterias o hongos por la piel macerada.",
    "Dificultad para establecer relaciones sociales e íntimas.",
    "Disminución en el desempeño laboral.",
]


def build_test():
    path = "test-nivel-de-severidad"
    title = "Test de severidad de la hiperhidrosis | Hiperhidrosis.cl"
    desc = ("Descubre la severidad de tu hiperhidrosis: responde 10 preguntas y conoce si tu sudoración es leve, "
            "moderada o severa, con el tratamiento sugerido para cada nivel.")
    hero = subpage_hero("Autoevaluación", "Descubre la severidad de tu hiperhidrosis",
                        "Responde las 10 preguntas según la frecuencia con que vives cada situación. Al finalizar conocerás tu nivel de severidad y el tratamiento sugerido. Esta orientación no reemplaza una consulta médica.")
    qs = "".join(f"""
      <div class="quiz-q">
        <fieldset>
          <legend>{i}. {q}</legend>
          <div class="quiz-opts">""" + "".join(f"""
            <label class="quiz-opt"><input type="radio" name="q{i}" value="{opt}"><span>{opt}</span></label>""" for opt in ("No", "Rara Vez", "A Veces", "A Diario")) + """
          </div>
        </fieldset>
      </div>""" for i, q in enumerate(QUIZ_QUESTIONS, 1))
    body = f"""<section class="prose-section" style="padding-bottom:54px">
  <div class="quiz">
    <form id="form-test" novalidate>{qs}
      <div class="quiz-actions">
        <button type="submit" class="btn-navy cta-btn" style="border:none;cursor:pointer;font-family:inherit">Ver mi resultado<span class="arrow">→</span></button>
        <span id="quiz-error" class="quiz-error">Responde las 10 preguntas para ver tu resultado.</span>
      </div>
    </form>
    <div id="quiz-result" class="quiz-result" role="status">
      <span class="qr-kicker">Tu nivel de severidad</span>
      <h2 id="quiz-result-level"></h2>
      <p id="quiz-result-text"></p>
      <div class="qr-actions">
        <a id="quiz-result-link" href="#" class="btn-pill cta-btn">Ver tratamiento sugerido<span class="arrow">→</span></a>
        <a href="#contacto" class="btn-pill cta-btn" style="background:rgba(255,255,255,.14)">Agendar consulta<span class="arrow">→</span></a>
        <button id="quiz-retry" type="button" class="btn-pill cta-btn" style="background:transparent;border:1.5px solid rgba(255,255,255,.4);cursor:pointer;font-family:inherit;font-size:inherit">Repetir el test</button>
      </div>
    </div>
  </div>
</section>
"""
    url = BASE + "/" + path
    page(path, title, desc, hero, body,
         [medical_page(url, title, desc)],
         scripts='<script src="/assets/quiz.js" defer></script>\n')


# =====================================================================================
# BLOG + POSTS
# =====================================================================================
POSTS = [
    {
        "slug": "2021/02/19/enfermedades-asociadas-a-la-hiperhidrosis",
        "title": "Enfermedades asociadas a la hiperhidrosis",
        "cat": "Causas",
        "date": "2021-02-19", "date_h": "19 de febrero, 2021",
        "mod": "2021-02-19",
        "desc": "La hiperhidrosis puede ser síntoma de otra enfermedad: diabetes, problemas de tiroides, menopausia, infecciones y más. Conoce el listado y cuándo consultar.",
        "hero_img": ("post-enfermedades.jpg", 900, 500, "Enfermedades asociadas a la hiperhidrosis"),
        "thumb": "thumb-enfermedades.jpg",
        "body": """
    <p>Se llama hiperhidrosis a la sudoración que ocurre de forma excesiva y poco frecuente, que se manifiesta sin necesidad de sentir calor o realizar algún ejercicio físico.</p>
    <p>Este exceso de sudoración puede ser a causa de dos factores:</p>
    <ul>
      <li>Es síntoma de una enfermedad específica.</li>
      <li>Es una <a href="/sobre-la-hiperhidrosis">condición en sí misma</a>.</li>
    </ul>
    <p>El artículo de hoy lo centraremos al primer factor y te contaremos cuáles son las enfermedades que tienen como síntoma la hiperhidrosis.</p>
    <p>Se debe señalar que es menos frecuente, pero no por eso inexistente. En este caso el paciente puede sufrir episodios de exceso de sudoración en todo el cuerpo, pero que dependiendo de la enfermedad que tenga asociada, se puede controlar con un buen tratamiento.</p>
    <p>Lo importante acá siempre será descartar que no haya otra enfermedad asociada a estos episodios de hiperhidrosis, ya que muchas de ellas pueden ser consideradas de extremo cuidado y urgencia.</p>
    <figure class="img-card">
      <img src="/assets/post-enfermedades-2.jpg" alt="Consulta médica por sudoración excesiva" width="900" height="500" loading="lazy">
    </figure>
    <p>A continuación, compartiremos contigo un listado de enfermedades y condiciones que pueden desarrollar como síntoma la hiperhidrosis:</p>
    <ul>
      <li>Diabetes</li>
      <li>Problemas en la tiroides</li>
      <li>Menopausia</li>
      <li>Algunos tipos de cánceres</li>
      <li>Problemas cardiacos</li>
      <li>Bajos niveles de azúcar</li>
      <li>Infecciones</li>
      <li>Lesión en la médula espinal</li>
      <li>Accidentes cerebrovasculares</li>
    </ul>
    <p>¡Pero ojo! También existen tratamientos médicos que pueden causar hiperhidrosis como efecto secundario. Por lo que si estás en un tratamiento y comienzas con estos episodios te recomendamos consultar con tu médico.</p>
    <p>¡Recuerda que también puedes seguirnos en nuestro <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>!</p>""",
    },
    {
        "slug": "2021/01/18/hiperhidrosis-y-sus-consecuencias-en-la-salud-mental",
        "title": "Hiperhidrosis y sus consecuencias en la salud mental",
        "cat": "Salud mental",
        "date": "2021-01-18", "date_h": "18 de enero, 2021",
        "mod": "2021-01-18",
        "desc": "El exceso de sudoración no solo trae problemas a nivel corporal: estrés, ansiedad y baja autoestima. Cómo afecta la hiperhidrosis a la salud mental y dónde apoyarse.",
        "hero_img": ("post-salud-mental.jpg", 900, 500, "Hiperhidrosis y sus consecuencias en la salud mental"),
        "thumb": "thumb-salud-mental.jpg",
        "body": """
    <p>El exceso de sudoración no solo trae problemas a nivel corporal, debido a lo que conlleva. Así que en este post hablaremos de la hiperhidrosis y sus consecuencias en la salud mental.</p>
    <p>Una persona que padece hiperhidrosis debe enfrentar las molestias del exceso de sudoración al cual está sometida, pero también está en un constante nivel de estrés por algo que escapa a su control.</p>
    <p>Si nos ponemos a pensar, esta condición aparece sin previo aviso y de una manera muy invasiva, incomodando y angustiando a quien la sufre, ya que una vez que se desencadena es imposible que podamos ponerle freno.</p>
    <p>Las situaciones de estrés, miedo, vergüenza, ansiedad o que son de un alto nivel de tensión emocional, tienden a desencadenar una crisis de exceso de sudoración, colocando a la persona en una situación incómoda y desafiante.</p>
    <p>Actos tan simples como escribir en un teclado o con un lápiz, saludar con la mano, elegir la ropa diaria, conducir un auto, leer un libro, entre otras; se vuelven un impedimento y afectan directamente en su autoestima y autoconfianza.</p>
    <p>Nuestra recomendación es que te cobijes en <a href="/2020/10/13/que-especialista-consultar-para-la-hiperhidrosis">especialistas como dermatólogos y/o cirujanos torácicos</a> para solucionar el problema en sí; pero también que te apoyes con psiquiatras que puedan ayudarte a sobrellevar esta condición y sus tratamientos de la mejor manera posible.</p>
    <p>Y para ti, ¿la hiperhidrosis ha tenido consecuencias en tu salud mental?</p>""",
    },
    {
        "slug": "2021/01/12/por-que-me-sudan-tanto-los-pies",
        "title": "¿Por qué me sudan tanto los pies?",
        "cat": "Pies",
        "date": "2021-01-12", "date_h": "12 de enero, 2021",
        "mod": "2021-01-12",
        "desc": "Si tus pies sudan en exceso puede que padezcas de hiperhidrosis plantar. Conoce sus causas, consecuencias y qué hacer para controlarla.",
        "hero_img": ("post-pies.jpg", 1080, 675, "Hiperhidrosis plantar"),
        "thumb": "thumb-pies.jpg",
        "body": """
    <p>Si tus pies sudan en exceso puede que padezcas de <strong>hiperhidrosis plantar</strong>. Este exceso de sudoración si bien no tiene causa determinada, se relaciona generalmente a situaciones de ansiedad y estrés.</p>
    <p>La gran consulta de todo paciente con exceso de sudoración es: ¿a qué se debe?; y aunque no lo creas, las causas no siempre son del todo claras, menos en casos de hiperhidrosis plantar.</p>
    <p>Uno de los primeros pasos es descartar que el exceso de sudoración en los pies sea por <a href="/2021/02/19/enfermedades-asociadas-a-la-hiperhidrosis">algún otro trastorno o enfermedad</a>, aunque generalmente se debe a una condición sin causa (por lo que se le denomina <a href="/sobre-la-hiperhidrosis">primaria</a>) la que hasta en el 50% de los casos es hereditaria.</p>
    <p><strong>¿Qué consecuencias tiene la hiperhidrosis plantar?</strong></p>
    <ul>
      <li>Afecta la capacidad de andar.</li>
      <li>Tiene repercusiones emocionales.</li>
      <li>Puede provocar bromhidrosis.</li>
      <li>Puede generar hongos e infecciones.</li>
    </ul>
    <p>Por esto es muy importante tener en cuenta el tipo de calzado que utilizamos y cambiar calcetines, al menos una vez al día.</p>
    <p>Siempre consulta con un <a href="/2020/10/13/que-especialista-consultar-para-la-hiperhidrosis">especialista</a> quien puede recomendarte el mejor tratamiento para frenar o disminuir la sudoración excesiva en tus pies.</p>
    <p>¡Recuerda seguirnos en nuestro <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>!</p>""",
    },
    {
        "slug": "2020/11/13/sudoracion-compensatoria-el-temido-efecto-secundario-de-la-simpatectomia",
        "title": "Sudoración compensatoria: ¿Qué es?",
        "cat": "Cirugía",
        "date": "2020-11-14", "date_h": "13 de noviembre, 2020",
        "mod": "2020-11-14",
        "desc": "La sudoración compensatoria es el principal efecto secundario de la simpatectomía: aumento de sudoración en espalda y abdomen. Qué es, factores de riesgo y qué esperar.",
        "hero_img": ("post-sudoracion-compensatoria.jpg", 980, 551, "Sudoración compensatoria tras la simpatectomía"),
        "thumb": "thumb-sudoracion-compensatoria.jpg",
        "body": """
    <p>La <a href="/cirugia-hiperhidrosis">simpatectomía</a> es una cirugía que tiene como objetivo devolver la calidad de vida a quienes padecen <a href="/hiperhidrosis-localizada-severa">hiperhidrosis severa</a> y no han obtenido resultados satisfactorios con otros tratamientos. Pero como toda intervención, tiene efectos secundarios; y en el caso de la simpatectomía es la <strong>sudoración compensatoria</strong>.</p>
    <h2>¿Pero a qué nos referimos con sudoración compensatoria?</h2>
    <p>Es el aumento de sudoración en otras partes del cuerpo luego de someterse a la simpatectomía. Esta nueva sudoración se presenta en la mayoría de los pacientes operados, se localiza principalmente en la espalda y/o abdomen y su magnitud es variable, siendo en un alto porcentaje de los casos de cuantía leve.</p>
    <p>Los factores que hacen predecir que la sudoración compensatoria puede ser importante son: <strong>edad, nivel de sección del nervio simpático y sobrepeso u obesidad</strong>.</p>
    <p>En un <strong>95% de los casos</strong>, los pacientes se sienten contentos con los resultados de la simpatectomía, independientemente de la sudoración compensatoria. Para ello es de vital importancia la consulta con el cirujano, el cual explicará al detalle este efecto secundario, con lo cual se logran aterrizar expectativas, aclarar temores, resolver dudas y así intervenirse de la forma más informada y real posible.</p>
    <p>Recuerda que puedes seguirnos en nuestro <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a> para más contenido e información.</p>""",
    },
    {
        "slug": "2020/10/27/simpatectomia-la-cirugia-que-mejora-la-vida-de-quienes-tienen-hiperhidrosis",
        "title": "Simpatectomía: ¡Dile adiós a la hiperhidrosis!",
        "cat": "Cirugía",
        "date": "2020-10-27", "date_h": "27 de octubre, 2020",
        "mod": "2020-11-14",
        "desc": "¿Qué es la simpatectomía y cómo puede mejorar tu calidad de vida si padeces hiperhidrosis? Procedimiento, recuperación y riesgos de esta cirugía poco invasiva.",
        "hero_img": ("post-simpatectomia.jpg", 1080, 675, "Simpatectomía: cirugía de la hiperhidrosis"),
        "thumb": "thumb-simpatectomia.jpg",
        "body": """
    <p><strong>¿Qué es la simpatectomía? y ¿cómo puede ayudar a mejorar tu calidad de vida si padeces hiperhidrosis? ¡Te contamos todo en el siguiente artículo!</strong></p>
    <p>La <a href="/cirugia-hiperhidrosis">simpatectomía</a> es una cirugía video-endoscópica poco invasiva que requiere menos de 24 horas de hospitalización y se realiza bajo anestesia general. En general, una persona que se somete a esta intervención puede retomar su trabajo o estudios a partir del 3er día.</p>
    <p>Esta cirugía es ideal para pacientes que padecen de <a href="/hiperhidrosis-localizada-severa">hiperhidrosis severa</a> y que no hayan respondido bien a tratamientos médicos anteriores.</p>
    <p>Recuerda que si no conoces qué nivel de severidad padeces, puedes realizar nuestro <a href="/test-nivel-de-severidad">TEST online</a> y descubrirlo.</p>
    <h2>¿Cómo funciona este procedimiento?</h2>
    <blockquote>“Se hacen dos incisiones de 3 y 5 mm en el pliegue anterior de la axila, por una de ellas se introduce una cámara y por la otra se introducen pinzas para seccionar el nervio o cadena simpática, habitualmente a nivel de la tercera o cuarta costilla, para así controlar la producción del sudor en la cara, palmas de las manos y en las axilas. El procedimiento se repite en forma idéntica en ambos lados.”</blockquote>
    <h2>¿Qué riesgos tiene someterse a esta cirugía?</h2>
    <p>Como en cualquier cirugía existen riesgos y complicaciones, que aunque pueden darse muy rara vez, existen: sangrado, neumotórax e infección. También es importante conocer la <a href="/2020/11/13/sudoracion-compensatoria-el-temido-efecto-secundario-de-la-simpatectomia">sudoración compensatoria</a>, su principal efecto secundario.</p>
    <p>¡Si quieres conocer valores, convenios y coberturas, <a href="#contacto">agenda una consulta</a>!</p>""",
    },
    {
        "slug": "2020/10/13/que-especialista-consultar-para-la-hiperhidrosis",
        "title": "¿Qué especialista consultar para la hiperhidrosis?",
        "cat": "Especialistas",
        "date": "2020-10-13", "date_h": "13 de octubre, 2020",
        "mod": "2020-10-13",
        "desc": "¿Dermatólogo o cirujano torácico? Qué especialista consultar según el nivel de severidad de tu hiperhidrosis: leve, moderada o severa.",
        "hero_img": ("post-especialista.jpg", 1080, 675, "Consulta médica por hiperhidrosis"),
        "thumb": "thumb-especialista.jpg",
        "body": """
    <p>El momento exacto para consultar un especialista es cuando tu sudoración se vuelve invalidante y comienza a afectar tu vida social y laboral.</p>
    <p>Para mantenerla a raya podemos acudir a tratamientos que van desde cremas y antitranspirantes, pasando por el Botox, hasta incluso la cirugía; sin embargo, la invitación siempre será a consultar con un especialista, quien pueda guiarte para poner en marcha el mejor tratamiento según el nivel de sudoración que tengas.</p>
    <h2>Hiperhidrosis leve</h2>
    <p>Lo mejor es concurrir a un dermatólogo que podrá ayudarte con algún tratamiento en base a <a href="/hiperhidrosis-localizada-leve">antitranspirantes y cremas formuladas con cloruro de aluminio</a> y que pueden encontrarse fácilmente en el mercado.</p>
    <h2>Hiperhidrosis moderada</h2>
    <p>En este caso también es bueno recurrir a un dermatólogo especializado quien te sugerirá tratamientos como la <a href="/hiperhidrosis-localizada-moderada">iontoforesis, medicamentos orales y Botox</a>.</p>
    <h2>Hiperhidrosis severa</h2>
    <p>Las personas con <a href="/hiperhidrosis-localizada-severa">hiperhidrosis severa</a> (incluyendo a las que no hayan respondido favorablemente a los tratamientos anteriores) deben visitar a un <strong>cirujano torácico</strong>. El tratamiento es una cirugía llamada <a href="/cirugia-hiperhidrosis">simpatectomía</a> y es una excelente solución debido al éxito que tiene en los pacientes que se someten.</p>
    <p>¿Te gustaría conocer los detalles de cada nivel y sus tratamientos? ¡No te pierdas nuestro <a href="/blog">blog</a>!</p>""",
    },
    {
        "slug": "2020/08/30/como-saber-si-tengo-hiperhidrosis",
        "title": "¿Cómo saber si tengo hiperhidrosis?",
        "cat": "Causas",
        "date": "2020-08-30", "date_h": "30 de agosto, 2020",
        "mod": "2020-11-14",
        "desc": "¿Sudas más de lo habitual? Aprende a diferenciar la sudoración normal de la hiperhidrosis primaria y secundaria, y qué hacer para diagnosticarla.",
        "hero_img": ("post-como-saber.jpg", 1080, 675, "Cómo saber si tengo hiperhidrosis"),
        "thumb": "thumb-como-saber.jpg",
        "body": """
    <p>Llamamos hiperhidrosis a la sudoración excesiva e inusual que produce nuestro cuerpo para regular su temperatura. En algunas ocasiones nuestro cuerpo tiende a transpirar más de lo habitual: en el embarazo o cuando hacemos deporte. Entonces, ¿cómo saber si es hiperhidrosis?</p>
    <p>Este exceso de sudoración se da en zonas del cuerpo como palmas de las manos, plantas de los pies, axilas y zona craneofacial.</p>
    <p>Cuando está asociada a enfermedades como hipertiroidismo, menopausia, obesidad, tuberculosis, entre otras; se habla de <a href="/2021/02/19/enfermedades-asociadas-a-la-hiperhidrosis">hiperhidrosis generalizada o secundaria</a>, la que se soluciona tratando la enfermedad a la que está relacionada.</p>
    <p>Pero cuando hablamos de <a href="/sobre-la-hiperhidrosis">hiperhidrosis primaria o localizada</a>, nos referimos al exceso de sudoración que no tiene una causa aparente y que llega a nuestra vida de un momento a otro.</p>
    <p>Esta enfermedad tiene como gran problema que afecta a la calidad de vida de quienes la padecen. Llegando incluso a convertirse en un factor invalidante ya que va limitando a las personas en sus relaciones sociales y laborales.</p>
    <p>Aunque hoy en día no existe un examen específico para diagnosticarla, la historia clínica del paciente y el examen físico juegan un rol fundamental.</p>
    <p>Los tratamientos que se pondrán en marcha dependerán del nivel de severidad que tenga el paciente, donde la <a href="/cirugia-hiperhidrosis">cirugía</a> es una gran solución para aquellos con hiperhidrosis severa.</p>
    <p>¿Te gustaría saber qué nivel de hiperhidrosis tienes?</p>
    <p>¡Te invitamos a que te hagas nuestro <a href="/test-nivel-de-severidad">TEST</a> completamente gratis!</p>
    <p>Para más contenido te invitamos a seguir nuestro <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>.</p>""",
    },
]


def build_posts():
    for p in POSTS:
        path = p["slug"]
        url = f"{BASE}/{path}"
        title = f"{p['title']} | Hiperhidrosis.cl"
        img, w, h, alt = p["hero_img"]
        hero = subpage_hero("Blog · " + p["cat"], p["title"],
                            meta=f"Por el equipo de Hiperhidrosis.cl · <time datetime=\"{p['date']}\">{p['date_h']}</time>")
        body_text = p["body"].replace("{INSTAGRAM}", INSTAGRAM)
        body = f"""<section class="prose-section">
  <article class="prose">
    <figure class="img-card" style="margin-top:0">
      <img src="/assets/{img}" alt="{alt}" width="{w}" height="{h}">
    </figure>{body_text}
    <p style="margin-top:30px"><a href="/blog">← Volver al blog</a></p>
  </article>
</section>
"""
        article = {
            "@type": "BlogPosting",
            "@id": url + "#article",
            "headline": p["title"],
            "description": p["desc"],
            "url": url,
            "inLanguage": "es",
            "image": f"{BASE}/assets/{img}",
            "datePublished": p["date"],
            "dateModified": p["mod"],
            "author": {"@id": f"{BASE}/#physician"},
            "publisher": {"@id": f"{BASE}/#org"},
            "mainEntityOfPage": url,
            "isPartOf": {"@id": f"{BASE}/blog#blog"},
        }
        page(path, title, p["desc"], hero, body,
             [medical_page(url, title, p["desc"]), article],
             ogimage=f"assets/{img}", ogtype="article")


def build_blog():
    path = "blog"
    title = "Blog sobre hiperhidrosis: causas, tratamientos y vida diaria | Hiperhidrosis.cl"
    desc = ("Artículos sobre la sudoración excesiva: cómo saber si tienes hiperhidrosis, qué especialista "
            "consultar, la simpatectomía, la sudoración compensatoria y más.")
    hero = subpage_hero("Recursos", "Desde el blog",
                        "Artículos del equipo sobre causas, tratamientos y el día a día con hiperhidrosis.")
    cards = "".join(f"""
      <a href="/{p['slug']}" class="post">
        <div class="post__imgwrap"><img class="pimg" src="/assets/{p['thumb']}" alt="{p['title']}" width="400" height="250" loading="lazy"></div>
        <div class="post__body">
          <span class="post__cat">{p['cat']}</span>
          <h2 class="post__title">{p['title']}</h2>
          <div class="post__date"><time datetime="{p['date']}">{p['date_h']}</time></div>
        </div>
      </a>""" for p in POSTS)
    body = f"""<section class="blog-section" style="padding-top:54px">
  <div class="wrap">
    <div class="blog-grid">{cards}
    </div>
  </div>
</section>
"""
    url = f"{BASE}/{path}"
    blog_node = {
        "@type": "Blog",
        "@id": url + "#blog",
        "name": "Blog de Hiperhidrosis.cl",
        "url": url,
        "inLanguage": "es",
        "publisher": {"@id": f"{BASE}/#org"},
        "blogPost": [
            {"@type": "BlogPosting", "headline": p["title"],
             "url": f"{BASE}/{p['slug']}", "datePublished": p["date"]}
            for p in POSTS
        ],
    }
    page(path, title, desc, hero, body,
         [medical_page(url, title, desc), blog_node])


# =====================================================================================
# robots.txt + sitemap.xml
# =====================================================================================
ALL_PATHS = [
    "", "sobre-la-hiperhidrosis", "hiperhidrosis-localizada-leve",
    "hiperhidrosis-localizada-moderada", "hiperhidrosis-localizada-severa",
    "cirugia-hiperhidrosis", "rubor-facial-patologico", "test-nivel-de-severidad",
    "blog",
] + [p["slug"] for p in POSTS]


def build_robots_sitemap():
    robots = """# hiperhidrosis.cl — estándar de la red
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: CCBot
Allow: /

Sitemap: https://hiperhidrosis.cl/sitemap.xml
"""
    (OUT / "robots.txt").write_text(robots)

    mods = {p["slug"]: p["mod"] for p in POSTS}
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for p in ALL_PATHS:
        loc = BASE + ("/" + p if p else "/")
        lastmod = mods.get(p, "2026-07-04")
        lines.append(f"  <url><loc>{loc}</loc><lastmod>{lastmod}</lastmod></url>")
    lines.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(lines) + "\n")
    print("  robots.txt + sitemap.xml")


# =====================================================================================
if __name__ == "__main__":
    print("Generando dist/hiperhidrosis/ …")
    build_home()
    build_sobre()
    build_leve()
    build_moderada()
    build_severa()
    build_cirugia()
    build_rubor()
    build_test()
    build_blog()
    build_posts()
    build_robots_sitemap()
    print(f"OK — {len(ALL_PATHS)} páginas.")
