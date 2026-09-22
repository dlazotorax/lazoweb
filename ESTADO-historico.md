# ESTADO — HISTÓRICO (archivo)

> **Este archivo es el registro cronológico completo del proyecto, de julio a agosto de 2026.**
> No hace falta leerlo para trabajar: el documento de trabajo es **`ESTADO.md`**, que recoge
> el estado actual, las reglas y los pendientes.
>
> Se conserva porque contiene el detalle de cada sesión, las mediciones con su fecha y el
> razonamiento detrás de decisiones que en `ESTADO.md` aparecen solo como conclusión.
> Consúltalo cuando necesites saber **por qué** algo quedó como quedó.

---

## 1. Infraestructura

- **Repo:** `dlazotorax/lazoweb`, rama `main`. Sitios en `dist/<dominio>/`.
- **Hosting:** Vercel, deploy automático al pushear a `main`.
- **Propagación del CDN: ~40-90 s.** Si tras un push aún ves lo viejo, es caché
  (`x-vercel-cache: HIT`), no el sitio. Espera y revalida con `?v=N`.
- **Token GitHub:** `Paginas web/.github-token` (fine-grained, solo lazoweb). Nunca commitearlo.
- Flujo: clonar fresco desde GitHub en el sandbox → editar → commit → push a `main`.
- La carpeta `Projects/Paginas web` es respaldo y está **desactualizada** respecto al repo.

| Dominio | Páginas | Rol |
|---|---|---|
| cirugiatoracica.cl | 4 (`/`, `/perfil`, `/publicaciones`, `/links`) | Hub |
| hiperhidrosis.cl | 16 | Pacientes |
| cancerpulmonar.cl | 7 | Pacientes |
| broncoscopia.cl | 3 | Dual |
| rats.cl | 1 | Médicos referentes |
| videotoracoscopia.cl | 1 | Videotoracoscopía (VATS) — dominio principal desde jul-2026 |
| vats.cl | 308 → **videotoracoscopia.cl** | Redirect |
| cirugiadetorax.cl | 301 → cirugiatoracica.cl | Redirect |

---

## 2. YA ESTÁ HECHO — no volver a proponerlo

### Del lado de David (verificado en jul-2026)
- ✅ **Google Search Console** — los 6 dominios, propiedades de dominio (`sc-domain:`), sitemaps enviados
- ✅ **Google Business Profile** — existe, 160 interacciones, dirección Estoril 450 (CLC)
- ✅ **ORCID `0009-0007-0806-6679`** — 7 "also known as", bio, website, 2 empleos, **público**. Works: tiene 26 cargados; PENDIENTE reimportar `lazo_31_publicaciones.bib` para sumar los 5 abstracts → quedaría en 31
- ✅ **Dominio primario sin-www en Vercel** — verificado: `www.*` → `sin-www` en toda la red
- ✅ **LinkedIn actualizado** (ya no dice MEDS)

### Del lado del código
- ✅ Entidad unificada: `@id` = `https://cirugiatoracica.cl/#david-lazo` en **31 nodos Physician**
- ✅ `sameAs`: 6 dominios propios + ORCID + LinkedIn + Doctoralia (×2) + TopDoctors + CTSNet + Instagram + Encuadrado
- ✅ `identifier` con `propertyID: "ORCID"` en los 6 dominios
- ✅ `memberOf` (WABIP, ACS, IASLC, ERS, ISHLT, SOCICH, **ALAT**, **SER**) y `alumniOf` en schema
- ✅ **31 publicaciones verificadas** en `/publicaciones` (2004-2023): 26 artículos revisados por pares + 5 resúmenes de congreso indexados
- ✅ Publicaciones enlazadas desde broncoscopia (7), cancerpulmonar (6), vats (2)
- ✅ FAQ visible y distinto por dominio (24 preguntas) — antes había uno oculto y clonado
- ✅ Claims de ranking `#1`/`nº 1` eliminados (9 lugares)
- ✅ robots.txt con bots de IA en los 6; `cleanUrls` en todos
- ✅ 301: `/perfil.html`, `/index.html`, `/publicaciones.html`

---

## 3. PENDIENTE DE VERDAD (revisado 5-ago-2026)

### De David — por impacto

| # | Qué | Por qué importa |
|---|---|---|
| 1 | **GA4: marcar conversiones y vincular Search Console** | El tag ya está instalado (ver §13). Falta marcar `reserva_presencial` y `reserva_telemedicina` como eventos clave, y añadir los 6 dominios en Admin → Flujos de datos → Configurar dominios |
| 2 | **Google Business Profile: conseguir reseñas** | Tiene **0**. Es la ficha que sale al googlear su nombre. Tiene 58 en Doctoralia — el flujo hacia GBP no existe |
| 3 | **GBP: cargar horario y categoría** | Google lo pide en el panel. El teléfono ya está |
| 4 | **ORCID: borrar el duplicado** "Resistencia a ciprofloxacino" (marca 32, son 31) | 2 minutos |
| 5 | **ORCID: cargar la regencia WABIP** | Su credencial internacional más fuerte y no aparece en ninguna parte del registro |
| 6 | **Fusionar las 2 fichas de Doctoralia** | 58 reseñas partidas. Doctoralia es el resultado #1 en "cirujano torácico Santiago" |
| 7 | **Pedir el enlace a WABIP, SOCICH y Finis Terrae** | Única vía de backlink institucional que queda. Backlinks actuales: cero |
| 8 | Cerrar el convenio para poder publicar la sección de cobertura | Es el hueco más grande de "cirugia hiperhidrosis" |
| 9 | CV: corregir coautores omitidos (ver §6) | |
| 10 | TopDoctors: reactivar ("no es posible contactar") | |

### De Claude

| # | Qué |
|---|---|
| 1 | ~~Página de docencia y menciones~~ — **HECHO** el 16/17-ago. Publicada en `/docencia` (§18 y adendas). Nota: eran **7** notas de CLC, no ~10 |
| 2 | ~~Instalar GA4 en las 33 páginas~~ — **HECHO** el 6-ago (§13). Sigue pendiente de David marcar las conversiones |
| 3 | Acordeón de FAQ en el resto de hiperhidrosis.cl — **sigue pendiente**, verificado hoy: `rubor-facial-patologico` no tiene ni un `.faq-q` |
| 4 | `/rats-vs-vats` — **sigue pendiente**, verificado hoy: `dist/rats/` solo tiene `index.html` |

---

## 4. DIAGNÓSTICO — el cuello de botella real

**No es indexación, no es estructura. Es autoridad.**

Datos de Search Console (**30 jul 2026**, últimos 3 meses):

| Dominio | Impresiones | Clics | Posición media |
|---|---|---|---|
| rats.cl | 82 | **4** | **8,2** |
| cancerpulmonar.cl | 71 | 2 | 23,6 |
| cirugiatoracica.cl | 223 | 1 | 45,6 |
| broncoscopia.cl | 49 | 1 | 19,4 |
| hiperhidrosis.cl | 133 | 0 | 44 |
| **Total** | **558** | **8** | — |

Comparado con jul-2026 (~112 impresiones, **0 clics**): la red pasó de invisible a
tener tráfico. **rats.cl es el activo que funciona** — posición 8,2 y la mitad de los
clics de toda la red. Confirma la tesis de la ventana abierta: RATS en Chile no tiene
competencia de contenido.

Toda la red **está indexada**. El 30-jul se pidió indexación manual de tres URLs que
Google conocía y no había indexado: `/publicaciones` y `/links` (estaban en
"Descubierta: actualmente sin indexar") y `cancerpulmonar.cl/que-es` (estaba en
"Rastreada: actualmente sin indexar" — peor señal: Google la rastreó y decidió no
indexarla).

**En las búsquedas objetivo la red no aparece.** Dominan Doctoralia y TopDoctors. En "EBUS Chile" la IA cita a **Clínica Alemana** como pionera — compite directo con el claim de David.

---

## 5. DECISIONES TOMADAS (no revisitar sin motivo nuevo)

- **NO partir rats.cl en subpáginas.** Tiene 1.104 palabras totales; partirlo en 5 daría ~220/pág.
  cancerpulmonar funciona porque cada página tiene ~1.100 propias: escribieron 7, no partieron 1.
  Primero contenido, después partición.
- **rats.cl NO cita publicaciones**: de los 26 artículos, **ninguno es de RATS**. Esa producción está en
  comunicaciones a congreso (programa SOCICH 2025), no en revistas indexadas. Presentarla como
  publicación sería inflar.
- **NO hay huella de PBN.** La duplicación real de prosa entre dominios es **3-10%**, solo el pie de
  contacto = boilerplate normal. (El "46%" que circuló era un error de medición: era CSS compartido.)
- **Sin claims de ranking.** Se conservan las cifras de volumen (+5.700 cirugías, +3.200 EBUS desde 2010,
  +200 RATS desde 2015) porque son dato propio y verificable. Pendiente decisión de David sobre
  "mayor experiencia en X en Chile" y "pionero en CryoEBUS en Latinoamérica" (siguen en rats/broncoscopia/perfil).
- **Categoría GBP "Cirujano torácico" NO EXISTE.** La única disponible es "Cirujano cardiovascular y
  torácico", que ya está puesta. No es un error. Compensar vía **Servicios** del GBP.
- **Graphify no aplica** a este proyecto: indexa grafos de dependencias de código; aquí es HTML estático
  sin funciones ni imports, ~40 archivos.

---

## 6. REGLA CRÍTICA — verificar antes de afirmar

Este es contenido médico bajo la responsabilidad profesional de David (YMYL). **Nunca publicar autoría,
cifras, credenciales o citas desde resúmenes de IA de buscadores.** Abrir siempre la fuente primaria.

**Errores cometidos en la sesión de jul-2026 (para no repetir):**
1. Atribuí a David un paper de **Bellvitge** basándome en un resumen de búsqueda. Cero coincidencias de
   "Lazo" al abrir el artículo.
2. Reporté **46% de duplicación** entre dominios; era CSS, no prosa. Casi provoca un rediseño innecesario.
3. Inventé la **paginación** de un paper (`149(2)` en vez de `171-177`) y adiviné un DOI (salió correcto
   por suerte, no por método).
4. Propuse Search Console, GBP, ORCID y una categoría inexistente — **todo ya hecho o imposible**.
   Verificar el estado ANTES de recomendar.

**Regla de oro del schema:** todo lo que va en JSON-LD **debe estar visible en la página**.
Antes había un FAQPage oculto clonado en 4 dominios (infracción de Google). Ya corregido — no reintroducir.

---

## 7. IDENTIDAD — datos canónicos

- **ORCID:** `0009-0007-0806-6679`
- **`@id`:** `https://cirugiatoracica.cl/#david-lazo`
- **Indexación del nombre:** SciELO → `Lazo P` · PubMed → **`Lazo P D`** · Elsevier → `P. David Lazo`
  (buscar "Lazo D" o "David Lazo" devuelve **cero**; ya resuelto vía "also known as" en ORCID)
- **Afiliación vigente:** Clínica Las Condes (desde ene-2026) + Hospital Clínico San Borja Arriarán
  (desde oct-2022). **MEDS terminó en dic-2025.**
- **Formación:** Médico-Cirujano PUC (2004) · Esp. Cirugía Torácica U. de Chile / INT (2009) ·
  Fellowship Trasplante Pulmonar, H.U. Puerta de Hierro Majadahonda (2010-2011)

### Publicaciones: 31 verificadas (26 artículos + 5 resúmenes de congreso)
**26 artículos revisados por pares:** 10 Rev Chil Enf Respir · 6 Rev Chil Cirugía · 4 Rev Med Chile ·
3 Rev Med Clin Condes · 1 Rev Chil Radiología · 1 Cir Cir · 1 Rev Chil Urología.
**5 resúmenes de congreso indexados** (verificados por DOI en Crossref salvo el de 2014):
- J Heart Lung Transplant 2023;42(4):S298 — PLLTX (DOI …685) y PLTX 15 años (DOI …684)
- Pediatr Crit Care Med 2021;22(Supl 1) — Awake ECMO (:135, DOI …252) y Chilean PICU (:196, DOI …832)
- J Thorac Oncol 2014;9(9):S184-5 — lipiodol marking (SIN DOI; solo ResearchGate)

Identificadores: 21 PID SciELO · 11 DOI · 5 PMID · 1 LILACS · 1 sin ID.
Archivo para importar: `lazo_31_publicaciones.bib`. Fuente del cruce final: ResearchGate
`/profile/David-Lazo-2` (listaba 31; 2 de ellas eran duplicados con codificación rota, descartados).

**7 artículos no estaban en el CV original** (los más valiosos): biopsia líquida en adenocarcinoma
(Rev Med Clin Condes 2022) y recomendaciones de broncoscopía COVID-19 de la SER (2020).
El CV `CV_David_Lazo_2026.docx` ya incluye los 5 abstracts bajo el encabezado
"Resúmenes en Congresos Internacionales (indexados)".

**Errores del CV a corregir:** omite coautores sistemáticamente — #17 lista 4 de **14**; #14 lista 4 de 9
("Yévene" → **Yévenes**); #18 falta Clavero JM. CV corregido ya generado: `CV_David_Lazo_2026.docx`.

---

## 8. Archivos en esta carpeta

| Archivo | Para qué |
|---|---|
| `CV_David_Lazo_2026.docx` / `.pdf` | CV completo, Carta, 26 citas Vancouver verificadas |
| `lazo_31_publicaciones.bib` | Importar las 31 publicaciones a ORCID |
| `ORCID-instrucciones.md` | Pasos ORCID (ya ejecutados) |
| `apply_orcid.py` | Inyecta un ORCID en los nodos Physician de la red |
| `foto-publicaciones.jpg` | Hero de /publicaciones (ver nota abajo) |
| `.github-token` | Token GitHub — **nunca commitear** |

> **Nota sobre la imagen del hero:** es una escena generada por IA. Incluye una taza con el logo de
> **STS** (Society of Thoracic Surgeons), sociedad a la que David **no pertenece**, y manuscritos de
> escritura de ficción. Se mantiene por decisión suya. Reemplazar por una foto real de congreso ALAT
> cuando esté disponible.

---

## 9. Estándar SEO de la red

- **Canonical = SIN www** en toda la red.
- `cleanUrls: true` en `vercel.json` es obligatorio donde hay subpáginas `.html`.
- robots.txt permite explícitamente GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-Web,
  PerplexityBot, Google-Extended, Applebot-Extended, CCBot.
- Sitemap por dominio, siempre sin-www.
- Estilo: Arial/Figtree, teal `#0891b2`, navy `#0c1526`, serif `DM Serif Display`.

---

## 10. Intercambio vats.cl → videotoracoscopia.cl (25-jul-2026)

**Qué se hizo.** El término en español pasó a ser el dominio principal de la
videotoracoscopía; la sigla quedó como atajo memorable que redirige con 308.

**Por qué.** "VATS" casi no se busca en Chile — es jerga de cirujanos, que además
ya conocen a David. "Videotoracoscopía" es lo que escribe el paciente recién
derivado ("lo vamos a operar por videotoracoscopía") y el médico que deriva:
intención alta, abajo del embudo. La auditoría mostró además que ese resultado
está vacío de contenido chileno (lo ocupan Quirónsalud, Elsevier, hospitales
españoles). **Ninguno de los dos dominios tuvo sitio antes** (confirmado por
David), así que la migración no arrastra historial y fue el momento más barato
de hacerla: vats.cl tenía 1 página, 1 URL indexada y 0 clics.

**Estado:** videotoracoscopia.cl en línea, proyecto Vercel `videotoracoscopia`
creado con root `dist/videotoracoscopia`, www → apex 308. vats.cl sirve el stub
de redirección. 31 páginas de los otros 5 dominios actualizadas (enlaces, texto
visible y `sameAs`). `dist/uploads/` eliminado (47 archivos basura).

**No soltar vats.cl:** un .cl de 4 letras es escaso, está pagado hasta 2028 y es
el atajo que se dice en voz alta en un congreso.

### CORRECCIÓN a la auditoría del 25-jul — dos falsos positivos

Verificado contra el panel de Vercel, que es la fuente de verdad:

- **`cirugiadetorax.cl` NO devuelve 302.** Está configurado como **308** hacia
  cirugiatoracica.cl. El "302" venía de WebFetch.
- **Los host `www` NO responden 200.** Los seis dominios tienen `www` → apex con
  **308** (hiperhidrosis usa **301**, igualmente permanente). El estándar sin-www
  está bien aplicado en toda la red.

**Lección de método:** WebFetch reporta las redirecciones de forma poco fiable —
dio "302 Found" donde había 308, y sirvió contenido sin declarar el salto www→apex.
Para cualquier afirmación sobre códigos de redirección, **verificar en el panel de
Vercel**, no con WebFetch. Ver §6.

### Dos trampas de Vercel a recordar

1. Al agregar un dominio, la casilla **"Redirect apex domains to www (recommended)"
   viene MARCADA por defecto**. Es lo contrario al estándar sin-www: hay que
   desmarcarla siempre.
2. El desplegable de redirección a nivel de dominio **arranca en 307 (temporal)**.
   Hay que cambiarlo a **308** a mano. La configuración del panel gana sobre el
   `vercel.json` del repo.

### Pendiente menor
- `www.vats.cl` encadena 2 saltos (→ vats.cl → videotoracoscopia.cl). Funciona,
  pero se puede apuntar directo al destino final.
- Commits `5b5028d` y `590937a` quedaron firmados con el correo de David en vez
  del de Claude (el rebase para corregirlo fue bloqueado). Cosmético.

---

## 11. Vocabulario: "cirugía de tórax" (30-jul-2026)

**Hallazgo.** El hub tenía **223 impresiones** y **107 de ellas** (48%) venían de
`cirugía de tórax` (70) y `cirugía torax` (37) — en posición ~45. Auditado el HTML:
la página decía **"cirugía torácica" 9 veces** y **"cirugía de tórax" cero**. Estaba
posicionando para un término que nunca usaba.

**Corrección aplicada** (commit `5ad0bb3`) en `dist/cirugiatoracica/index.html`:

- `<title>` y `og:title` → "Cirugía de Tórax: ¿Qué hacemos y cómo te podemos ayudar?"
- `description` y `og:description` reescritas con ambos términos. De paso se eliminó
  el claim superlativo *"mayor experiencia en EBUS y cirugía robótica en Chile"*,
  que contradecía el estándar de §9 (sin claims de ranking).
- `H2` → "¿Qué es la cirugía de tórax o cirugía torácica?"
- Párrafo-definición nuevo que declara la equivalencia de forma citable por una IA.
- `H2` de abordajes → "Cirugía de Tórax: vías de abordaje"

**No es keyword stuffing:** son sinónimos reales y David firma sus papers como
*"Cirujano de Tórax"* (Rev Med Chile 2021;149(2)). El `H1` conserva "Cirugía Torácica",
así que la página cubre las dos variantes. Además `cirugiadetorax.cl` ya redirige 308
al hub — el dominio de coincidencia exacta apunta a una página que ahora sí usa el término.

**Qué medir:** la posición de `cirugía de tórax` en GSC hacia fines de agosto. Si baja
de 45 a página 2-3, el mismo método (auditar la brecha entre lo que la gente escribe y
lo que la página dice) se aplica al resto de la red.

---

## 12. Sesión del 5-ago-2026

### Búsqueda: dónde estamos de verdad
GSC (3 meses, cuenta **`dr.david.lazo@gmail.com`**, authuser=1 — `dlazo.torax@` no tiene propiedades):

| Dominio | Imp | Clics | Pos |
|---|---|---|---|
| cirugiatoracica.cl | 282 | 2 | 42,9 |
| hiperhidrosis.cl | 156 | 0 | 42,6 |
| rats.cl | 105 | 5 | 7,9 |
| cancerpulmonar.cl | 97 | 2 | 22,3 |
| broncoscopia.cl | 53 | 2 | 18,3 |
| videotoracoscopia.cl | 7 | 1 | 18,6 |
| **Total** | **700** | **10** | |

Venía de 558/8 el 30-jul. **25 URLs indexadas.** Las dos que pedí indexar el 30-jul (`/publicaciones` y `cancerpulmonar.cl/que-es`) **entraron**.

**CORRECCIÓN a la §11:** dije "cirugía de tórax en posición 45". Falso — 45,6 era la media del dominio. La consulta está en **83,4**. Para leer posiciones por consulta hay que activar la métrica Posición (`&metrics=CLICKS%2CIMPRESSIONS%2CPOSITION`) o disparar pointerdown+mousedown+mouseup+click sobre el `div[role="button"]` "Posición media".

**Patrón:** marca en pág. 1 (`david lazo` 7,4 · `cirujano cardiotoracico` 5,5) · genéricas en pág. 7-9 (`cirugía de tórax` 83,4 · `hiperhidrosis` 74,7). Perfil clásico de sitio sin autoridad. En `"david lazo" cirujano toracico` ya salen **4 dominios propios en el top 10**.

### La corroboración externa SÍ existía (corrige "backlinks: CERO")
- **Universidad Finis Terrae** lo lista en el **Comité Académico** del Programa de Subespecialidad en Cirugía de Tórax (`medfinis.cl/postitulo/subesp-cirugia-torax/`), con foto y bio.
- **clinicalascondes.cl**: ~3 páginas de resultados citándolo desde 2016. Verificado en la fuente: la nota del trasplante bilobar (12-jul-2018) lo llama *"cirujano de tórax y **jefe de cirugía adulto** de Clínica Las Condes"*.
- ORCID sumó dos cargos que la web no menciona: **ALAT — Director del Depto. de Cirugía (2020-2022)** y **SER — Director (2016-2019)**.

**Nada de esto está publicado en la red.** Es la mejor apuesta pendiente: una página de docencia y menciones.

### Cambios aplicados hoy
- **Hub:** ilustración 2,79 MB → JPG q95 con `srcset` 960/1408. Home de **3.040 KB a 622 KB**. (Probé WebP primero; David pidió revertir, luego JPG. El JPG q95 4:4:4 da PSNR 42,4 dB.)
- **/links:** el canonical decía `/links/` con barra y el sitemap `/links` sin barra — señales contradictorias, probable causa de que no se indexara. Corregido + `meta robots` + fuera el claim "#1 EBUS en Chile".
- **hiperhidrosis.cl:** el `Organization` tenía `sameAs` **vacío** pese a enlazar `@hiperhidrosis.cl` 20 veces en el pie. Ahora declara la cuenta y la conecta con `founder` → `#david-lazo`. En el bloque de RRSS, Doctoralia dio paso al IG propio (sigue en `sameAs`).
- **/cirugia-hiperhidrosis/** (era 612 palabras, pos. 61): reordenada para abrir con **¿Quién es candidato?**, + recuperación, + **FAQ en acordeón con 9 preguntas** y schema. 1.373 palabras.
- **"Es ambulatoria"** — dato que dio David. El sitio decía lo contrario en 4 lugares (entradilla, ¿En qué consiste?, recuperación, `howPerformed`) más el post de 2020 que decía "menos de 24 h de hospitalización" y "3er día". Todo alineado.
- La página de sudoración compensatoria (pos. 15,2, la mejor con volumen) ahora **empuja hacia la cirugía** con el dato del 95% de satisfacción, que estaba enterrado.

### Decisiones de David (no revisitar)
- **NO destacar por sudoración compensatoria** — es el principal motivo por el que la gente no se opera.
- **Rubor facial: cada vez se opera menos**, por alta probabilidad de SC posoperatoria. No priorizar esa página pese a tener 70 impresiones.
- **No tocar precio ni cobertura todavía** — hay un convenio en curso. La estructura de la página admite la sección entre "Recuperación" y "Resultados" sin rehacer nada. Es el hueco más grande: 7 de las 12 búsquedas asociadas a "cirugia hiperhidrosis" son sobre plata y **ninguna clínica responde**.
- El video que rankea en el carrusel de "sudoración compensatoria" **no es suyo**: es de `@biotorax`, de otro país. No interesa.

### Pendiente conocido
- `publicaciones.html` tiene un `</section>` mal anidado — viene del commit `d29c6c4` de David, no de mis cambios.
- 12,5 MB de imágenes huérfanas en `dist/cirugiatoracica/imgs/` (`hero-pabellon2/3/pabellón.jpg`). No se sirven; engordan el repo.
- El resto del sitio de hiperhidrosis todavía tiene las FAQ como títulos sueltos, no en acordeón (`rubor-facial-patologico`).

---

## 13. Analítica — GA4 (5-ago-2026)

**ID de medición: `G-X3GX2HCVZL`** · propiedad creada en `dr.david.lazo@gmail.com`, la misma cuenta que Search Console.

Hasta hoy la red **no medía nada**: `/links` traía el snippet de GA4 y del píxel de Meta pero **comentado entero** y con los IDs de ejemplo (`G-XXXXXXXXXX`, `TU_PIXEL_ID`); las otras 32 páginas no tenían analítica. Todo el tráfico de Instagram —con UTM y todo— se perdía.

Instalado en **las 32 páginas publicadas**, en el `<head>`, con:
- `linker.domains` con los 6 dominios, para que un recorrido entre sitios cuente como una visita y no como varias.
- Eventos por delegación en `document` (captura): `reserva_presencial` (reserva.clinicalascondes.cl), `reserva_telemedicina` (encuadrado.com), `salida_doctoralia`, `salida_instagram`.

Verificado en vivo: `gtag/js` carga, el hit lleva `tid=G-X3GX2HCVZL`, dispara en cirugiatoracica.cl y en hiperhidrosis.cl, los UTM llegan intactos y el clic a reservar emite `en=reserva_presencial`.

**Ojo al medir:** GA4 envía por `sendBeacon` y agrupa los eventos, así que un conteo inmediato de `performance.getEntriesByType('resource')` puede dar cero aunque el evento sí haya salido. Comprobar el parámetro `en=` del último hit `/g/collect`, no el número de hits.

`dist/index.html` es una "Vista General" de rediseños que no se publica (los roots de Vercel son `dist/<dominio>`). Es el mismo artefacto que `project/`. Sin GA a propósito.

---

## 14. Chequeo del 14-ago-2026 (9 días después de la sesión grande)

### Search Console — 3 meses

| Dominio | 5-ago | 14-ago | Δ impresiones |
|---|---|---|---|
| cirugiatoracica.cl | 282 / 2 / 42,9 | **375 / 5 / 36,7** | +93 |
| hiperhidrosis.cl | 156 / 0 / 42,6 | **204 / 0 / 42,1** | +48 |
| rats.cl | 105 / 5 / 7,9 | **175 / 8 / 7,3** | +70 |
| cancerpulmonar.cl | 97 / 2 / 22,3 | **163 / 4 / 25,2** | +66 |
| broncoscopia.cl | 53 / 2 / 18,3 | **86 / 3 / 17,5** | +33 |
| videotoracoscopia.cl | 7 / 1 / 18,6 | **19 / 1 / 13,6** | +12 |
| **Total** | **700 / 10** | **1.022 / 21** | **+46% imp · +110% clics** |

### Lo que NO se movió — importante para no engañarse
- **`cirugía de tórax` sigue en 82,9** (era 83,4). El cambio de vocabulario del 2-ago no movió nada en 12 días. Confirma que ahí el problema es autoridad, no on-page.
- **`/cirugia-hiperhidrosis/` sigue en 60,7** (era 60,8) pese a la reescritura completa del 5-ago. Solo +5 impresiones. 9 días es poco, pero conviene no prometer nada.
- **hiperhidrosis.cl: 204 impresiones y 0 clics.** Sigue sin convertir. `sudoración compensatoria` está en **posición 9,1** y no recibe un solo clic — pero David decidió no destacar esa página.

### Lo que sí
- `doctor lazo` → **posición 1,0**. `david lazo` → 6,1 con 2 clics.
- rats.cl sigue siendo el mejor activo: 8 clics, posición 7,3.
- En `"david lazo" cirujano toracico` ya salen **5 dominios propios** (entró videotoracoscopia.cl).
- El cambio de nombre de Instagram **ya se refleja en Google**: el resultado aparece como *"Cirujano Torácico (@dr.david.lazo.p)"*.

### GA4 — primera medición real (instalado el 6-ago)
80 sesiones · 25 usuarios nuevos · 329 vistas. Search Console **ya vinculado**.

| Canal | Sesiones | Interacción media |
|---|---|---|
| Direct | 56 (70%) | **2 s** |
| Organic Search | 15 | **54 s**, 5,73 páginas/sesión |
| Organic Social | 5 | — |
| Referral | 3 | — |

**Cuidado al leer:** el 70% "Direct" con 2 segundos de interacción, más el reparto por país (US 27, Chile 16, luego Alemania 4, India 4, Francia 3, NZ 3, Canadá 2) es el patrón clásico de **bots**. El tráfico real es Chile 16 usuarios y las 15 sesiones de búsqueda orgánica, que sí leen: 54 segundos y casi 6 páginas por sesión.

**Página más vista: videotoracoscopia.cl con 28 vistas**, por encima del hub (15). Es la que menos impresiones tiene y la que más se lee — el formato largo funciona.

Conviene activar el filtro de bots y considerar excluir su propia IP.

### Redes
- **@dr.david.lazo.p**: nombre ya es `David Lazo • Cirujano Torácico` ✓ · 2.427 seguidores · siguiendo bajó a 1.287 · enlace a cirugiatoracica.cl/links ✓
- **@hiperhidrosis.cl**: 1.110 seguidores, 625 publicaciones, **sigue apuntando a beacons.page** ✗ — pendiente
- `/links` **sigue sin indexar**.

---

## 15. Sesión del 16-ago-2026 — enlazado, meta, peso y schema

Cuatro bloques de trabajo técnico. **Ningún texto clínico fue modificado**: los cambios
son de enlazado, metadatos, formato de imagen y JSON-LD.

### Herramienta nueva: `scripts/audit.py`

Auditor de la red, ejecutable con `python3 scripts/audit.py` desde la raíz. Comprueba las
32 páginas publicadas: anidado HTML (pila de etiquetas), JSON-LD parseable, **cada pregunta
y respuesta de FAQPage presente en el texto visible**, recursos locales existentes, GA4
instalado una sola vez, `title` ≤60 y `description` 120-158 sin duplicados, y `@id` canónico
sin variantes locales. Devuelve 1 si algo falla. **Estado actual: 0 fallos, 0 avisos.**

Dos correcciones que hubo que hacerle, y que conviene recordar:
- **GA4 aparece 2 veces por página y está bien**: una en el `src` del loader y otra en
  `gtag('config', …)`. Contar la cadena suelta marcaba las 32 páginas como duplicadas. Lo
  que debe ser único es cada una de esas dos piezas.
- **Comparar el schema con el texto visible exige ignorar la puntuación**: en la página el
  texto va partido por `<strong>` y `<a>`, lo que mete espacios junto a comas y puntos que
  no existen en el JSON-LD. Sin eso, `rubor-facial-patologico` daba un falso positivo de
  "respuesta no visible" cuando el contenido sí estaba (línea 317). Casi corrijo contenido
  médico que estaba bien: verificar el detector antes de creerle.

### Bloque 1 — Enlazado interno

Contando solo enlaces **contextuales** (fuera de `nav`, `header` y `footer`):

| Dominio → hub | Antes | Después |
|---|---|---|
| rats.cl | **0** | 3 |
| hiperhidrosis.cl | 1 | 4 |
| broncoscopia.cl | 3 | 4 |
| videotoracoscopia.cl | 2 | 2 |
| cancerpulmonar.cl | 12 | 13 |

| Página del hub | Páginas que la enlazan: antes → después |
|---|---|
| `/publicaciones` | 3 → **7** |
| `/links` | **0** → 1 |
| `/perfil` | 1 → 5 |

Anclas descriptivas y variadas ("cirujano torácico en Santiago", "sus 31 publicaciones
indexadas", "videotoracoscopía (VATS)", "cirujano de tórax con formación en cirugía
mínimamente invasiva"), siempre dentro de una frase.

**Ojo con dos trampas de precisión aquí:**
- El enlace de rats.cl a `/publicaciones` está redactado como *trayectoria académica* del
  cirujano, **sin insinuar que las publicaciones sean de RATS** — ninguna lo es (§5).
- Escribí "31 publicaciones revisadas por pares" en cancerpulmonar y lo corregí en el acto:
  son **26 artículos revisados por pares + 5 resúmenes de congreso** (§7). El enlace dice
  ahora "26 artículos revisados por pares".

### Bloque 2 — Titles y descriptions

| Métrica | Antes | Después |
|---|---|---|
| `title` > 60 caracteres | **22** de 32 | **0** |
| `description` fuera de 120-158 | **21** de 32 | **0** |
| `og:`/`twitter:` desincronizados | **39** | **0** |
| Duplicados | 0 | 0 |

Término principal al principio y marca al final. Los peores casos bajaron mucho:
`videotoracoscopia` (title 90→50, description 268→139),
`hiperhidrosis-localizada-moderada` (88→54), `broncoscopia/intervencional` (84→54),
`cancerpulmonar/tratamiento` (84→57).

### Bloque 3 — Peso de las páginas

Peso de cada home **tal como la descarga un navegador moderno** (elige WebP, y no baja el
vídeo si lleva `preload="none"`):

| Home | Antes | Después | |
|---|---|---|---|
| videotoracoscopia.cl | 13.801 KB | **1.375 KB** | −90% |
| broncoscopia.cl | 4.689 KB | **1.376 KB** | −71% |
| cancerpulmonar.cl | 2.729 KB | **668 KB** | −76% |
| hiperhidrosis.cl | 1.041 KB | **788 KB** | −24% |
| cirugiatoracica.cl | 1.434 KB | 1.434 KB | sin cambio |
| **rats.cl** | 6.413 KB | **3.762 KB** | −41% · **sigue sobre el umbral** |

- **11 imágenes a WebP con fallback**, todas con PSNR ≥ 40 dB (rango 40,3–99 dB). Las
  ilustraciones de línea van sin pérdida (equivalente a 4:4:4); las fotos a q88-90.
- **El original nunca se borra**: es el fallback de `<picture>` y de `image-set()`.
- Los heroes eran **fotos de teléfono sin redimensionar** (rats: 4032×3024). Ese era el
  problema real, más que el formato: hero-davinci 3.265 KB → 612 KB.
- Fondos CSS: no admiten `<picture>`, así que usan `image-set()` con doble declaración.
  **Verificado en navegador real**: los tres heroes descargan el `.webp`.
- `VATS1.mp4` (12,4 MB): `preload="none"` + `poster` de 69 KB. No se recomprimió.
- `width`, `height`, `loading` y `decoding` añadidos a **118 de 127** `<img>`. Los logos van
  `eager` (están sobre el pliegue); el resto `lazy`.
- Renderizado verificado sirviendo cada dominio por HTTP con navegador real: 0 imágenes
  rotas, 0 respuestas 4xx.

### Bloque 4 — Schema y frescura

- **12 nodos `MedicalWebPage`** añadidos (7 cancerpulmonar, 3 broncoscopia, 1 rats,
  1 videotoracoscopia), replicando el patrón de `cirugiatoracica/index.html`: `@id`, `url`,
  `name`, `inLanguage`, `about`, `author`, `reviewedBy` → `#david-lazo`, `specialty`,
  `isPartOf`, `lastReviewed` y `dateModified`.
- Páginas con `lastReviewed`: **2 de 32 → 14 de 32**.
- `<lastmod>` actualizado en los sitemaps de cancerpulmonar, broncoscopia y rats (decían
  2026-06-11) y **añadido al de videotoracoscopia, que no tenía ninguno**. XML validado.

**Criterio de fecha, importante:** `lastReviewed` y `dateModified` llevan **2026-08-06**,
la fecha del último cambio real del archivo *antes* de esta sesión (`git log -1` sobre
`21f57e7`), no la de hoy. Los cambios de hoy fueron técnicos, no clínicos: poner la fecha
de hoy en `lastReviewed` afirmaría una revisión médica que no ocurrió. En cambio el
`<lastmod>` del sitemap sí lleva **2026-08-16**, porque ahí la afirmación es "el archivo
cambió", que es cierta.

### Pendiente de esta sesión

| # | Qué | Por qué no se hizo |
|---|---|---|
| 1 | **rats.cl sigue en 3,76 MB.** El culpable es `imgs/robotfantoma.mp4` (2,6 MB), decorativo y con `autoplay muted loop`. Sin él la home queda en ~1,1 MB | Ponerle `preload="none"` rompe la reproducción automática y recomprimirlo requiere tu visto bueno. **Decisión tuya** |
| 2 | 18 páginas siguen sin `lastReviewed` (15 de hiperhidrosis + `/perfil`, `/publicaciones` y `/links` del hub) | Estampar esa fecha afirma una revisión clínica. Dime qué fecha corresponde y las pongo |
| 3 | El hub tiene `MedicalWebPage` en 1 de sus 4 páginas | El encargo acotaba el bloque a los otros 4 dominios |
| 4 | El `name` de los `MedicalWebPage` de hiperhidrosis conserva los titles largos anteriores | No estaba en el encargo; es cosmético y de una línea por archivo |
| 5 | `broncoscopia/imgs/rigida-ilustracion.jpg` se sirve como JPG (306 KB en WebP, ahorro menor) | Convertida igualmente; el fallback pesa lo mismo |
| 6 | **La verificación en vivo no se pudo hacer desde el sandbox** | La lista de egreso del entorno devuelve `403 host_not_allowed` para los 6 dominios (y para cualquier host). Hay que comprobarlo desde un navegador propio |

### Cómo verificar el despliegue

Los 6 dominios no son alcanzables desde el entorno de Claude. Para confirmar en tu máquina,
~60-90 s después del push:

```
curl -s https://rats.cl/ | grep -c hero-davinci.webp     # debe dar 1
curl -s https://cancerpulmonar.cl/ | grep -o 'lastReviewed[^,]*'
```

Y en Search Console, el dato a mirar en 2-3 semanas: si `/publicaciones` y `/links` empiezan
a recibir impresiones. Eran las dos páginas sin enlaces entrantes y por eso no se indexaban.

### Corrección posterior (mismo día): regresión de las imágenes

Al revisar visualmente, David detectó que `foto-dr-lazo-bio` salía alargada y con la cara
cortada. **Era una regresión mía del Bloque 3.**

**Causa.** Al añadir `width`/`height` a 118 `<img>`, el atributo `height="800"` actúa como
*presentational hint* y **fija el alto**, anulando el `aspect-ratio: 3/4` que definía el CSS.
La foto pasó de 260×347 a 260×800: con `object-fit: cover` sobre una imagen cuadrada, eso
deja ver solo la franja central del 32% — de ahí la cara cortada.

**Alcance real: 16 imágenes**, no solo la del doctor. Las peores:
`crio-muestra` 350×417 → 350×1436 · `stent-img` 263×263 → 263×1024 ·
`rigida-ilustracion-ai` 518×324 → 518×1024 · `image5_jpeg` 338×470 → 338×1024.

**Por qué hiperhidrosis.cl no se rompió:** su `site.css` ya tenía
`img { display:block; max-width:100%; height:auto; }` (línea 33). Ese contraste confirmó el
diagnóstico. videotoracoscopia tenía la regla, pero **solo dentro de una media query**, así
que en escritorio no aplicaba.

**Arreglo.** Regla base `img { height: auto; }` en los 4 sitios con `<style>` inline
(15 páginas) y al principio de `styles.css` de videotoracoscopia. Los atributos se conservan
—siguen protegiendo del CLS— pero el CSS recupera el control, porque cualquier regla de autor
gana a un presentational hint. Verificado con navegador: **las 16 cajas vuelven a su tamaño
previo y no queda ninguna imagen con la proporción rota.**

De paso se corrigió algo que ya venía mal: `cirugia-ilustracion-960` se estiraba a 553×768
cuando su proporción real da 553×302, y la foto del hub pasó de 521×497 (recortada) a
521×521 (completa).

**Lección para la próxima:** añadir `width`/`height` a `<img>` **exige** que exista
`img { height: auto; }` en el CSS del sitio. Sin eso se rompe cualquier maquetación que use
`aspect-ratio` o alturas por CSS. El script `scripts/audit.py` no detecta esto porque es un
problema de renderizado, no de HTML: hace falta un navegador. Conviene comprobarlo midiendo
la caja de cada imagen antes y después.

---

## 16. Cierre del 16-ago-2026 — los cuatro pendientes del bloque técnico

### Vídeo de rats.cl
Pesaba 2.637 KB con `autoplay muted loop` y **sin `preload`**: se descargaba entero al abrir
la página. Ahora lleva `preload="none"`, un `poster` WebP de 50 KB extraído del segundo 1,5
del propio vídeo, y un `IntersectionObserver` (`rootMargin: 300px`) que inyecta el `<source>`
y lo reproduce **solo al acercarse a esa sección**. El comportamiento visible es el mismo.

**rats.cl: carga inicial de 3,70 MB → 1,15 MB.**

### lastReviewed
Añadido a **17 páginas**, con la fecha real de cada archivo sacada de `git log`, no la de hoy:
- Las **15 de hiperhidrosis** ya tenían `MedicalWebPage`; solo les faltaban `lastReviewed`,
  `dateModified` y `author`.
- **`perfil.html`** no tenía `MedicalWebPage`: se le creó uno completo.
- **`publicaciones.html`** recibió `dateModified` + `author` en su `CollectionPage`. **No** se
  le puso `lastReviewed` a propósito: es una bibliografía, no consejo médico.
- **`links/index.html` se omitió deliberadamente.** Es una página de enlaces sin contenido
  clínico; marcarla como "revisada por un médico" sería ruido. Si un auditor la reporta como
  faltante, es un falso positivo.

### Sitemap del hub y .gitignore
`cirugiatoracica/sitemap.xml` tenía fechas de junio, julio y 2 de agosto en páginas tocadas
hoy; las 4 quedaron con su fecha real. Creado `.gitignore` (pycache, .DS_Store, `.github-token`,
`.env`) y sacado del índice `scripts/__pycache__/audit.cpython-311.pyc`, que se había commiteado.

### Verificación
`python3 scripts/audit.py` → 0 fallos. Auditoría independiente en paralelo (anidado, JSON-LD,
FAQ visible contra texto normalizado, recursos, GA4, fechas de revisión) → 0 hallazgos.

### Dos correcciones a mi propio método
- **GA4 aparece 2 veces por página y está bien** (loader + `gtag('config')`). Esperar 3 marcaba
  las 32 páginas como anómalas. Claude Code cayó en lo mismo con su auditor.
- **`image-set()` en CSS es la forma correcta de servir WebP en fondos.** Cuatro imágenes
  (`hero-davinci`, `hero-or`, `hero-petct`, `hero-dr-lazo`) las di por "no conectadas" porque
  mi detector solo buscaba `<picture>`. Al no contarlas, los pesos que calculé primero estaban
  inflados: contaba el JPG de respaldo en vez del WebP.

### Corregido: el matiz clínico del estadio IIB
El commit `fd2c927` simplificó la columna "Posibilidad de cirugía" de `cancerpulmonar/que-es`
quitando las técnicas entre paréntesis (IA1, IA2, IA3) — eso era lo pedido. Pero de paso el
estadio **IIB** pasó de *"Sí (con evaluación)"* a *"Sí"* a secas. David confirmó que fue un
error de instrucción y en `fafb7a6` se repuso el texto original.

**Por qué importa:** la fila IIB usa `var(--accent2)`, un color distinto al de los estadios I
y IIA, precisamente porque su operabilidad es condicional. Sin el "(con evaluación)" el color
quedaba sin explicación y la tabla decía a un paciente con IIB lo mismo que a uno con IA1.

**Regla que deja:** en las tablas de operabilidad por estadio, los paréntesis pueden contener
dos cosas muy distintas — la **técnica** (lobectomía, VATS, RATS), que es prescindible, o una
**condición clínica** ("con evaluación", "en casos seleccionados"), que no lo es. Antes de
simplificar una columna entera hay que distinguirlas fila por fila.

---

## 17. Chequeo de visibilidad para IA (16-ago-2026, tarde)

### Salud técnica: 0 hallazgos
32 páginas. Anidado, JSON-LD, FAQ visible, recursos, GA4, títulos, descripciones, H1,
duplicados: **todo limpio**. El trabajo de Claude Code y el cierre posterior quedaron sólidos.

### Infraestructura GEO: buena
- **Ningún `Disallow` activo** en los 6 dominios; todos con `User-agent: * / Allow: /`.
- Bots de IA nombrados explícitamente en 5 de 6. **hiperhidrosis.cl no nombra `OAI-SearchBot`
  ni `ChatGPT-User`** — cosmético, porque el comodín ya los cubre, pero conviene igualar.
- **46 pares pregunta-respuesta** en 7 `FAQPage` — es el formato que las IA citan.
- Schema con ORCID, 14 `sameAs`, 8 `memberOf`, 3 `alumniOf`, `knowsAbout`, `worksFor`.
- **No existe `llms.txt`** en ningún dominio.
- `videotoracoscopia.cl` es el único sin `FAQPage`.

### Resultado real: la red es invisible para las IA
Tres consultas de prueba, con búsqueda en vivo:

| Consulta | Qué respondió | ¿Aparece David? |
|---|---|---|
| "mejor cirujano torácico Santiago cirugía robótica RATS" | Destaca al **Dr. Pablo Pérez Castro (oncotorax.cl)** + UC Christus y Bupa | **No** |
| "EBUS CryoEBUS broncoscopía intervencional Chile" | **Clínica Alemana como pionera del EBUS en Chile desde 2010**; menciona al Dr. Alfredo Jalilie (Sta. María) | **No** |
| "David Lazo Pérez cirujano torácico publicaciones" | Cita Doctoralia, TopDoctors, CTSNet, LinkedIn, Horalibre, medicosonline. Concluye: *"los resultados no contienen detalles específicos sobre sus publicaciones científicas"* | **Ningún dominio propio** |

**El tercero es el diagnóstico.** Buscando su nombre + "publicaciones", la IA no encuentra
`/publicaciones` —31 referencias verificadas con `ScholarlyArticle`— y responde que no hay datos.
Los directorios de terceros tapan por completo a sus propios sitios.

**Dos conflictos de claim confirmados en vivo:**
- Clínica Alemana reclama públicamente EBUS **desde 2010**. **Matizado por David el 17-ago-2026:**
  es verdad a medias — partieron el mismo año, pero con otro médico que ya no está en Chile; su
  equipo actual se formó en **2014**. La web de David nunca dijo "pionero en EBUS" sino
  *"el cirujano con mayor experiencia en EBUS en Chile (desde 2010, +3.200 procedimientos)"*,
  que con este dato queda **reforzado**, no debilitado: 16 años de práctica continua frente a 12.
  **No es un conflicto de claims.** (Yo había confundido este claim con el de "pionero en
  CryoEBUS", que es otra técnica.)
- El Dr. Jalilie, **coautor suyo** en las recomendaciones COVID de la SER, sí es citado por nombre.

### Conclusión
El on-page está resuelto y ya no es el problema. **El cuello de botella sigue siendo el mismo
de julio: cero backlinks.** Sin dominios externos que lo respalden, las IA prefieren directorios
con autoridad antes que sus seis sitios, por bien construidos que estén.

Lo que cambiaría esto es lo que lleva pendiente desde el 5-ago: **publicar la página de docencia
y menciones** (Comité Académico de Finis Terrae + ~10 notas de Clínica Las Condes) y **pedir a
WABIP, SOCICH y Finis Terrae que enlacen el sitio**.

### Menor pero accionable
- **LinkedIn sigue indexado como "Clínica MEDS"** en los resultados, pese a que terminó en
  dic-2025. Aparece así en la respuesta de IA.
- 7 páginas bajo 400 palabras (todas en hiperhidrosis.cl).

*(No se pudieron leer GSC ni GA4 en esta pasada: la extensión de Chrome estaba desconectada.)*

---

## 18. `/docencia` — la página de docencia y menciones (16-ago-2026, noche)

Publicada `https://cirugiatoracica.cl/docencia`. Es la respuesta al cuello de botella descrito
en §17: la red no tenía ninguna página que expusiera autoridad institucional verificable, y las
IA respondían con Doctoralia y TopDoctors porque era lo único con respaldo externo que encontraban.

### Qué contiene

**Docencia.** Comité académico del Programa de Formación de Subespecialista en Cirugía de Tórax
de la Universidad Finis Terrae. Verificado en `medfinis.cl/postitulo/subesp-cirugia-torax/`:
jefe de programa Dr. Felipe Undurraga Machicao; comité con Dr. Javier Vega Salas, Dr. Huáscar
Rodríguez Galbán, Dr. David Lazo Pérez y Dr. Nicolás Von Jentschyk. Dos años, campos clínicos
Clínica Las Condes y Hospital San Borja Arriarán.

**Menciones.** Siete notas de Clínica Las Condes, **todas abiertas en la fuente primaria el
16-ago-2026** antes de publicarlas:

| Fecha | Nota | Cargo que le atribuyen |
|---|---|---|
| 12-07-2018 | Doble trasplante de pulmón infantil | cirujano de tórax y **jefe de cirugía adulto** de CLC |
| 05-04-2018 | ¿Conoces la iontoforesis? | cirujano de tórax de CLC — **única voz de la nota** |
| 22-11-2017 | Endosonografía bronquial | cirujano de tórax de CLC |
| 22-08-2017 | ¿Sólo sudor en exceso o hiperhidrosis? | del equipo de cirugía de tórax |
| 19-10-2016 | ¿Es la cirugía la mejor opción para la hiperhidrosis? | cirujano torácico de la **Unidad de Hiperhidrosis** de CLC |
| 11-08-2016 | ¿Sabes si tu sudoración excesiva es idiopática? | listado entre los especialistas del equipo |
| s/f | Inédito caso médico: 123 días en ECMO | médico cirujano que participó en la operación |

### Corrección de una cifra que yo mismo había dado mal
En sesiones anteriores dije "unas diez notas de CLC". Eran una aproximación de un `site:` en
Google, no un recuento. Verificadas al abrirlas: **siete**. Tres candidatas quedaron fuera y
**no se publicaron** por no estar verificadas:
`/CENTROS-Y-ESPECIALIDADES/.../Trasplante-de-pulmon-de-importancia-mundial`, `AFICHE-CER.pdf`
(Jornadas CR y CT 2018) y `Programa-Oficial-Puesta-al-dia-enfermedades-Resp-2016.pdf`.
Google mostraba 3 páginas de resultados para `site:clinicalascondes.cl "David Lazo"`, así que
es probable que existan más. **Si aparecen, verificar antes de añadir.**

### Dos trampas encontradas en las fuentes
1. **La nota de 2016 dice "un día de hospitalización"** para la simpatectomía. Contradice lo que
   hoy afirma hiperhidrosis.cl (ambulatoria). Por eso la página cierra con una nota que aclara
   que esas cifras reflejan la práctica del momento y remite a `/cirugia-hiperhidrosis/`.
   **No citar esa frase en ningún otro sitio.**
2. **Error de atribución del lado de CLC** en la nota de EBUS: la cita *"Yo entré a pabellón a
   las 18:30..."* está marcada en el HTML como del Dr. Lazo, pero el texto deja claro que habla
   el paciente Rodrigo Campos. **No reproducirla.**

### Implementación
- `dist/cirugiatoracica/docencia.html`, 53,9 KB, 696 palabras visibles, sirve en `/docencia`
  por `cleanUrls`.
- Plantilla y CSS reutilizados de `publicaciones.html` — cero assets nuevos, cero imágenes.
- Schema: `Physician` canónico + `MedicalWebPage` (`lastReviewed` 2026-08-16) +
  `EducationalOccupationalProgram` (Finis Terrae) + **7 nodos `Article`** con
  `publisher: Clínica Las Condes` y `mentions → https://cirugiatoracica.cl/#david-lazo`.
  Es el primer marcado de la red que declara explícitamente *quién cita a David desde fuera*.
- Enlaces contextuales entrantes: hub (`index.html`, sección Sobre el autor), `perfil.html`
  (bio y bloque de publicaciones) y `publicaciones.html` (lead). Añadida al nav de las cuatro
  páginas del hub y a `sitemap.xml`.
- `scripts/audit.py`: 33 páginas, 0 hallazgos. Verificada en vivo tras el despliegue.

### Adenda — Universidad de Chile (misma noche)
David señaló que es docente de la Universidad de Chile desde 2014 y pidió añadirlo aunque no
haya referencia web. Al abrir su CV el dato resultó **más fuerte de lo que él mismo dijo**: la
entrada de 2014 no es "docente", es **Director** del Programa de Perfeccionamiento en Cirugía
Toracoscópica para Cirujanos Generales, Escuela de Postgrado, Facultad de Medicina, U. de Chile
(2014 – presente). Y el vínculo con la U. de Chile es mucho más largo: profesor en Bases
Biomédicas de la Medicina Intensiva (Esp. Enfermería, 2012–2016) y examinador OSCE + docente de
Cirugía Experimental en 4º de Medicina (2004–2009).

Añadido:
- Sección **Universidad de Chile** en `/docencia` con los tres cargos y sus fechas, más el
  Train-the-Trainers de broncoscopía (Bronchoscopy International / WABIP / AABE, 2018).
- Segundo nodo `EducationalOccupationalProgram` con `provider: Universidad de Chile` y
  `director → #david-lazo`.
- **`affiliation` universitaria en el nodo `Physician` de las 32 páginas que lo tienen** (las
  16 de hiperhidrosis.cl ya traían `affiliation` con los dos hospitales, con otra estructura;
  ahí las universidades se anexaron al array existente en vez de crear uno nuevo). No la tienen
  `dist/index.html` ni `/links`, que no llevan nodo Physician.
- Lead, `description`, bio de `/perfil` y bloque del hub reescritos para abrir con la U. de Chile.

**Regla de procedencia:** este dato viene del CV de David, no de una fuente web externa. Es su
propia declaración biográfica, no una afirmación clínica ni una autoría — la regla YMYL de
§verificar-antes-de-afirmar no lo bloquea, pero conviene tenerlo presente: si algún día Finis
Terrae o la U. de Chile publican una ficha suya, hay que enlazarla desde `/docencia`.

### Adenda 2 — YouTube y prensa nacional (misma noche)

**Canal de YouTube.** `youtube.com/@hiperhidrosiscl` — 4 suscriptores, **un solo vídeo**.
Verificado vía oEmbed y abriendo la página con Chrome:

- **"Hiperhidrosis en Dr. TV"** · uploadDate `2017-07-18` · 13 min 39 s (`PT13M39S`) · 327 vistas.
- Añadida sección **Televisión** en `/docencia` con embed `youtube-nocookie` + `loading="lazy"`
  (no descarga el reproductor hasta que se acerca al viewport) y nodo `VideoObject` con
  `actor → #david-lazo`.
- El canal se añadió al `sameAs` del nodo `Organization` `https://hiperhidrosis.cl/#org` en las
  16 páginas de hiperhidrosis.cl — **no** al `sameAs` del `Physician`, porque el canal es de la
  marca hiperhidrosis.cl, no un perfil personal de David.
- **Pendiente de confirmar con David:** el vídeo se titula "Dr TV", que era el programa de
  Claudio Aldunate en **Mega** (2011); desde 2014 el mismo conductor produce "Doctor en Casa".
  Por eso la página dice sólo *"el programa de salud Dr. TV"* **sin nombrar el canal**. Si él
  confirma la emisora, añadirla.

**Prensa nacional.** `La Tercera / Paula`, 25-ene-2021, por Camila Ossandón:
*"Sudor por hiperhidrosis: cómo las expectativas sociales impiden que tratemos antes esta condición"*.
Verificado en la fuente. Cita literal:

> "explica **David Lazo, cirujano torácico y creador de la página hiperhidrosis.cl** para
> combatir la desinformación que ha existido hasta el momento"

**Es la fuente externa más valiosa de todo el proyecto**: un medio nacional asocia editorialmente
su nombre a un dominio de la red. Hasta ahora ninguna fuente de terceros lo hacía. Añadida como
sección **Prensa nacional** con nodo `NewsArticle` (`publisher: La Tercera`, `mentions → #david-lazo`).

**Dos cosas a vigilar en ese reportaje:**
1. Contiene un testimonio de mal resultado por sudoración compensatoria y una cita suya diciendo
   que las probabilidades de que exista "son absolutas". David pidió expresamente no destacar la
   SC (§12). Por eso la ficha en `/docencia` describe el reportaje por su titular —la demora en
   consultar— y por la acreditación como creador del sitio, sin ese ángulo. **No es ocultamiento:
   el enlace al artículo completo está ahí.**
2. Ese "absolutas" se refiere a que aparezca *alguna* SC, no a que sea severa. hiperhidrosis.cl
   maneja 8% de SC severa (nota CLC 2016). No hay contradicción, pero conviene que la página de
   cirugía deje explícita esa distinción por si un paciente lee ambos.

**David dijo "artículos" en plural y sólo entregó uno.** Si hay más, verificar y añadir; la
sección ya está montada para recibirlos.

### Adenda 3 — correcciones y WABIP (cierre de la noche)

**1. El programa de la U. de Chile terminó en nov-2022, no sigue vigente.** Lo corrigió David.
Cambiado a "2014 – noviembre de 2022" y pasado a tiempo pasado en `/docencia` (lead, ficha,
intro de sección y el puente desde Finis Terrae), en la bio de `/perfil` y en el bloque del hub.
En schema, el `director` del `EducationalOccupationalProgram` pasó a ser un `Role` con
`startDate: 2014` / `endDate: 2022-11`.

**Consecuencia que no era obvia:** la `affiliation` a "Universidad de Chile — Escuela de
Postgrado" que había añadido horas antes al nodo `Physician` de 32 páginas quedaba afirmando
un vínculo académico vigente que ya no existe. **Retirada de las 32 páginas.** La U. de Chile
sigue en `alumniOf` (eso no caduca) y `affiliation` queda sólo con Finis Terrae.
*Si David conserva algún nombramiento académico en la U. de Chile, hay que reponerla.*

**2. CV actualizado.** `CV_David_Lazo_2026.docx` p41: "2014 – presente" → "2014 – 2022".
PDF regenerado con LibreOffice headless (`soffice --headless --convert-to pdf`). Verificado:
6 páginas antes y después, `pdftotext -layout` muestra la línea correctamente alineada, y el
`diff` del texto extraído no arroja ninguna otra diferencia. Copia de seguridad del docx
original en `/tmp/CV_backup.docx` (se pierde al cerrar la sesión).

**3. Dr. TV.** David confirmó que es el programa de **Claudio Aldunate**. Añadido a la ficha.
El canal sigue sin nombrarse: Dr. TV era de Mega (2011) pero desde 2014 Aldunate produce
"Doctor en Casa", así que para 2017 la emisora no está clara y no se afirma.

**4. WABIP — sección propia (pedida por David).** Antes de escribirla comprobé el directorio
oficial abriéndolo con Chrome (la web de WABIP es client-side; WebFetch devuelve vacío):

> https://www.wabip.com/about/board-of-regents/ → **"Lazo, David, MD · Chile Bronchology · Chile"**

**Es la primera cita externa de un organismo internacional que verificamos en el proyecto**, y
está en el mismo listado que los regentes de la ATS, la Japan Society for Respiratory Endoscopy,
la Asociación Argentina de Broncoesofagología, etc. Sección `#wabip` con dos fichas —regente por
Chile y Train-the-Trainers 2018 (Bronchoscopy International / WABIP / AABE)— y nodo
`MedicalOrganization` con `member: Role{roleName: "Regent for Chile"}`.

### Adenda 4 — Ambu/AEER, ALAT y un deploy que no corrió

**Fuente nueva (verificada):** `ambu.es/registro-primera-pildora-de-broncoscopia` — ficha del
webinar *"Primera Píldora de Broncoscopia"*, ciclo organizado por **Ambu con el respaldo de la
AEER** (Asociación Española de Endoscopia Respiratoria), moderado por el **Dr. Javier Flandes**
(Hospital Fundación Jiménez Díaz, Madrid; presidente de la AEER). Tema: los cambios que impuso
el COVID-19 en la broncoscopía diaria. Ambu presenta a David como:

> "Jefe Unidad Cirugía Torácica y Neumología Intervencionista, Clínica Las Condes.
> **Regente, WABIP - Chile. Dtor. Dpto. Cirugía Torácica - ALAT.**"

Dos cosas importantes:
1. **Segunda confirmación externa e independiente de la regencia WABIP**, ahora desde España.
   La primera es el propio Board of Regents de WABIP.
2. **Credencial que no estaba en la red: dirección del Departamento de Cirugía Torácica de ALAT.**
   Hasta ahora ALAT sólo figuraba en `memberOf`. Está citada textualmente dentro de la ficha del
   webinar, no afirmada por separado, **porque no tengo fechas**.

Añadida como tercera ficha de la sección `#wabip`.

**Dos datos que faltan y bloquean contenido (para David):**
- **Año del webinar de Ambu.** La página sólo dice "El 3 de noviembre". Por el contexto COVID
  es 2020 o 2021, pero no se afirma. La ficha va sin fecha hasta que él lo confirme.
- **Fechas de la dirección del Dpto. de Cirugía Torácica de ALAT.** Con ellas, merece sección
  propia igual que WABIP; sin ellas se queda como cita dentro del webinar.

**Incidencia de despliegue (sin resolver, decisión de David: esperar).**
Los commits `f09bfea` (WABIP + corrección 2014-2022) y `730c104` (Ambu) **están en
`origin/main`** —verificado con `git fetch` + `git rev-parse`— pero **Vercel no generó
deployment para el proyecto `cirugiatoracica`**. Comprobado en el panel
(`vercel.com/drdavidlazo/cirugiatoracica/deployments`): el último despliegue de producción es
`5c93723` (sección Prensa). En la vista global, `730c104` sí desplegó… en el proyecto `vats`.

Diagnóstico: no es caché. `/perfil` y `/` se sirven con `x-vercel-cache: MISS`, `age: 0`, y aun
así muestran el texto viejo ("Dirige desde 2014"). La cuenta es **Hobby**, que tiene tope diario
de despliegues, y hoy se hicieron muchos en 7 proyectos — es la explicación más probable.

**Consecuencia:** en producción, `/docencia` está en la versión de la sección Prensa. **Faltan en
vivo: la sección WABIP, la ficha de Ambu y la corrección de "2014 – presente" a "2014 – 2022"**,
tanto en `/docencia` como en `/perfil` y el hub. Si mañana sigue igual: panel de Vercel →
proyecto `cirugiatoracica` → menú «…» del último deployment → **Redeploy**.

### Adenda 5 — barrido de fuentes y CV (cierre)

David señaló, con razón, que él estaba encontrando más material suyo que yo. Barrido sistemático
de fuentes públicas. **Conclusión honesta: su CV ya era casi completo — de todo lo verificado,
sólo tres cosas faltaban.**

**Fuentes verificadas en origen (16-ago-2026):**

| Fuente | Qué acredita |
|---|---|
| `eventio-back.alatorax.org` (19° Congreso ALAT 2026, Cartagena, 8–11 jul) | **Moderador**, sesión "Segmentectomías: ¿Cómo las hago?", mié 8 jul, 08:00–10:15, sala Fragata 1 |
| `instagram.com/p/Cbqc6BzrC29` (post del 28-mar-2022) | Webinar ALAT "Cirugía Robótica Torácica en Latinoamérica", **5 de abril de 2022** |
| `aac.org.ar/93congreso/cursos.htm` | 93° Congreso Argentino de Cirugía (nov-2023), Curso de Cirugía Torácica: **"EBUS, la visión del cirujano"** (13 nov) y **"Cirugía robótica y opérculo torácico"** (15 nov) |
| `aac.org.ar/94congreso/invitados.htm` | 94° Congreso Argentino (2024): figura como **Invitado Extranjero**, con foto |
| `socich.cl` (XCVII Congreso Chileno de Cirugía, 20–21 nov 2025) | Ponencia **"Otras Cirugías por robot"** (jue 20 nov, 16:10–16:30) + coautoría en 11 trabajos libres |

**Lo añadido al CV (`.docx` + PDF regenerado, 6 páginas, verificado con `pdftotext -layout`):**
1. Resumen **#18** — "Cirugía post-quimioinmunoterapia neoadyuvante en cáncer pulmonar: experiencia
   en el HCSBA" (SOCICH 2025).
2. Resumen **#19** — "Volumen quirúrgico de programa de formación de subespecialistas en cirugía
   torácica en Chile, comparado con estándares internacionales" (SOCICH 2025).
   Los 17 resúmenes del congreso SER 2025 se renumeraron 18–34 → **20–36**.
3. Congreso **#81** — "[Mod.] 19° Congreso ALAT — Cartagena de Indias, Colombia".
4. Perfil profesional: "más de 60 congresos" → **"más de 80"** (ahora son 81 entradas).

**Ya estaba en el CV** (comprobado uno a uno): 93° y 94° Congreso Argentino (#66, #71), XCVII
Chileno (#79), Webinar ALAT Cirugía Robótica LATAM (#50), Píldoras de Broncoscopía (#45) y los
otros 9 resúmenes de SOCICH 2025.

**Detalle verificado que el CV no recoge, por estilo** (una línea por evento, sin títulos de
ponencia): los títulos de las charlas del 93° Argentino, el de SOCICH 2025, la fecha exacta del
webinar ALAT 2022 y la condición de Invitado Extranjero en el 94°. **Si se quiere una versión
del CV con títulos de ponencia, hay material verificado para hacerlo.**

**Aviso:** el 94° Congreso Argentino lo lista con afiliación **Clínica MEDS**, igual que LinkedIn.
Es la misma afiliación desactualizada que ya estaba pendiente de corregir (§17).

**Instagram:** su grid no es legible sin sesión iniciada (Instagram lo bloquea). Si quiere que
se explote su archivo de IG como fuente, tiene que dejar la sesión abierta en Chrome.

### Adenda 6 — vaciado del Instagram (177 posts) y 5 altas más en el CV

David dejó la sesión de Instagram abierta en Chrome. Extraídos **176 de 177 posts** vía
`/api/v1/feed/user/1486809562/` con `x-ig-app-id`, paginando de 33 en 33 (el navegador corta a
los 45 s, así que hubo que trocear en tandas y acumular en `window`). Rango: **20-may-2019 a
16-ago-2026**. Filtrados por palabras clave de actividad académica: **53 posts relevantes**.

**Cinco entradas nuevas en el CV** (ahora **86 congresos**, perfil actualizado a "más de 85"):

| # | Entrada | Fuente (post IG) |
|---|---|---|
| 67 | [Dir./Rel.] Curso Internacional de Broncoscopía — Santiago | 6-abr-2024 (con J.M. Lucchelli, apoyo de Zepeda y Erbe) |
| 69 | [Rel.] 3er Curso AIRE — Guayaquil, Ecuador | 23-jun-2024 (hands-on + 7 procedimientos en vivo) |
| 71 | [Dir./Doc.] 2° Curso de Actualización en Cirugía Torácica — Clínica MEDS / IMP | 27-jul-2024 (28 asistentes; broncoscopía intervencional + OTS de pared y pectus con modelos cadavéricos) |
| 73 | [Rel.] Jornadas de Actualización en Neumología Intervencional — Sociedad Peruana de Neumología | 14-sep-2024 |
| 85 | [Dir./Doc.] 1er Curso de Broncoscopía Intervencional Clínica Las Condes — WABIP / Ambu Academy | 22-may y 21-jun-2026 (18–19 jun 2026: criobiopsias, EBUS, obstrucción de vía aérea, stenting; teoría + simulación) |

Toda la lista se renumeró 1–86 y se verificó que la secuencia no tiene saltos. PDF regenerado:
**7 páginas** (antes 6, por las altas). Copia del docx previo en `/tmp/CV_pre_ig.docx`.

**Tres cosas que NO se tocaron por riesgo de duplicar — pendientes de que David decida:**
1. **"Curso Latinoamericano Osteosíntesis Pared Torácica"** (IG 10-may-2023) podría ser el mismo
   que el #58 actual, "Curso Pared Torácica MedXpert LATAM — Bogotá".
2. **"Webinar SBCT-GBOT-ALAT"** (IG 27-sep-2021) podría ser el #47, "Webinar ALAT: Nuevas
   Modalidades Terapéuticas en Adyuvancia para Cáncer Pulmonar".
3. **Discrepancia de ordinal:** el CV dice "#64 3° International SRS LATAM Robotic Surgery Congress
   — Río de Janeiro", pero el post del 25-ago-2023 dice "**2do** Congreso de la Society of Robotic
   Surgery LATAM y **COLCIR**". Ni el ordinal ni la sede coinciden. **Hay que revisarlo.**

**Procedencia:** estas cinco altas vienen de los posts del propio David, no de fuentes de terceros.
Es su propia declaración sobre su propia actividad —el mismo estándar que su CV— pero conviene
saberlo: no son verificables desde fuera como sí lo son ALAT, AAC, SOCICH o WABIP.

**Dato útil para el futuro:** el archivo de IG es la mejor fuente de su actividad reciente y sólo
es accesible con su sesión abierta en Chrome. 123 de los 176 posts son clínicos o personales y no
aportan al CV; el filtro de palabras clave que se usó está en esta sesión y puede rehacerse.

### Adenda 7 — WABIP con sección propia, y la causa real del bloqueo de despliegue

**Sección WABIP ampliada a siete fichas**, a petición de David, que la considera lo más
destacable. Ya no es una entrada suelta sino un arco 2018→2026 con un hilo explícito —la
formación de formadores—:

1. **Regente por Chile** · Board of Regents (verificado en wabip.com)
2. **Instructor Train-the-Trainers** (2018) · Bronchoscopy International / WABIP / AABE
3. **Workshop de Broncoscopía Rígida** (2019) · WABIP, La Paz, Bolivia
4. **1er Curso WABIP/Chile de Broncoscopía Intervencional** · 5–6 dic 2022, Santiago
5. **22° WCBIP/WCBE**, congreso mundial · 2022, Marsella
6. **Curso de Broncoscopía Intervencional Clínica Las Condes** · 18–19 jun 2026, con WABIP y
   Ambu Academy
7. **Ponente, Primera Píldora de Broncoscopia** · Ambu con respaldo de la AEER

El `<title>` pasó a "Docencia, WABIP y menciones" (50 car.) y el lead abre con la regencia.
Página: 1.460 palabras, 66,8 KB.

### La causa del bloqueo de despliegue (resuelta como diagnóstico)

Redeploy **no servía**: el diálogo de Vercel dice literalmente *"Create a new deployment with the
same source code as your current one"* — habría reconstruido el commit viejo.

Consultando la API desde la sesión del panel:

- `/api/v2/user` → plan **hobby**, `resourceConfig: {concurrentBuilds: 1}`, `softBlock: null`.
- `/api/v6/deployments` contando desde las 00:00 → **115 despliegues hoy**, todos READY.
  Reparto: cirugiatoracica 15, videotoracoscopia 15, broncoscopia 14, cancerpulmonar 14,
  hiperhidrosis 14, rats 14, vats 14.

**El límite del plan Hobby es 100 despliegues al día. Se superó.**

**La causa estructural:** los siete proyectos observan el mismo repositorio, así que
**cada commit dispara siete despliegues**. Unos quince commits en una jornada = ~105.
No es un fallo: es la configuración multiplicando.

**Arreglo recomendado (no aplicado, requiere decisión de David):** configurar el
**Ignored Build Step** de cada proyecto para que solo construya cuando cambie su propio
`dist/<dominio>/`. En Vercel, Settings → Git → Ignored Build Step, con un comando del tipo
`git diff --quiet HEAD^ HEAD -- dist/<dominio>/`. Eso divide los despliegues por siete y el
problema no vuelve. Mientras tanto, el límite se reinicia solo.

**Estado en producción:** `/docencia` sigue mostrando la versión del commit `5c93723`
(sección Prensa). **Faltan por salir: WABIP, Ambu, la corrección de 2014-2022 y el nuevo
title/description**, en `/docencia`, `/perfil` y el hub. Todo está en `main` y auditado.

### Adenda 8 — Ignored Build Step configurado en los 7 proyectos

Aplicado el arreglo de la §7 vía la API de Vercel desde la sesión del panel
(`PATCH /api/v9/projects/{id}`), no por formulario. Los 7 devolvieron HTTP 200 y se releyó la
lista para confirmar que quedó escrito.

**Comprobación previa:** los 7 proyectos tienen `rootDirectory = dist/<nombre>` (verificado
uno a uno, incluidos `dist/videotoracoscopia` y `dist/cirugiatoracica`) y **ninguno** tenía
comando previo, así que no se pisó nada.

**Comando, idéntico en los 7:**

```
git diff --quiet HEAD^ HEAD ./
```

Vercel ejecuta el Ignored Build Step **desde el Root Directory**, así que `./` significa
`dist/<dominio>` en cada proyecto — no hace falta un comando distinto por sitio. Semántica:
salida **0** (sin cambios) → se salta el build; salida **1** (hay cambios) → construye.
Si `HEAD^` no existiera, git da error y la salida no es 0, con lo que **construye**: el modo
de fallo es seguro.

**Efecto esperado:** un commit que toque sólo `dist/cirugiatoracica/` genera 1 despliegue en
vez de 7. Los commits a `ESTADO.md`, `scripts/` o `README.md` —raíz del repo— pasan a generar
**cero**. Es donde se iba buena parte del cupo: hoy hubo ~15 commits, varios sólo de
documentación, y cada uno gastaba 7 despliegues.

**Comprobado en caliente, dos pruebas:**
1. Commit `c4ad227`, que sólo tocaba `ESTADO.md` → **cero despliegues**. La regla funciona.
2. Commit siguiente, que sólo tocaba `dist/cirugiatoracica/index.html` → **también cero**,
   pero por otra razón: el cupo diario está agotado y Vercel ya no crea ningún despliegue.

**Hallazgo que cierra el diagnóstico de la §7.** Mirando el histórico se ve que, al pasarse
del cupo, Vercel no dejó de desplegar de golpe: **degradó a un solo proyecto por push**.
`df57e56` → sólo `vats`. `730c104` → sólo `vats`. `d955a48` → sólo `videotoracoscopia`.
Los siete proyectos competían por una plaza y **cirugiatoracica llevaba varias rondas
perdiendo el sorteo**. Por eso parecía que "no se desplegaba nada" cuando en realidad sí se
desplegaba — pero siempre otro sitio.

Con el Ignored Build Step ya no hay competencia: un commit a `dist/cirugiatoracica/` es el
único candidato posible. En cuanto el cupo se reinicie, sale a la primera.

**Si algún proyecto dejara de construir cuando debe:** quitar el comando desde
Settings → Git → Ignored Build Step.

### Adenda 9 — desplegado y verificado (17-ago-2026)

El cupo se reinició y el commit `cc01a67` (`lastReviewed` y `lastmod` al 17-ago) confirmó la
regla en condiciones normales:

| Proyecto | Resultado |
|---|---|
| **cirugiatoracica** | **READY** — construyó |
| broncoscopia, cancerpulmonar, hiperhidrosis, rats, vats, videotoracoscopia | **CANCELED** — saltados por el Ignored Build Step |

**1 despliegue en vez de 7.** El arreglo de la §8 funciona en producción.

**Verificado en vivo con `cache: no-store`:**
- `/docencia` — `<title>` "Docencia, WABIP y menciones", 6 secciones incluida
  **WABIP · Broncoscopía intervencional**, ficha de Ambu presente, `lastReviewed: 2026-08-17`,
  66,1 KB.
- `/perfil` — "Dirigió entre 2014 y 2022" ✓, ya no aparece "Dirige desde 2014".
- Hub `/` — "Dirigió entre 2014 y 2022" ✓ y el enlace `/docencia#wabip` ✓.

Con esto **queda cerrado todo lo que arrastraba la §7**: WABIP, Ambu, la corrección del
programa de la U. de Chile y el nuevo title/description están en producción.

**Nota sobre el registro CANCELED de anoche** (`b82671b`, proyecto hiperhidrosis): no era un
fallo. Es el comportamiento correcto — Vercel crea el despliegue, ejecuta el Ignored Build Step,
obtiene salida 0 y cancela el build. Los despliegues cancelados **no consumen minutos de build**.

### Adenda 10 — registro sobrio (corrección de estilo pedida por David)

David marcó como **"poco serio"** el registro narrativo con el que había escrito la página, y
pidió eliminar todas las descripciones de eventos. Tenía razón: lo que empezó como contexto
acabó siendo autopromoción. Ejemplos de lo retirado:

- *"Antes de este programa dirigí durante ocho años… Buena parte de lo que enseño es…"*
- *"Figuro en el directorio oficial de regentes… en el mismo listado que los regentes de la
  American Association for Bronchology, la Japan Society…"* (comparación jactanciosa)
- *"Es el curso que cierra el arco que empieza en el Train-the-Trainers de 2018"*
- *"Primer curso dictado fuera de Chile bajo el alero de la asociación"*
- *"La nota más leída del grupo"*, *"Única voz técnica de la nota"*
- *"El hilo que une lo que hago con esa asociación es la formación de formadores: no enseñar a
  broncoscopiar, sino enseñar a enseñar broncoscopía"*

**Criterio nuevo de la página:** cada entrada es **título · fecha · institución · enlace**.
Nada más. Se conservó lo verificable y se eliminó lo interpretativo:

- **Sí se conserva** el `Citado como «…»` de cada nota, porque es atribución literal de un
  tercero —es la prueba, no un adorno— y es justo lo que la página existe para demostrar.
- **Se eliminan** valoraciones, comparaciones, superlativos y cualquier frase que explique
  por qué algo es importante.
- Los encabezados pasaron a nombrar la institución sin adjetivos: "Universidad Finis Terrae",
  "Universidad de Chile", "Prensa", "Televisión", "Clínica Las Condes".

**Resultado:** 605 palabras visibles (antes 1.460), 60,2 KB (antes 66,8). Menos de la mitad
del texto, con la misma información verificable y los mismos enlaces a fuente. El schema
JSON-LD no se tocó.

**Regla para lo que venga:** en las páginas de David, describir los hechos y enlazar la fuente.
No explicar su relevancia. Si un dato necesita que yo argumente por qué importa, probablemente
no debería estar.

### Adenda 11 — chequeo completo de la red y directivas de snippet (17-ago-2026)

**Estado técnico: todo en verde.**

| Comprobación | Resultado |
|---|---|
| `audit.py` | 33 páginas, 0 hallazgos |
| Repo ↔ producción | mismo commit |
| Páginas en vivo | 33/33 responden 200 |
| GA4 | 2 apariciones en las 33 (loader + config) |
| Canonical y `@id` canónico | correctos en las 33 |
| robots.txt + sitemaps | 6/6, **33 URLs**, cuadran con las páginas |
| `cirugiadetorax.cl` | redirige al hub |
| Ignored Build Step | 1 READY + 6 CANCELED por push |
| Despliegues | 35 en el día, frente a 115 el día anterior con el mismo trabajo |

**Cambio aplicado — directivas de snippet en las 33 páginas.** Antes: 17 páginas con
`index, follow` (que es el valor por defecto de Google y por tanto no hacía nada) y 16 sin
etiqueta. Ahora, todas con:

```html
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
```

- `max-snippet:-1` — sin límite de longitud de fragmento. **Es el relevante para el objetivo
  del proyecto:** autoriza a Google, y a los sistemas que se alimentan de su índice, a usar
  texto largo en vez de un recorte corto.
- `max-image-preview:large` — miniatura grande en resultados y en Discover.
- `max-video-preview:-1` — sin límite de previsualización; aplica al vídeo de rats.cl y al de
  Dr. TV en `/docencia`.

Verificado en producción en los 6 dominios. De paso desaparece la única inconsistencia
estructural que quedaba (hiperhidrosis.cl no llevaba la etiqueta).

### Pendiente de decisión de David — claims de «pionero» y «referente»

El barrido de tono con el criterio de la §10 encontró, **en contenido anterior a esta sesión**,
el mismo registro que él rechazó en `/docencia`:

- **«pionero»** en 8 páginas de 4 dominios. La frase *"pionero en la técnica CryoEBUS a nivel
  latinoamericano"* viaja en el bloque de bio compartido (broncoscopia ×3, cancerpulmonar,
  perfil, rats). Además *"pionero en Chile"* (broncoscopia), *"El Dr. David Lazo es pionero en
  esta técnica en Chile, realizándola desde 2015"* (cancerpulmonar/tratamiento) y *"Fue el
  primero en desarrollar un programa sistemático de cirugía torácica robótica"* (rats).
- **`/perfil`**: H1 *«Referente en Cirugía Torácica en Latinoamérica»* y H2 *«Cirugía Torácica
  de Vanguardia»*.

**Dos razones para revisarlo:** es el registro que él calificó de poco serio, y **el claim de
pionería en EBUS está disputado** — Clínica Alemana reclama públicamente lo mismo desde 2010
(§17). Las cifras verificables (+3.200 EBUS desde 2010, +200 RATS desde 2015, 19 años de
ejercicio) transmiten lo mismo sin afirmar una primacía que un tercero discute.

**DECIDIDO POR DAVID (17-ago-2026): se quedan como están. Tema cerrado — no volver a plantearlo.**

Contexto para entender la decisión:
- El claim de EBUS no está disputado (ver corrección en §17).
- Los dos claims de RATS **sí tienen respaldo publicado**: su propio resumen de congreso se
  titula *"Cirugía torácica robótica en hospital público docente en Chile: análisis de 79 casos
  del primer programa nacional"*. Si alguna vez se quisiera reforzar, basta con enlazarlo.
- Quedaron sin fuente y así se mantienen por decisión suya: *"pionero en CryoEBUS a nivel
  latinoamericano"* (sin año de inicio) y el H1 de `/perfil` *"Referente en Cirugía Torácica en
  Latinoamérica"* + el H2 *"Cirugía Torácica de Vanguardia"*.

**Nota de método:** el criterio sobrio de la §10 aplica a **prosa que escribo yo**. Las
afirmaciones que David hace sobre sí mismo son suyas: se señalan una vez, se documenta el
estado, y se respeta su decisión.

### Estado de `/docencia` al cierre
**Verificado el 17-ago-2026, después de la reescritura sobria de la §10:**
**500 palabras visibles, 58,8 KB, 14 nodos JSON-LD** (`Physician`, `MedicalWebPage`,
2× `EducationalOccupationalProgram`, `MedicalOrganization`, `NewsArticle`, `VideoObject`,
7× `Article`). Seis secciones: **Universidad Finis Terrae · Universidad de Chile · WABIP ·
Prensa · Televisión · Clínica Las Condes**.

*(La cifra anterior aquí —1.290 palabras— era de antes de la reescritura y quedó desfasada
durante unas horas. Corregida.)*

### Lo que sigue siendo el problema
La página **documenta** autoridad; no la **importa**. El backlink sigue siendo cero. Los tres
enlaces que moverían la aguja son los mismos de §17 y dependen de David:
**Finis Terrae** (que la ficha del comité enlace a cirugiatoracica.cl), **WABIP** (regencia) y
**SOCICH**. Con `/docencia` publicada, ahora hay una URL concreta que pedirles que enlacen.

---

# ARCHIVO — `ESTADO.md` completo al 22-sep-2026 (antes de la reestructuración)

> Copia literal de la versión larga (835 líneas) que se reemplazó el 22-sep-2026 por el `ESTADO.md`
> compacto. Los encabezados bajan un nivel. Aquí está el detalle de las pasadas del CV, la cadena
> documental de EBUS, el criterio de eyebrows y los errores de método con su contexto.

## ESTADO — Red web Dr. David Lazo Pérez

> **Léeme primero.** Estado actual, reglas y pendientes. Evita proponer cosas ya hechas.
> **Última actualización: 22 sep 2026** (correcciones del reanálisis del 20-sep: backlinks cancelados, Doctoralia,
> cuenta GSC, opérculo indexado, `/docencia`; medición de Instagram vía Metricool).
> El detalle cronológico de cada sesión está en **`ESTADO-historico.md`**. Consúltalo solo
> cuando necesites saber *por qué* algo quedó como quedó.

---

### 1. Infraestructura

- **Repo:** `dlazotorax/lazoweb`, rama `main`. Sitios estáticos, sin build, en `dist/<dominio>/`.
- **Hosting:** Vercel, cuenta **Hobby**, 7 proyectos apuntando al mismo repo.
- **Token GitHub:** `Paginas web/.github-token` (fine-grained, solo lazoweb). **Nunca commitearlo.**
- **Flujo:** clonar fresco en el sandbox → editar → `audit.py` → commit → push a `main`.
- Antes de commitear: `git config user.email noreply@anthropic.com && git config user.name Claude`.
- La carpeta `Projects/Paginas web` es respaldo; el repo manda.

| Dominio | Páginas | Rol |
|---|---|---|
| cirugiatoracica.cl | 6 (`/`, `/perfil`, `/cv`, `/publicaciones`, `/docencia`, `/links`) | Hub |
| hiperhidrosis.cl | 16 | Pacientes |
| cancerpulmonar.cl | 7 | Pacientes |
| broncoscopia.cl | 3 | Dual |
| rats.cl | 6 (`/` + `/operculo-toracico` y 4 subpáginas) | Médicos referentes |
| videotoracoscopia.cl | 1 | VATS — dominio principal desde jul-2026 |
| vats.cl | 308 → videotoracoscopia.cl | Redirect |
| cirugiadetorax.cl | 308 → cirugiatoracica.cl | Redirect |

**Total: 34 páginas publicadas.**

### 1.b `/cv` — la fuente de trayectoria (publicado 20-ago-2026)

`cirugiatoracica.cl/cv` — **Currículum académico**. Es la referencia que justifica cualquier
afirmación sobre formación, credenciales, cargos, membresías y actividad en congresos.

- **Sin datos personales**: sin RUT, fecha de nacimiento, correo ni móvil. Verificado a cero.
- **Contenido**: formación con fechas · docencia · 8 sociedades con año de ingreso y cargos ·
  31 publicaciones (resumen + enlace) · **86 congresos fechados**, 2003-2026, con el rol de cada uno.
- **Legible por máquina**: `ProfilePage` + `Physician` + `BreadcrumbList`; `hasCredential` por cada
  título (incluido FACS-2020 con el ACS como emisor), `memberOf` con las 8 sociedades y sus URLs,
  `knowsAbout` con 12 áreas. **92 etiquetas `<time datetime>`**. Todo en HTML plano, sin depender de JS.

**Cómo se conecta con el resto — esto es lo que la hace "la referencia":**

1. **`subjectOf` → `/cv#page` en el `Physician` de las 33 páginas.** Cualquier página donde aparezca
   una cifra o un superlativo declara en su schema dónde está la fuente.
2. **Enlace visible** bajo el bloque de cifras en los 5 dominios (broncoscopia, rats, cancerpulmonar,
   videotoracoscopia, cirugiatoracica): *"Formación, sociedades científicas y 86 congresos fechados
   en el currículum académico"*.
3. **`/perfil` es `mainEntityOfPage`** de la entidad y `/cv` la desarrolla. Jerarquía explícita.
4. **`llms.txt`** en la raíz del hub, referenciado desde `robots.txt`, que dice literalmente que para
   verificar trayectoria la fuente es `/cv` — y aclara que **las cifras de volumen provienen del
   registro personal del autor**.

**Menú del hub:** Especialidades · Sobre mí · **Currículum académico ▾** (└ Publicaciones) ·
Docencia · Contacto · Reservar hora. Submenú en CSS puro, sin JS.

**También se corrigió `/perfil`:** tenía **dos `<h2>` idénticos** con dos biografías que repetían
formación, credenciales y cifras (551 palabras para una sola trayectoria). Ahora hay una sola bio;
la segunda sección quedó como tarjeta con foto y cifras.

#### Auditoría completa de la red (20-ago-2026) — 4 hallazgos, todos corregidos

Barrido de las 34 páginas buscando errores no detectados antes.

**Limpio:** cifras coherentes en toda la red (5.700 / 3.200 / 200 / 19 años, sin una sola
contradicción) · fechas de inicio consistentes (EBUS 2010 en 13 páginas, RATS 2015 en 5) ·
**0 enlaces internos rotos** · un solo `<h1>` por página · ningún `alt` vacío · los 6 sitemaps
cuadran exactamente con las páginas reales · `robots.txt` en los 6 dominios · MEDS ya no figura
como afiliación vigente.

**Corregidos:**

1. **`rats.cl` contaba la misma cifra dos veces** en la barra del hero: *"+200 cirugías robóticas
   torácicas realizadas"* y *"+200 cirugías RATS torácicas desde 2015"*. Ahora: **+200 RATS ·
   2015 inicio · +5.700 torácicas · 19 años**. Sin repetición y con un dato más.
2. **`broncoscopia/index.html`** repetía la regencia WABIP y "+3.200 desde 2010" en dos párrafos
   seguidos — mismo patrón que `/perfil`. Segundo párrafo aligerado.
3. **`/links` sin `lastReviewed`.** Añadidos `dateModified`, `@id`, `url` e `inLanguage`.
4. **`dist/index.html` eliminado.** Era una página de trabajo del primer commit
   (*"Rediseños Dr. Lazo — Vista General"*), huérfana, sin `canonical` ni `noindex`, y **enlazaba a
   `hub.html`, que ya no existe**. No estaba expuesta porque los Root Directory apuntan a
   `dist/<dominio>/`, pero se habría publicado sola si alguien tocaba esa configuración.

**Revalidación tras los arreglos:** 114/114 JSON-LD válidos · 0 páginas huérfanas · 0 sin
`lastReviewed` · 0 párrafos repetidos dentro de una misma página · cifras únicas por concepto.
**34 páginas.**

#### Despliegue — cómo funciona ahora

Los 7 proyectos observan el mismo repo, así que **un commit disparaba 7 despliegues**. El
17-ago se superó el tope del plan Hobby (**100 al día**; llevábamos 115) y Vercel degradó a
un despliegue por push, eligiendo un proyecto arbitrario: cirugiatoracica se quedó tres commits
sin publicar y parecía que "no se desplegaba nada".

**Arreglado.** Los 7 proyectos llevan **Ignored Build Step** (Settings → Git):

```
git diff --quiet HEAD^ HEAD ./
```

Vercel lo ejecuta **desde el Root Directory**, así que `./` es `dist/<dominio>` en cada uno —
mismo comando para todos. Salida 0 (sin cambios) → salta el build; salida 1 → construye. Si
`HEAD^` no existiera, git falla y construye: el modo de fallo es seguro.

Resultado verificado: un commit a un solo dominio da **1 READY + 6 CANCELED**. Los commits a
la raíz (`ESTADO.md`, `scripts/`) dan **0 despliegues**. Los CANCELED no consumen minutos.

- **Propagación del CDN: ~40-90 s.** Si tras un push ves lo viejo, revalida con `?v=N`.
- **`Redeploy` del panel NO sirve** para publicar código nuevo: reconstruye *el mismo commit*.

---

### 2. Identidad — datos canónicos

- **ORCID:** `0009-0007-0806-6679`
- **`@id` de la entidad:** `https://cirugiatoracica.cl/#david-lazo` — presente en las 38 páginas
  con `Physician` (`/links` no lo lleva). **Nunca crear un `@id` local por dominio.**
- **El `@id` compartido obliga a que los datos colgados de él coincidan.** Los motores consolidan
  por `@id`: si dos dominios le cuelgan valores distintos, la misma entidad llega con dos versiones.
  Corregido en hiperhidrosis.cl el **20-sep-2026** — ver §5.f.
- **Indexación del nombre:** SciELO → `Lazo P` · PubMed → **`Lazo P D`** · Elsevier → `P. David Lazo`.
  Buscar "Lazo D" o "David Lazo" devuelve cero; resuelto con "also known as" en ORCID.
- **Homonimia:** su hermano Diego es el "Lazo D" de PubMed. La huella real de David son 5 artículos ahí.
- **Afiliación vigente:** Clínica Las Condes (desde ene-2026) + Hospital Clínico San Borja Arriarán
  (desde oct-2022). **MEDS terminó en dic-2025** — ya no aparece en la SERP del nombre (20-sep-2026); sigue en la
  ficha del 94° Congreso Argentino.
- **Formación:** Médico-Cirujano PUC (2004) · Esp. Cirugía Torácica U. de Chile / INT (2009) ·
  Fellowship Trasplante Pulmonar, H.U. Puerta de Hierro Majadahonda (2010-2011).
- **Cargos internacionales:** Regente por Chile de **WABIP** (verificado en su Board of Regents) ·
  Director Depto. Cirugía Torácica **ALAT** (2020-2022) · Director **SER** (2016-2019).
- **Docencia:** Comité Académico de la subespecialidad en Cirugía de Tórax, **U. Finis Terrae**
  (verificado en medfinis.cl) · Director de perfeccionamiento en la **Escuela de Postgrado de la
  U. de Chile, 2014 – nov 2022** (terminó; no es vigente).

#### Actividad verificada en fuentes de terceros (17-ago-2026)

Material encontrado al rastrear serchile.cl y savalnet.cl. **Todo abierto en la fuente.**

| Fecha | Qué | Fuente |
|---|---|---|
| 17-20 oct 2012 | Charla "Trasplante pulmonar en FQ. Experiencia chilena" — Congreso Soc. Latinoamericana de Neumología Pediátrica, Hotel del Mar | savalnet.cl `20121017_12354/17676` |
| 6-9 nov 2013 | Charla "Situación actual del trasplante pulmonar en Chile" — Congreso SER 2013, Viña del Mar | savalnet.cl `20131106_20393/20430` |
| **may 2014** | **"Endosonografía bronquial: innovadora tecnología mínimamente invasiva"** — revista **Vivir Más** de CLC. Es la voz técnica de la nota, citado como «cirujano de tórax del Centro Clínico del Cáncer». Dice que CLC tiene EBUS **desde diciembre de 2012** y que se ha usado en «alrededor de 30 pacientes» | clinicalascondes.cl `/App_Themes/CLC/revista/revista_vivir_mas_201405/ventana-16.html` |
| **may 2015** | **"Avances en videobroncoscopía"** — **primer autor**, Rev Med Clin Condes 2015;26(3):387-392, **DOI 10.1016/j.rmclc.2015.06.013**, CC BY-NC-ND. Coautora: E.U. Karina Bunster D. Palabras clave: *videobroncoscopia, **EBUS**, autofluorescencia, navegador electromagnético* | Crossref + elsevier.es |
| 2-3 jul 2015 | Charla "Manejo de la fístula broncopleural" — Desafíos en patologías pulmonares avanzadas, Auditorio CLC | savalnet.cl `20150602_25449/25462` (¡la URL dice junio, la página dice julio!) |
| 9-12 nov 2016 | **Coordinador de Cirugía del 49° Congreso Chileno de Enfermedades Respiratorias**, Viña del Mar. Coordinó 2 simposios médico-quirúrgicos de pleura, el simposio quirúrgico y la Conferencia Magistral "Trasplante Pulmonar en España" con el Dr. Ángel Salvatierra | serchile.cl/congreso2016/ |
| 2-3 ago 2018 | Charlas **"EBUS"** y "Puesta al día en el manejo del nódulo pulmonar" — Patologías pulmonares complejas, Auditorio CLC | savalnet.cl `20180802_39747` |
| 25 mar 2020 | Coautor de las recomendaciones COVID de la **Comisión de Broncoscopía y Neumología Intervencionista de la SER** | serchile.cl `noticia.php?id=619` |

**El hallazgo más fuerte:** en SciELO (*Rev Chil Enferm Respir* 2020;36(2):135-137,
DOI 10.4067/S0717-73482020000200135) su afiliación declarada **es la comisión**:

> David Lazo P.\* — \* *Comisión de Broncoscopía y Neumología Intervencionista de la Sociedad
> Chilena de Enfermedades Respiratorias*

No es "participó en": es miembro, en documento indexado y con DOI. Coautores: Alfredo Jalilie E.,
Paula Barcos M., Arturo Morales S., Macarena Rodríguez V.

**Las charlas de Savalnet tienen grabación en vídeo** (tras registro profesional). Son contenido
suyo, fechado y alojado por un tercero.

#### Desde cuándo — fechas exactas de formación por técnica

**RESUELTO (19-ago-2026).** David aportó **`CV David Lazo 2024.pdf`** (Projects/Paginas web).
Ese CV **sí lleva la fecha exacta en las 65 entradas** de la sección V (Cursos y Conferencias);
el CV 2026 en Word las perdió. Es la fuente de fechas del proyecto: **consultarlo antes de
deducir cronología por posición en la lista.**

| Técnica | Ancla de formación / docencia | Fecha exacta | Rol | CV24 |
|---|---|---|---|---|
| Video-cirugía torácica | Curso Postgrado "Aspectos Técnicos en Video Cirugía", Viña | 23-26 nov **2003** | Asistente | V.2 |
| **EBUS** | **Workshop EBUS-TBNA — Thoraxklinik am Universitätsklinikum Heidelberg** | **9 y 10 dic 2010** | Asistente | **V.12** |
| VATS avanzada | Advanced Video-assisted and Thoracoscopic Procedures — **IRCAD Estrasburgo** | 21-23 nov **2013** | Asistente | V.24 |
| **RATS** | **da Vinci "Console Surgeon" — da Vinci System Training, Florida Hospital Celebration, Orlando** | **11 jun 2015** | — | **V.29** |
| Hiperhidrosis / simpatectomía | 11th World Symposium of the International Society of Sympathetic Surgery, Santiago | 15-16 oct **2015** | **Coordinador y Moderador** | V.31 |
| Broncoscopía intervencional (docencia) | Curso Internacional de Broncoscopía Intervencionista — Soc. Boliviana de Neumología / **WABIP**, La Paz | 11-12 jul **2019** | **Instructor** | V.43 |
| RATS (docencia) | Webinar ALAT "Cirugía Robótica Torácica en LATAM" | 5 abr **2022** | **Director** | V.51 |
| UVATS / URATS (docencia) | MasterClass UVATS / URATS, Santiago | 17 ago **2023** | **Director y Expositor** | V.63 |

**"EBUS desde 2010" y "RATS desde 2015" quedan acreditados.** No son cifras redondeadas: son
entradas fechadas, con institución y ciudad, contrastables con el resto del CV. Heidelberg (dic-2010)
cae dentro de su fellowship en Puerta de Hierro (2010-2011) y seis meses antes del 44° SEPAR de
Oviedo (17-20 jun 2011, V.13). Orlando (11 jun 2015) cae tres días después del 48° SEPAR de Gran
Canaria (5-8 jun 2015, V.28). **No hace falta publicar ningún certificado** — David los conserva.

#### EBUS — la cadena documental completa (19-ago-2026)

Era el claim más débil. Ya no lo es: **diez años de rastro, cada eslabón abierto en la fuente.**

| Fecha | Hecho | Fuente |
|---|---|---|
| **dic 2010** | Workshop EBUS-TBNA, **Thoraxklinik am Universitätsklinikum Heidelberg** | CV 2024, V.12 |
| dic 2012 | CLC adquiere el equipo de EBUS | nota de *Vivir Más*, may-2014 |
| **may 2014** | Revista **Vivir Más** de CLC: es la voz técnica de la nota; ~30 pacientes a esa fecha | clinicalascondes.cl |
| **may 2015** | **"Avances en videobroncoscopía", primer autor**, Rev Med Clin Condes, **con DOI** | Crossref |
| nov 2017 | La misma nota, republicada en el blog de CLC | clinicalascondes.cl |
| ago 2018 | Charla titulada **"EBUS"**, Auditorio CLC | savalnet.cl |
| mar 2020 | **Comisión de Broncoscopía y Neumología Intervencionista de la SER** | serchile.cl + SciELO |

**La nota de EBUS estaba mal fechada en `/docencia`.** Figura como *22 de noviembre de 2017*; esa es
la **republicación** en el blog. El original es la revista *Vivir Más* de **mayo de 2014** — texto
idéntico. Se comprobó abriendo las dos. Al reciclarla en 2017, CLC **borró los dos datos que
envejecían**: "desde diciembre de 2012" y "alrededor de 30 pacientes". Por eso la de 2014 vale más.

**Y la versión de 2014 no tiene el error de atribución.** La trampa registrada en §3.1 —la cita
*"Yo entré a pabellón a las 18:30…"* marcada como del Dr. Lazo cuando habla el paciente— **solo
existe en la versión de 2017**. Si alguna vez se cita esta nota, citar la de 2014.

Evidencia adicional en fuente de terceros: trasplante **2012** · pleura **2015** ·
hiperhidrosis **2016** (notas CLC).

**Corrección importante (error mío, 17-ago):** ofrecí el resumen *"análisis de 79 casos del primer
programa nacional"* como respaldo del claim de RATS. **No lo respalda.** David lo aclaró: ese es el
programa del **Hospital San Borja Arriarán, que partió en 2022**; el título dice literalmente *"en
hospital público docente"*. Acredita el primer programa **en un hospital público**, no su práctica
personal desde 2015. Es exactamente el tipo de conflación contra la que advierte la §3.1.

**Resuelto también:** la duda del "3° SRS LATAM". El CV 2024 dice **V.64 · 3º International and SRS
LATAM Robotic Surgery Congress · Expositor · 23-25 ago 2023 · Río de Janeiro**. Coincide con el CV
2026; lo que discrepa es el post de Instagram ("2do… COLCIR"), no el CV.

#### CV 2026 — fechas repobladas (19-ago-2026)

Se trasladaron las fechas del CV 2024 al `CV_David_Lazo_2026.docx`. Emparejamiento por título
normalizado, con siete correcciones manuales (los "Congreso Anual ACS Chile", que el CV 2026 abrevia)
y un falso positivo descartado (V.13 SEPAR Oviedo se había emparejado con el 21° Congreso Colombiano).

- **63 fechas insertadas** en formato `· mes año` al final de cada entrada. Total fechadas: **64 / 86**.
- **Validación:** la lista es cronológica y las 63 fechas salen en **orden ascendente estricto, sin una
  sola inversión**, de nov-2003 a oct-2023. Un emparejamiento falso habría roto el orden. Es la prueba
  de que el mapeo es correcto.
- **Corregido un rol inflado:** entrada #29 (11th World Symposium ISSS, oct-2015) decía `[Dir./Mod.]`;
  el CV 2024 dice **"Coordinador y Moderador"**. Ahora `[Coord./Mod.]`. **Revisar el resto de roles
  del CV 2026 contra el 2024 antes de difundirlo** — este apareció al azar, no en una revisión sistemática.
**Segunda pasada — 9 fechas más, todas en fuente externa:**

| # | Entrada | Fecha | Fuente |
|---|---|---|---|
| 48 | XCIII Congreso Chileno de Cirugía — Coquimbo-La Serena | 7-10 **nov 2021** | socich.cl |
| 56 | XCIV Chileno / XXVIII AIACT — Pucón | **nov 2022** | socich.cl (el mismo programa confirma el AIACT) |
| 66 | 93° Congreso Argentino de Cirugía — Sheraton BA | 13-16 **nov 2023** | aac.org.ar |
| 70 | 17° Congreso ALAT — Santiago | 10-13 **jul 2024** | alatorax.org |
| 75 | 94° Congreso Argentino — Hilton Puerto Madero | 25-27 **nov 2024** | aac.org.ar |
| 76 | 30° AIACT / **Sixth International Joint Meeting** — Barcelona | 19-22 **nov 2024** | thoracicsurgery2024.org |
| 81 | 18° Congreso ALAT — Cancún | 9-12 **jul 2025** | alatorax.org |
| 83 | XCVII Congreso Chileno — Pucón | 18-21 **nov 2025** | socich.cl |
| 86 | 19° Congreso ALAT — Cartagena de Indias | 8-11 **jul 2026** | alatorax.org |

**Hallazgo fuerte en el #76:** el programa oficial del *Sixth International Joint Meeting on Thoracic
Surgery* (Barcelona) lista, en la sesión del AIACT Congress del **miércoles 20 de noviembre de 2024**
moderada por Iñigo Royo Crespo y Miguel A. Mesa Guzmán, a **"David Lazo Pérez (Chile)"**. Es fuente
externa, europea, indexable y con su nombre completo — la mejor credencial internacional documentada
del expediente después de la regencia WABIP.

**Total: 73 / 86 fechadas · 0 inversiones cronológicas.** El orden ascendente estricto sigue
validando cada emparejamiento.

**Ojo con un detalle de orden:** #75 (94° Argentino, 25-27 nov) va *antes* de #76 (Barcelona, 19-22
nov) y ambas son de nov-2024, así que a nivel mes no hay inversión, pero **a nivel día el CV los
tiene invertidos**. Corregirlo solo si se pasa a fechas con día.

**Tercera pasada — 6 más.** David aclaró el criterio: **fechar el evento, no su participación** —
él conserva los certificados que la acreditan. Eso baja la barra a "¿existió el evento y cuándo?".

| # | Entrada | Fecha | Fuente |
|---|---|---|---|
| 68 | 66° Congreso Anual ACS Chile — Hotel del Mar, Viña | 9-12 **jun 2024** | congresoacs.cl |
| 74 | XVII Congreso Boliviano de Neumología — La Paz | 16-19 **oct 2024** | alatorax.org |
| 78 | VI Jornada de Actualización en Cirugía Torácica — Clínica Alemana La Dehesa | 5 **dic 2024** | alemanacursos.cl |
| 82 | 21° Congreso Colombiano de Neumología (ASONEUMOCITO) — InterContinental Medellín | 17-20 **sep 2025** | asoneumocito.org |
| 84 | XXXI Congreso AIACT — Santa Cruz de la Sierra | 7-8 **nov 2025** | SECT / SOPACI |
| 85 | 1er Curso de Broncoscopía Intervencional CLC — WABIP / Ambu Academy | 18-19 **jun 2026** | CLC (inscripciones a `dlazo@clinicalascondes.cl`) |

**Cuarta pasada — #69, aportada por David.** *3er Curso de Avances e Innovación en Medicina
Respiratoria y Endoscópica (**AIRE 2024**)*, **21-22 jun 2024**, Hotel Sheraton de Guayaquil,
organizado por el **Centro de Investigación Respiratorio (CIR)**. Confirmado de forma independiente
que el evento existe y quién lo organiza (`eventoscir.com`, "Evento AIRE tercera edición, Curso de
Neumología 2024 + Workshop, presencial"); **la fecha exacta viene del dato de David**, no de esa
página. Corrobora igual la posición: cae en el hueco de nueve días entre el 66° ACS (9-12 jun) y el
17° ALAT (10-13 jul). El CV la abrevia como "3er Curso AIRE" — **conviene poner el nombre completo**.

**Quinta pasada — #80, desde un reel de Instagram.** *Curso "El ABC del EBUS y la Pleuroscopía"*,
Miraflores (Lima), **may 2025**. Publicado por **@cardioperfusion** el **30 de mayo de 2025**, en
pasado ("Así vivimos…"), con David y el Dr. Alejandro Sánchez (México) como los dos docentes. Se leyó
con Claude in Chrome (Instagram no se deja abrir con WebFetch) y la fecha salió del
`meta[name=description]` de la propia página.

**Trampa evitada:** intenté deducir la fecha decodificando el shortcode del reel (los IDs de Instagram
llevan el timestamp embebido). Puse un control con un post ya fechado — y el algoritmo lo situó diez
años tarde. **Fórmula descartada, no ajustada hasta que cuadrara.** Regla: cuando un método derivado
falla el control, se tira; no se calibra contra el resultado que uno quiere.

**Sexta pasada — #79, desde el afiche.** *III Curso Teórico Práctico de Pared Torácica **MedXpert***,
Santiago, **4 de marzo de 2025** (el afiche dice `04-03-2025`; contexto chileno, valor en CLP, luego
dd-mm). Anunciado por **@torax_otorrinos_impchile** el 22-ene-2025. Expositores: **Dr. David Lazo
(Chile)**, Dra. Gabriela Ambriz (México), Dr. José Matilla Sigüenza (Austria). Temas: reconstrucción
de pared, pectus excavatum, fijación de costillas, práctica de fijación costal en muestras anatómicas.
Organizan IMP Chile y MedXpert.

> **El afiche lo lista dos veces: como expositor y como moderador** ("Moderador: Dr. David Lazo,
> Cirujano de Tórax"). El CV lo marca solo `[Rel.]`; correspondería `[Rel./Mod.]`.

**Séptima pasada — #73, desde el afiche que David publicó en LinkedIn.** *I Jornada Internacional de
Neumología Intervencionista*, **Sociedad Peruana de Neumología**, **12 de septiembre de 2024**,
presencial, 48 cupos, Av. Guardia Civil 236, San Isidro (Lima). Figura como **"Dr. David Lazo Pérez ·
Cirujano de Tórax, Clínica MEDS – Chile"** con **dos intervenciones**: la charla *"Uso de criosonda"*
(8:30-8:50) y el taller de broncoscopía avanzada, rotación *"Uso de criosonda"* (11:50-13:00).
Coexpositores: Llontop Calderón (EsSalud), Moreira (SOLCA Quito), Villanueva Villegas (Dos de Mayo),
Monge Espinoza (Hipólito Unanue), Bejarano Cacho (Clínica Internacional).

> **El post decía "1 año"**, lo que a primera vista sugiere 2025. LinkedIn redondea a la baja: 23
> meses se muestran como "1 año". La posición en el CV (entre el 17° ALAT de jul-2024 y el XVII
> Boliviano de oct-2024) y la afiliación que le atribuyen (**Clínica MEDS**, que terminó en dic-2025)
> fijan **sep-2024**. El CV lo titula "Jornadas de Actualización…"; el nombre oficial es
> **I Jornada Internacional de Neumología Intervencionista**.

**Octava pasada — #72, en la web oficial del Capítulo Chileno del ACS.** *Diplomado de Cirugía*,
**versión 2024** (265 horas pedagógicas, 12-18 meses, online asincrónico; por eso va con año y sin
mes). Director general: Dr. Mario Uribe Maturana, FACS, Gobernador del Capítulo Chileno. Certificado
por el Capítulo Chileno del ACS, patrocinado por **CONACEM**. Fuente:
`acseduca.com/curso/diplomado-de-cirugia` + `acseduca.online/material/2024/diplomadoacs/`.

En el **Módulo Cirugía de Tórax** (directores: Dr. Raúl Berríos y Dra. Lorena Pérez) figura con **dos
clases propias**:

- **Clase 11 — Mediastinitis** · Dr. David Lazo P., FACS
- **Clase 12 — Cirugía torácica robótica** · Dr. David Lazo P., FACS

#### FACS — confirmado por David. Y un error mío de bulto

La web del Capítulo Chileno del ACS lo nombra **dos veces** como **"Dr. David Lazo P., FACS"** —
en el listado de clases y en el equipo docente, con afiliación *"Hospital San Borja Arriarán. Clínica
MEDS"*. David lo confirmó: **es Fellow of the American College of Surgeons.**

**Error mío (19-ago-2026):** anuncié esto como "credencial nueva sin registrar" y afirmé que no
estaba ni en el CV, ni en los seis dominios, ni en el JSON-LD. **Las tres cosas eran falsas.**

- El **CV ya lo tenía**: tabla de Sociedades Científicas → *"American College of Surgeons · **Fellow
  (FACS) desde 2020**"*. No lo vi porque estuve todo el día extrayendo el docx con `d.paragraphs`,
  y **el contenido de las tablas no está en los párrafos**. Trabajé sobre ese archivo durante horas
  sin leer su única tabla.
- La **red ya tiene el ACS**: `memberOf` con *American College of Surgeons (ACS)* en 32 de 33 páginas,
  y visible en `/perfil` en la bio y en el FAQ.

**Regla: afirmar una ausencia exige la misma verificación que afirmar una presencia.** Un `grep` de
diez segundos habría evitado las tres afirmaciones. Ver §3.1.

**Lo que sí es cierto, y es el hallazgo real:** en toda la red se le llama **"miembro"** del ACS,
nunca **Fellow**. Cero ocurrencias visibles de "FACS" en las 33 páginas y cero `honorificSuffix`.
**No es lo mismo:** el fellowship del ACS se otorga tras revisión de credenciales, certificación y
referencias; "miembro" es genérico. La red lo degrada.

**`honorificSuffix: "FACS"` ya está en los 6 dominios** (verificado en producción el 20-sep-2026).
Queda pendiente solo cambiar *"miembro del American College of Surgeons"* por *"Fellow del American
College of Surgeons (FACS), desde 2020"* donde aparezca visible, y revisar el resto de la tabla del
CV por si hay más membresías con fecha que la red no refleja (ISHLT 2020, IASLC 2014, ERS 2015,
Soc. de Cirujanos de Chile 2016).

**Novena pasada — #71, aportada por David.** *2° Curso de Actualización en Cirugía Torácica*,
Clínica MEDS / IMP, Santiago, **26 de julio de 2024** (reel en su Instagram). Encaja en el hueco de
trece días entre el 17° ALAT (10-13 jul) y el Diplomado ACS.

**Décima pasada — #67, aportada por David.** *Curso Internacional de Broncoscopía*, Santiago,
**4 de abril de 2024**, como Director.

### ✅ CV CERRADO: 86 / 86 fechadas · 0 inversiones cronológicas

De **1 entrada con año** a **las 86**, en orden ascendente estricto de **nov-2003 a jul-2026**.
La lista es ahora autoverificable: cualquier fecha futura mal puesta romperá el orden.

#### Cómo se resolvieron las 85 (para repetir el método)

| Vía | Cuántas |
|---|---|
| **CV 2024 en PDF** (tenía todas las fechas; el 2026 las perdió) | 63 |
| Webs oficiales de sociedades (ALAT, SOCICH, AAC, ACS Chile, AIACT, ASONEUMOCITO, Clínica Alemana) | 15 |
| **Aportadas por David** (enlace, captura de afiche o dato directo) | 8 |

**Lo más eficiente, con diferencia, fue que David mandara el enlace o la captura.** Rastrear cuentas
de Instagram o LinkedIn desde cero **no** funciona: scroll infinito, el renderer se congela, y no se
llega más atrás de unos meses. Cuando falte una fecha, **pedirle el enlace antes de buscar.**

**Método que sí funciona para estos: el enlace directo.** Tres de tres — el reel del curso de Lima, el
afiche de MedXpert y el dato del AIRE se resolvieron en minutos cuando David aportó la URL o la
captura. Rastrear la cuenta de Instagram desde cero **no** funciona: el perfil de IMP Chile carga por
scroll infinito y tras varias pasadas solo se llega a abril de 2026; el renderer se congela antes de
alcanzar 2024. En LinkedIn tampoco: ver abajo.

#### LinkedIn: hay DOS perfiles, y el que revisé era el vacío (corregido 19-ago-2026)

**Error mío, corregido el mismo día.** Escribí que "LinkedIn está vacío" tras abrir
`linkedin.com/in/david-lazo-272a82317/` con su sesión: cero actividad, 0 seguidores, certificaciones
en blanco. **Ese no es su perfil real.** David envió después una captura de un post suyo con **56
reacciones, 2 comentarios y 1.598 impresiones**, publicado desde **"David Lazo Pérez ✓ · Cirujano
Torácico y de Trasplante Pulmonar"**, con la insignia de verificado.

**RESUELTO el mismo día.** Los dos perfiles, ya identificados:

| Perfil | URL | Estado |
|---|---|---|
| ✅ **El bueno** | `linkedin.com/in/david-lazo-pérez-7b194748/` | *"David Lazo Pérez · Cirujano Torácico y de Trasplante Pulmonar"*, verificado, **20 publicaciones**, posts con 46-62 reacciones y hasta 1.598 impresiones |
| ❌ **El duplicado** | `linkedin.com/in/david-lazo-272a82317/` | Cero actividad, 0 seguidores, certificaciones vacías |

**La URL buena ya estaba en la red**, en el pie de `/perfil`, desde antes de esta sesión. La encontré
mirando la propia página en producción, no navegando LinkedIn.

**El dato que importa: la sesión de Chrome de David está abierta con la cuenta VACÍA.** Por eso el
feed me llevó al duplicado, y por eso el perfil bueno se ve desde ahí con botón "Conectar" — como un
tercero. Si esa es la cuenta que usa habitualmente, cualquier actividad nueva se publica en el perfil
muerto.

**Pendientes concretos:**
1. Cerrar o fusionar el duplicado `david-lazo-272a82317` (mismo problema que las 2 fichas de Doctoralia).
2. Comprobar desde qué cuenta se publica habitualmente.
3. El perfil bueno **no tiene URL personalizada**: `7b194748` es sufijo automático. Cambiarla a algo
   como `/in/dr-david-lazo-perez` mejora la señal de entidad.

**Lección de método:** llegar a un perfil "por el camino obvio" (el enlace del propio feed) no prueba
que sea el canónico. Cuando un perfil aparece inesperadamente vacío, la hipótesis por defecto es
**duplicado**, no inactividad. Y antes de investigar fuera, **mirar qué enlaza ya la propia red**.

**Nota de orden a nivel día** (invisible a nivel mes, que es como está el CV): #75 (94° Argentino,
25-27 nov) figura antes de #76 (Barcelona, 19-22 nov), y #83 (XCVII Chileno, 18-21 nov) antes de #84
(XXXI AIACT, 7-8 nov). Solo importa si algún día se pasa a fechas con día.

PDF regenerado, 7 páginas.

#### No abrir secciones con una sola entrada (19-ago-2026)

Creé en `/docencia` una sección **Conferencias** con una única entrada (la V Jornada de Clínica
Alemana). David: **"una sola entrada es paupérrimo"**. Eliminada, con su JSON-LD.

**Regla:** una sección nueva necesita **masa crítica antes de existir** — tres o cuatro entradas
verificadas como mínimo. Una sección de una línea no comunica trayectoria: comunica que no hay más.
Es la misma lógica del registro sobrio (§3.2): el continente también habla. Si aparecen suficientes
programas públicos de congresos, se reabre; mientras tanto, los 86 congresos viven en el CV.

Material verificado que quedó fuera por esto (guardado, no publicado):
**V Jornada de Actualización en Cirugía Torácica**, Clínica Alemana Santiago, 25-26 oct 2023 ·
invitado nacional · charla *"Opérculo torácico. ¿Es la hora de los cirujanos torácicos?"*, 25-oct
11:30 · junto a Baste (CHU Rouen), Terra (Instituto do Câncer, São Paulo) y Smith (Hospital Italiano
de Buenos Aires) · brochure en `alemanacursos.cl/contenido/Jornada-Actualizacion-Cirugia-Toracica/
Brochure-Jornada-Actualizacion-Cirugia-Toracica.pdf` · le atribuyen "Clínica Meds". Confirma la
fecha de V.65 del CV. **El PDF está en un servidor de cursos: conviene que David guarde una copia.**

#### Publicaciones: 31 verificadas (2004-2023)

**26 artículos revisados por pares:** 10 Rev Chil Enf Respir · 6 Rev Chil Cirugía · 4 Rev Med Chile ·
3 Rev Med Clin Condes · 1 Rev Chil Radiología · 1 Cir Cir · 1 Rev Chil Urología.

**5 resúmenes de congreso indexados** (DOI verificado en Crossref salvo el de 2014):
J Heart Lung Transplant 2023;42(4):S298 (×2) · Pediatr Crit Care Med 2021;22(Supl 1) (×2) ·
J Thorac Oncol 2014;9(9):S184-5 (sin DOI).

Identificadores: 21 PID SciELO · 11 DOI · 5 PMID · 1 LILACS · 1 sin ID.
Archivo para ORCID: `lazo_31_publicaciones.bib`.

**No confundir:** son **26 revisados por pares + 5 resúmenes**, no "31 revisadas por pares".
**Ninguna de las 26 es de RATS** — esa producción está en comunicaciones a congreso.

#### CV

`CV_David_Lazo_2026.docx` / `.pdf` — 7 páginas. **86 congresos**, **36 resúmenes presentados
en congresos**, 31 publicaciones. Perfil: "más de 85 congresos".

---

### 3. Reglas que no se negocian

#### 3.1 Verificar antes de afirmar (YMYL)

Contenido médico bajo la responsabilidad profesional de David. **Nunca publicar autoría, cifras,
credenciales, afiliaciones ni citas desde un resumen de IA de buscador.** Abrir la fuente primaria
y confirmar el dato literal.

Errores ya cometidos, para no repetirlos:
1. Atribuí a David un paper de **Bellvitge** desde un resumen de búsqueda. Cero coincidencias de
   "Lazo" al abrir el artículo.
2. Reporté **46% de duplicación** entre dominios: era CSS, no prosa. Casi provoca un rediseño.
3. Inventé la paginación de un paper y adiviné un DOI.
4. Repetí durante semanas "unas diez notas de Clínica Las Condes". Al abrirlas: **siete**.
   Una cifra mía sin comprobar se había vuelto dato del proyecto.
5. Fechar una nota por su **republicación**. La de EBUS quedó como "22-nov-2017" porque esa es la
   fecha que muestra el blog de CLC. El original es de **mayo de 2014** (revista *Vivir Más*), y lo
   encontró David, no yo. **Antes de fechar una nota, buscar si es una republicación** — el CMS
   muestra la fecha de la reedición, no la de la primera publicación.

**También hay que verificar las fuentes ya verificadas:** la nota de CLC de 2016 dice "un día de
hospitalización" cuando hoy la cirugía es ambulatoria. **No reproducir esa frase.** El error de
atribución de la cita del paciente en la nota de EBUS **solo está en la versión de 2017**; la de
mayo de 2014 es correcta y además más completa.

#### 3.2 Registro sobrio

David marcó como **"poco serio"** el registro narrativo y pidió borrar todas las descripciones de
eventos que yo había añadido a `/docencia` (bajó de 1.460 a 500 palabras).

**Criterio:** cada entrada es **título · fecha · institución · enlace**. Se conserva la atribución
literal de terceros (`Citado como «…»`) porque es la prueba. Se eliminan valoraciones,
comparaciones con otras instituciones, superlativos y cualquier frase que explique por qué algo
importa. **Si un dato necesita que yo argumente su relevancia, probablemente no debería estar.**

Aplica a las seis webs y al CV. **No aplica a las afirmaciones que David hace sobre sí mismo:**
esas son suyas, se señalan una vez y se respeta su decisión.

#### 3.3 Schema

Todo lo que va en JSON-LD **debe estar visible en la página**. Hubo un `FAQPage` oculto clonado en
4 dominios (infracción de Google); ya corregido, no reintroducir.

#### 3.4 Contenido que no se toca

- **No tocar precios ni cobertura.** Hay un convenio en negociación.
- **No destacar la sudoración compensatoria** — es el principal motivo por el que la gente no se opera.
- **Rubor facial: cada vez se opera menos** por alta probabilidad de SC posoperatoria. No priorizar.
- **Sin claims de ranking** ("el mejor", "el número 1"). Las cifras de volumen sí se conservan.

---

### 4. Decisiones tomadas — no revisitar

- **NO partir rats.cl en subpáginas.** Tiene 1.104 palabras; partirlo daría ~220/pág. Primero contenido.
- **rats.cl NO cita publicaciones**: ninguno de los 26 artículos es de RATS. Presentarlo así sería inflar.
- **NO hay huella de PBN.** La duplicación real de prosa es 3-10%: solo el pie de contacto.
- **Categoría GBP "Cirujano torácico" NO EXISTE.** La única es "Cirujano cardiovascular y torácico",
  ya puesta. Compensar vía Servicios del GBP.
- **No soltar vats.cl:** un .cl de 4 letras, pagado hasta 2028, es el atajo que se dice en voz alta.
- **Los claims de «pionero» y «referente» se quedan** (decisión de David, 17-ago). Ver §7.
- **Graphify no aplica**: indexa grafos de dependencias de código; aquí es HTML estático.
- **NO pedir backlinks a sociedades científicas ni instituciones** (WABIP, SOCICH, Finis Terrae,
  HCSBA ni ninguna otra). Decisión de David, 20-sep-2026, **definitiva**: que una sociedad enlace
  a un médico en particular es recomendarlo, y es impropio. No reproponer en ninguna forma —
  ni correos, ni plantillas, ni «notas institucionales». Ver `claude/decision-no-pedir-backlinks.md`.
- **No desmentir la nota de FALP** («primera cirugía robótica de tórax del país», 2022). Decisión de
  David, 20-sep-2026. Cronología real en `claude/cronologia-robotica-toracica-chile.md`.

---

### 5. Estado actual de la red (medido el 17-ago-2026)

| Comprobación | Resultado |
|---|---|
| `python3 scripts/audit.py` | 33 páginas, **0 hallazgos** |
| Repo ↔ producción | mismo commit |
| Páginas en vivo | **33/33 responden 200** |
| GA4 `G-X3GX2HCVZL` | 2 apariciones por página (loader + config) en las 33 |
| Canonical y `@id` | correctos en las 33 |
| robots.txt + sitemaps | 6/6, **33 URLs**, cuadran |
| `<meta robots>` | las 33 con `max-snippet:-1, max-image-preview:large, max-video-preview:-1` |
| Redirects | `cirugiadetorax.cl` y `vats.cl` correctos; `www` → apex en los 6 |

#### Search Console — última lectura (14-ago-2026, 3 meses)

| Dominio | Impresiones | Clics | Posición |
|---|---|---|---|
| cirugiatoracica.cl | 375 | 5 | 36,7 |
| hiperhidrosis.cl | 204 | **0** | 42,1 |
| rats.cl | 175 | **8** | **7,3** |
| cancerpulmonar.cl | 163 | 4 | 25,2 |
| broncoscopia.cl | 86 | 3 | 17,5 |
| videotoracoscopia.cl | 19 | 1 | 13,6 |
| **Total** | **1.022** | **21** | |

Venía de 700/10 el 5-ago y 558/8 el 30-jul. **rats.cl es el mejor activo.**
Cuenta de GSC: **`dr.david.lazo@gmail.com`**; `dlazo.torax@` no tiene propiedades. **Ojo:** al
20-sep-2026 esa cuenta es `authuser=0`; `authuser=1` resuelve a `dlazo.torax@` (sin acceso).

**Lectura del 20-sep-2026 (3 meses, 19-jun → 18-sep):** red **3.405 impr / 68 clics**, 370 en IA
generativa de Google. rats.cl 705/21/**6,7** · cirugiatoracica 802/18/20,6 · cancerpulmonar
690/15/29,1 · hiperhidrosis 507/5/42,2 · videotoracoscopia 371/3/7,8 · broncoscopia 330/6/13,6.
Ningún dominio retrocedió. Detalle en `claude/reanalisis-2026-09-20.md`.

**Lo que no se movió, para no engañarse:** `cirugía de tórax` sigue en **82,9** pese al cambio
de vocabulario del 2-ago, y `/cirugia-hiperhidrosis/` en **60,7** pese a la reescritura completa.
Ahí el problema es autoridad, no on-page.

#### 5.e Etiquetas «eyebrow» — limpieza (29-ago-2026)

Las etiquetas en versalitas cian sobre cada titular eran el *tell* visual más
reconocible de la red. Criterio, aplicado etiqueta por etiqueta (nunca con sed):

1. Si repite lo que dice el `h2` (o su bajada) → se quita.
2. Si la etiqueta es mejor que el `h2` → se fusionan y gana la etiqueta.
3. Si cumple función real (cambio de audiencia, navegación) → se conserva,
   reestilizada sin versalitas ni tracking:
   `text-transform:none;letter-spacing:0;font-size:0.8rem;font-weight:600;`

Antes de tocar cada una: comprobar que su texto no está en el JSON-LD de la
página y que ninguna ancla depende de ella. Renderizar antes y después.

**Hecho** (`class="eyebrow"` y equivalentes inline):

| Página | Antes | Después | Detalle |
|---|---|---|---|
| broncoscopia/index | 8 | 1 | commit `04b462c`; se conserva «Para médicos referentes» (criterio 3) |
| rats/index | 4 | 0 | 2 quitadas · 2 fusiones («Qué se puede operar con cirugía robótica», «Preguntas frecuentes sobre cirugía robótica») |
| cancerpulmonar/index | 3 | 0 | 2 quitadas · 1 fusión («Preguntas frecuentes sobre el cáncer pulmonar») |
| cirugiatoracica/perfil | 5 | 0 | 3 quitadas · 2 fusiones («Formación y trayectoria» — sin el nombre, por longitud, decisión de David — y «Preguntas frecuentes sobre la atención»). El h2-claim «Cirugía Torácica de Vanguardia» intacto (§7) |
| cv · docencia · publicaciones | 1+1+1 | 1+1+1 | **No eran decorativas**: son el enlace de retorno «← Dr. David Lazo Pérez» a `/perfil` (cv con BreadcrumbList). Conservadas sin versalitas (criterio 3) |
| hiperhidrosis (16 pág.) | 20 | 10 | 20-sep-2026, commit `4bf65c7`. 10 quitadas por criterio 1 · 10 conservadas por criterio 3 y reestilizadas en `assets/site.css`. Detalle abajo |

**hiperhidrosis.cl (20-sep-2026) — el conteo correcto es 20, no 36.** La cifra de 36 sale de
sumar las **16 `cta-eyebrow`** (una por página), que son **otra familia** y siguen en pie por la
decisión de más abajo. `class="eyebrow"` en el cuerpo: **20**.

- **Quitadas (10)** — repetían el `h` vecino o eran relleno valorativo: portada ×4 («Entender la
  condición», «Autoevaluación», «Alternativas reales», «Recursos»), `/blog/` («Recursos»),
  `/cirugia-hiperhidrosis/` («Tratamiento quirúrgico»), `/rubor-facial-patologico/` («Otra cara de
  la condición»), `/sobre-la-hiperhidrosis/` ×2 y `/test-nivel-de-severidad/` («Autoevaluación»).
- **Conservadas (10)** — criterio 3, ubican la página dentro de una serie: los 7 «Blog · ‹tema›»
  de los posts y los 3 «Grados de severidad» de leve/moderada/severa.
- También se eliminó `.navy-panel__head .eyebrow`, que quedó huérfana.

**Pendiente — fuera del inventario del encargo (detectado al cerrar):**
`cirugiatoracica/index.html` tiene **7** `class="eyebrow"` del rediseño 3a — ojo:
una de ellas ES el `h2` SEO «Enfermedades que tratamos» (el titular visible grande
es un div); ahí la etiqueta no se puede quitar sin mover el h2.

**Pendiente — familias no tocadas en esta pasada, se deciden aparte:**
`cta-eyebrow` (29) — probablemente se quedan: en el CTA la etiqueta sí introduce
un cambio de contexto · `sec-eyebrow` (12) · `bio-eyebrow` (4, p. ej. «Especialista»
en la tarjeta de bio de /perfil) · `hero-eyebrow` (2) · `page-nav-eyebrow` (2).

#### 5.f Entidad `Physician` de hiperhidrosis.cl alineada con el hub (20-sep-2026)

Los 6 dominios comparten el `@id` `https://cirugiatoracica.cl/#david-lazo`, pero hiperhidrosis.cl
le colgaba datos distintos en sus 16 páginas: **el mismo identificador llegaba a los motores con dos
nombres**. Corregido copiando lo que los otros cinco dominios ya publican — no es una afirmación
nueva, así que no requería aprobación. Commit `7c817c1`.

| Campo | Antes (las 16) | Ahora |
|---|---|---|
| `name` | «Dr. David Lazo» | **«Dr. David Lazo Pérez»** |
| `medicalSpecialty` | `schema.org/Surgical` | los 3 valores del hub |
| `jobTitle` · `knowsAbout` (9) · `worksFor` (2 `Hospital`) · `availableService` | ausentes | **añadidos, idénticos al hub** |

- **`hasCredential` se dejó fuera a propósito.** Declara *«Cirugía Torácica — Universidad de
  Chile»* y ese texto **no está visible en ninguna de las 16 páginas** («Universidad de Chile» en
  0/16; «Cirugía Torácica» solo en 1/16). Ponerlo infringiría la §3.3. Si alguna vez se quiere,
  primero tiene que aparecer en el texto.
- **`availableService` sí entró**: el box «Agendar consulta · Clínica Las Condes · Telemedicina»
  está visible en las 16.
- Intactos `@id`, `subjectOf`, `honorificSuffix`, `memberOf`, `sameAs`, `alumniOf`, `affiliation`,
  `description` (propia del vertical), `address`, `areaServed`, `identifier`, `image` y `url`.

> **Detalle menor sin resolver:** el `url` del `Physician` es `https://cirugiatoracica.cl` en
> hiperhidrosis y `https://cirugiatoracica.cl/` (con barra) en el hub. No se tocó porque estaba
> fuera del encargo; conviene unificarlo cuando se toque el schema del hub.

#### GA4 — primera medición real

80 sesiones · 25 usuarios nuevos · 329 vistas. **Cuidado:** 70% "Direct" con 2 s de interacción y
reparto por país anómalo = **bots**. El tráfico real son las 15 sesiones de orgánica, que sí leen
(54 s, 5,73 páginas/sesión). Página más vista: **videotoracoscopia.cl**, la que menos impresiones
tiene. Conviene activar el filtro de bots.

#### Peso de las homes (como las descarga un navegador moderno)

videotoracoscopia 1.375 KB · broncoscopia 1.376 KB · cirugiatoracica 1.434 KB · hiperhidrosis 788 KB ·
cancerpulmonar 668 KB · **rats 1.150 KB** (venía de 6.413 KB).

---

### 6. Pendientes

#### De David — por impacto

| # | Qué | Por qué importa |
|---|---|---|
| 1 | **ORCID: borrar el duplicado y cargar la regencia WABIP** (ver #5 y #6) | Es la fuente de autoridad externa más fuerte que controla él entero. Sube a #1 tras cancelar los backlinks (§4) |
| 2 | **GBP: conseguir reseñas** | Tiene **0** (20-sep). Es la ficha que sale al googlear su nombre |
| 3 | **GA4: marcar conversiones** | `reserva_presencial` y `reserva_telemedicina` como eventos clave + los 6 dominios en Admin → Flujos de datos |
| 4 | **Fusionar las 2 fichas de Doctoralia y conseguir reseñas** | **1 opinión en total, no 58** (verificado 20-sep): `/david-rene-lazo-perez` 1 (feb-2024), `/david-rene-lazo-perez-3` (la completa) 0. Doctoralia es el #1 de «cirujano torácico Santiago» y lo nombra en el snippet. No se sabe de dónde salió el 58: no reusarlo |
| 5 | **ORCID: borrar el duplicado** "Resistencia a ciprofloxacino" (marca 32, son 31) | 2 minutos |
| 6 | **ORCID: cargar la regencia WABIP** | Su credencial internacional más fuerte, ausente del registro |
| 7 | ~~LinkedIn indexado como «Clínica MEDS»~~ | **Cerrado 20-sep-2026**: ya no aparece en la SERP del nombre. Sigue pendiente cerrar el perfil duplicado y la URL personalizada (§2, LinkedIn) |
| 8 | **@hiperhidrosis.cl (IG): cambiar el enlace de beacons.page** | Debería ir a hiperhidrosis.cl o al perfil |
| 9 | GBP: cargar horario y categoría | Google lo pide en el panel |
| 10 | Cerrar el convenio para publicar la sección de cobertura | El hueco más grande de "cirugía hiperhidrosis" |
| 11 | CV: corregir coautores omitidos | #17 lista 4 de 14; #14 lista 4 de 9 ("Yévene" → **Yévenes**); #18 falta Clavero JM |
| 12 | TopDoctors: reactivar | "no es posible contactar" |

| 13 | **Instagram @dr.david.lazo.p: cadencia** | Metricool (conectado 7-sep-2026): **2.437 seguidores, planos** (+4 en dos semanas). 4 reels entre jul y sep (9-jul, 9-ago, 16-ago, 14-sep) y **0 historias**. Cada reel alcanza 440-975 cuentas; entre reels, el alcance cae a menos de 15 al día. El problema es la frecuencia, no la calidad |
| 14 | **Verificar que `/docencia` entró en Google** | No estaba indexada («Google no reconoce esta URL»); indexación solicitada el 20-sep-2026. Sitemap correcto. Si a las 2-3 semanas sigue fuera, revisar enlazado interno |

#### De Claude

| # | Qué | Estado |
|---|---|---|
| 1 | Acordeón de FAQ en el resto de hiperhidrosis.cl | Verificado 17-ago: `rubor-facial-patologico` no tiene ni un `.faq-q` |
| 2 | `/rats-vs-vats` — contenido nuevo | Verificado 17-ago: `dist/rats/` solo tiene `index.html` |
| 3 | **14** de las 16 páginas de hiperhidrosis.cl bajo 400 palabras | Medido el 20-sep-2026 (antes se decía 7). **Ninguna es plantilla vacía** — ver §6.b antes de escribir nada |
| 4 | `videotoracoscopia.cl` es el único sin `FAQPage` | |

> Los antiguos #4 (`hiperhidrosis.cl` sin `OAI-SearchBot`/`ChatGPT-User`) y #5 (no existe
> `llms.txt`) **se eliminan: ambos están hechos**, verificados en producción el 20-sep-2026.
> Los 6 dominios sirven `robots.txt` con los 9 bots de IA y `llms.txt` como `text/plain`.

#### 6.b Contenido de hiperhidrosis.cl — diagnóstico (20-sep-2026)

Medido con el CTA y la navegación excluidos. **14 de 16 bajo 400 palabras, pero ninguna es
plantilla con relleno**: todas tienen texto propio. La cifra baja tiene tres causas distintas y
cada una pide una respuesta distinta —o ninguna.

| Tipo | Páginas | Qué pasa |
|---|---|---|
| **Estructural, no es déficit** | `/blog/` (índice de los 7 posts) · `/test-nivel-de-severidad/` (herramienta: 10 enunciados + 40 radios, **en HTML plano**) · `/` (hub de tarjetas hacia el test, los tratamientos y el blog) | Contar palabras aquí no mide nada. **No ampliar.** |
| **Texto real corto, con contenido clínico específico** | `/hiperhidrosis-localizada-leve/` (cloruro de aluminio: mecanismo, pauta nocturna, 98% de efectividad, irritación) · `/hiperhidrosis-localizada-severa/` (simpatectomía, videotoracoscopía, quién la hace, plantar experimental) | Son cortas de verdad. **`leve` es la única genuinamente subdesarrollada**: su hermana `moderada` (317 pal.) da a cada tratamiento su `h2` con posología y cifras; `leve` explica uno solo en prosa corrida y sin subtítulos. `severa` es corta **a propósito**: deriva a `/cirugia-hiperhidrosis/` (1.144 pal.) |
| **Posts de 2020-21, artículos reales** | los 7 de `/20xx/` | Tienen estructura y contenido propios. El problema no es el tamaño: es el **registro**. Tutean, exclaman («¡Dile adiós a la hiperhidrosis!», «¡Recuerda seguirnos en nuestro Instagram!») y cierran con llamadas a redes. Choca con la §3.2 y con el resto de la red rediseñada |

**Las dos largas:** `/cirugia-hiperhidrosis/` (1.144 pal., 9 FAQ) y `/sobre-la-hiperhidrosis/`
(877 pal.). Son las que sostienen el dominio.

**Hallazgo de arquitectura:** el sitio se organiza por **grado de severidad** (leve/moderada/severa),
pero la demanda de búsqueda está en el **nombre del tratamiento**. «Toxina botulínica»,
«iontoforesis» y «medicación oral» no tienen página propia: viven en una línea de la portada y
dentro de `/hiperhidrosis-localizada-moderada/`. Es el hueco más grande del dominio, y no se
resuelve alargando las páginas que ya existen.

**Fuera de alcance por la §3.4:** no se amplían `/2020/11/13/sudoracion-compensatoria…/` ni
`/rubor-facial-patologico/`. Son las dos que mejor rankean; es una decisión, no un error.

> **Discrepancia menor detectada:** el post de sudoración compensatoria vive en `/2020/11/13/`
> pero su `datePublished` dice `2020-11-14`. Un día de diferencia entre la URL y el schema. No se
> tocó: corregir el schema sería adivinar cuál de las dos es la buena, y mover la URL rompería
> enlaces.

#### `rats.cl/operculo-toracico` — PUBLICADO (13-sep-2026)

- **En producción** (commits `3ffab67` y anteriores). Tras la revisión de David sobre la maqueta:
  **H1 propio por subpágina** (Causas / Síntomas / Estudio / Tratamiento del opérculo torácico;
  la portada conserva el masthead) y **sinónimos en español** —«síndrome de la salida torácica»,
  «síndrome del desfiladero torácico»— visibles en la portada (§2) y declarados en el
  `alternateName` solo de la portada (regla 3.3). Todo generado desde el lienzo con `convert_dc.py`.
- **Indexación: hecha sola** — 6/6 URL de rats.cl indexadas al 20-sep, sin solicitarla. 7 de las 10
  consultas principales ya son del opérculo, pero anatómicas/académicas y con 0 clics.
- **Pendiente tras publicar:** vídeo del autor
  para `tratamiento` (en producción; irá con `VideoObject`).

- Sección de 5 páginas en `dist/rats/operculo-toracico/` (`index`, `causas`, `clinica`, `estudio`,
  `tratamiento` + `imgs/`, 20 webp). David revisó y aprobó el contenido página por página (8–13 sep).
- **Fuente de verdad:** `_design/maquetas/operculo/_build/lienzo-design-v2.dc.html` (lienzo Claude Design).
  Se regenera con `python3 _design/maquetas/operculo/_build/convert_dc.py --publicar` (sin flag genera la
  maqueta en `_design/maquetas/operculo/`). **No editar los HTML generados a mano.**
- Textos clínicos: PPT de David, Kök 2023, Donahue 2020, Burt 2020 (verificados en texto completo o PubMed)
  y criterio del autor. Regla de David (12-sep): **nada clínico sin bibliografía, y no preguntar**.
- Enlaces de entrada añadidos: tarjeta "Síndrome del Opérculo Torácico" en `dist/rats/index.html`,
  tarjeta "Opérculo torácico" del hub (`dist/cirugiatoracica/index.html`) y pie de `dist/videotoracoscopia/index.html`.
  Sitemap y `llms.txt` de rats.cl actualizados. `audit.py`: 39 páginas, todo correcto.
- Pendiente tras publicar: vídeo del autor (en producción; se insertará en `tratamiento`).

#### Tres dudas del CV pendientes de David

1. ¿"Curso Latinoamericano Osteosíntesis Pared Torácica" (may-2023) es el mismo que el **#58**,
   "Curso Pared Torácica MedXpert LATAM — Bogotá"?
2. ¿"Webinar SBCT-GBOT-ALAT" (sep-2021) es el **#47**, "Webinar ALAT: Nuevas Modalidades Terapéuticas"?
3. **Discrepancia real:** el CV dice "#64 **3°** International SRS LATAM Robotic Surgery Congress —
   **Río de Janeiro**", pero su post del 25-ago-2023 dice "**2do** Congreso de la Society of Robotic
   Surgery LATAM y **COLCIR**". Ni el ordinal ni la sede coinciden.

---

### 7. Diagnóstico — el cuello de botella

**No es indexación, no es estructura, no es on-page. Es autoridad externa.**

Tres consultas de prueba a IA con búsqueda en vivo (16-ago):

| Consulta | Resultado | ¿Aparece David? |
|---|---|---|
| "mejor cirujano torácico Santiago cirugía robótica RATS" | Destaca al Dr. Pablo Pérez Castro (oncotorax.cl), UC Christus, Bupa | **No** |
| "EBUS CryoEBUS broncoscopía intervencional Chile" | Clínica Alemana como pionera del EBUS | **No** |
| "David Lazo Pérez cirujano torácico publicaciones" | Doctoralia, TopDoctors, CTSNet, LinkedIn. Concluye que *"no hay detalles sobre sus publicaciones"* | **Ningún dominio propio** |

El tercero es el diagnóstico: buscando su nombre + "publicaciones", la IA no encuentra
`/publicaciones` —31 referencias con `ScholarlyArticle`— y responde que no hay datos. Los
directorios de terceros tapan sus propios sitios.

**El on-page está resuelto.** Lo que falta son dominios externos que lo respalden.

**Actualización 20-sep-2026:** la vía institucional (pedir enlaces a sociedades) está **cerrada
por norma profesional** — ver §4. El diagnóstico sigue en pie, pero la conclusión ya no es «pedir
enlaces». Lo que queda, sin pedirle nada a nadie: **ORCID** (regencia WABIP, duplicado),
**Wikidata** (entidad factual), **directorios propios** (Doctoralia, GBP, TopDoctors, CTSNet) con
reseñas de pacientes, y **producción indexada** con DOI. Y aceptar que el resto es lento.

#### Sobre el claim de EBUS y Clínica Alemana

Clínica Alemana reclama EBUS desde 2010. **Matizado por David (17-ago):** partieron el mismo año
pero con otro médico que ya no está en Chile; su equipo actual se formó en **2014**. La web de
David nunca dijo "pionero en EBUS" sino *"el cirujano con mayor experiencia en EBUS en Chile
(desde 2010, +3.200 procedimientos)"*, que con ese dato queda **reforzado**: 16 años de práctica
continua frente a 12. **No es un conflicto de claims.**

Claims que siguen sin fuente externa, **por decisión suya de dejarlos**: *"pionero en CryoEBUS a
nivel latinoamericano"* (6 páginas, sin año de inicio), el H1 de `/perfil` *"Referente en Cirugía
Torácica en Latinoamérica"* y el H2 *"Cirugía Torácica de Vanguardia"*. Los dos claims de RATS
*sí* tienen respaldo publicado: su resumen de congreso se titula *"…análisis de 79 casos del
**primer programa nacional**"*. Si algún día se quiere reforzar, basta con enlazarlo.

---

### 8. Trampas de método — comprobado a base de equivocarse

| Trampa | Qué hacer |
|---|---|
| **WebFetch miente en redirecciones** | Dio "302" donde había 308 y sirvió contenido sin declarar el salto www→apex. Para códigos HTTP y despliegues: **panel de Vercel** |
| **GA4 aparece 2 veces por página y está bien** | Loader + `gtag('config')`. Esperar 3 marcaba las 32 páginas como anómalas |
| **GA4 envía por `sendBeacon` y agrupa** | Un conteo inmediato de recursos da cero aunque el evento salió. Mirar el parámetro `en=` del último hit `/g/collect` |
| **`image-set()` en CSS es la forma correcta de servir WebP en fondos** | Un detector que solo busque `<picture>` los da por "no conectados" e infla los pesos calculados |
| **`width`/`height` en `<img>` exigen `img { height: auto; }` en el CSS** | Sin eso, el atributo `height` actúa como *presentational hint*, anula el `aspect-ratio` y rompe 16 imágenes |
| **Posiciones de GSC: la media del dominio ≠ la de la consulta** | 45,6 era la media; la consulta estaba en 83,4. Activar la métrica Posición |
| **Vercel: "Redirect apex to www" viene MARCADA** | Desmarcarla. Y el desplegable arranca en 307: cambiar a 308. El panel gana sobre `vercel.json` |
| **Instagram no es legible sin sesión iniciada** | Con su sesión abierta en Chrome: `/api/v1/feed/user/1486809562/` con `x-ig-app-id`, paginando de 33 en 33. El navegador corta a los 45 s: trocear y acumular en `window` |
| **Comparar schema con texto visible exige ignorar puntuación** | `<strong>` y `<a>` meten espacios junto a comas. Sin normalizar, da falsos positivos de "respuesta no visible" |
| **Tablas de operabilidad por estadio** | Los paréntesis contienen o una **técnica** (prescindible) o una **condición clínica** ("con evaluación") que no lo es. Distinguir fila por fila |

---

### 9. Archivos de la carpeta

| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Este documento — estado, reglas y pendientes |
| `ESTADO-historico.md` | Registro cronológico completo (jul-ago 2026) |
| `CV_David_Lazo_2026.docx` / `.pdf` | CV completo, 7 páginas |
| `lazo_31_publicaciones.bib` | Importar las 31 publicaciones a ORCID |
| `ORCID-instrucciones.md` · `apply_orcid.py` | ORCID (ya ejecutado) |
| `foto-publicaciones.jpg` | Hero de `/publicaciones` — ver nota |
| `.github-token` | **Nunca commitear** |

> **Nota sobre el hero de `/publicaciones`:** es una escena generada por IA. Incluye una taza con
> el logo de **STS**, sociedad a la que David **no pertenece**, y manuscritos de ficción. Se
> mantiene por decisión suya. Reemplazar por una foto real de congreso ALAT cuando la haya.

#### `scripts/audit.py`

`python3 scripts/audit.py` desde la raíz. Comprueba las 33 páginas: anidado HTML, JSON-LD
parseable, cada pregunta y respuesta de `FAQPage` presente en el texto visible, recursos locales
existentes, GA4 una sola vez, `title` ≤60 y `description` 120-158 sin duplicados, y `@id` canónico.
Devuelve 1 si algo falla. **No detecta problemas de renderizado** — para eso hace falta navegador.

---

### 10. Estándar de la red

- Canonical **sin www** en toda la red · `cleanUrls: true` donde hay subpáginas `.html`.
- `robots.txt` permite GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-Web, PerplexityBot,
  Google-Extended, Applebot-Extended, CCBot. Sitemap por dominio, sin-www.
- `<meta robots>` con `max-snippet:-1, max-image-preview:large, max-video-preview:-1`.
- Estilo: Arial/Figtree, teal `#0891b2`, navy `#0c1526`, serif `DM Serif Display`.
- `lastReviewed` lleva la fecha del **último cambio clínico real** (`git log`), no la de hoy.
  El `<lastmod>` del sitemap sí lleva la fecha del cambio de archivo.
- `/links` no lleva `lastReviewed` a propósito: no tiene contenido clínico.
  `/publicaciones` tampoco: es bibliografía, no consejo médico.
