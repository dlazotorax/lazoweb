# -*- coding: utf-8 -*-
# Contenido de las cinco páginas. Se ejecuta desde build_operculo.py.

# ═══════════════════════════════════════════════ HUB ═══
BODY_HUB = f'''
  <section class="section" id="que-es">
    <div class="inner">
      <h2 class="section-title">Qué es el síndrome del opérculo torácico</h2>
      <p class="section-lead">Es el conjunto de síntomas y signos que produce la compresión de las estructuras neurovasculares del brazo —plexo braquial, arteria subclavia y vena subclavia— a su paso por el espacio que forman la clavícula, la primera costilla y los músculos escalenos. Según cuál sea la estructura comprimida, existen tres variantes: <strong>neurogénica</strong> (más del 95 % de los casos), <strong>venosa</strong> (alrededor del 3 %) y <strong>arterial</strong> (cerca del 1 %).</p>
      <div class="defs">
        <div class="def"><span class="d-tag">Espacio 1</span><h3>Triángulo interescalénico</h3><p>Entre el escaleno anterior, el escaleno medio y la primera costilla. Por aquí pasan el plexo braquial y la arteria subclavia: es el sitio de compresión del SOT neurogénico y del arterial.</p></div>
        <div class="def"><span class="d-tag">Espacio 2</span><h3>Espacio costoclavicular</h3><p>Entre la clavícula y la primera costilla. Por aquí pasa la vena subclavia, por delante del escaleno anterior: es el sitio de compresión del SOT venoso.</p></div>
        <div class="def"><span class="d-tag">Espacio 3</span><h3>Espacio del pectoral menor</h3><p>Bajo el tendón del pectoral menor, ya fuera del tórax. Su estrechamiento por hipertrofia muscular es una causa menos frecuente de compresión, sobre todo venosa.</p></div>
      </div>
      <div class="cards-4">
        <a class="card-link" href="{BASE}/causas"><div class="cl-num">01</div><h3>Causas</h3><p>Costilla cervical, primera costilla anómala, bandas fibrosas de Roos, anomalías musculares y trauma.</p><span class="cl-go">Ver causas →</span></a>
        <a class="card-link" href="{BASE}/clinica"><div class="cl-num">02</div><h3>Clínica</h3><p>Cómo se presenta cada variante: neurogénica, venosa (Paget-Schroetter) y arterial.</p><span class="cl-go">Ver clínica →</span></a>
        <a class="card-link" href="{BASE}/estudio"><div class="cl-num">03</div><h3>Estudio</h3><p>Radiografía, EMG, Doppler, angioTC/angioRM con maniobras y el bloqueo con toxina botulínica.</p><span class="cl-go">Ver estudio →</span></a>
        <a class="card-link" href="{BASE}/tratamiento"><div class="cl-num">04</div><h3>Tratamiento</h3><p>Terapia física, cirugía abierta y la resección robótica transtorácica de la primera costilla.</p><span class="cl-go">Ver tratamiento →</span></a>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="por-que-toracico">
    <div class="inner">
      <div class="two-col">
        <div>
          <h2 class="section-title">Por qué un cirujano torácico</h2>
          <p class="section-lead" style="margin-bottom:1rem;">Durante décadas, en Chile, la cirugía del opérculo torácico no atrajo a los cirujanos torácicos y quedó en manos de la cirugía vascular. Las técnicas mínimamente invasivas cambiaron eso: la primera costilla se puede abordar desde el interior del tórax, el territorio habitual del cirujano torácico, con la videotoracoscopía primero y con la plataforma robótica después.</p>
          <p class="section-lead" style="margin-bottom:0;">El manejo sigue siendo multidisciplinario —fisiatría, kinesiología, neurología, cirugía vascular— y el cirujano torácico aporta la vía de acceso que evita las incisiones en el cuello y la axila y la tracción del plexo braquial.</p>
        </div>
        <figure class="fig">
          <img src="local-imgs/pabellon-robot-dr-lazo.webp" alt="Dr. David Lazo en pabellón, junto al sistema robótico Da Vinci acoplado al paciente" loading="lazy" width="1600" height="1200" decoding="async">
          <figcaption>Pabellón de cirugía robótica. Foto del autor.</figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section id="cirugia-robotica" class="section section-dark">
    <div class="inner">
      <p class="ref-label">Resolución robótica</p>
      <h2 class="section-title w">Resección de la primera costilla<br><em style="font-style:italic;color:var(--teal-lt);">desde el interior del tórax</em></h2>
      <p class="section-lead w">Con el sistema Da Vinci, la primera costilla se aborda por tres o cuatro puertos en el costado, por debajo de la pleura. La cámara 3D magnificada muestra la costilla completa y, ordenados sobre ella, la vena subclavia, el escaleno anterior, la arteria subclavia, el plexo braquial y el escaleno medio. Los escalenos se desinsertan, la costilla se desarticula por delante y se secciona por detrás, cerca de la vértebra, y se retira. Ninguna estructura neurovascular se retrae ni se tracciona.</p>
      <div class="two-col">
        <div class="video-slot">
          <div><strong>Vídeo: resección robótica de la primera costilla</strong><small>Espacio reservado para el vídeo que el autor está produciendo. Formato previsto: MP4 con póster, carga diferida como en la portada de rats.cl.</small></div>
        </div>
        <ul class="feature-list">
          <li class="fi"><div class="fi-ico"><span class="fi-num">1</span></div><div class="fi-text"><h4>Sin incisión en el cuello ni en la axila</h4><p>Los puertos quedan en el costado del tórax.</p></div></li>
          <li class="fi"><div class="fi-ico"><span class="fi-num">2</span></div><div class="fi-text"><h4>Sin tracción del plexo</h4><p>El plexo se ve desde abajo y no se manipula para llegar a la costilla.</p></div></li>
          <li class="fi"><div class="fi-ico"><span class="fi-num">3</span></div><div class="fi-text"><h4>Costilla completa a la vista</h4><p>Desde la unión esternal hasta la vértebra, bajo magnificación.</p></div></li>
          <li class="fi"><div class="fi-ico"><span class="fi-num">4</span></div><div class="fi-text"><h4>Escalenectomía bajo visión directa</h4><p>Con el nervio frénico y el plexo identificados.</p></div></li>
        </ul>
      </div>
      <p class="section-lead w" style="margin-top:2rem;">La técnica completa, la comparación con las vías transaxilar y supraclavicular y los resultados publicados están en <a href="{BASE}/tratamiento" style="color:var(--teal-lt);font-weight:600;">Tratamiento</a>.</p>
    </div>
  </section>

  <section class="section" id="equipo-vascular">
    <div class="inner">
      <h2 class="section-title">Un mismo mecanismo, una misma solución</h2>
      <p class="section-lead">En las tres variantes, cuando la compresión depende de la primera costilla o de los escalenos, el tratamiento definitivo es el mismo: liberar el espacio resecando la costilla y seccionando los escalenos, y eso es lo que se hace con el robot. Hay situaciones en que la vía robótica no basta por sí sola y la cirugía se planifica en conjunto con <strong>cirugía vascular</strong>, en el mismo acto o en tiempos sucesivos:</p>
      <ul class="list-check">
        <li><strong>Costilla cervical o bandas anómalas supraclaviculares o cervicales</strong>, que requieren un abordaje supraclavicular complementario.</li>
        <li><strong>Trombosis venosa o arterial activa</strong>: trombólisis o trombectomía antes de la descompresión y eventual venoplastía después.</li>
        <li><strong>Aneurisma o dilatación postestenótica de la arteria subclavia</strong>, que exige reparación arterial.</li>
        <li><strong>Neurólisis del plexo braquial</strong> cuando hay fibrosis perineural que la vía torácica no alcanza.</li>
      </ul>
    </div>
  </section>

  <section class="section section-dark" id="derivadores">
    <div class="inner">
      <p class="ref-label">Para médicos derivadores</p>
      <h2 class="section-title w">Neurólogos, fisiatras, traumatólogos, cirujanos vasculares y médicos del deporte</h2>
      <div class="ref-grid">
        <div class="ref-card"><h3>Perfil de derivación</h3><ul>
          <li>Síntomas neurológicos de extremidad superior de predominio cubital, sin causa cervical ni periférica, que no mejoran tras terapia física dirigida.</li>
          <li>Atrofia intrínseca de la mano con compromiso del tronco inferior del plexo.</li>
          <li>Trombosis de esfuerzo de la vena subclavia (Paget-Schroetter), idealmente precoz tras la trombólisis.</li>
          <li>Isquemia digital, embolias distales o asimetría de pulsos con la abducción en paciente joven.</li>
          <li>Costilla cervical sintomática.</li></ul></div>
        <div class="ref-card"><h3>Qué adjuntar</h3><ul>
          <li>Radiografía de tórax y columna cervical.</li>
          <li>AngioTC o angioRM con maniobras provocativas (brazos en reposo y en abducción).</li>
          <li>Electromiografía y conducción nerviosa de extremidad superior.</li>
          <li>Ecografía Doppler dinámica en las formas vasculares.</li>
          <li>Resumen de la terapia física realizada y su duración.</li></ul></div>
        <div class="ref-card"><h3>Coordinación</h3><ul>
          <li>Neurogénico: evaluación electiva; la indicación se define con el estudio completo y, si hace falta, un bloqueo diagnóstico de escalenos.</li>
          <li>Venoso: descompresión programada precoz tras la trombólisis, coordinada con cirugía vascular.</li>
          <li>Arterial: evaluación prioritaria y planificación conjunta con cirugía vascular.</li>
          <li>El autor ha dictado conferencias sobre este tema en Chile y en el extranjero; su trayectoria académica está en el <a href="https://cirugiatoracica.cl/cv">currículum académico</a>.</li></ul></div>
      </div>
    </div>
  </section>
'''

FAQ_HUB = [
 ('¿Qué es el síndrome del opérculo torácico?', 'Es la compresión del plexo braquial, la arteria subclavia o la vena subclavia en el espacio que forman la primera costilla, la clavícula y los músculos escalenos, a la salida del tórax hacia el brazo. Según la estructura comprimida se clasifica en neurogénico, venoso o arterial.'),
 ('¿Cómo se opera el opérculo torácico con robot?', 'Por tres o cuatro incisiones de menos de dos centímetros en el costado del tórax. El robot aborda la primera costilla desde el interior, secciona los escalenos anterior y medio y reseca la costilla desde su unión anterior hasta cerca de la vértebra, bajo visión 3D magnificada, sin incisión en el cuello ni en la axila y sin traccionar el plexo braquial.'),
 ('¿La cirugía robótica sirve para los tres tipos: neurogénico, venoso y arterial?', 'Sí, siempre que la compresión dependa de la primera costilla o de los escalenos, que es el mecanismo habitual en las tres variantes. Si además hay una costilla cervical, bandas anómalas en el cuello, una trombosis activa o un aneurisma de la arteria subclavia, la resección robótica se combina con cirugía vascular.'),
 ('¿Siempre hay que operar?', 'No. En la forma neurogénica el primer tratamiento es la terapia física durante varios meses; la cirugía se indica cuando no controla los síntomas o hay déficit neurológico progresivo. En las formas venosa y arterial la indicación es más precoz, porque el riesgo es vascular.'),
 ('¿Dónde se realiza esta cirugía en Chile?', 'El Dr. David Lazo realiza cirugía torácica robótica en Clínica Las Condes y en el Hospital Clínico San Borja Arriarán, en Santiago. La evaluación inicial puede hacerse en consulta presencial o por telemedicina.'),
]

page('index.html', BASE,
     'Opérculo torácico: cirugía robótica · Dr. David Lazo',
     'Síndrome del opérculo torácico neurogénico, venoso y arterial: causas, clínica, estudio y resección robótica de la primera costilla. Dr. David Lazo, Santiago.',
     'Síndrome del opérculo torácico: resolución robótica', None, 'index',
     'Síndrome del opérculo torácico:<br><em>resolución robótica</em>',
     'Cuando la primera costilla o los músculos escalenos comprimen el plexo braquial, la arteria o la vena subclavia, la descompresión puede hacerse por vía robótica transtorácica: sin incisión en el cuello ni en la axila y con visión directa y magnificada de las estructuras que hay que liberar.',
     BODY_HUB, FAQ_HUB, 'Preguntas frecuentes sobre el opérculo torácico',
     [('Cirugía torácica robótica','https://rats.cl/'),('Opérculo torácico',BASE)],
     extra_ld={"about":{"@type":"MedicalCondition","name":"Síndrome del opérculo torácico","alternateName":["Thoracic outlet syndrome","TOS","SOT"],"possibleTreatment":{"@type":"MedicalProcedure","name":"Resección robótica de la primera costilla","procedureType":"https://schema.org/SurgicalProcedure"}}})

# ═══════════════════════════════════════════════ CAUSAS ═══
BODY_CAUSAS = f'''
  <section class="section" id="anomalias-oseas">
    <div class="inner">
      <h2 class="section-title">Anomalías óseas</h2>
      <p class="section-lead">Son la causa más reconocible y la que con mayor frecuencia se asocia a las formas vasculares. Se detectan en una radiografía simple y condicionan la planificación quirúrgica: definen si la vía robótica transtorácica basta por sí sola o si hace falta un abordaje supraclavicular complementario.</p>
      <div class="defs">
        <div class="def"><span class="d-tag">Costilla cervical</span><h3>Costilla supernumeraria desde C7</h3><p>Presente en menos del 1 % de la población, más frecuente en mujeres. Es el hallazgo característico del SOT arterial: la arteria subclavia pasa sobre ella y se estenosa, con dilatación postestenótica, aneurisma y embolias. Puede ser completa o incompleta, unida a la primera costilla por una banda fibrosa.</p></div>
        <div class="def"><span class="d-tag">Primera costilla anómala</span><h3>Alteración del espacio costoclavicular</h3><p>Una primera costilla hipoplásica, fusionada o de inserción anómala estrecha el espacio entre la clavícula y la costilla, donde pasa la vena subclavia. Es un mecanismo del SOT venoso y del síndrome de Paget-Schroetter.</p></div>
        <div class="def"><span class="d-tag">Apófisis transversa de C7</span><h3>Apófisis prominente o elongada</h3><p>Una apófisis transversa de C7 alargada actúa como una costilla cervical rudimentaria y suele acompañarse de una banda fibrosa hacia la primera costilla, con compresión del plexo o de la arteria.</p></div>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="bandas">
    <div class="inner">
      <h2 class="section-title">Bandas fibromusculares: la clasificación de Roos</h2>
      <p class="section-lead">Roos describió siete tipos de bandas fibrosas y musculares anómalas en el opérculo, a partir de más de 2.300 pacientes evaluados y 980 operaciones. Son la causa más frecuente del SOT neurogénico y no se ven en la radiografía: se identifican durante la cirugía. Su distribución se correlaciona con la variante clínica.</p>
      <div class="cmp-wrap">
        <table class="cmp-table">
          <thead><tr><th>Tipo</th><th>Presentación</th><th>Descripción</th></tr></thead>
          <tbody>
            <tr><td><strong>I</strong></td><td>Neurogénico-arterial</td><td>Costilla cervical larga con banda que se inserta hacia el tubérculo del escaleno.</td></tr>
            <tr><td><strong>II</strong></td><td>Neurogénico-arterial</td><td>Costilla cervical corta con una banda larga de inserción similar al tipo I.</td></tr>
            <tr><td><strong>III</strong></td><td>Neurogénico</td><td>Banda miofascial con el trayecto de una costilla cervical, insertada cerca del tubérculo del escaleno; comprime las ramas C8-T1 del plexo.</td></tr>
            <tr><td><strong>IV</strong></td><td>Neurogénico-arterial</td><td>Banda en V formada por las fibras posteriores del escaleno anterior y las anteriores del escaleno medio, sobre el espacio neuroarterial.</td></tr>
            <tr><td><strong>V</strong></td><td>Neurogénico-arterial</td><td>Escaleno mínimo: fibras independientes de origen escalénico que se insertan en la primera costilla entre la arteria y el plexo.</td></tr>
            <tr><td><strong>VI</strong></td><td>Neurogénico-arterial</td><td>Similar al tipo V, pero las fibras se insertan en la fascia de Sibson sin alcanzar la primera costilla.</td></tr>
            <tr><td><strong>VII</strong></td><td>Venoso</td><td>Banda en V formada por un componente costoclavicular hipertrófico por delante y las fibras anteriores del escaleno anterior, insertada en la primera costilla por detrás de la vena.</td></tr>
          </tbody>
        </table>
      </div>
      {robot_box('Qué cambia con el robot', [
        'Las bandas de Roos y los escalenos anómalos se insertan en la primera costilla. Al abordarla desde el interior del tórax bajo magnificación, se ven las inserciones de los escalenos y de las bandas sobre la costilla y se seccionan bajo visión directa junto con ella, sin tener que retraer el plexo para descubrirlas.',
        'Las bandas de tipo I y II —asociadas a costilla cervical— y las que nacen en el cuello quedan fuera del campo torácico: en esos casos la resección robótica se complementa con un abordaje supraclavicular. Por eso el estudio previo con imagen es lo que define la vía.'])}
    </div>
  </section>

  <section class="section" id="anomalias-musculares">
    <div class="inner">
      <h2 class="section-title">Anomalías musculares y trauma</h2>
      <div class="defs">
        <div class="def"><span class="d-tag">Escalenos</span><h3>Alteraciones del triángulo interescalénico</h3><p>Fusiones musculares, músculos supernumerarios, cambios histológicos e hipertrofia de los escalenos anterior y medio. Afectan sobre todo a la arteria subclavia y al plexo braquial.</p></div>
        <div class="def"><span class="d-tag">Pectoral menor</span><h3>Espacio subcoracoideo</h3><p>La hipertrofia severa del pectoral menor —fisicoculturistas, levantadores de pesas— estrecha el espacio bajo su tendón. Es causa principalmente de compresión venosa y se trata por separado (tenotomía del pectoral menor).</p></div>
        <div class="def"><span class="d-tag">Trauma agudo</span><h3>Hiperextensión-flexión del cuello</h3><p>Accidentes de tránsito (latigazo cervical), fracturas de clavícula o de primera costilla y los cambios inflamatorios crónicos que dejan. Se asocia con mayor frecuencia al SOT neurogénico, pero puede producir cualquiera de las tres variantes.</p></div>
        <div class="def"><span class="d-tag">Trauma crónico</span><h3>Movimientos repetitivos</h3><p>Uso repetido del cuello y las extremidades superiores: apiladores de cajas, lanzadores de béisbol, nadadores, músicos. También puede asociarse a cualquiera de las tres variantes.</p></div>
      </div>
      {refs_html(['connolly','roos','martinez','hussain','nguyen'])}
      {pager(None, ('clinica','Clínica'))}
    </div>
  </section>
'''
FAQ_CAUSAS = [
 ('¿Qué causa el síndrome del opérculo torácico?', 'Cualquier estructura que estreche el espacio entre la clavícula, la primera costilla y los escalenos: una costilla cervical, una primera costilla anómala, una apófisis transversa de C7 elongada, bandas fibrosas o musculares anómalas, hipertrofia de los escalenos o del pectoral menor, y las secuelas de un traumatismo agudo o repetitivo.'),
 ('¿La costilla cervical siempre da síntomas?', 'No. Está presente en menos del 1 % de la población y la mayoría de las personas que la tienen no desarrollan síntomas. Cuando los produce, es la causa característica de la variante arterial.'),
 ('¿Se ven las bandas fibrosas en los exámenes?', 'Habitualmente no. Las bandas de Roos son estructuras fibromusculares que no aparecen en la radiografía y rara vez en la tomografía; se identifican durante la cirugía, en las inserciones de los escalenos sobre la primera costilla.'),
]
page('causas.html', BASE+'/causas',
     'Opérculo torácico: causas · Dr. David Lazo',
     'Causas del síndrome del opérculo torácico: costilla cervical, primera costilla anómala, bandas de Roos, anomalías musculares y trauma. Dr. David Lazo.',
     'Causas del síndrome del opérculo torácico', 'Causas', 'causas',
     'Causas del <em>opérculo torácico</em>',
     'Anomalías óseas, bandas fibromusculares, alteraciones de los escalenos y del pectoral menor, y trauma. Lo que estrecha el espacio define la variante clínica y también la vía quirúrgica.',
     BODY_CAUSAS, FAQ_CAUSAS, 'Preguntas frecuentes sobre las causas',
     [('Cirugía torácica robótica','https://rats.cl/'),('Opérculo torácico',BASE),('Causas',BASE+'/causas')])

# ═══════════════════════════════════════════════ CLÍNICA ═══
BODY_CLINICA = f'''
  <section class="section" id="variantes">
    <div class="inner">
      <h2 class="section-title">Tres variantes, tres formas de presentarse</h2>
      <p class="section-lead">El síndrome se clasifica por la estructura comprimida. La variante neurogénica es la más frecuente con diferencia; las vasculares son raras, pero son las que exigen actuar antes.</p>
      <div class="defs">
        <div class="def"><span class="d-tag">SOT neurogénico · &gt; 95 %</span><h3>Compresión del plexo braquial</h3>
          <ul><li>Dolor, parestesias y debilidad de la extremidad superior afectada, con frecuencia de predominio cubital (cuarto y quinto dedo).</li><li>Se agrava con la elevación o el uso sostenido de los brazos y con las maniobras provocativas: rotación del cuello, abducción del brazo.</li><li>Sensibilidad a la palpación de los escalenos.</li><li>Atrofia muscular de la mano: rara, propia de casos avanzados.</li></ul></div>
        <div class="def"><span class="d-tag">SOT venoso · ~3 %</span><h3>Compresión de la vena subclavia</h3>
          <ul><li>Fatiga de los antebrazos con el esfuerzo.</li><li>Aumento de volumen de antebrazo, mano y dedos con cianosis, parestesias, dolor y edema.</li><li>Circulación colateral venosa visible en hombro y cuello.</li><li>Trombosis venosa profunda de esfuerzo: <strong>síndrome de Paget-Schroetter</strong>, típico de personas jóvenes y deportistas, de inicio brusco.</li><li>Tromboembolismo pulmonar y gangrena venosa: raros.</li></ul></div>
        <div class="def"><span class="d-tag">SOT arterial · ~1 %</span><h3>Compresión de la arteria subclavia</h3>
          <ul><li>Dolor, palidez, parestesias y frialdad de la extremidad: isquemia.</li><li>Diferencia de pulsos y de presión arterial entre ambos brazos.</li><li>Soplo subclavio, masa pulsátil supraclavicular.</li><li>A diferencia del neurogénico, no hay sensibilidad a la palpación de los escalenos.</li><li>La estenosis o trombosis de la subclavia puede derivar en embolias digitales y aneurisma postestenótico.</li></ul></div>
      </div>
      {robot_box('Qué cambia con el robot', [
        'Las tres variantes comparten el mecanismo —la primera costilla y los escalenos— y por eso comparten la solución: resecar la costilla y seccionar los escalenos, hoy por vía robótica transtorácica. Lo que cambia entre una y otra es la urgencia y lo que hay que hacer antes o después de la descompresión.',
        'En el SOT venoso con trombosis de esfuerzo, la secuencia es trombólisis dirigida por catéter y descompresión precoz; en series robóticas publicadas, una parte de los pacientes requiere venoplastía posterior para completar la permeabilidad. En el arterial, la dilatación o el aneurisma de la subclavia se reparan con cirugía vascular en el mismo plan. Ver <a href="' + BASE + '/tratamiento">Tratamiento</a>.'])}
    </div>
  </section>

  <section class="section section-alt" id="diferencial">
    <div class="inner">
      <h2 class="section-title">Con qué se confunde</h2>
      <p class="section-lead">El SOT neurogénico llega tarde a diagnóstico con frecuencia, después de un largo estudio por otras causas. Los síntomas se superponen con varias entidades más comunes, y descartarlas es parte del diagnóstico.</p>
      <ul class="list-check">
        <li><strong>Radiculopatía cervical</strong> C8-T1, por hernia discal o espondilosis.</li>
        <li><strong>Síndrome del túnel carpiano</strong> y <strong>neuropatía cubital en el codo</strong>.</li>
        <li><strong>Patología del hombro</strong>: manguito rotador, capsulitis, inestabilidad.</li>
        <li><strong>Síndrome del pectoral menor</strong>, que puede coexistir con el SOT y tratarse por separado.</li>
        <li><strong>Distrofia simpática refleja</strong> y dolor miofascial de la cintura escapular.</li>
        <li><strong>Trombosis venosa por catéter</strong> en la forma venosa; <strong>vasculitis</strong> y <strong>Raynaud</strong> en la arterial.</li>
      </ul>
      {refs_html(['hussain','cook','nguyen','burt2018'])}
      {pager(('causas','Causas'), ('estudio','Estudio'))}
    </div>
  </section>
'''
FAQ_CLINICA = [
 ('¿Cuáles son los síntomas del opérculo torácico neurogénico?', 'Dolor, hormigueo y debilidad del brazo y la mano, habitualmente en el borde cubital, que se agravan al trabajar con los brazos elevados o con la rotación del cuello. La atrofia de la musculatura de la mano es rara y aparece en casos avanzados.'),
 ('¿Qué es el síndrome de Paget-Schroetter?', 'Es la trombosis de esfuerzo de la vena subclavia: la expresión más grave del opérculo torácico venoso. Se presenta en personas jóvenes y deportistas como un brazo hinchado, pesado y azulado de inicio brusco, con venas visibles en hombro y pecho.'),
 ('¿Cómo sé si la compresión es arterial?', 'Por frialdad, palidez y dolor de la mano o los dedos, diferencia de pulsos o de presión entre ambos brazos, y un soplo o una masa pulsátil sobre la clavícula. Casi siempre hay una costilla cervical o una primera costilla anómala.'),
]
page('clinica.html', BASE+'/clinica',
     'Opérculo torácico: síntomas y clínica · Dr. David Lazo',
     'Clínica del opérculo torácico neurogénico, venoso (Paget-Schroetter) y arterial: síntomas, signos y diagnóstico diferencial. Dr. David Lazo, Santiago.',
     'Clínica del síndrome del opérculo torácico', 'Clínica', 'clinica',
     'Clínica del <em>opérculo torácico</em>',
     'Cómo se presenta cada variante —neurogénica, venosa y arterial—, qué la agrava y con qué se confunde. Las tres comparten el mecanismo; difieren en la urgencia.',
     BODY_CLINICA, FAQ_CLINICA, 'Preguntas frecuentes sobre los síntomas',
     [('Cirugía torácica robótica','https://rats.cl/'),('Opérculo torácico',BASE),('Clínica',BASE+'/clinica')])

# ═══════════════════════════════════════════════ ESTUDIO ═══
BODY_ESTUDIO = f'''
  <section class="section" id="examenes">
    <div class="inner">
      <h2 class="section-title">Los exámenes y para qué sirve cada uno</h2>
      <p class="section-lead">El diagnóstico es clínico. Ningún examen lo confirma por sí solo: el estudio identifica la causa anatómica, define la variante, descarta los diagnósticos diferenciales y —esto es lo que interesa al cirujano— establece si la compresión depende de la primera costilla y los escalenos o de estructuras que exigen otra vía.</p>
      <div class="defs">
        <div class="def"><span class="d-tag">Todo SOT</span><h3>Radiografía de tórax y columna cervical</h3><p>Costilla cervical, primera costilla anómala, apófisis transversa de C7 elongada, fracturas antiguas de clavícula y callos óseos.</p></div>
        <div class="def"><span class="d-tag">Sospecha neurogénica</span><h3>Electromiografía y conducción nerviosa</h3><p>Sirven sobre todo para descartar túnel carpiano, neuropatía cubital y radiculopatía. En el SOT neurogénico verdadero pueden mostrar compromiso del tronco inferior del plexo (nervio cutáneo antebraquial medial, cubital).</p></div>
        <div class="def"><span class="d-tag">Sospecha arterial</span><h3>Registro de volumen de pulso (PVR)</h3><p>Pletismografía segmentaria de ambas extremidades, en reposo y con el brazo en abducción: documenta la caída de presión y de la onda de pulso del lado comprimido.</p></div>
        <div class="def"><span class="d-tag">SOT vasculares</span><h3>Ecografía Doppler / dúplex</h3><p>Muestra trombos y aneurismas y, de forma dinámica, la oclusión del vaso con el brazo elevado (aumento de la velocidad del flujo arterial, cese del flujo venoso).</p></div>
        <div class="def"><span class="d-tag">Todo SOT</span><h3>AngioTC o angioRM con maniobras provocativas</h3><p>Con los brazos en reposo y en abducción. Muestra la compresión dinámica de la arteria o la vena, el sitio exacto y la relación con la costilla y los escalenos. Es el examen que planifica la cirugía.</p></div>
        <div class="def"><span class="d-tag">Solo neurogénico</span><h3>Bloqueo de escalenos con toxina botulínica</h3><p>Inyección guiada en el escaleno anterior. Alivio transitorio de los síntomas en una parte de los pacientes; se usa como prueba diagnóstica previa a la cirugía y como puente terapéutico.</p></div>
      </div>
      {robot_box('Qué cambia con el robot', [
        'La angioTC o la angioRM con maniobras es el examen que decide la vía. Si la compresión está en la primera costilla y en los escalenos, la resección robótica transtorácica la resuelve. Si hay costilla cervical, bandas cervicales o una lesión vascular que reparar, el plan incluye un abordaje supraclavicular o la cirugía vascular. La imagen se lee pensando en esa decisión.'])}
    </div>
  </section>

  <section class="section section-alt" id="toxina">
    <div class="inner">
      <h2 class="section-title">Toxina botulínica: qué dice la evidencia</h2>
      <p class="section-lead">Una revisión sistemática de 2023 reunió ocho estudios (un ensayo aleatorizado, una cohorte prospectiva y seis retrospectivas) con 716 procedimientos en al menos 497 pacientes con SOT presumiblemente neurogénico.</p>
      <div class="stat-strip">
        <div class="st"><b>716</b><span>procedimientos en ≥ 497 pacientes, 8 estudios</span><small>Kök 2023</small></div>
        <div class="st"><b>46–63 %</b><span>de los procedimientos primarios con reducción de síntomas</span><small>Kök 2023</small></div>
        <div class="st"><b>1–6 meses</b><span>de duración del alivio sintomático</span><small>Kök 2023</small></div>
        <div class="st"><b>0</b><span>complicaciones mayores reportadas</span><small>Kök 2023</small></div>
      </div>
      <p class="section-lead" style="margin-top:1.5rem;">La conclusión de los autores: con evidencia de calidad limitada, la toxina puede dar un alivio breve en algunos pacientes neurogénicos, y su papel como herramienta diagnóstica sigue poco explorado. En la práctica, una buena respuesta al bloqueo orienta hacia la cirugía; una mala respuesta no la descarta.</p>
      {refs_html(['hussain','kok','cook','nguyen'])}
      {pager(('clinica','Clínica'), ('tratamiento','Tratamiento'))}
    </div>
  </section>
'''
FAQ_ESTUDIO = [
 ('¿Qué examen confirma el opérculo torácico?', 'Ninguno por sí solo: el diagnóstico es clínico. La angioTC o la angioRM con los brazos en reposo y en abducción muestra la compresión dinámica y el sitio exacto, y es el examen que planifica la cirugía. La electromiografía sirve sobre todo para descartar otras neuropatías.'),
 ('¿Para qué sirve la toxina botulínica en el opérculo torácico?', 'Se inyecta en el escaleno anterior como prueba: si los síntomas se alivian de forma transitoria, apoya el diagnóstico y orienta a la cirugía. Solo se usa en la variante neurogénica y el alivio, cuando ocurre, dura de uno a seis meses.'),
 ('¿Qué exámenes debo llevar a la consulta?', 'Radiografía de tórax y columna cervical, angioTC o angioRM con maniobras, electromiografía con conducción nerviosa y, si se sospecha compromiso vascular, ecografía Doppler dinámica.'),
]
page('estudio.html', BASE+'/estudio',
     'Opérculo torácico: estudio y diagnóstico · Dr. David Lazo',
     'Estudio del opérculo torácico: radiografía, EMG, PVR, Doppler, angioTC o angioRM con maniobras y bloqueo con toxina botulínica. Dr. David Lazo, Santiago.',
     'Estudio del síndrome del opérculo torácico', 'Estudio', 'estudio',
     'Estudio del <em>opérculo torácico</em>',
     'Radiografía, electromiografía, registro de volumen de pulso, Doppler y angioTC o angioRM con maniobras provocativas. El objetivo del estudio es doble: descartar lo que se parece y decidir la vía quirúrgica.',
     BODY_ESTUDIO, FAQ_ESTUDIO, 'Preguntas frecuentes sobre el estudio',
     [('Cirugía torácica robótica','https://rats.cl/'),('Opérculo torácico',BASE),('Estudio',BASE+'/estudio')])

# ═══════════════════════════════════════════════ TRATAMIENTO ═══
BODY_TRAT = f'''
  <section class="section" id="multidisciplinario">
    <div class="inner">
      <h2 class="section-title">Un manejo multidisciplinario</h2>
      <p class="section-lead">El síndrome del opérculo torácico se trata en equipo: cirugía torácica, fisiatría y kinesiología, neurología, cirugía vascular y radiología intervencional. El cirujano torácico coordina la evaluación y aporta la vía robótica transtorácica; la terapia física es el primer escalón en la variante neurogénica, y la cirugía vascular entra cuando hay una lesión del vaso que reparar.</p>
      <div class="defs">
        <div class="def"><span class="d-tag">Primer escalón · neurogénico</span><h3>Terapia física</h3><ul><li>Masoterapia y ultratermia.</li><li>Ejercicios cervicales y elongación de los escalenos.</li><li>Fortalecimiento del trapecio y de la cintura escapular.</li><li>Corrección postural y ergonomía; analgesia.</li><li>Bloqueo con toxina botulínica en casos seleccionados.</li></ul><p style="margin-top:0.6rem;">Varios meses de tratamiento bien realizado antes de plantear la cirugía, salvo déficit neurológico progresivo.</p></div>
        <div class="def"><span class="d-tag">Venoso</span><h3>Anticoagulación y trombólisis</h3><p>En la trombosis de esfuerzo: anticoagulación, venografía y trombólisis farmacomecánica dirigida por catéter, seguidas de descompresión quirúrgica precoz. Tras la resección de la costilla, una parte de los pacientes necesita venoplastía con balón para completar la permeabilidad.</p></div>
        <div class="def"><span class="d-tag">Arterial</span><h3>Descompresión y reparación arterial</h3><p>Con dilatación de la subclavia sin complicaciones basta la descompresión y vigilancia; con aneurisma o embolias distales se añade reconstrucción arterial, tromboembolectomía o bypass, con cirugía vascular.</p></div>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="vias">
    <div class="inner">
      <h2 class="section-title">Las vías quirúrgicas</h2>
      <p class="section-lead">La primera costilla puede resecarse por encima de la clavícula, por la axila o desde el interior del tórax. Cada vía tiene su lugar; la diferencia principal está en cómo se ve la costilla y cuánto hay que manipular el plexo braquial para llegar a ella.</p>
      <div class="cmp-wrap">
        <table class="cmp-table">
          <thead><tr><th>Vía</th><th>Incisión</th><th>Qué permite</th><th>Plexo braquial</th><th>Cuándo se prefiere</th></tr></thead>
          <tbody>
            <tr><td><strong>Supraclavicular / infraclavicular</strong></td><td>Una, sobre o bajo la clavícula</td><td>Reparaciones arteriales o venosas, neurólisis del plexo, resección de costillas cervicales y bandas cervicales</td><td>Se expone y se moviliza directamente</td><td>Costilla cervical, lesión vascular que reparar</td></tr>
            <tr><td><strong>Transaxilar</strong> (Roos)</td><td>Una, en la axila</td><td>Resección de la primera costilla y escalenectomía parcial; versión videoasistida descrita</td><td>Se retrae para exponer la costilla</td><td>Vía clásica del neurogénico y del venoso sin anomalías asociadas</td></tr>
            <tr class="cmp-hl"><td><strong>Mínimamente invasiva transtorácica</strong> (VATS / RATS)</td><td>Tres o cuatro puertos de menos de 2 cm en el costado</td><td>Resección completa de la primera costilla, desarticulación costoesternal y sección de los escalenos bajo visión magnificada</td><td>Se ve desde abajo; no se retrae ni se manipula</td><td>Compresión por primera costilla o escalenos, en las tres variantes</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section id="robotica" class="section section-dark">
    <div class="inner">
      <p class="ref-label">Resolución robótica</p>
      <h2 class="section-title w">Resección robótica transtorácica<br><em style="font-style:italic;color:var(--teal-lt);">de la primera costilla, paso a paso</em></h2>
      <div class="two-col">
        <ul class="feature-list">
          <li class="fi"><div class="fi-ico"><span class="fi-num">1</span></div><div class="fi-text"><h4>Posición y puertos</h4><p>Decúbito lateral. Tres o cuatro puertos en el costado del tórax, con el pulmón excluido. El robot se acopla y el cirujano opera desde la consola.</p></div></li>
          <li class="fi"><div class="fi-ico"><span class="fi-num">2</span></div><div class="fi-text"><h4>Exposición desde el interior</h4><p>Se abre la pleura parietal sobre la primera costilla. Bajo magnificación 3D se identifican, ordenados sobre ella, la vena subclavia, el escaleno anterior, la arteria subclavia, el plexo braquial y el escaleno medio.</p></div></li>
          <li class="fi"><div class="fi-ico"><span class="fi-num">3</span></div><div class="fi-text"><h4>Sección de los escalenos</h4><p>Los escalenos anterior y medio se desinsertan de la costilla con instrumental articulado, con el nervio frénico y el plexo a la vista y sin retraerlos.</p></div></li>
          <li class="fi"><div class="fi-ico"><span class="fi-num">4</span></div><div class="fi-text"><h4>Desarticulación y resección</h4><p>La costilla se desarticula de la unión costoesternal por delante y se secciona por detrás, cerca de la apófisis transversa, para no dejar un muñón posterior que vuelva a comprimir. Se retira por un puerto.</p></div></li>
          <li class="fi"><div class="fi-ico"><span class="fi-num">5</span></div><div class="fi-text"><h4>Comprobación y cierre</h4><p>Se verifica que vena, arteria y plexo quedaron libres en todo su trayecto. Drenaje pleural fino que se retira antes del alta.</p></div></li>
        </ul>
        <div>
          <div class="video-slot">
            <div><strong>Vídeo: resección robótica de la primera costilla</strong><small>Espacio reservado para el vídeo del autor, en producción.</small></div>
          </div>
          <figure class="fig" style="margin-top:1.25rem;">
            <img src="local-imgs/marcacion-puertos.webp" alt="Marcación preoperatoria de los puertos robóticos en el costado del paciente" loading="lazy" width="585" height="744" decoding="async">
            <figcaption>Marcación de los puertos en el costado del tórax. Foto del autor <em>(confirmar)</em>.</figcaption>
          </figure>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="resultados">
    <div class="inner">
      <h2 class="section-title">Resultados publicados de la vía robótica</h2>
      <p class="section-lead">Las series robóticas transtorácicas publicadas son todavía de un solo centro y sin comparación aleatorizada con las vías clásicas, pero coinciden en dos hallazgos: la exposición completa del opérculo sin retracción neurovascular y la ausencia de lesiones neurovasculares.</p>
      <div class="stat-strip">
        <div class="st"><b>83</b><span>resecciones robóticas por Paget-Schroetter: sin complicaciones quirúrgicas ni lesión neurovascular</span><small>Gharagozloo 2019</small></div>
        <div class="st"><b>100 %</b><span>de permeabilidad de la vena subclavia a 24 meses de mediana de seguimiento</span><small>Gharagozloo 2019</small></div>
        <div class="st"><b>31 %</b><span>necesitó angioplastía (24 %) o stent (7 %) tras la resección para completar la permeabilidad</span><small>Gharagozloo 2019</small></div>
        <div class="st"><b>4 días</b><span>de hospitalización (mediana); 128 min de tiempo operatorio medio</span><small>Gharagozloo 2019</small></div>
      </div>
      <p class="section-lead" style="margin-top:1.5rem;">Burt describe la técnica robótica transtorácica como la que ofrece «una exposición incontestable de la anatomía del opérculo y libertad de toda retracción neurovascular». La revisión de técnica de Costantino y Schumacher anticipa que las vías mínimamente invasivas serán cada vez más comunes a medida que más cirujanos adquieran experiencia toracoscópica y robótica, y que faltan datos a largo plazo para establecer su equivalencia o superioridad frente a la cirugía abierta.</p>
      {robot_box('Qué cambia con el robot', [
        'Frente a la vía transaxilar, el robot no trabaja en túnel: la costilla se ve entera, con las estructuras neurovasculares por encima, sin retraerlas. Frente a la vía supraclavicular, evita la disección del cuello y el riesgo sobre el frénico y el conducto torácico. Lo que no puede hacer es resecar una costilla cervical ni reparar un vaso: por eso el plan quirúrgico se define con la imagen y, cuando corresponde, con cirugía vascular en el mismo acto.'])}
      {refs_html(['burt2018','burt2020','ghara2019','costantino','kara','cook','nguyen','kok'])}
      {pager(('estudio','Estudio'), None)}
    </div>
  </section>
'''
FAQ_TRAT = [
 ('¿Cuándo se opera el opérculo torácico?', 'En la variante neurogénica, cuando varios meses de terapia física bien realizada no controlan los síntomas o hay déficit neurológico progresivo. En la venosa, de forma precoz tras la trombólisis de la trombosis de esfuerzo. En la arterial, ante estenosis, aneurisma o embolias, con planificación conjunta con cirugía vascular.'),
 ('¿Qué ventajas tiene la resección robótica de la primera costilla?', 'Se hace desde el interior del tórax por tres o cuatro puertos pequeños: sin incisión en el cuello ni en la axila, con la costilla completa a la vista bajo magnificación 3D y sin retraer el plexo braquial ni los vasos subclavios. Las series publicadas no reportan lesiones neurovasculares.'),
 ('¿Cuánto dura la recuperación?', 'La hospitalización es corta —en la serie robótica más grande publicada, cuatro días de mediana— y el retorno a la actividad es progresivo. En la variante venosa se mantiene anticoagulación durante unos meses y se controla la permeabilidad de la vena. El plan se define caso a caso.'),
 ('¿Cuándo se necesita además un cirujano vascular?', 'Cuando hay una lesión del vaso que tratar o reparar: trombosis activa que requiere trombólisis, estenosis venosa residual que necesite venoplastía, o dilatación, aneurisma o embolias de la arteria subclavia. También cuando hay una costilla cervical, que se reseca por vía supraclavicular.'),
]
page('tratamiento.html', BASE+'/tratamiento',
     'Opérculo torácico: tratamiento robótico · Dr. David Lazo',
     'Tratamiento del opérculo torácico: terapia física, vías supraclavicular y transaxilar, y resección robótica de la primera costilla. Dr. David Lazo, Santiago.',
     'Tratamiento del síndrome del opérculo torácico', 'Tratamiento', 'tratamiento',
     'Tratamiento del <em>opérculo torácico</em>',
     'Terapia física primero en la variante neurogénica; trombólisis y descompresión precoz en la venosa; reparación arterial en la arterial. Y en las tres, cuando la compresión depende de la primera costilla y los escalenos, la resección robótica transtorácica.',
     BODY_TRAT, FAQ_TRAT, 'Preguntas frecuentes sobre el tratamiento',
     [('Cirugía torácica robótica','https://rats.cl/'),('Opérculo torácico',BASE),('Tratamiento',BASE+'/tratamiento')],
     extra_ld={"about":{"@type":"MedicalCondition","name":"Síndrome del opérculo torácico","alternateName":["Thoracic outlet syndrome","TOS","SOT"],"possibleTreatment":{"@type":"MedicalProcedure","name":"Resección robótica transtorácica de la primera costilla","procedureType":"https://schema.org/SurgicalProcedure"}}})
