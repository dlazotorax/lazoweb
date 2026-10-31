import re,json,html,sys
from pathlib import Path
REPO=Path(sys.argv[1]); OUTDIR=Path(sys.argv[2]); MODE=sys.argv[3]  # 'final' or 'preview'
MAQ = MODE=='preview'
src=(REPO/'dist/rats/operculo-toracico/index.html').read_text()
exec(open(Path(__file__).parent/'refs_block.py').read())
REF={k:(t,d) for k,t,d in refs}
ACC='#0E7490'; BG2='#EDEBE6'; TODAY='2026-10-30'
BASE='https://rats.cl/verde-indocianina'
PAGES=[('','Portada'),('nodulos','01 Nódulos'),('segmentectomia','02 Segmentectomía'),('conducto-toracico','03 Conducto torácico')]
IMG='imgs/icg-firefly.webp' if MAQ else '/verde-indocianina/imgs/icg-firefly.webp'
IMG5='imgs/nodulo-vision.webp' if MAQ else '/verde-indocianina/imgs/nodulo-vision.webp'
CORTES=open(Path(__file__).parent/'cortes.svg').read().replace('<svg class="cortes"','<svg class="cortes" style="display:block;width:100%;height:auto"',1)
IMG4='imgs/lobulos-segmentos.webp' if MAQ else '/verde-indocianina/imgs/lobulos-segmentos.webp'
IMG3='imgs/conducto-anatomia.webp' if MAQ else '/verde-indocianina/imgs/conducto-anatomia.webp'
IMG2='imgs/icg-fenomeno.webp' if MAQ else '/verde-indocianina/imgs/icg-fenomeno.webp'
def url(slug): return BASE+('/'+slug if slug else '')
def link(slug):
    if not MAQ: return url(slug)
    return (slug or 'index')+'.html'

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
    def rn(s,*ks):
        return re.sub(r'<a [^>]*>(\d+)</a>',r'\1',s.r(*ks))
def H2(n,t,id_): return f'''<div id="{id_}" style="display:flex;align-items:baseline;gap:16px;border-bottom:2px solid #0B0B0B;padding-bottom:8px;margin-bottom:24px;scroll-margin-top:60px">
        {f"<span style=\"font-family:'Bebas Neue',sans-serif;font-size:34px;line-height:1;color:{ACC}\">§{n}</span>" if n else ''}
        <h2 style="font-family:'Bebas Neue',sans-serif;font-size:clamp(28px,3.4vw,46px);line-height:1">{t}</h2>
      </div>'''
def Pp(t,lead=False): return f'<p style="font-size:{17 if lead else 16.5}px;{"font-weight:500;" if lead else ""}max-width:920px;margin-bottom:14px">{t}</p>'
def media(label): return f'<div style="flex:1 1 360px;aspect-ratio:16/9;border:2px dashed #0B0B0B;display:flex;align-items:center;justify-content:center;text-align:center;padding:16px;font-size:13px;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#3A3A3A;background:{BG2}">{label}</div>'
def table(head,rows,minw=640,maxw=None):
    h=''.join(f'<th style="{TH}">{x}</th>' for x in head)
    b='\n'.join('<tr>'+''.join(f'<td style="{TD}{";font-weight:700;white-space:nowrap" if i==0 else ""}">{c}</td>' for i,c in enumerate(row))+'</tr>' for row in rows)
    return f'<div style="overflow-x:auto;border:2px solid #0B0B0B;background:#fff;margin:6px 0 14px{";max-width:"+maxw if maxw else ""}"><table style="width:100%;border-collapse:collapse;font-size:15px;min-width:{minw}px"><thead><tr>{h}</tr></thead><tbody>\n{b}\n</tbody></table></div>'
EV=['Serie','Pacientes','Resultados']
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
        frame=f'''<div style="flex:0 1 360px;max-width:360px;width:100%">
          <div style="position:relative;aspect-ratio:9/16;border:2px solid #0B0B0B;background:#0B0B0B">
            <iframe class="yt-auto" src="https://www.youtube-nocookie.com/embed/{yt}?rel=0&amp;playsinline=1&amp;mute=1&amp;loop=1&amp;playlist={yt}&amp;enablejsapi=1" title="{title}" loading="lazy" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0"></iframe>
          </div>
        </div>'''
        return f'''{SEC}
      {H2(n,'Video','video')}
      <div style="display:flex;flex-wrap:wrap;gap:32px;align-items:center">
        {frame}
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

VIDEO_SEG='Segmentectomía anatómica robótica del segmento posterior del lóbulo superior derecho (S2). Se seccionan en forma selectiva la arteria, el bronquio y la vena del segmento; luego, el ICG intravenoso con la visión Firefly® delimita el segmento sin perfusión y el plano intersegmentario, que se secciona con endograpadora.'
VIDEO_CT='Ligadura robótica del conducto torácico por una fístula quilosa cervical. En luz blanca el conducto no se distingue en la grasa del mediastino posterior; con verde de indocianina y la visión Firefly® se identifica su trayecto, se diseca y se liga con clips bajo visión de fluorescencia.'
VIDEO_TXT='Nódulo subpleural del lóbulo superior izquierdo, marcado con verde de indocianina antes de la cirugía. Se localiza con la cámara Firefly®, se reseca en cuña con endograpadora robótica y se comprueba con fluorescencia que la lesión queda dentro del margen.'
# ---------------- page bodies ----------------
def body_index(p):
    def bigcard(slug,num,t,txt):
        return f'''<a href="{link(slug)}" style="flex:1 1 300px;display:flex;flex-direction:column;gap:10px;border:2px solid #0B0B0B;border-top:6px solid {ACC};background:#fff;padding:22px;color:#0B0B0B;text-decoration:none" class="hv3c">
          <span style="font-family:'Bebas Neue',sans-serif;font-size:30px;line-height:1;color:{ACC}">{num}</span>
          <span style="font-family:'Bebas Neue',sans-serif;font-size:34px;line-height:0.95">{t}</span>
          <span style="font-size:15px">{txt}</span>
          <span style="margin-top:auto;font-size:11px;font-weight:700;letter-spacing:0.16em;text-transform:uppercase;color:{ACC}">Ver página →</span>
        </a>'''
    faq=FAQ_INDEX
    fh='\n'.join(f'''        <details style="border-bottom:1px solid #0B0B0B;padding:14px 0">
          <summary style="cursor:pointer;list-style:none;font-size:17px;font-weight:700">{q}</summary>
          <p style="font-size:15.5px;margin-top:10px">{a}</p>
        </details>''' for q,a in faq)
    return f'''{SEC}
      {H2(1,'Qué es y cómo se ve','que-es')}
      <div style="display:flex;flex-wrap:wrap;gap:32px;align-items:center;margin-bottom:28px">
        <div style="flex:1 1 420px;max-width:640px">
          {Pp('El verde de indocianina (ICG) es un colorante que emite fluorescencia cuando se ilumina con luz en el infrarrojo cercano: la molécula absorbe esa luz y emite otra de una longitud de onda algo mayor, que capta una cámara especial.',True)}
        </div>
        <figure style="flex:1 1 360px;max-width:600px;margin:0">
          <img src="{IMG2}" alt="Esquema del fenómeno físico del verde de indocianina: excitación con luz infrarroja, absorción de energía por la molécula y emisión de fluorescencia captada por una cámara" width="1200" height="512" style="width:100%;display:block;border:2px solid #0B0B0B" loading="lazy" />
        </figure>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:32px;align-items:center">
        <div style="flex:1 1 420px;max-width:640px">
          {Pp('El robot da Vinci integra esa visión (Firefly®): con un comando, el cirujano pasa de la imagen normal a la de fluorescencia, en la que el ICG aparece en verde.'+p.r('viana'),True)}
          {Pp('En la cirugía robótica el cirujano no palpa el pulmón. La fluorescencia compensa en parte esa falta de tacto, porque muestra estructuras que con la visión normal no se distinguen.'+p.r('yan'))}
        </div>
        <figure style="flex:1 1 360px;max-width:600px;margin:0">
          <img src="{IMG}" alt="Visión con fluorescencia Firefly del robot da Vinci durante una cirugía torácica: el verde de indocianina se ve en verde sobre el pulmón y el resto del campo en escala de grises" width="1200" height="932" style="width:100%;display:block;border:2px solid #0B0B0B" loading="lazy" />
          <figcaption style="font-size:12.5px;color:#3A3A3A;margin-top:8px">Visión Firefly® en cirugía robótica: el ICG aparece en verde sobre el pulmón.</figcaption>
        </figure>
      </div>
    </section>

    {SEC}
      {H2(2,'Usos en cirugía robótica torácica','usos')}
      {Pp('Según dónde y cómo se administre, el ICG cumple funciones distintas. Cada una tiene su página:')}
      <div style="display:flex;flex-wrap:wrap;gap:18px">
        {bigcard('nodulos','01','Marcación de nódulos pulmonares','Punción bajo TAC el día de la cirugía para encontrar nódulos pequeños, en vidrio esmerilado o profundos. En una serie de 471 pacientes se localizó el 98,4 % de los nódulos.'+p.rn('li'))}
        {bigcard('segmentectomia','02','Identificación del plano intersegmentario','ICG por vena después de seccionar los vasos del segmento: el pulmón irrigado se ve verde y el segmento a resecar queda oscuro. En una revisión de 1.090 pacientes, el plano se identificó en el 94 %.'+p.rn('peeters'))}
        {bigcard('conducto-toracico','03','Identificación del conducto torácico','ICG en la ingle que viaja por los linfáticos y muestra el conducto en verde, para no lesionarlo o para encontrar una fuga de linfa (quilotórax).'+p.rn('varshney'))}
      </div>
    </section>

    {SEC}
      {H2(3,'Preguntas frecuentes','faq')}
      <div style="max-width:900px">
{fh}
      </div>
    </section>

    {refs_html(p)}'''

def body_nodulos(p):
    return f'''{SEC}
      {H2(1,'Por qué marcar el nódulo','porque')}
      {Pp('Los nódulos pequeños, en vidrio esmerilado o alejados de la superficie del pulmón no se ven ni se palpan durante la cirugía robótica, en la que el cirujano no toca el pulmón. La localización previa es necesaria, no opcional.'+p.r('yan'),True)}
      {Pp('Gran utilidad en nódulos superficiales a menos de 2 cm. Requiere un equipo específico y puede haber falsos positivos y negativos propios de la fluorescencia.')}
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;margin-top:22px">
        <figure style="margin:0"><div style="border:2px solid #0B0B0B;background:#0f1416">{CORTES}</div><figcaption style="font-size:12.5px;color:#3A3A3A;margin-top:8px">Esquema de la ubicación del mismo nódulo, en el lóbulo superior derecho, en cortes axial, sagital y coronal.</figcaption></figure>
        <figure style="margin:0"><img src="{IMG5}" alt="Ilustración de la visión intraoperatoria: el nódulo pulmonar queda oculto bajo el tejido y no se ve en la superficie del pulmón" width="1024" height="722" style="width:100%;display:block;border:2px solid #0B0B0B" loading="lazy" /><figcaption style="font-size:12.5px;color:#3A3A3A;margin-top:8px">Visión intraoperatoria: un nódulo de 1 cm bajo 10 mm de tejido no se ve en la superficie del pulmón.</figcaption></figure>
      </div>
    </section>

    {SEC}
      {H2(2,'La técnica','tecnica')}
      {Pp('El mismo día de la operación, bajo TAC y con una aguja fina, se inyecta ICG dentro del nódulo o junto a él. El ICG difunde en el tejido con las horas, por eso la cirugía se hace poco después. En el pabellón, la cámara Firefly® del robot muestra la marca como una mancha verde sobre el pulmón; se reseca el nódulo con margen, en cuña o por segmentectomía, y la pieza se analiza durante la cirugía (biopsia contemporánea).'+p.r('viana'))}
    </section>

    {video_sec(3,'',yt='w076_YlJ5XE',title='Marcación de un nódulo pulmonar con verde de indocianina — Dr. David Lazo Pérez',text=VIDEO_TXT)}

    {SEC}
      {H2(4,'Evidencia publicada','evidencia')}
      {table(EV,[
        ('Nagai 2018'+p.r('nagai'),'37 pacientes, nódulos de 2 a 22 mm (media 9,1 mm), a una profundidad media de 9,9 mm','Marca visible en la pleura en el 95 %. Neumotórax leve en el 8 %; sin complicaciones graves'),
        ('Li 2021'+p.r('li'),'471 pacientes, 512 nódulos de 2 cm o menos (media 9,1 mm; profundidad media 8,9 mm)','98,4 % de los nódulos localizados. Neumotórax asintomático en el 5,9 %; ninguno requirió drenaje pleural'),
        ('Han 2024'+p.r('han'),'86 pacientes con nódulos en vidrio esmerilado: 48 marcados con ICG y 38 con arpón','Éxito técnico de 100 % con ICG y 97,4 % con arpón. Neumotórax en el 6,3 % con ICG y en el 27,3 % con arpón'),
        ('Viana 2026'+p.r('viana'),'84 pacientes con nódulos de 2 cm o menos operados por cirugía robótica (São Paulo)','Todos los nódulos localizados con Firefly® y resecados con márgenes negativos; sin conversiones ni complicaciones de la marcación'),
      ])}
    </section>

    {SEC}
      {H2(5,'Verde de indocianina y lipiodol','comparacion')}
      {table(['','Verde de indocianina','Lipiodol'],[
        ('Plataforma quirúrgica','RATS y VATS','VATS'),
        ('Cómo se ve','Fluorescencia en el infrarrojo cercano','Radioscopia'),
        ('Radiación en la cirugía','No','Sí'),
        ('Persistencia de la marca','Difunde en horas: la cirugía se hace poco después','Se mantiene en el pulmón'),
      ],560,'920px')}
      {Pp('La marcación con lipiodol se describe en <a href="https://videotoracoscopia.cl/cirugia-nodulo-pulmonar">videotoracoscopia.cl</a>, junto con los tipos de resección y nuestros resultados publicados.')}
    </section>

    {refs_html(p)}'''

def body_seg(p):
    return f'''{SEC}
      {H2(1,'El problema del límite entre segmentos','problema')}
      <div style="display:flex;flex-wrap:wrap;gap:32px;align-items:center">
        <div style="flex:1 1 380px;max-width:560px">
          {Pp('En la segmentectomía se reseca un segmento del pulmón y no el lóbulo completo. El límite entre segmentos no se ve en la superficie, y la sección debe seguirlo para obtener un margen adecuado.',True)}
        </div>
        <figure style="flex:1 1 420px;max-width:680px;margin:0">
          <img src="{IMG4}" alt="Pulmón derecho en vista lateral: a la izquierda, los lóbulos superior, medio e inferior; a la derecha, los segmentos apical, posterior, anterior, lateral, medial, superior y basales anterior, lateral y posterior" width="1200" height="896" style="width:100%;display:block;border:2px solid #0B0B0B;background:#fff" loading="lazy" />
          <figcaption style="font-size:12.5px;color:#3A3A3A;margin-top:8px">Pulmón derecho, vista lateral: lóbulos y segmentos.</figcaption>
        </figure>
      </div>
    </section>

    {SEC}
      {H2(2,'La técnica','tecnica')}
      {Pp('Después de seccionar los vasos del segmento, se inyecta ICG por vía intravenosa. El pulmón irrigado se ve verde y el segmento a resecar, sin irrigación, queda oscuro. El borde entre ambos se marca y guía la sección.'+p.r('pardolesi','geraci'))}
      {Pp('El efecto es breve. En una revisión sistemática, la fluorescencia apareció entre 10 y 40 segundos después de la inyección y duró entre 90 y 140 segundos tras un bolo.'+p.r('peeters'))}
    </section>

    {video_sec(3,'',yt='BykskDhQulc',title='Segmentectomía S2 derecha robótica con plano intersegmentario por ICG — Dr. David Lazo Pérez',text=VIDEO_SEG)}

    {SEC}
      {H2(4,'Evidencia publicada','evidencia')}
      {table(EV,[
        ('Geraci 2019'+p.r('geraci'),'245 segmentectomías robóticas consecutivas de un cirujano (Nueva York)','ICG intravenoso después de ligar la arteria en todos los casos. Resección R0 en el 100 %; morbilidad mayor en 3 pacientes y sin mortalidad a 30 ni 90 días'),
        ('Hao 2023'+p.r('hao'),'155 segmentectomías robóticas consecutivas','Plano intersegmentario bien delimitado en el 96,8 %, sin relación con el segmento resecado; sin eventos adversos por el ICG'),
        ('Peeters 2024'+p.r('peeters'),'Revisión sistemática: 18 estudios, 1.090 pacientes operados por VATS o RATS','El ICG intravenoso identificó el plano en el 94 % de los casos, incluso con dosis bajas (0,05 mg/kg). No se informaron reacciones adversas'),
      ])}
      {Pp('Las indicaciones de la segmentectomía frente a la lobectomía en tumores de hasta 2 cm se revisan en <a href="https://videotoracoscopia.cl/cirugia-nodulo-pulmonar">videotoracoscopia.cl</a>.')}
    </section>

    {refs_html(p)}'''

def body_ct(p):
    return f'''{SEC}
      {H2(1,'El conducto torácico y sus lesiones','problema')}
      <div style="display:flex;flex-wrap:wrap;gap:32px;align-items:flex-start">
        <div style="flex:1 1 420px;max-width:640px">
          {Pp('El conducto torácico lleva al sistema venoso la linfa del abdomen, incluida la grasa absorbida en el intestino.'+p.r('phang')+' Nace en el abdomen, a menudo en una dilatación llamada cisterna del quilo, presente en alrededor de la mitad de las personas,'+p.r('plutecki')+' y entra al tórax por el hiato aórtico. Asciende por el mediastino posterior, a la derecha de la línea media, entre la aorta y la vena ácigos y por detrás del esófago; en la parte media del tórax cruza hacia la izquierda y sube junto al esófago hasta la base del cuello. Desemboca con mayor frecuencia en la vena yugular interna (46 %), seguida del ángulo yugulosubclavio (32 %) y la vena subclavia (18 %). Su formación, su trayecto y su terminación son muy variables.'+p.r('phang'),True)}
          {Pp('Su lesión produce salida de linfa a ese nivel, que puede traducirse en una fístula quilosa en el cuello o en su acumulación en el tórax, llamada quilotórax.'+p.r('tokumaru'))}
        </div>
        <figure style="flex:1 1 300px;max-width:440px;margin:0">
          <img src="{IMG3}" alt="Ilustración anatómica del conducto torácico: nace en la cisterna del quilo, atraviesa el diafragma junto a la aorta, asciende entre la aorta y la vena ácigos y desemboca en la confluencia de la vena yugular interna y la subclavia izquierdas" width="900" height="1117" style="width:100%;display:block;border:2px solid #0B0B0B;background:#fff" loading="lazy" />
          <figcaption style="font-size:12.5px;color:#3A3A3A;margin-top:8px">Trayecto del conducto torácico, desde la cisterna del quilo hasta la confluencia venosa izquierda del cuello.</figcaption>
        </figure>
      </div>
    </section>

    {SEC}
      {H2(2,'La técnica','tecnica')}
      {Pp('El ICG se inyecta en los ganglios inguinales, guiado por ecografía, o en el tejido subcutáneo de ambas ingles. Viaja por los linfáticos y, en la visión de fluorescencia, el conducto torácico aparece en verde.'+p.r('varshney','tokumaru'))}
      {Pp('Se usa para evitar lesionarlo durante cirugías del mediastino y del esófago y, cuando ya hay un quilotórax, para encontrar el sitio de la fuga y comprobar que la ligadura la cerró.'+p.r('kuo'))}
    </section>

    {video_sec(3,'',yt='EW5Z0sYQY-E',title='Ligadura robótica del conducto torácico guiada por fluorescencia ICG — Dr. David Lazo Pérez',text=VIDEO_CT)}

    {SEC}
      {H2(4,'Evidencia publicada','evidencia')}
      {table(EV,[
        ('Varshney 2022'+p.r('varshney'),'21 esofagectomías mínimamente invasivas (15 toracoscópicas y 6 robóticas)','ICG en los ganglios inguinales guiado por ecografía. Conducto visualizado en todos los casos, con una mediana de 35 minutos; una lesión del conducto detectada y clipada durante la cirugía; sin quilotórax postoperatorio'),
        ('Tokumaru 2022'+p.r('tokumaru'),'16 esofagectomías toracoscópicas','ICG subcutáneo en ambas ingles (0,2 a 0,5 mg/kg). Conducto identificado en el 93,8 %; la fluorescencia se mantuvo durante toda la etapa torácica; sin complicaciones del ICG'),
        ('Kuo 2024'+p.r('kuo'),'Quilotórax refractario después de una cirugía por cáncer pulmonar','ICG en los ganglios inguinales 20 minutos antes de la cirugía. La fuga se localizó en la región paratraqueal derecha y, tras la ligadura, dejó de salir linfa fluorescente'),
      ])}
    </section>

    {refs_html(p)}'''

FAQ_INDEX=[
 ('¿Qué es el verde de indocianina?','Es un colorante que, iluminado con luz en el infrarrojo cercano, emite fluorescencia. El robot da Vinci tiene una cámara que capta esa luz y muestra en verde las estructuras que lo contienen, que con la visión normal no se distinguen.'),
 ('¿Cómo se marca un nódulo pulmonar con verde de indocianina?','El mismo día de la cirugía, bajo TAC y con una aguja fina, se deja una pequeña cantidad de verde de indocianina dentro del nódulo o junto a él. Durante la operación, la cámara del robot muestra la marca en verde sobre el pulmón.'),
 ('¿Para qué sirve en la segmentectomía?','Se inyecta por la vena después de seccionar los vasos del segmento que se va a resecar. El resto del pulmón se ve verde y el segmento queda oscuro, lo que muestra el límite entre ambos.'),
 ('¿Para qué sirve en el conducto torácico?','Se inyecta en la ingle y viaja por los vasos linfáticos hasta el conducto torácico, que se ve en verde. Ayuda a no lesionarlo durante la cirugía y, cuando hay una fuga de linfa (quilotórax), a encontrar el sitio de la fuga.'),
 ('¿Tiene riesgos?','En una revisión de 18 estudios con 1.090 pacientes que recibieron verde de indocianina por la vena no se informaron reacciones adversas. La punción para marcar un nódulo tiene los riesgos de una punción pulmonar: en una serie de 471 pacientes hubo neumotórax en el 5,9 %, y ninguno requirió drenaje pleural.'),
]

SPEC={
 '':dict(h1='RATS y verde de indocianina',title='RATS y verde de indocianina (ICG) · Dr. David Lazo Pérez',
   desc='Usos del verde de indocianina en cirugía robótica torácica: marcación de nódulos pulmonares, plano intersegmentario en la segmentectomía y conducto torácico.',
   sub='Fluorescencia en el infrarrojo cercano en cirugía robótica torácica: marcación de nódulos, plano intersegmentario y conducto torácico.',
   name='RATS y verde de indocianina',body=body_index,
   about=[('MedicalProcedure','Marcación de nódulos pulmonares con verde de indocianina'),('MedicalProcedure','Segmentectomía pulmonar robótica con verde de indocianina'),('MedicalProcedure','Identificación del conducto torácico con verde de indocianina')]),
 'nodulos':dict(h1='Marcación de nódulos con verde de indocianina',title='Nódulos marcados con ICG en RATS · Dr. David Lazo Pérez',
   desc='Marcación de nódulos pulmonares con verde de indocianina bajo TAC y resección por cirugía robótica con fluorescencia: técnica, evidencia y lipiodol.',
   sub='Punción bajo TAC el día de la cirugía y localización del nódulo con la cámara de fluorescencia del robot.',
   name='Marcación de nódulos pulmonares con verde de indocianina',body=body_nodulos,
   about=[('MedicalProcedure','Marcación de nódulos pulmonares con verde de indocianina bajo TAC')]),
 'segmentectomia':dict(h1='Plano intersegmentario con verde de indocianina',title='Segmentectomía robótica con ICG · Dr. David Lazo Pérez',
   desc='Verde de indocianina intravenoso para delimitar el plano intersegmentario en la segmentectomía pulmonar robótica: técnica, duración del efecto y evidencia.',
   sub='ICG por vena después de seccionar los vasos del segmento: el pulmón irrigado se ve verde y el segmento a resecar queda oscuro.',
   name='Plano intersegmentario con verde de indocianina',body=body_seg,
   about=[('MedicalProcedure','Segmentectomía pulmonar robótica con verde de indocianina')]),
 'conducto-toracico':dict(h1='Conducto torácico con verde de indocianina',title='Conducto torácico con ICG en RATS · Dr. David Lazo Pérez',
   desc='Verde de indocianina inyectado en la ingle para ver el conducto torácico con fluorescencia: evitar su lesión y localizar la fuga en el quilotórax. Evidencia.',
   sub='ICG en la ingle que viaja por los linfáticos y muestra el conducto torácico en verde.',
   name='Conducto torácico con verde de indocianina',body=body_ct,
   about=[('MedicalProcedure','Identificación del conducto torácico con verde de indocianina')]),
}

head_end=src.index('</head>'); HEAD0=src[:head_end]; BODY0=src[head_end:]
PHYS=[m.group(0) for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>',HEAD0,re.S) if '"Physician"' in m.group(1)][0]
PRE=BODY0[:BODY0.index('<header')]; TAIL=BODY0[BODY0.index('</main>')+7:].replace('#C4500E',ACC)
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
    head=re.sub(r'<meta property="og:image" content="[^"]*" />','<meta property="og:image" content="https://rats.cl/verde-indocianina/imgs/icg-firefly.webp" />',head)
    head=re.sub(r'\s*<script type="application/ld\+json">.*?</script>','',head,flags=re.S)
    crumbs=[{"@type":"ListItem","position":1,"name":"Cirugía robótica torácica","item":"https://rats.cl/"},{"@type":"ListItem","position":2,"name":"RATS y verde de indocianina","item":BASE}]
    if slug: crumbs.append({"@type":"ListItem","position":3,"name":sp['name'],"item":U})
    web={"@context":"https://schema.org","@type":"MedicalWebPage","@id":U+"#webpage","url":U,"name":sp['name'],"description":sp['desc'],"inLanguage":"es-CL",
      "about":[{"@type":t,"name":n} for t,n in sp['about']],
      "author":{"@id":"https://cirugiatoracica.cl/#david-lazo"},"reviewedBy":{"@id":"https://cirugiatoracica.cl/#david-lazo"},
      "lastReviewed":TODAY,"dateModified":TODAY,"specialty":"https://schema.org/Surgical",
      "isPartOf":{"@type":"WebSite","@id":"https://rats.cl/#website","url":"https://rats.cl/","name":"rats.cl","inLanguage":"es-CL"},
      "breadcrumb":{"@type":"BreadcrumbList","itemListElement":crumbs},
      "citation":[re.sub('<.*?>','',REF[k][0]) for k in p.order]}
    ld=PHYS+'\n  <script type="application/ld+json">\n'+json.dumps(web,ensure_ascii=False,indent=2)+'\n  </script>\n'
    if slug=='nodulos':
        vo={"@context":"https://schema.org","@type":"VideoObject","@id":U+"#video",
            "name":"Resección robótica de nódulo pulmonar guiada por fluorescencia ICG | RATS",
            "description":VIDEO_TXT,"uploadDate":"2026-10-30T11:43:37-07:00","duration":"PT38S",
            "thumbnailUrl":"https://i.ytimg.com/vi/w076_YlJ5XE/hqdefault.jpg",
            "embedUrl":"https://www.youtube-nocookie.com/embed/w076_YlJ5XE","url":"https://www.youtube.com/shorts/w076_YlJ5XE",
            "inLanguage":"es-CL","author":{"@id":"https://cirugiatoracica.cl/#david-lazo"},"isPartOf":{"@id":U+"#webpage"}}
        ld+='  <script type="application/ld+json">\n'+json.dumps(vo,ensure_ascii=False,indent=2)+'\n  </script>\n'
    if slug=='segmentectomia':
        vo={"@context":"https://schema.org","@type":"VideoObject","@id":U+"#video",
            "name":"Segmentectomía S2 derecha robótica con plano intersegmentario por ICG | RATS",
            "description":VIDEO_SEG,"uploadDate":"2026-10-31T07:37:32-07:00","duration":"PT45S",
            "thumbnailUrl":"https://i.ytimg.com/vi/BykskDhQulc/hqdefault.jpg",
            "embedUrl":"https://www.youtube-nocookie.com/embed/BykskDhQulc","url":"https://www.youtube.com/shorts/BykskDhQulc",
            "inLanguage":"es-CL","author":{"@id":"https://cirugiatoracica.cl/#david-lazo"},"isPartOf":{"@id":U+"#webpage"}}
        ld+='  <script type="application/ld+json">\n'+json.dumps(vo,ensure_ascii=False,indent=2)+'\n  </script>\n'
    if slug=='conducto-toracico':
        vo={"@context":"https://schema.org","@type":"VideoObject","@id":U+"#video",
            "name":"Ligadura robótica del conducto torácico guiada por fluorescencia ICG | RATS",
            "description":VIDEO_CT,"uploadDate":"2026-10-30T11:46:06-07:00","duration":"PT38S",
            "thumbnailUrl":"https://i.ytimg.com/vi/EW5Z0sYQY-E/hqdefault.jpg",
            "embedUrl":"https://www.youtube-nocookie.com/embed/EW5Z0sYQY-E","url":"https://www.youtube.com/shorts/EW5Z0sYQY-E",
            "inLanguage":"es-CL","author":{"@id":"https://cirugiatoracica.cl/#david-lazo"},"isPartOf":{"@id":U+"#webpage"}}
        ld+='  <script type="application/ld+json">\n'+json.dumps(vo,ensure_ascii=False,indent=2)+'\n  </script>\n'
    if slug=='':
        fq={"@context":"https://schema.org","@type":"FAQPage","@id":U+"#faq","isPartOf":{"@id":U+"#webpage"},"inLanguage":"es-CL",
            "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ_INDEX]}
        ld+='  <script type="application/ld+json">\n'+json.dumps(fq,ensure_ascii=False,indent=2)+'\n  </script>\n'
    head=head.replace('<!-- Google Analytics 4',ld+'<!-- Google Analytics 4',1).replace('#C4500E',ACC)
    head=head.replace('.hv5:hover','.hv3c:hover{border-color:'+ACC+';text-decoration:none}\n  .hv5:hover')
    kicker=f'<a href="{"https://rats.cl" if not MAQ else "#"}" style="color:{ACC}">RATS</a>'+('' if not slug else f' · <a href="{link("")}" style="color:{ACC}">Verde de indocianina</a>')+' · Dr. David Lazo Pérez'
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
    nav='<nav aria-label="RATS y verde de indocianina" style="position:sticky;top:0;z-index:50;background:#0B0B0B;color:#F6F5F1">\n      <div style="max-width:1280px;margin:0 auto;padding:0 24px;display:flex;flex-wrap:wrap;align-items:stretch">\n'+'\n'.join(navlink(s2,l) for s2,l in PAGES)+'\n      </div>\n    </nav>\n    '
    main=f'<main style="max-width:1280px;margin:0 auto;padding:0 24px">\n    {body}\n  </main>'
    out=head+PRE+header+nav+main+TAIL
    fn=OUTDIR/((slug or 'index')+'.html'); fn.parent.mkdir(parents=True,exist_ok=True); fn.write_text(out); print('ok',fn.name,len(out),p.order)
