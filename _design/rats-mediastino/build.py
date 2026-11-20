# Genera rats.cl/tumores-mediastino a partir de la plantilla de /resecciones/lobectomia
# Uso: python3 _design/rats-mediastino/build.py dist/rats/resecciones/lobectomia.html dist/rats/tumores-mediastino.html [VID_BASE]
import sys, re, json
src = open(sys.argv[1], encoding='utf-8').read()
URL = "https://rats.cl/tumores-mediastino"
TITLE = "Tumores de mediastino y timectomía robótica · Dr. David Lazo"
DESC = ("Cirugía robótica de tumores de mediastino anterosuperior y posterior, y timectomía "
        "por timoma o miastenia gravis: técnica y evidencia publicada.")
FECHA = "2026-11-16"

# Todas verificadas en PubMed el 16-nov-2026 (autores, revista, volumen, páginas, DOI y cifras del resumen)
REFS = [
 ("Carter BW, Tomiyama N, Bhora FY, et al. A modern definition of mediastinal compartments.", "J Thorac Oncol", "2014;9(9 Suppl 2):S97-101.", "10.1097/JTO.0000000000000292"),
 ("Asaf BB, Bishnoi S, Vardhanpuri H, et al. Robotic excision of posterior mediastinal neurogenic tumours: technique and surgical outcomes.", "J Minim Access Surg", "2024;20(2):136-141.", "10.4103/jmas.jmas_151_22"),
 ("Wolfe GI, Kaminski HJ, Aban IB, et al. Randomized trial of thymectomy in myasthenia gravis.", "N Engl J Med", "2016;375(6):511-522.", "10.1056/NEJMoa1602489"),
 ("Rückert JC, Swierzy M, Ismail M. Comparison of robotic and nonrobotic thoracoscopic thymectomy: a cohort study.", "J Thorac Cardiovasc Surg", "2011;141(3):673-677.", "10.1016/j.jtcvs.2010.11.042"),
 ("Marulli G, Rea F, Melfi F, et al. Robot-aided thoracoscopic thymectomy for early-stage thymoma: a multicenter European study.", "J Thorac Cardiovasc Surg", "2012;144(5):1125-1130.", "10.1016/j.jtcvs.2012.07.082"),
 ("Yang CJ, Hurd J, Shah SA, et al. A national analysis of open versus minimally invasive thymectomy for stage I to III thymoma.", "J Thorac Cardiovasc Surg", "2020;160(2):555-567.e15.", "10.1016/j.jtcvs.2019.11.114"),
 ("Wu WJ, Zhang FY, Xiao Q, Li XK. Does robotic-assisted thymectomy have advantages over video-assisted thymectomy in short-term outcomes? A systematic view and meta-analysis.", "Interact Cardiovasc Thorac Surg", "2021;33(3):385-394.", "10.1093/icvts/ivab109"),
]

# ---------- VIDEOS: pegar el ID de YouTube (o "local" para MP4 propio) ----------
VID_BASE = sys.argv[3] if len(sys.argv) > 3 else "/videos/"
VIDEOS = {
  "posterior": {"id": None, "local": "tumor-neurogenico-mediastino", "yt": "https://www.youtube.com/shorts/w8D6EowlRTQ", "duracion": "PT17S", "subido": "2026-11-18", "formato": "9/16", "titulo": "Resección robótica de tumor neurogénico mediastínico", "texto": "Tumor neurogénico encapsulado en el mediastino posterior. Incisión pleural peritumoral y disección en plano subpleural, disección circunferencial de la cápsula con energía bipolar, disección del plano profundo sobre la pared costal posterior y enucleación íntegra del tumor con control del lecho paravertebral."},
  "subxifoidea": {"id": None, "local": "timectomia-subxifoidea", "yt": "https://www.youtube.com/shorts/MM3SPFpmpZo", "duracion": "PT58S", "subido": "2026-11-18", "formato": "9/16", "titulo": "Timectomía robótica subxifoidea", "texto": "Paciente en decúbito dorsal con tres brazos robóticos: cámara subxifoidea y un brazo pleural a cada lado en línea medioclavicular. Acceso subxifoideo y apertura pleural mediastínica bilateral, movilización en bloque del timoma sobre el pericardio, visión panorámica con preservación de ambos nervios frénicos, disección de la vena innominada y de los cuernos tímicos superiores, extracción subxifoidea en bolsa y control del lecho quirúrgico."},
  "timectomia": {"id": None, "local": "timectomia-robotica", "yt": "https://www.youtube.com/shorts/GJTmgVj_ilA", "duracion": "PT39S", "subido": "2026-11-16", "formato": "9/16", "titulo": "Timectomía robótica por el hemitórax izquierdo", "texto": "Timectomía robótica por el hemitórax izquierdo en un tumor tímico. Apertura de la pleura anterior y del espacio retroesternal, disección y sección del polo superior izquierdo del timo, control y sección de la vena tímica junto al tumor, disección y resección del cuerno superior derecho, liberación final y resección completa de la glándula tímica. Pieza quirúrgica en bloque con el tumor tímico."},
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
 "name": "Tumores de mediastino y timectomía robótica",
 "description": DESC, "inLanguage": "es-CL",
 "about": [
   {"@type": "MedicalCondition", "name": "Tumores del mediastino", "alternateName": ["Tumor de mediastino", "Masa mediastínica"]},
   {"@type": "MedicalProcedure", "name": "Timectomía robótica", "alternateName": ["Timectomía extendida", "Timectomía mínimamente invasiva"]},
   {"@type": "MedicalProcedure", "name": "Resección robótica de tumores del mediastino"}],
 "author": {"@id": "https://cirugiatoracica.cl/#david-lazo"},
 "reviewedBy": {"@id": "https://cirugiatoracica.cl/#david-lazo"},
 "lastReviewed": FECHA, "dateModified": FECHA,
 "specialty": "https://schema.org/Surgical",
 "isPartOf": {"@type": "WebSite", "@id": "https://rats.cl/#website", "url": "https://rats.cl/", "name": "rats.cl", "inLanguage": "es-CL"},
 "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
   {"@type": "ListItem", "position": 1, "name": "Cirugía robótica torácica", "item": "https://rats.cl/"},
   {"@type": "ListItem", "position": 2, "name": "Tumores de mediastino", "item": URL}]},
 "citation": [f"{a} {j}. {c}" for a, j, c, d in REFS],
}
ld = '<script type="application/ld+json">\n' + json.dumps(webpage, ensure_ascii=False, indent=2) + '\n  </script>'
for clave, v in VIDEOS.items():
    if v.get("local"):
        vo = {"@context": "https://schema.org", "@type": "VideoObject", "@id": f"{URL}#video-{clave}",
              "name": v["titulo"] + " | RATS", "description": v["texto"], "uploadDate": v["subido"] + "T00:00:00-03:00", "duration": v["duracion"],
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
H3 = "font-family:'Bebas Neue',sans-serif;font-size:clamp(30px,3vw,40px);line-height:1;margin-bottom:16px"

def columna(nombre, sub, items, anchor=None):
    aid = f' id="{anchor}"' if anchor else ''
    return f'''        <div{aid} style="flex:1 1 400px;max-width:600px;border-top:3px solid #0B0B0B;padding-top:14px;scroll-margin-top:60px">
          <p style="{LBL};color:#C4500E;margin-bottom:4px">{sub}</p>
          <h3 style="{H3}">{nombre}</h3>
{ul(items)}        </div>
'''

def esquema_compartimentos():
    # Corte axial esquemático (vista caudal, convención radiológica): anterior arriba
    T = "font-family:Public Sans,sans-serif"
    return f'''<svg viewBox="0 0 560 300" role="img" aria-label="Corte axial esquemático del tórax con los tres compartimentos del mediastino" style="width:100%;max-width:520px;display:block;border:2px solid #0B0B0B;background:#fff">
  <ellipse cx="210" cy="150" rx="196" ry="132" fill="#F6F5F1" stroke="#0B0B0B" stroke-width="2"/>
  <ellipse cx="96" cy="152" rx="70" ry="98" fill="#fff" stroke="#3A3A3A" stroke-width="1.2"/>
  <ellipse cx="324" cy="152" rx="70" ry="98" fill="#fff" stroke="#3A3A3A" stroke-width="1.2"/>
  <text x="96" y="156" text-anchor="middle" {T} font-size="11" fill="#3A3A3A">pulmón</text>
  <text x="324" y="156" text-anchor="middle" {T} font-size="11" fill="#3A3A3A">pulmón</text>
  <rect x="190" y="18" width="40" height="16" fill="#0B0B0B"/><text x="210" y="14" text-anchor="middle" {T} font-size="10" fill="#3A3A3A">esternón</text>
  <path d="M170 40 Q210 32 250 40 L246 84 Q210 76 174 84 Z" fill="#67D3E8" fill-opacity="0.55" stroke="#0E7490" stroke-width="1.5"/>
  <path d="M174 86 Q210 78 246 86 L252 200 Q210 212 168 200 Z" fill="#D9D7D0" stroke="#3A3A3A" stroke-width="1.5"/>
  <circle cx="210" cy="118" r="16" fill="#fff" stroke="#3A3A3A"/><text x="210" y="122" text-anchor="middle" {T} font-size="9" fill="#3A3A3A">aorta</text>
  <circle cx="210" cy="166" r="11" fill="#fff" stroke="#3A3A3A"/><text x="210" y="190" text-anchor="middle" {T} font-size="9" fill="#3A3A3A">esófago</text>
  <circle cx="210" cy="238" r="26" fill="#fff" stroke="#0B0B0B" stroke-width="2"/><text x="210" y="242" text-anchor="middle" {T} font-size="9" fill="#0B0B0B">vértebra</text>
  <path d="M150 214 L180 214 L180 270 L150 262 Z" fill="#C4500E" fill-opacity="0.45" stroke="#C4500E" stroke-width="1.5"/>
  <path d="M240 214 L270 214 L270 262 L240 270 Z" fill="#C4500E" fill-opacity="0.45" stroke="#C4500E" stroke-width="1.5"/>
  <line x1="148" y1="214" x2="272" y2="214" stroke="#0B0B0B" stroke-width="1.2" stroke-dasharray="4 3"/>
  <line x1="248" y1="58" x2="430" y2="58" stroke="#0E7490" stroke-width="1"/><circle cx="248" cy="58" r="3" fill="#0E7490"/>
  <text x="436" y="62" {T} font-size="12" font-weight="700" fill="#0E7490">1 · anterosuperior</text><text x="436" y="76" {T} font-size="10.5" fill="#0E7490">prevascular</text>
  <line x1="240" y1="150" x2="430" y2="150" stroke="#3A3A3A" stroke-width="1"/><circle cx="240" cy="150" r="3" fill="#3A3A3A"/>
  <text x="436" y="154" {T} font-size="12" font-weight="700" fill="#3A3A3A">2 · medio</text><text x="436" y="168" {T} font-size="10.5" fill="#3A3A3A">visceral</text>
  <line x1="262" y1="242" x2="430" y2="242" stroke="#C4500E" stroke-width="1"/><circle cx="262" cy="242" r="3" fill="#C4500E"/>
  <text x="436" y="246" {T} font-size="12" font-weight="700" fill="#C4500E">3 · posterior</text><text x="436" y="260" {T} font-size="10.5" fill="#C4500E">paravertebral</text>
</svg>'''

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
TD = 'style="padding:12px 14px;border-top:1px solid #0B0B0B;vertical-align:top"'
TH = 'style="text-align:left;padding:12px 14px;font-size:10.5px;letter-spacing:0.18em;text-transform:uppercase;background:#0B0B0B;color:#F6F5F1"'
def tabla(cab, filas, minw=640):
    th = ''.join(f'<th {TH}>{c}</th>' for c in cab)
    tb = ''.join('<tr>' + ''.join((f'<td {TD[:-1]};font-weight:700{";white-space:nowrap" if minw < 640 else ""}">{x}</td>' if k == 0 else f'<td {TD}>{x}</td>') for k, x in enumerate(f)) + '</tr>\n' for f in filas)
    return f'''      <div style="overflow-x:auto;border:2px solid #0B0B0B;background:#fff;margin:6px 0 14px"><table style="width:100%;border-collapse:collapse;font-size:15px;min-width:{minw}px"><thead><tr>{th}</tr></thead><tbody>
{tb}</tbody></table></div>
'''

# §1 Anatomía del mediastino
s_anat = (P("El mediastino es el espacio del tórax entre ambos pulmones, desde el estrecho torácico superior hasta el diafragma. Se divide en tres compartimentos: anterosuperior, medio y posterior, equivalentes a los compartimentos prevascular, visceral y paravertebral de la clasificación por tomografía computada de la ITMIG" + sup(1) + ".", True) +
 '      <div style="display:flex;flex-wrap:wrap;gap:28px;align-items:flex-start;margin:6px 0 8px">\n'
 f'        <figure style="flex:0 1 520px;margin:0">{esquema_compartimentos()}<figcaption style="font-size:12.5px;color:#3A3A3A;margin-top:8px">Corte axial esquemático. La línea discontinua marca el límite entre el mediastino medio (visceral) y el posterior (paravertebral), 1 cm por detrás del borde anterior de los cuerpos vertebrales.</figcaption></figure>\n'
 '        <div style="flex:1 1 380px">\n' +
 tabla(["Compartimento", "Límites", "Contenido"], [
   ("1 · Anterosuperior<br><span style='font-weight:400;color:#3A3A3A'>prevascular</span>", "Por delante, el esternón; por detrás, la cara anterior del pericardio", "Timo, grasa, ganglios linfáticos y vena braquiocefálica izquierda"),
   ("2 · Medio<br><span style='font-weight:400;color:#3A3A3A'>visceral</span>", "Por detrás, una línea 1 cm posterior al borde anterior de los cuerpos vertebrales", "Corazón y pericardio, aorta, vena cava superior, tráquea, esófago, conducto torácico y ganglios"),
   ("3 · Posterior<br><span style='font-weight:400;color:#3A3A3A'>paravertebral</span>", "A ambos lados de la columna torácica, hasta las apófisis transversas", "Columna torácica, nervios intercostales, raíces nerviosas y cadena simpática"),
 ], minw=520) +
 '        </div>\n      </div>\n')

# §2 Tumores del mediastino
s_tum = (P("El compartimento donde está la lesión orienta el diagnóstico diferencial, los exámenes y la vía de abordaje.", True) +
 tabla(["Compartimento", "Lesiones más frecuentes"], [
   ("1 · Anterosuperior<br><span style='font-weight:400;color:#3A3A3A'>prevascular</span>", "Las <strong>4 T</strong>: <strong>T</strong>imoma y carcinoma tímico · <strong>T</strong>eratoma y otros tumores de células germinales · <strong>T</strong>iroides (bocio endotorácico) · «<strong>T</strong>errible» linfoma. Además, quistes tímicos"),
   ("2 · Medio<br><span style='font-weight:400;color:#3A3A3A'>visceral</span>", "Adenopatías, quistes broncogénicos y pericárdicos, tumores del esófago"),
   ("3 · Posterior<br><span style='font-weight:400;color:#3A3A3A'>paravertebral</span>", "Tumores neurogénicos: schwannoma, neurofibroma, ganglioneuroma"),
 ], minw=360) +
 ul([
   "Los tumores neurogénicos son los más frecuentes del mediastino posterior" + sup(2) + ". Se originan en nervios intercostales, raíces nerviosas o cadena simpática.",
   "En el linfoma y en los tumores de células germinales malignos el tratamiento inicial es médico; la cirugía aporta la biopsia o reseca la masa residual.",
   'Los tumores tímicos se tratan con resección del tumor junto con todo el timo (<a href="#anterosuperior">timectomía</a>).',
 ]))

def videos_en(*claves):
    vs = [VIDEOS[c] for c in claves if c in VIDEOS]
    if not vs: return ''
    return ('      <div style="display:flex;flex-wrap:wrap;gap:48px 224px;align-items:flex-start;justify-content:center;margin-top:24px">\n'
            + ''.join(bloque_video(c, VIDEOS[c]["titulo"]) for c in claves if c in VIDEOS) + '      </div>\n'
            + (AUTOPLAY if any(v["id"] for v in vs) else '') + (AUTOPLAY_MP4 if any(v.get("local") for v in vs) else ''))

# §3 Tumores del mediastino anterosuperior y del timo
s_ant = (P("El timo ocupa el mediastino anterosuperior. La timectomía, extirpación del timo junto con la grasa que lo rodea, se indica en los tumores tímicos y en la miastenia gravis; la misma vía permite resecar los demás tumores de este compartimento.", True) +
 '      <div style="display:flex;flex-wrap:wrap;gap:32px;margin-top:10px">\n' +
 columna("Tumores tímicos", "Timoma · carcinoma tímico", [
   "Timectomía total con el tumor, sin abrir su cápsula.",
   "El estadio y el tipo histológico definen si se requiere tratamiento complementario.",
 ]) +
 columna("Miastenia gravis", "Con o sin timoma", [
   "En la miastenia gravis generalizada con anticuerpos contra el receptor de acetilcolina, sin timoma, la timectomía más prednisona mejoró la evolución a 3 años frente a prednisona sola en un ensayo aleatorizado (MGTX)" + sup(3) + ".",
   "La cirugía se planifica con el neurólogo y se programa con la enfermedad estable.",
 ]) +
 '      </div>\n' +
 '      <h3 style="' + H3 + ';margin-top:22px">Timectomía extendida</h3>\n' +
 ul([
   "Se reseca el timo completo con la grasa del mediastino anterosuperior: de un nervio frénico al otro y desde el diafragma hasta los polos tímicos en el cuello.",
   "Incluye la grasa pericardiofrénica y la de la ventana aortopulmonar, que pueden contener tejido tímico.",
 ]) +
 '      <h3 style="' + H3 + ';margin-top:22px">Técnica robótica</h3>\n' +
 ul([
   "Acceso robótico: nuestra vía preferente es la subxifoidea, ya que permite acceder a ambas cavidades pleurales y tener un manejo completo del mediastino y sus estructuras sin necesidad de una esternotomía o de reposicionar el robot.",
   "Insuflación de CO<sub>2</sub> para ampliar el espacio de trabajo.",
   "Se identifican y preservan ambos nervios frénicos.",
   "Si el tumor compromete pericardio, pulmón o un nervio frénico, se resecan en bloque con él. El compromiso de los grandes vasos suele requerir cirugía abierta.",
 ]) + videos_en("subxifoidea", "timectomia"))

# §4 Tumores del mediastino posterior
s_post = (P("Los tumores del mediastino posterior son en su mayoría neurogénicos" + sup(2) + ". Se resecan por vía robótica, por incisiones pequeñas entre las costillas, sin toracotomía.", True) +
 ul([
   "Acceso por el hemitórax del lado del tumor.",
   "Resección completa del tumor con su cápsula y control del nervio de origen en el agujero de conjunción.",
   "Tumores en reloj de arena, con extensión al canal raquídeo: se estudian con resonancia magnética y se operan junto con neurocirugía.",
   "Tumores del vértice: proximidad del ganglio estrellado (síndrome de Horner) y del plexo braquial. Tumores bajos: proximidad de la arteria de Adamkiewicz, que irriga la médula espinal.",
 ]) + videos_en("posterior"))

s4 = tabla(["Estudio", "Pacientes", "Resultado"], [
 ("MGTX · Wolfe 2016" + sup(3), "126 pacientes con miastenia gravis generalizada sin timoma, aleatorizados a timectomía extendida por esternotomía más prednisona o prednisona sola",
  "A 3 años, con timectomía: menor puntaje de gravedad (QMG 6,15 y 8,99), menor dosis de prednisona (44 y 60 mg en días alternos) y menos hospitalizaciones por exacerbación (9% y 37%)"),
 ("Rückert 2011" + sup(4), "153 pacientes con miastenia gravis: timectomía robótica (74) o toracoscópica convencional (79)",
  "Remisión completa acumulada a 42 meses: 39,3% y 20,3%"),
 ("Marulli 2012" + sup(5), "79 pacientes con timoma en estadio I-II de Masaoka, operados por vía robótica en 4 centros europeos",
  "Una conversión a cirugía abierta; complicaciones en 12,7%; estadía mediana de 3 días; sobrevida a 5 años de 90%"),
 ("NCDB · Yang 2020" + sup(6), "1.223 timectomías por timoma en estadio I-III: 317 mínimamente invasivas (176 robóticas) y 906 abiertas",
  "En el análisis pareado, con cirugía mínimamente invasiva: estadía de 3 y 4 días, sin diferencias en márgenes positivos ni en sobrevida a 5 años (89,4% y 81,6%)"),
 ("Wu 2021 · metaanálisis" + sup(7), "9 estudios, 723 pacientes: timectomía robótica (315) o videotoracoscópica (408)",
  "Con el robot: menos conversiones y menor duración del drenaje; recurrencia similar"),
 ("Asaf 2024" + sup(2), "20 pacientes con tumores neurogénicos del mediastino posterior resecados por vía robótica",
  "Schwannoma, la histología más frecuente; 2 conversiones; estadía de 2,4 días"),
])
refs = ''.join(f'        <li id="ref-{i}" style="margin:8px 0;scroll-margin-top:60px">{a} <em>{j}</em>. {c} <a href="https://doi.org/{d}" target="_blank" rel="noopener">DOI</a></li>\n' for i, (a, j, c, d) in enumerate(REFS, 1))
s5 = f'      <ol style="padding-left:22px;max-width:920px;font-size:14.5px">\n{refs}      </ol>\n'

NAVA = "font-family:'Public Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;padding:14px 18px;display:block;text-decoration:none;border-right:1px solid #333;color:#F6F5F1"
nav_items = [("https://rats.cl", "← rats.cl", True), ("#anatomia", "Anatomía", False), ("#tumores", "Tumores", False), ("#anterosuperior", "Anterosuperior y timo", False), ("#posterior", "Posterior", False), ("#evidencia", "Evidencia", False)]
nav = ''.join(f'<a href="{h}" style="{NAVA}{";color:#9A9A9A" if g else ""}" class="hv4">{t}</a>\n        ' for h, t, g in nav_items)

body = f'''{topbar}<header style="border-bottom:3px solid #0B0B0B">
      <div style="max-width:1280px;margin:0 auto;padding:20px 24px 0;display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:16px">
        <div>
          <p style="font-size:10.5px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#C4500E;margin-bottom:6px"><a href="https://rats.cl" style="color:#C4500E">RATS</a> · Mediastino · Dr. David Lazo Pérez</p>
          <h1 style="font-family:'Bebas Neue',sans-serif;font-size:clamp(46px,7.5vw,112px);line-height:0.86;letter-spacing:0.005em">Tumores de mediastino</h1>
        </div>
        <a href="#contacto" style="background:#C4500E;color:#fff;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;padding:14px 18px;margin-bottom:8px" class="hv5">Agendar consulta</a>
      </div>
      <div style="max-width:1280px;margin:0 auto;padding:14px 24px 0">
        <p style="font-size:13px;border-top:1px solid #0B0B0B;padding-top:10px;padding-bottom:14px">Cirugía robótica de tumores del mediastino anterosuperior y posterior, y timectomía por tumores tímicos o miastenia gravis.</p>
      </div>
    </header>
    <nav aria-label="Tumores de mediastino" style="position:sticky;top:0;z-index:50;background:#0B0B0B;color:#F6F5F1">
      <div style="max-width:1280px;margin:0 auto;padding:0 24px;display:flex;flex-wrap:wrap;align-items:stretch">
        {nav}</div>
    </nav>
    <main style="max-width:1280px;margin:0 auto;padding:0 24px">
{sec(1, "anatomia", "Anatomía del mediastino", s_anat)}{sec(2, "tumores", "Tumores del mediastino", s_tum)}{sec(3, "anterosuperior", "Tumores del mediastino anterosuperior y del timo", s_ant)}{sec(4, "posterior", "Tumores del mediastino posterior", s_post)}{sec(5, "evidencia", "Evidencia publicada", s4)}{sec(None, "referencias", "Referencias", s5, last=True)}  </main>
'''
out = head + physician + '\n  ' + ld + '\n' + ga + '</head>\n' + body + contact_footer
open(sys.argv[2], 'w', encoding='utf-8').write(out)
print(len(TITLE), len(DESC), len(out))
