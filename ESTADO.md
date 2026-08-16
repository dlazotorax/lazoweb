# ESTADO — Red web Dr. David Lazo Pérez

> **Léeme primero.** Este archivo evita proponer cosas ya hechas o rehacer trabajo.
> Última actualización: **16 ago 2026** (2.ª revisión: GEO).

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
- Clínica Alemana reclama públicamente ser pionera del EBUS en Chile **desde 2010**, el mismo
  año y el mismo terreno que el claim de David (+3.200 EBUS desde 2010).
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

### Estado de `/docencia` al cierre
1.290 palabras visibles, 65,8 KB (en el repo; ver la incidencia de despliegue), 14 nodos JSON-LD: `Physician`, `MedicalWebPage`,
2× `EducationalOccupationalProgram`, `MedicalOrganization`, `NewsArticle`, `VideoObject`
y 7× `Article`. Seis secciones: Formación de subespecialistas · Universidad de Chile ·
WABIP · Prensa nacional · Televisión · Menciones en Clínica Las Condes.

### Lo que sigue siendo el problema
La página **documenta** autoridad; no la **importa**. El backlink sigue siendo cero. Los tres
enlaces que moverían la aguja son los mismos de §17 y dependen de David:
**Finis Terrae** (que la ficha del comité enlace a cirugiatoracica.cl), **WABIP** (regencia) y
**SOCICH**. Con `/docencia` publicada, ahora hay una URL concreta que pedirles que enlacen.
