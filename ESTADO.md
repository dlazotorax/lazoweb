# ESTADO — Red web Dr. David Lazo Pérez

> **Léeme primero.** Este archivo evita proponer cosas ya hechas o rehacer trabajo.
> Última actualización: **14 ago 2026**.

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
| 1 | **Página de docencia y menciones** — Finis Terrae (Comité Académico) + las ~10 notas de CLC. Autoridad ya publicada que la red no usa |
| 2 | Instalar GA4 en las 33 páginas + medición entre dominios + conversiones de reserva |
| 3 | Acordeón de FAQ en el resto de hiperhidrosis.cl (`rubor-facial-patologico` aún los tiene como títulos sueltos) |
| 4 | `/rats-vs-vats` — contenido nuevo |

---|---|---|
| 1 | **Fusionar las 2 fichas de Doctoralia** (`-3/…/santiago` y `/…/las-condes`) — reseñas partidas; Doctoralia es el resultado #1 en "cirujano torácico Santiago" | David |
| 2 | **GBP: falta teléfono y horario** (lo dice Google en el panel) | David |
| 3 | **ORCID: keywords y país vacíos** (2 min) | David |
| 4 | `/rats-vs-vats` — mejor apuesta de contenido nuevo | Claude |
| 5 | `dist/uploads/` — 47 archivos basura (copias viejas). No se publica (404), pero conviene limpiar | Claude |
| 6 | CV: corregir coautores omitidos (ver §6) | David |

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
