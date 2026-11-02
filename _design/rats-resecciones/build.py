import re,json,html,sys
from pathlib import Path
REPO=Path(sys.argv[1]); OUTDIR=Path(sys.argv[2]); MODE=sys.argv[3]  # 'final' or 'preview'
MAQ = MODE=='preview'
src=(REPO/'dist/rats/operculo-toracico/index.html').read_text()
ACC='#C4500E'; BG2='#EDEBE6'; TODAY='2026-10-31'
BASE='https://rats.cl/resecciones'
PAGES=[('','Resecciones'),('cuna','01 Cuña'),('segmentectomia','02 Segmentectomía'),('lobectomia','03 Lobectomía')]
IMG_SEG='imgs/lobulos-segmentos.webp' if MAQ else '/verde-indocianina/imgs/lobulos-segmentos.webp'
def IMG3D(k): return ('imgs/' if MAQ else '/resecciones/imgs/')+f'reseccion-{k}.webp'
DIM={'cuna':(748,1100),'segmentectomia':(703,1100),'lobectomia':(635,1100)}
ALT={'cuna':'Ilustración 3D del pulmón derecho en vista lateral: resección en cuña del borde anterior del lóbulo superior, con el nódulo dentro de la pieza y la línea de grapas en el pulmón y en la pieza',
 'segmentectomia':'Ilustración 3D del pulmón derecho: segmentectomía del segmento posterior del lóbulo superior (S2); el segmento, en forma de pirámide, se separa del lóbulo y quedan los muñones de su bronquio, arteria y vena',
 'lobectomia':'Ilustración 3D del pulmón derecho: lobectomía superior; el lóbulo superior se separa de los lóbulos medio e inferior y quedan los muñones del bronquio, la arteria y la vena del lóbulo'}
CAP={'cuna':'Resección en cuña de un nódulo periférico del lóbulo superior derecho. La pieza incluye el nódulo con un margen de tejido sano.',
 'segmentectomia':'Segmentectomía del segmento posterior del lóbulo superior derecho (S2), con sección de su bronquio, su arteria y su vena.',
 'lobectomia':'Lobectomía superior derecha: muñones del bronquio, la arteria y la vena del lóbulo.'}
def fig3d(k): 
    w,h=DIM[k]
    return f'''<figure style="flex:1 1 320px;max-width:460px;margin:0">
          <img src="{IMG3D(k)}" alt="{ALT[k]}" width="{w}" height="{h}" style="width:100%;display:block;border:2px solid #0B0B0B;background:#fff" loading="lazy" />
          <figcaption style="font-size:12.5px;color:#3A3A3A;margin-top:8px">{CAP[k]}</figcaption>
        </figure>'''
def url(slug): return BASE+('/'+slug if slug else '')
def link(slug):
    if not MAQ: return url(slug)
    return (slug or 'index')+'.html'
ICG_URL='https://rats.cl/verde-indocianina'

refs=[
 ('ginsberg','Ginsberg RJ, Rubinstein LV. Randomized trial of lobectomy versus limited resection for T1 N0 non-small cell lung cancer. Lung Cancer Study Group. <em>Ann Thorac Surg</em>. 1995;60(3):615-622.','10.1016/0003-4975(95)00537-u'),
 ('jcog0802','Saji H, Okada M, Tsuboi M, et al. Segmentectomy versus lobectomy in small-sized peripheral non-small-cell lung cancer (JCOG0802/WJOG4607L): a multicentre, open-label, phase 3, randomised, controlled, non-inferiority trial. <em>Lancet</em>. 2022;399(10335):1607-1617.','10.1016/S0140-6736(21)02333-3'),
 ('calgb','Altorki N, Wang X, Kozono D, et al. Lobar or sublobar resection for peripheral stage IA non-small-cell lung cancer. <em>N Engl J Med</em>. 2023;388(6):489-498.','10.1056/NEJMoa2212083'),
 ('jcog1211','Aokage K, Suzuki K, Saji H, et al. Segmentectomy for ground-glass-dominant lung cancer with a tumour diameter of 3 cm or less including ground-glass opacity (JCOG1211): a multicentre, single-arm, confirmatory, phase 3 trial. <em>Lancet Respir Med</em>. 2023;11(6):540-549.','10.1016/S2213-2600(23)00041-3'),
 ('jcog0804','Suzuki K, Watanabe SI, Wakabayashi M, et al. A single-arm study of sublobar resection for ground-glass opacity dominant peripheral lung cancer. <em>J Thorac Cardiovasc Surg</em>. 2022;163(1):289-301.e2.','10.1016/j.jtcvs.2020.09.146'),
 ('miyoshi','Miyoshi T, Ito H, Wakabayashi M, et al. Risk factors for loss of pulmonary function after wedge resection for peripheral ground-glass opacity dominant lung cancer. <em>Eur J Cardiothorac Surg</em>. 2023;64(6).','10.1093/ejcts/ezad365'),
 ('geraci','Geraci TC, Ferrari-Light D, Kent A, et al. Technique, outcomes with navigational bronchoscopy using indocyanine green for robotic segmentectomy. <em>Ann Thorac Surg</em>. 2019;108(2):363-369.','10.1016/j.athoracsur.2019.03.032'),
 ('violet','Lim E, Harris RA, McKeon HE, et al. Impact of video-assisted thoracoscopic lobectomy versus open lobectomy for lung cancer on recovery assessed using self-reported physical function: VIOLET RCT. <em>Health Technol Assess</em>. 2022;26(48):1-162.','10.3310/THBQ1793'),
 ('rvlob','Jin R, Zheng Y, Yuan Y, et al. Robotic-assisted versus video-assisted thoracoscopic lobectomy: short-term results of a randomized clinical trial (RVlob trial). <em>Ann Surg</em>. 2022;275(2):295-302.','10.1097/SLA.0000000000004922'),
]
REF={k:(t,d) for k,t,d in refs}

TH='text-align:left;padding:12px 14px;font-size:10.5px;letter-spacing:0.18em;text-transform:uppercase;background:#0B0B0B;color:#F6F5F1'
TD='padding:12px 14px;border-top:1px solid #0B0B0B;vertical-align:top'
SEC='<section style="padding:32px 0;border-bottom:1px solid #0B0B0B">'
class Page:
    def __init__(s): s.order=[]
    def r(s,*ks):
        out=[]
        for k in ks:
            if k not in s.order: s.order.append(k)
            n=s.order.index(k)+1; out.append(f'<a href="#ref-{n}" style="font-weight:700">{n}</a>')
        return '<sup>'+','.join(out)+'</sup>'
def H2(n,t,id_): return f'''<div id="{id_}" style="display:flex;align-items:baseline;gap:16px;border-bottom:2px solid #0B0B0B;padding-bottom:8px;margin-bottom:24px;scroll-margin-top:60px">
        {f"<span style=\"font-family:'Bebas Neue',sans-serif;font-size:34px;line-height:1;color:{ACC}\">§{n}</span>" if n else ''}
        <h2 style="font-family:'Bebas Neue',sans-serif;font-size:clamp(28px,3.4vw,46px);line-height:1">{t}</h2>
      </div>'''
def Pp(t,lead=False): return f'<p style="font-size:{17 if lead else 16.5}px;{"font-weight:500;" if lead else ""}max-width:920px;margin-bottom:14px">{t}</p>'
def UL(items): return '<ul style="max-width:920px;margin:0 0 14px;padding-left:0;list-style:none">'+''.join(f'<li style="font-size:16.5px;padding:10px 0 10px 22px;border-top:1px solid #0B0B0B;position:relative"><span style="position:absolute;left:0;top:10px;color:{ACC};font-weight:700">—</span>{i}</li>' for i in items)+'</ul>'
def media(label): return f'<div style="flex:1 1 360px;aspect-ratio:16/9;border:2px dashed #0B0B0B;display:flex;align-items:center;justify-content:center;text-align:center;padding:16px;font-size:13px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#3A3A3A;background:{BG2}">{label}</div>'
def table(head,rows,minw=640):
    h=''.join(f'<th style="{TH}">{x}</th>' for x in head)
    b='\n'.join('<tr>'+''.join(f'<td style="{TD}{";font-weight:700;white-space:nowrap" if i==0 else ""}">{c}</td>' for i,c in enumerate(row))+'</tr>' for row in rows)
    return f'<div style="overflow-x:auto;border:2px solid #0B0B0B;background:#fff;margin:6px 0 14px"><table style="width:100%;border-collapse:collapse;font-size:15px;min-width:{minw}px"><thead><tr>{h}</tr></thead><tbody>\n{b}\n</tbody></table></div>'
EV=['Estudio','Pacientes','Resultados']
def refs_html(p):
    items='\n'.join(f'        <li id="ref-{i+1}" style="margin:8px 0;scroll-margin-top:60px">{REF[k][0]} <a href="https://doi.org/{REF[k][1]}" target="_blank" rel="noopener">DOI</a></li>' for i,k in enumerate(p.order))
    return f'''<section style="padding:32px 0">
      {H2('','Referencias','referencias')}
      <ol style="padding-left:22px;max-width:920px;font-size:14.5px">
{items}
      </ol>
    </section>'''
def video_sec(n,label,yt=None,title='',text=''):
    if yt:
        return f'''{SEC}
      {H2(n,'Video','video')}
      <div style="display:flex;flex-wrap:wrap;gap:32px;align-items:center">
        <div style="flex:0 1 360px;max-width:360px;width:100%">
          <div style="position:relative;aspect-ratio:9/16;border:2px solid #0B0B0B;background:#0B0B0B">
            <iframe class="yt-auto" src="https://www.youtube-nocookie.com/embed/{yt}?rel=0&amp;playsinline=1&amp;mute=1&amp;loop=1&amp;playlist={yt}&amp;enablejsapi=1" title="{title}" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
          </div>
        </div>
        <div style="flex:1 1 320px;max-width:560px">{Pp(text,True) if text else ''}<p style="font-size:14px"><a href="https://www.youtube.com/shorts/{yt}" target="_blank" rel="noopener">Ver en YouTube →</a></p></div>
      </div>
      <script>(function(){{var f=document.currentScript.parentNode.querySelector('iframe.yt-auto');if(!f||!('IntersectionObserver' in window))return;
      function cmd(c){{try{{f.contentWindow.postMessage(JSON.stringify({{event:'command',func:c,args:[]}}),'*');}}catch(e){{}}}}
      var vis=false;f.addEventListener('load',function(){{if(vis){{cmd('mute');cmd('playVideo');}}}});
      new IntersectionObserver(function(es){{es.forEach(function(e){{vis=e.isIntersecting;if(vis){{cmd('mute');cmd('playVideo');}}else{{cmd('pauseVideo');}}}});}},{{threshold:0.5}}).observe(f);}})();</script>
    </section>'''
    return f'''{SEC}
      {H2(n,'Video','video')}
      <div style="display:flex;flex-wrap:wrap;gap:16px">{media(label)}</div>
    </section>''' if MAQ else ''

# ---------------- esquemas (de videotoracoscopia.cl/cirugia-nodulo-pulmonar) ----------------
OL='M100,12 C72,12 44,58 34,118 C24,178 28,226 44,242 C76,254 150,254 172,238 C184,198 180,150 162,110 C147,72 126,12 100,12 Z'
FI='<g fill="none" stroke="#9A9A9A" stroke-width="2"><path d="M150,82 C122,140 84,190 42,214" /><path d="M32,132 C70,138 100,140 126,128" /></g>'
HL={'cuna':('M33,96 L66,108 L37,132 C33,120 32,108 33,96 Z',(44,112)),
    'segmentectomia':('M100,12 C76,12 54,42 44,74 L104,88 L124,42 C116,24 108,12 100,12 Z',(88,52)),
    'lobectomia':('M100,12 C72,12 44,58 34,118 L32,132 C70,138 100,140 126,128 C134,112 142,96 150,82 C140,50 122,12 100,12 Z',(88,52))}
NAME={'cuna':'Resección en cuña','segmentectomia':'Segmentectomía','lobectomia':'Lobectomía'}
def lung(k,maxw=170):
    d,(cx,cy)=HL[k]
    return f'<svg viewBox="0 0 206 266" role="img" aria-label="Esquema: {NAME[k].lower()}" style="width:100%;max-width:{maxw}px;height:auto;display:block;margin:0 auto"><path d="{d}" fill="#2F8F5B" fill-opacity="0.55"/><path d="{OL}" fill="none" stroke="#0B0B0B" stroke-width="2"/>{FI}<circle cx="{cx}" cy="{cy}" r="6" fill="#C62828"/></svg>'
NOTE='Esquema: en verde, la porción de pulmón que se reseca; en rojo, el nódulo.'
DEF={'cuna':'Resección no anatómica de una porción periférica del pulmón que contiene el nódulo, con un margen de tejido sano. También se llama resección atípica o <i>wedge</i>.',
     'segmentectomia':'Resección anatómica de un segmento pulmonar, con su arteria, su vena y su bronquio. También se llama resección segmentaria típica.',
     'lobectomia':'Resección de un lóbulo pulmonar completo, con su arteria, su vena y su bronquio.'}
def que_es(k,extra,fig=None):
    fig=fig or fig3d(k)
    return f'''{SEC}
      {H2(1,'Qué es','que-es')}
      <div style="display:flex;flex-wrap:wrap;gap:32px;align-items:center">
        <div style="flex:1 1 420px;max-width:640px">
          {Pp(DEF[k],True)}
          {extra}
        </div>
        {fig}
      </div>
    </section>'''

FAQ_INDEX=[
 ('¿Qué diferencia hay entre una resección en cuña y una segmentectomía?','La cuña retira una porción periférica del pulmón alrededor del nódulo, sin seguir los límites anatómicos y sin seccionar vasos ni bronquios. La segmentectomía retira un segmento pulmonar completo, con su arteria, su vena y su bronquio.'),
 ('¿Cuándo se prefiere una lobectomía?','Los estudios que compararon la segmentectomía o la resección sublobar con la lobectomía incluyeron tumores periféricos de 2 cm o menos sin compromiso ganglionar. Fuera de ese grupo, la lobectomía sigue siendo la resección habitual para el cáncer pulmonar.'),
 ('¿Cuánta función pulmonar se pierde?','Depende de cuánto pulmón se reseca. En el estudio JCOG0802, la caída del VEF1 al año fue 3,5 puntos menor con segmentectomía que con lobectomía. En el estudio CALGB 140503, la diferencia a los 6 meses fue de 2 puntos a favor de la resección sublobar.'),
 ('¿Se pueden hacer por cirugía robótica?','Sí. Las tres resecciones se pueden hacer con el robot da Vinci, por incisiones pequeñas entre las costillas y sin separarlas. La elección depende de la lesión y del paciente, no de la plataforma.'),
]

def FAQREF(p,q):
    if q.startswith('¿Cuándo se prefiere'): return p.r('jcog0802','calgb')
    if q.startswith('¿Cuánta función'): return p.r('jcog0802','calgb')
    return ''
def body_index(p):
    def card(k,num):
        return f'''<a href="{link(k)}" style="flex:1 1 280px;display:flex;flex-direction:column;gap:12px;border:2px solid #0B0B0B;border-top:6px solid {ACC};background:#fff;padding:22px;color:#0B0B0B;text-decoration:none" class="hv3c">
          <span style="font-family:'Bebas Neue',sans-serif;font-size:30px;line-height:1;color:{ACC}">{num}</span>
          {lung(k)}
          <span style="font-family:'Bebas Neue',sans-serif;font-size:34px;line-height:0.95">{NAME[k]}</span>
          <span style="font-size:15px">{DEF[k]}</span>
          <span style="margin-top:auto;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:{ACC}">Ver página →</span>
        </a>'''
    fh='\n'.join(f'''        <details style="border-bottom:1px solid #0B0B0B;padding:14px 0">
          <summary style="cursor:pointer;list-style:none;font-size:17px;font-weight:700">{q}</summary>
          <p style="font-size:15.5px;margin-top:10px">{a}{FAQREF(p,q)}</p>
        </details>''' for q,a in FAQ_INDEX)
    return f'''{SEC}
      {H2(1,'Cuánto pulmón se reseca','tipos')}
      {Pp('Según el tamaño, la ubicación y el tipo de lesión, se reseca una porción periférica del pulmón, un segmento o un lóbulo completo. Las tres operaciones se pueden hacer por cirugía robótica.',True)}
      <div style="display:flex;flex-wrap:wrap;gap:18px;margin-top:8px">
        {card('cuna','01')}
        {card('segmentectomia','02')}
        {card('lobectomia','03')}
      </div>
      <p style="font-size:12.5px;color:#3A3A3A;margin-top:10px">Esquemas: en verde, la porción de pulmón que se reseca; en rojo, el nódulo.</p>
    </section>

    {SEC}
      {H2(2,'Preguntas frecuentes','faq')}
      <div style="max-width:900px">
{fh}
      </div>
    </section>

    {refs_html(p)}'''

VIDEO_CUNA='Nódulo subpleural del lóbulo superior izquierdo, marcado con verde de indocianina antes de la cirugía. Se localiza con la cámara Firefly®, se reseca en cuña con endograpadora robótica y se comprueba con fluorescencia que la lesión queda dentro del margen.'
VIDEO_SEG='Segmentectomía anatómica robótica del segmento posterior del lóbulo superior derecho (S2). Se seccionan en forma selectiva la arteria, el bronquio y la vena del segmento; luego, el ICG intravenoso con la visión Firefly® delimita el segmento sin perfusión y el plano intersegmentario, que se secciona con endograpadora.'

def body_cuna(p):
    return f'''{que_es('cuna',Pp('No sigue los límites anatómicos del pulmón: no se seccionan arterias, venas ni bronquios. La endograpadora corta y sella el tejido alrededor del nódulo.'))}

    {SEC}
      {H2(2,'Indicaciones','indicaciones')}
      {UL([
        'Diagnóstico de un nódulo pulmonar indeterminado, con biopsia contemporánea durante la cirugía.',
        'Cáncer pulmonar periférico pequeño con predominio de vidrio esmerilado. En el estudio JCOG0804 se incluyeron tumores de 2 cm o menos con una proporción de componente sólido de 0,25 o menos.'+p.r('jcog0804'),
        'Metástasis pulmonares periféricas.',
        'Pacientes cuya función pulmonar o condición general no permite una resección mayor.',
      ])}
    </section>

    {SEC}
      {H2(3,'La técnica robótica','tecnica')}
      {Pp('Los nódulos pequeños, en vidrio esmerilado o alejados de la superficie no se ven ni se palpan durante la cirugía robótica, y se marcan antes con <a href="'+ICG_URL+'/nodulos">verde de indocianina</a> o con lipiodol.')}
      {Pp('Una vez localizado, se toma el pulmón con las pinzas del robot y se secciona con endograpadora alrededor del nódulo, con un margen de tejido sano. La pieza se extrae en una bolsa y se analiza durante la cirugía (biopsia contemporánea). Si el resultado es un cáncer y sus características lo indican, en la misma operación se puede completar una segmentectomía o una lobectomía.')}
    </section>

    {video_sec(4,'',yt='w076_YlJ5XE',title='Resección en cuña robótica de un nódulo marcado con verde de indocianina — Dr. David Lazo Pérez',text=VIDEO_CUNA)}

    {SEC}
      {H2(5,'Evidencia publicada','evidencia')}
      {table(EV,[
        ('Ginsberg 1995'+p.r('ginsberg'),'247 pacientes con cáncer pulmonar periférico T1N0, aleatorizados a lobectomía o resección limitada (segmentectomía o cuña amplia)','La resección limitada tuvo el triple de recurrencia local'),
        ('JCOG0804 · Suzuki 2022'+p.r('jcog0804'),'333 pacientes en 51 centros de Japón, con tumores de 2 cm o menos y predominio de vidrio esmerilado; 258 cuñas amplias y 56 segmentectomías','Sobrevida libre de recaída a 5 años: 99,7 %. Sin recaídas locales. Margen quirúrgico mediano de 15 mm. Complicaciones grado 3 o mayor en el 5,4 %, sin grado 4 ni 5'),
        ('Miyoshi 2023'+p.r('miyoshi'),'237 resecciones en cuña del estudio JCOG0804','El 16 % tuvo una caída del VEF1 de 10 % o más. La retracción pleural fue un factor de riesgo independiente'),
      ])}
    </section>

    {refs_html(p)}'''

def body_seg(p):
    extra=Pp('Cada lóbulo se divide en segmentos, cada uno con su propia arteria, vena y bronquio. El límite entre segmentos no se ve en la superficie del pulmón.')+f'''<figure style="margin:14px 0 0;max-width:520px">
          <img src="{IMG_SEG}" alt="Pulmón derecho en vista lateral: a la izquierda, los lóbulos superior, medio e inferior; a la derecha, los segmentos apical, posterior, anterior, lateral, medial, superior y basales anterior, lateral y posterior" width="1200" height="896" style="width:100%;display:block;border:2px solid #0B0B0B;background:#fff" loading="lazy" />
          <figcaption style="font-size:12.5px;color:#3A3A3A;margin-top:8px">Pulmón derecho, vista lateral: lóbulos y segmentos.</figcaption>
        </figure>'''
    fig=None
    return f'''{que_es('segmentectomia',extra,fig)}

    {SEC}
      {H2(2,'Indicaciones','indicaciones')}
      {UL([
        'Cáncer pulmonar periférico de 2 cm o menos con predominio de componente sólido, como en el estudio JCOG0802.'+p.r('jcog0802'),
        'Cáncer pulmonar con predominio de vidrio esmerilado de hasta 3 cm, como en el estudio JCOG1211.'+p.r('jcog1211'),
        'Nódulos demasiado profundos para una resección en cuña con margen adecuado.',
        'Pacientes con función pulmonar reducida, en quienes conviene preservar tejido.',
      ])}
    </section>

    {SEC}
      {H2(3,'La técnica robótica','tecnica')}
      {Pp('Se disecan y seccionan en forma selectiva la arteria, la vena y el bronquio del segmento. El límite entre segmentos se identifica con <a href="'+ICG_URL+'/segmentectomia">verde de indocianina intravenoso</a>, que deja oscuro el segmento sin irrigación, o insuflando el pulmón, y se secciona con endograpadora.')}
      {Pp('Se resecan los ganglios hiliares, interlobares e intrapulmonares y los del mediastino para la etapificación. La biopsia contemporánea confirma el diagnóstico y el margen; si no es suficiente, se puede ampliar a una lobectomía en la misma operación.')}
    </section>

    {video_sec(4,'',yt='BykskDhQulc',title='Segmentectomía S2 derecha robótica con plano intersegmentario por ICG — Dr. David Lazo Pérez',text=VIDEO_SEG)}

    {SEC}
      {H2(5,'Evidencia publicada','evidencia')}
      {table(EV,[
        ('JCOG0802 · Saji 2022'+p.r('jcog0802'),'1.106 pacientes en 70 centros de Japón, con tumores periféricos de 2 cm o menos y predominio de componente sólido, aleatorizados a segmentectomía o lobectomía','Sobrevida global a 5 años: 94,3 % con segmentectomía y 91,1 % con lobectomía. Recaída local: 10,5 % y 5,4 %. Al año, la caída del VEF1 fue 3,5 puntos menor con segmentectomía'),
        ('CALGB 140503 · Altorki 2023'+p.r('calgb'),'697 pacientes con tumores periféricos de 2 cm o menos y ganglios negativos confirmados durante la cirugía, aleatorizados a resección sublobar o lobectomía','Resección sublobar no inferior en sobrevida libre de enfermedad. Sobrevida global a 5 años: 80,3 % y 78,9 %'),
        ('JCOG1211 · Aokage 2023'+p.r('jcog1211'),'357 segmentectomías en 42 centros de Japón, por tumores de hasta 3 cm con predominio de vidrio esmerilado','Sobrevida libre de recaída a 5 años: 98,0 %. Complicaciones grado 3 o 4 en el 2 %, sin muertes'),
        ('Geraci 2019'+p.r('geraci'),'245 segmentectomías robóticas consecutivas de un cirujano (Nueva York)','Resección R0 en el 100 %; morbilidad mayor en 3 pacientes y sin mortalidad a 30 ni 90 días'),
      ])}
    </section>

    {refs_html(p)}'''

def body_lob(p):
    return f'''{que_es('lobectomia',Pp('El pulmón derecho tiene tres lóbulos (superior, medio e inferior) y el izquierdo, dos (superior e inferior).'))}

    {SEC}
      {H2(2,'Indicaciones','indicaciones')}
      {UL([
        'Cáncer pulmonar de células no pequeñas en etapas iniciales y en algunas etapas más avanzadas, como parte de un <a href="https://cancerpulmonar.cl/tratamiento">tratamiento multidisciplinario</a>.',
        'Tumores mayores de 2 cm, centrales o con compromiso ganglionar, que no cumplen los criterios de los estudios de resección sublobar.'+p.r('jcog0802','calgb'),
        'Otras enfermedades localizadas en un lóbulo, como las bronquiectasias.',
      ])}
    </section>

    {SEC}
      {H2(3,'La técnica robótica','tecnica')}
      {Pp('Se opera por incisiones pequeñas entre las costillas, sin separarlas. Se disecan y seccionan la vena, la arteria y el bronquio del lóbulo, en general con endograpadora, y se completan las cisuras.')}
      {Pp('Se resecan los ganglios del hilio y del mediastino para la etapificación. El lóbulo se extrae en una bolsa por una de las incisiones.')}
    </section>

    {video_sec(4,'Video de lobectomía robótica')}

    {SEC}
      {H2(5 if MAQ else 4,'Evidencia publicada','evidencia')}
      {table(EV,[
        ('Ginsberg 1995'+p.r('ginsberg'),'247 pacientes con cáncer pulmonar periférico T1N0, aleatorizados a lobectomía o resección limitada','La lobectomía tuvo un tercio de la recurrencia local de la resección limitada y quedó como la cirugía de elección'),
        ('VIOLET · Lim 2022'+p.r('violet'),'503 pacientes en 9 hospitales del Reino Unido, aleatorizados a lobectomía por videotoracoscopía o por toracotomía','Con videotoracoscopía: mejor función física a las 5 semanas, estadía mediana de 4 y 5 días y menos complicaciones. Sobrevida similar'),
        ('RVlob · Jin 2022'+p.r('rvlob'),'320 pacientes aleatorizados a lobectomía robótica (157) o por videotoracoscopía (163)','Estadía y complicaciones similares, sin mortalidad. Con el robot: más ganglios resecados (mediana 11 y 10) y más estaciones evaluadas (6 y 5); mayor drenaje pleural y mayor costo'),
      ])}
    </section>

    {refs_html(p)}'''

SPEC={
 '':dict(h1='Resecciones pulmonares robóticas',title='Resecciones pulmonares robóticas · Dr. David Lazo Pérez',
   desc='Resección en cuña, segmentectomía y lobectomía por cirugía robótica: cuánto pulmón se reseca en cada una, sus indicaciones y la evidencia publicada.',
   sub='Cuña, segmentectomía y lobectomía por cirugía robótica asistida.',
   name='Resecciones pulmonares robóticas',body=body_index,
   about=[('MedicalProcedure','Resección pulmonar en cuña robótica'),('MedicalProcedure','Segmentectomía pulmonar robótica'),('MedicalProcedure','Lobectomía pulmonar robótica')]),
 'cuna':dict(h1='Resección en cuña robótica',title='Resección en cuña robótica · Dr. David Lazo Pérez',
   desc='Resección pulmonar en cuña por cirugía robótica: qué es, indicaciones, técnica con marcación del nódulo y evidencia del estudio JCOG0804.',
   sub='Resección no anatómica de una porción periférica del pulmón que contiene el nódulo.',
   name='Resección en cuña robótica',body=body_cuna,
   about=[('MedicalProcedure','Resección pulmonar en cuña robótica')]),
 'segmentectomia':dict(h1='Segmentectomía robótica',title='Segmentectomía pulmonar robótica · Dr. David Lazo Pérez',
   desc='Segmentectomía pulmonar anatómica por cirugía robótica: qué es, indicaciones, técnica con verde de indocianina y evidencia de JCOG0802, CALGB y JCOG1211.',
   sub='Resección anatómica de un segmento pulmonar, con su arteria, su vena y su bronquio.',
   name='Segmentectomía pulmonar robótica',body=body_seg,
   about=[('MedicalProcedure','Segmentectomía pulmonar robótica')]),
 'lobectomia':dict(h1='Lobectomía robótica',title='Lobectomía pulmonar robótica · Dr. David Lazo Pérez',
   desc='Lobectomía pulmonar por cirugía robótica: qué es, indicaciones, técnica y evidencia publicada frente a la toracotomía y la videotoracoscopía.',
   sub='Resección de un lóbulo pulmonar completo, con su arteria, su vena y su bronquio.',
   name='Lobectomía pulmonar robótica',body=body_lob,
   about=[('MedicalProcedure','Lobectomía pulmonar robótica')]),
}

head_end=src.index('</head>'); HEAD0=src[:head_end]; BODY0=src[head_end:]
PHYS=[m.group(0) for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',HEAD0,re.S) if '"Physician"' in m.group(1)][0]
PRE=BODY0[:BODY0.index('<header')]; TAIL=BODY0[BODY0.index('</main>')+7:]
na="font-family:'Public Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;padding:14px 18px;display:block;text-decoration:none;border-right:1px solid #333;color:#F6F5F1"
for slug,sp in SPEC.items():
    assert len(sp['title'])<=60 and 120<=len(sp['desc'])<=158,(slug,len(sp['title']),len(sp['desc']))
    p=Page(); body=sp['body'](p); U=url(slug)
    head=HEAD0
    head=re.sub(r'<title>.*?</title>',f'<title>{sp["title"]}</title>',head)
    for prop,val in [('og:title',sp['title']),('og:description',sp['desc']),('og:url',U)]:
        head=re.sub(rf'<meta property="{prop}" content="[^"]*" />',f'<meta property="{prop}" content="{html.escape(val)}" />',head)
    head=re.sub(r'<meta name="description" content="[^"]*" />',f'<meta name="description" content="{html.escape(sp["desc"])}" />',head)
    head=re.sub(r'<link rel="canonical" href="[^"]*" />',f'<link rel="canonical" href="{U}" />',head)
    head=head.replace('<html lang="es">','<html lang="es-CL">')
    head=re.sub(r'\s*<script type="application/ld\+json">.*?</script>','',head,flags=re.S)
    crumbs=[{"@type":"ListItem","position":1,"name":"Cirugía robótica torácica","item":"https://rats.cl/"},{"@type":"ListItem","position":2,"name":"Resecciones pulmonares robóticas","item":BASE}]
    if slug: crumbs.append({"@type":"ListItem","position":3,"name":sp['name'],"item":U})
    web={"@context":"https://schema.org","@type":"MedicalWebPage","@id":U+"#webpage","url":U,"name":sp['name'],"description":sp['desc'],"inLanguage":"es-CL",
      "about":[{"@type":t,"name":n} for t,n in sp['about']],
      "author":{"@id":"https://cirugiatoracica.cl/#david-lazo"},"reviewedBy":{"@id":"https://cirugiatoracica.cl/#david-lazo"},
      "lastReviewed":TODAY,"dateModified":TODAY,"specialty":"https://schema.org/Surgical",
      "isPartOf":{"@type":"WebSite","@id":"https://rats.cl/#website","url":"https://rats.cl/","name":"rats.cl","inLanguage":"es-CL"},
      "breadcrumb":{"@type":"BreadcrumbList","itemListElement":crumbs},
      "citation":[re.sub('<.*?>','',REF[k][0]) for k in p.order]}
    ld=PHYS+'\n  <script type="application/ld+json">\n'+json.dumps(web,ensure_ascii=False,indent=2)+'\n  </script>\n'
    if slug=='':
        fq={"@context":"https://schema.org","@type":"FAQPage","@id":U+"#faq","isPartOf":{"@id":U+"#webpage"},"inLanguage":"es-CL",
            "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ_INDEX]}
        ld+='  <script type="application/ld+json">\n'+json.dumps(fq,ensure_ascii=False,indent=2)+'\n  </script>\n'
    head=head.replace('<!-- Google Analytics 4',ld+'<!-- Google Analytics 4',1)
    head=head.replace('.hv5:hover','.hv3c:hover{border-color:'+ACC+';text-decoration:none}\n  .hv5:hover')
    kicker=f'<a href="{"https://rats.cl" if not MAQ else "#"}" style="color:{ACC}">RATS</a>'+('' if not slug else f' · <a href="{link("")}" style="color:{ACC}">Resecciones pulmonares</a>')+' · Dr. David Lazo Pérez'
    header=f'''<header style="border-bottom:3px solid #0B0B0B">
      <div style="max-width:1280px;margin:0 auto;padding:20px 24px 0;display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:16px">
        <div>
          <p style="font-size:10.5px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:{ACC};margin-bottom:6px">{kicker}</p>
          <h1 style="font-family:'Bebas Neue',sans-serif;font-size:clamp(46px,{9 if not slug else 7.5}vw,{132 if not slug else 112}px);line-height:0.86;letter-spacing:0.005em">{sp['h1']}</h1>
        </div>
        <a href="#contacto" style="background:{ACC};color:#fff;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;padding:14px 18px;margin-bottom:8px" class="hv5">Agendar consulta</a>
      </div>
      <div style="max-width:1280px;margin:0 auto;padding:14px 24px 0">
        <p style="font-size:13px;border-top:1px solid #0B0B0B;padding-top:10px;padding-bottom:14px">{sp['sub']}</p>
      </div>
    </header>
    '''
    def navlink(s2,label):
        cur=(s2==slug)
        bar=f'<span style="display:block;height:3px;background:{ACC};margin:10px -18px -14px"></span>' if cur else ''
        ac=' aria-current="page"' if cur else ''
        return f'        <a href="{link(s2)}"{ac} style="{na}" class="hv4">{label}{bar}</a>'
    nav='<nav aria-label="Resecciones pulmonares robóticas" style="position:sticky;top:0;z-index:50;background:#0B0B0B;color:#F6F5F1">\n      <div style="max-width:1280px;margin:0 auto;padding:0 24px;display:flex;flex-wrap:wrap;align-items:stretch">\n'+f'        <a href="{"https://rats.cl" if not MAQ else "#"}" style="{na};color:#9A9A9A" class="hv4">← rats.cl</a>\n'+'\n'.join(navlink(s2,l) for s2,l in PAGES)+'\n      </div>\n    </nav>\n    '
    main=f'<main style="max-width:1280px;margin:0 auto;padding:0 24px">\n    {body}\n  </main>'
    PRE2=PRE.replace('<span>Cirugía torácica robótica · Santiago de Chile</span>','<a href="https://rats.cl" style="color:#F6F5F1;text-decoration:none">Cirugía torácica robótica · Santiago de Chile</a>',1)
    out=head+PRE2+header+nav+main+TAIL
    fn=OUTDIR/((slug or 'index')+'.html'); fn.parent.mkdir(parents=True,exist_ok=True); fn.write_text(out); print('ok',fn.name,len(out),p.order)
