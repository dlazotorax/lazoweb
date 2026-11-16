# Genera rats.cl/esofagectomia a partir de la plantilla de /resecciones/lobectomia
# Uso: python3 _design/rats-esofagectomia/build.py dist/rats/resecciones/lobectomia.html dist/rats/esofagectomia.html
import sys, re, json
src = open(sys.argv[1], encoding='utf-8').read()
URL = "https://rats.cl/esofagectomia"
TITLE = "Esofagectomía robótica · Dr. David Lazo Pérez"
DESC = ("Esofagectomía robótica: el tiempo torácico en una cirugía conjunta de cirujanos "
        "digestivos y torácicos, técnicas McKeown e Ivor Lewis y evidencia publicada.")
FECHA = "2026-11-15"

REFS = [
 ("van der Sluis PC, van der Horst S, May AM, et al. Robot-assisted minimally invasive thoracolaparoscopic esophagectomy versus open transthoracic esophagectomy for resectable esophageal cancer: a randomized controlled trial.", "Ann Surg", "2019;269(4):621-630.", "10.1097/SLA.0000000000003031"),
 ("Yang Y, Li B, Yi J, et al. Robot-assisted versus conventional minimally invasive esophagectomy for resectable esophageal squamous cell carcinoma: early results of a multicenter randomized controlled trial: the RAMIE trial.", "Ann Surg", "2022;275(4):646-653.", "10.1097/SLA.0000000000005023"),
 ("Yang Y, Liu Z, Li C, et al. Robot-assisted versus conventional minimally invasive oesophagectomy for oesophageal squamous cell carcinoma (RAMIE): a multicentre, open-label, randomised, phase 3, non-inferiority trial.", "Lancet Gastroenterol Hepatol", "2026;11(6):452-462.", "10.1016/S2468-1253(25)00402-9"),
 ("van Workum F, Verstegen MHP, Klarenbeek BR, et al. Intrathoracic vs cervical anastomosis after totally or hybrid minimally invasive esophagectomy for esophageal cancer: a randomized clinical trial.", "JAMA Surg", "2021;156(7):601-610.", "10.1001/jamasurg.2021.1555"),
 ("Kooij CD, de Jongh C, Kingma BF, et al. The current state of robot-assisted minimally invasive esophagectomy (RAMIE): outcomes from the Upper GI International Robotic Association (UGIRA) Esophageal Registry.", "Ann Surg Oncol", "2025;32(2):823-833.", "10.1245/s10434-024-16364-9"),
]


# ---------- VIDEOS: pegar aquí el ID de YouTube (o dejar None) y el formato ----------
# formato: "9/16" para Shorts verticales, "16/9" para videos horizontales
# Base de los MP4 propios: "/videos/" en producción; la maqueta usa "videos/" (argv[3])
VID_BASE = sys.argv[3] if len(sys.argv) > 3 else "/videos/"
VIDEOS = {
  "mck": {"id": None, "local": "esofagectomia-mckeown", "yt": "https://www.youtube.com/shorts/LtiA-GZl6j8", "duracion": "PT1M25S", "subido": "2026-11-15", "formato": "9/16", "titulo": "Esofagectomía robótica McKeown: tiempo torácico", "texto": "Tiempo torácico de una esofagectomía McKeown robótica. Apertura de la pleura mediastínica, resección de adenopatías periesofágicas, disección y sección de la vena ácigos con vessel loop y endograpadora, aislamiento del esófago con cinta radiopaca para su tracción, movilización circunferencial del esófago torácico y linfadenectomía mediastínica."},
  "il":  {"id": None, "local": "esofagectomia-ivor-lewis", "yt": "https://www.youtube.com/shorts/lNsIUog6s_A", "duracion": "PT1M43S", "subido": "2026-11-15", "formato": "9/16", "titulo": "Esofagectomía robótica Ivor Lewis: tiempo torácico", "texto": "Tiempo torácico de una esofagectomía Ivor Lewis robótica. Apertura de la pleura mediastínica, movilización circunferencial del esófago intratorácico con linfadenectomía, sección del esófago con endograpadora lineal, ascenso del tubo gástrico al tórax, anastomosis esofagogástrica intratorácica latero-lateral con endograpadora y cierre robótico de la brecha con sutura barbada en dos planos."},
}

# ---------- head ----------
head_end = src.index('<script type="application/ld+json"')
head = src[:head_end]
head = re.sub(r'<title>.*?</title>', f'<title>{TITLE}</title>', head)
head = re.sub(r'(<meta name="description" content=")[^"]*', r'\g<1>' + DESC, head)
head = re.sub(r'(<meta property="og:title" content=")[^"]*', r'\g<1>' + TITLE, head)
head = re.sub(r'(<meta property="og:description" content=")[^"]*', r'\g<1>' + DESC, head)
head = re.sub(r'(<meta property="og:url" content=")[^"]*', r'\g<1>' + URL, head)
head = re.sub(r'\s*<meta property="og:image" content="[^"]*" />', '', head)
head = re.sub(r'(<link rel="canonical" href=")[^"]*', r'\g<1>' + URL, head)

blocks = re.findall(r'<script type="application/ld\+json">.*?</script>', src, re.S)
physician = [b for b in blocks if '"Physician"' in b][0]

webpage = {
 "@context": "https://schema.org", "@type": "MedicalWebPage",
 "@id": URL + "#webpage", "url": URL,
 "name": "Esofagectomía robótica: tiempo torácico",
 "description": DESC, "inLanguage": "es-CL",
 "about": [{"@type": "MedicalProcedure", "name": "Esofagectomía robótica",
            "alternateName": ["Esofaguectomía robótica", "Esofagectomía de McKeown", "Esofagectomía de Ivor Lewis"]}],
 "author": {"@id": "https://cirugiatoracica.cl/#david-lazo"},
 "reviewedBy": {"@id": "https://cirugiatoracica.cl/#david-lazo"},
 "lastReviewed": FECHA, "dateModified": FECHA,
 "specialty": "https://schema.org/Surgical",
 "isPartOf": {"@type": "WebSite", "@id": "https://rats.cl/#website", "url": "https://rats.cl/", "name": "rats.cl", "inLanguage": "es-CL"},
 "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
   {"@type": "ListItem", "position": 1, "name": "Cirugía robótica torácica", "item": "https://rats.cl/"},
   {"@type": "ListItem", "position": 2, "name": "Esofagectomía robótica", "item": URL}]},
 "citation": [f"{a} {j}. {c}" for a, j, c, d in REFS],
}
ld = '<script type="application/ld+json">\n' + json.dumps(webpage, ensure_ascii=False, indent=2) + '\n  </script>'
for clave, v in VIDEOS.items():
    if v.get("local"):
        vo = {"@context": "https://schema.org", "@type": "VideoObject", "@id": f"{URL}#video-{clave}",
              "name": v["titulo"] + " | RATS", "description": v["texto"], "uploadDate": v["subido"], "duration": v["duracion"],
              "thumbnailUrl": f"https://rats.cl/videos/{v['local']}.jpg", "contentUrl": f"https://rats.cl/videos/{v['local']}.mp4",
              "inLanguage": "es-CL", "author": {"@id": "https://cirugiatoracica.cl/#david-lazo"}, "isPartOf": {"@id": URL + "#webpage"}}
        ld += '\n  <script type="application/ld+json">\n' + json.dumps(vo, ensure_ascii=False, indent=2) + '\n  </script>'

ga_start = src.index('<!-- Google Analytics 4')
ga = src[ga_start:src.index('</head>')]
topbar = src[src.index('<body>'):src.index('<header')]
contact_footer = src[src.index('<section id="contacto"'):]

# ---------- helpers ----------
H2 = "font-family:'Bebas Neue',sans-serif;font-size:clamp(28px,3.4vw,46px);line-height:1"
def sec(n, anchor, title, body, last=False):
    num = f'<span style="font-family:\'Bebas Neue\',sans-serif;font-size:34px;line-height:1;color:#C4500E">§{n}</span>\n        ' if n else ''
    border = '' if last else ';border-bottom:1px solid #0B0B0B'
    return f'''
    <section style="padding:32px 0{border}">
      <div id="{anchor}" style="display:flex;align-items:baseline;gap:16px;border-bottom:2px solid #0B0B0B;padding-bottom:8px;margin-bottom:24px;scroll-margin-top:60px">
        {num}<h2 style="{H2}">{title}</h2>
      </div>
{body}
    </section>
'''
P = lambda t, big=False: f'      <p style="font-size:{"17px;font-weight:500" if big else "16.5px"};max-width:920px;margin-bottom:14px">{t}</p>\n'
def ul(items):
    li = ''.join(f'<li style="font-size:16.5px;padding:10px 0 10px 22px;border-top:1px solid #0B0B0B;position:relative"><span style="position:absolute;left:0;top:10px;color:#C4500E;font-weight:700">—</span>{i}</li>' for i in items)
    return f'      <ul style="max-width:920px;margin:0 0 14px;padding-left:0;list-style:none">{li}</ul>\n'
sup = lambda *n: '<sup>' + ','.join(f'<a href="#ref-{i}" style="font-weight:700">{i}</a>' for i in n) + '</sup>'
LBL = "font-size:10.5px;font-weight:700;letter-spacing:0.18em;text-transform:uppercase"

def esquema(variante):
    # Esquema lineal: cuello / tórax / abdomen; tubo gástrico y punto de anastomosis
    mck = variante == 'mck'
    yan = 46 if mck else 196
    orden = [('1', 170), ('2', 330), ('3', 66)] if mck else [('2', 170), ('1', 330)]
    badges = ''.join(f'<circle cx="252" cy="{y}" r="13" fill="#0B0B0B"/><text x="252" y="{y+5}" text-anchor="middle" font-family="Public Sans,sans-serif" font-size="14" font-weight="700" fill="#F6F5F1">{n}</text>' for n, y in orden)
    cerv = '<line x1="122" y1="30" x2="132" y2="16" stroke="#C4500E" stroke-width="3"/><text x="152" y="20" font-family="Public Sans,sans-serif" font-size="11" fill="#C4500E">incisión cervical</text>' if mck else ''
    return f'''<svg viewBox="0 0 280 400" role="img" aria-label="{'McKeown: anastomosis en el cuello' if mck else 'Ivor Lewis: anastomosis en el tórax'}" style="width:100%;max-width:280px;display:block;border:2px solid #0B0B0B;background:#fff">
  <rect x="0" y="0" width="280" height="80" fill="#F6F5F1"/><rect x="0" y="262" width="280" height="138" fill="#F6F5F1"/>
  <text x="12" y="20" font-family="Public Sans,sans-serif" font-size="10" font-weight="700" letter-spacing="2" fill="#3A3A3A">CUELLO</text>
  <text x="12" y="102" font-family="Public Sans,sans-serif" font-size="10" font-weight="700" letter-spacing="2" fill="#3A3A3A">TÓRAX</text>
  <text x="12" y="284" font-family="Public Sans,sans-serif" font-size="10" font-weight="700" letter-spacing="2" fill="#3A3A3A">ABDOMEN</text>
  <path d="M0 268 Q140 236 280 268" fill="none" stroke="#0B0B0B" stroke-width="2"/>
  <text x="270" y="256" text-anchor="end" font-family="Public Sans,sans-serif" font-size="10" fill="#3A3A3A">diafragma</text>
  <path d="M60 150 Q100 136 130 150" fill="none" stroke="#3A3A3A" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="58" y="166" font-family="Public Sans,sans-serif" font-size="10" fill="#3A3A3A">ácigos</text>
  <line x1="140" y1="0" x2="140" y2="{yan}" stroke="#0B0B0B" stroke-width="7" stroke-linecap="round"/>
  <path d="M140 {yan} L140 300 Q140 352 176 356 Q206 358 206 332" fill="none" stroke="#0E7490" stroke-width="16" stroke-linecap="round"/>
  <circle cx="140" cy="{yan}" r="9" fill="#C4500E" stroke="#fff" stroke-width="2"/>
  <text x="156" y="{yan+4}" font-family="Public Sans,sans-serif" font-size="11" font-weight="700" fill="#C4500E">anastomosis</text>
  <text x="160" y="226" font-family="Public Sans,sans-serif" font-size="10" fill="#0E7490">tubo gástrico</text>
  {cerv}{badges}
</svg>'''

def variante(nombre, sub, svg, items, cap):
    return f'''        <div style="flex:1 1 400px;max-width:600px;border-top:3px solid #0B0B0B;padding-top:14px">
          <p style="{LBL};color:#C4500E;margin-bottom:4px">{sub}</p>
          <h3 style="font-family:'Bebas Neue',sans-serif;font-size:clamp(30px,3vw,40px);line-height:1;margin-bottom:16px">{nombre}</h3>
          <div style="display:flex;flex-wrap:wrap;gap:20px;align-items:flex-start">
            <figure style="flex:0 1 220px;margin:0">{svg}<figcaption style="font-size:12.5px;color:#3A3A3A;margin-top:8px">{cap}</figcaption></figure>
            <div style="flex:1 1 240px">{ul(items)}</div>
          </div>
        </div>
'''


def bloque_video(clave, nombre):
    v = VIDEOS[clave]
    caja = f"position:relative;aspect-ratio:{v['formato']};border:2px solid #0B0B0B;background:#0B0B0B"
    if v.get("local"):
        n = v["local"]
        media = (f'<div style="{caja}"><video class="vid-auto" src="{VID_BASE}{n}.mp4" poster="{VID_BASE}{n}.jpg" muted loop playsinline preload="none" '
                 f'aria-label="{v["titulo"]} — Dr. David Lazo Pérez" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block"></video></div>'
                 + (f'<p style="font-size:14px;margin-top:8px"><a href="{v["yt"]}" target="_blank" rel="noopener">Ver en YouTube →</a></p>' if v.get("yt") else ''))
    elif v["id"]:
        i = v["id"]
        media = (f'<div style="{caja}"><iframe class="yt-auto" src="https://www.youtube-nocookie.com/embed/{i}?rel=0&amp;playsinline=1&amp;mute=1&amp;loop=1&amp;playlist={i}&amp;enablejsapi=1" '
                 f'title="{v["titulo"]} — Dr. David Lazo Pérez" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
                 f'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe></div>'
                 f'<p style="font-size:14px;margin-top:8px"><a href="https://www.youtube.com/watch?v={i}" target="_blank" rel="noopener">Ver en YouTube →</a></p>')
    else:
        media = (f'<div style="{caja};display:flex;align-items:center;justify-content:center;background:repeating-linear-gradient(45deg,#EDEBE6,#EDEBE6 12px,#F6F5F1 12px,#F6F5F1 24px)">'
                 f'<p style="{LBL};color:#3A3A3A;background:#fff;border:1px solid #0B0B0B;padding:8px 12px">[ MAQUETA ] Pegar ID de YouTube</p></div>')
    ancho = "360px" if v["formato"] == "9/16" else "600px"
    return (f'        <div style="flex:1 1 320px;max-width:{ancho}">\n'
            f'          <p style="{LBL};color:#C4500E;margin-bottom:8px">{nombre}</p>\n'
            f'          {media}\n'
            f'          <p style="font-size:15px;margin-top:8px">{v["texto"]}</p>\n'
            f'        </div>\n')

AUTOPLAY_MP4 = """      <script>(function(){document.currentScript.parentNode.querySelectorAll('video.vid-auto').forEach(function(v){
      if(!('IntersectionObserver' in window)){v.setAttribute('controls','');return;}
      new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){v.preload='auto';var p=v.play();if(p&&p.catch)p.catch(function(){v.setAttribute('controls','');});}else{v.pause();}});},{threshold:0.5}).observe(v);});})();</script>
"""
AUTOPLAY = """      <script>(function(){document.currentScript.parentNode.querySelectorAll('iframe.yt-auto').forEach(function(f){if(!('IntersectionObserver' in window))return;
      function cmd(c){try{f.contentWindow.postMessage(JSON.stringify({event:'command',func:c,args:[]}),'*');}catch(e){}}
      var vis=false;f.addEventListener('load',function(){if(vis){cmd('mute');cmd('playVideo');}});
      new IntersectionObserver(function(es){es.forEach(function(e){vis=e.isIntersecting;if(vis){cmd('mute');cmd('playVideo');}else{cmd('pauseVideo');}});},{threshold:0.5}).observe(f);});})();</script>
"""

# ---------- contenido ----------
s1 = (P("La esofagectomía (o esofaguectomía) por cáncer se opera en dos o tres campos: abdomen, tórax y, en una de sus variantes, cuello. En la esofagectomía robótica intervienen dos equipos quirúrgicos en una misma cirugía: cirugía digestiva y cirugía torácica.", True) +
f'''      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:0;border:2px solid #0B0B0B;max-width:920px;margin:6px 0 18px;background:#fff">
        <div style="padding:18px 20px;border-right:1px solid #0B0B0B"><p style="{LBL};color:#3A3A3A;margin-bottom:6px">Cirugía digestiva</p><p style="font-family:'Bebas Neue',sans-serif;font-size:26px;line-height:1;margin-bottom:8px">Tiempo abdominal</p><p style="font-size:15.5px">Movilización del estómago, linfadenectomía abdominal y confección del tubo gástrico que reemplaza al esófago.</p></div>
        <div style="padding:18px 20px;background:#0B0B0B;color:#F6F5F1"><p style="{LBL};color:#67D3E8;margin-bottom:6px">Cirugía torácica</p><p style="font-family:'Bebas Neue',sans-serif;font-size:26px;line-height:1;margin-bottom:8px">Tiempo torácico</p><p style="font-size:15.5px">Disección del esófago torácico y linfadenectomía del mediastino.</p></div>
      </div>
''' + P("Esta página describe el tiempo torácico."))

s2 = ul([
 "Acceso por el hemitórax derecho, con los brazos del robot introducidos por incisiones pequeñas entre las costillas. Según la técnica, el paciente se ubica en decúbito lateral izquierdo o semiprono.",
 "Cayado de la vena ácigos: en Ivor Lewis se preserva; en McKeown, según el caso, se preserva o se secciona.",
 "Disección del esófago torácico junto con el tejido que lo rodea, desde el hiato diafragmático hasta el estrecho torácico superior (McKeown) o hasta bajo el cayado de la vena ácigos (Ivor Lewis).",
 "Linfadenectomía mediastínica: ganglios paraesofágicos y subcarinales y, según el tumor, ganglios a lo largo de los nervios laríngeos recurrentes.",
 'Conducto torácico: se identifica y, según el caso, se preserva o se reseca junto al esófago. Puede visualizarse con <a href="/verde-indocianina/conducto-toracico">verde de indocianina</a>.',
])

s3 = P("La diferencia entre ambas técnicas está en la indicación de la cirugía por la localización tumoral, el orden de los tiempos y en el lugar donde se une el tubo gástrico con el esófago remanente.") + \
 '      <div style="display:flex;flex-wrap:wrap;gap:32px;margin-top:10px">\n' + \
 variante("McKeown", "Tres campos · tórax, abdomen y cuello", esquema('mck'), [
   "Orden: <strong>1</strong> tórax · <strong>2</strong> abdomen · <strong>3</strong> cuello.",
   "En el tórax se moviliza todo el esófago hasta el estrecho torácico superior.",
   "El tubo gástrico se asciende hasta el cuello y la anastomosis se hace por una incisión cervical izquierda.",
   "Permite resecar más esófago proximal y la linfadenectomía del mediastino superior.",
   "Uso habitual: tumores del tercio medio y superior del esófago.",
 ], "McKeown: anastomosis cervical.") + \
 variante("Ivor Lewis", "Dos campos · abdomen y tórax", esquema('il'), [
   "Orden: <strong>1</strong> abdomen · <strong>2</strong> tórax.",
   "El tubo gástrico, preparado en el abdomen, se asciende al tórax.",
   "El esófago se secciona bajo el cayado de la vena ácigos, que se preserva, y la anastomosis se hace dentro del tórax, por vía robótica.",
   "Sin incisión cervical.",
   'Uso habitual: tumores del tercio inferior y de la unión esofagogástrica.',
 ], "Ivor Lewis: anastomosis intratorácica.") + \
 '      </div>\n'

s_vid = ('      <div style="display:flex;flex-wrap:wrap;gap:48px 224px;align-items:flex-start;justify-content:center">\n' + bloque_video("mck", "McKeown") + bloque_video("il", "Ivor Lewis") + '      </div>\n' + (AUTOPLAY if any(v["id"] for v in VIDEOS.values()) else '') + (AUTOPLAY_MP4 if any(v.get("local") for v in VIDEOS.values()) else ''))

TD = 'style="padding:12px 14px;border-top:1px solid #0B0B0B;vertical-align:top"'
TH = 'style="text-align:left;padding:12px 14px;font-size:10.5px;letter-spacing:0.18em;text-transform:uppercase;background:#0B0B0B;color:#F6F5F1"'
rows = [
 ("ROBOT · van der Sluis 2019" + sup(1), "112 pacientes con cáncer de esófago intratorácico, aleatorizados a esofagectomía robótica o abierta transtorácica",
  "Complicaciones quirúrgicas en 59% y 80%; con el robot, menos complicaciones pulmonares y cardíacas y menos dolor. Resultados oncológicos comparables a 40 meses de seguimiento"),
 ("RAMIE · Yang 2022 y 2026" + sup(2, 3), "362 pacientes con carcinoma escamoso, aleatorizados a esofagectomía robótica (183) o toracoscópica convencional (179)",
  "Con el robot: operación más corta y mayor logro de la linfadenectomía del nervio recurrente izquierdo (79,5% y 67,6%), con complicaciones similares. Sobrevida a 5 años de 69,4% y 56,2%: no inferioridad confirmada"),
 ("ICAN · van Workum 2021" + sup(4), "245 pacientes con cáncer de esófago medio o distal o de la unión esofagogástrica, operados por vía mínimamente invasiva con anastomosis intratorácica (122) o cervical (123)",
  "Filtración anastomótica en 12,3% y 34,1%. Con la anastomosis intratorácica, menos complicaciones graves y menos parálisis del nervio recurrente"),
 ("UGIRA · Kooij 2025" + sup(5), "Registro de 28 centros: 2.012 esofagectomías robóticas Ivor Lewis y 1.180 McKeown (2016-2023)",
  "En 2021-2023: filtración anastomótica en 16% (Ivor Lewis) y 11% (McKeown); 30 y 34 ganglios resecados"),
]
tbl = ''.join(f'<tr><td {TD[:-1]};font-weight:700;white-space:nowrap">{a}</td><td {TD}>{b}</td><td {TD}>{c}</td></tr>\n' for a, b, c in rows)
s4 = f'''      <div style="overflow-x:auto;border:2px solid #0B0B0B;background:#fff;margin:6px 0 14px"><table style="width:100%;border-collapse:collapse;font-size:15px;min-width:640px"><thead><tr><th {TH}>Estudio</th><th {TH}>Pacientes</th><th {TH}>Resultado</th></tr></thead><tbody>
{tbl}</tbody></table></div>
'''
refs = ''.join(f'        <li id="ref-{i}" style="margin:8px 0;scroll-margin-top:60px">{a} <em>{j}</em>. {c} <a href="https://doi.org/{d}" target="_blank" rel="noopener">DOI</a></li>\n' for i, (a, j, c, d) in enumerate(REFS, 1))
s5 = f'      <ol style="padding-left:22px;max-width:920px;font-size:14.5px">\n{refs}      </ol>\n'

NAVA = "font-family:'Public Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;padding:14px 18px;display:block;text-decoration:none;border-right:1px solid #333;color:#F6F5F1"
nav_items = [("https://rats.cl", "← rats.cl", True), ("#equipo", "Equipo", False), ("#tiempo-toracico", "Tiempo torácico", False), ("#variantes", "McKeown · Ivor Lewis", False), ("#videos", "Videos", False), ("#evidencia", "Evidencia", False)]
nav = ''.join(f'<a href="{h}" style="{NAVA}{";color:#9A9A9A" if g else ""}" class="hv4">{t}</a>\n        ' for h, t, g in nav_items)

body = f'''{topbar}<header style="border-bottom:3px solid #0B0B0B">
      <div style="max-width:1280px;margin:0 auto;padding:20px 24px 0;display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:16px">
        <div>
          <p style="font-size:10.5px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#C4500E;margin-bottom:6px"><a href="https://rats.cl" style="color:#C4500E">RATS</a> · Esófago · Dr. David Lazo Pérez</p>
          <h1 style="font-family:'Bebas Neue',sans-serif;font-size:clamp(46px,7.5vw,112px);line-height:0.86;letter-spacing:0.005em">Esofagectomía robótica</h1>
        </div>
        <a href="#contacto" style="background:#C4500E;color:#fff;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;padding:14px 18px;margin-bottom:8px" class="hv5">Agendar consulta</a>
      </div>
      <div style="max-width:1280px;margin:0 auto;padding:14px 24px 0">
        <p style="font-size:13px;border-top:1px solid #0B0B0B;padding-top:10px;padding-bottom:14px">Tiempo torácico de la esofagectomía mínimamente invasiva asistida por robot: técnicas McKeown e Ivor Lewis.</p>
      </div>
    </header>
    <nav aria-label="Esofagectomía robótica" style="position:sticky;top:0;z-index:50;background:#0B0B0B;color:#F6F5F1">
      <div style="max-width:1280px;margin:0 auto;padding:0 24px;display:flex;flex-wrap:wrap;align-items:stretch">
        {nav}</div>
    </nav>
    <main style="max-width:1280px;margin:0 auto;padding:0 24px">
{sec(1, "equipo", "Cirugía multiespecialidad", s1)}{sec(2, "tiempo-toracico", "El tiempo torácico", s2)}{sec(3, "variantes", "Dos variantes: McKeown e Ivor Lewis", s3)}{sec(4, "videos", "Videos", s_vid)}{sec(5, "evidencia", "Evidencia publicada", s4)}{sec(None, "referencias", "Referencias", s5, last=True)}  </main>
'''
out = head + physician + '\n  ' + ld + '\n' + ga + '</head>\n' + body + contact_footer
open(sys.argv[2], 'w', encoding='utf-8').write(out)
print(len(TITLE), len(DESC), len(out))
