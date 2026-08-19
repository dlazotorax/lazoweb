# ESTADO — Red web Dr. David Lazo Pérez

> **Léeme primero.** Estado actual, reglas y pendientes. Evita proponer cosas ya hechas.
> **Última actualización: 17 ago 2026.**
> El detalle cronológico de cada sesión está en **`ESTADO-historico.md`**. Consúltalo solo
> cuando necesites saber *por qué* algo quedó como quedó.

---

## 1. Infraestructura

- **Repo:** `dlazotorax/lazoweb`, rama `main`. Sitios estáticos, sin build, en `dist/<dominio>/`.
- **Hosting:** Vercel, cuenta **Hobby**, 7 proyectos apuntando al mismo repo.
- **Token GitHub:** `Paginas web/.github-token` (fine-grained, solo lazoweb). **Nunca commitearlo.**
- **Flujo:** clonar fresco en el sandbox → editar → `audit.py` → commit → push a `main`.
- Antes de commitear: `git config user.email noreply@anthropic.com && git config user.name Claude`.
- La carpeta `Projects/Paginas web` es respaldo; el repo manda.

| Dominio | Páginas | Rol |
|---|---|---|
| cirugiatoracica.cl | 5 (`/`, `/perfil`, `/publicaciones`, `/docencia`, `/links`) | Hub |
| hiperhidrosis.cl | 16 | Pacientes |
| cancerpulmonar.cl | 7 | Pacientes |
| broncoscopia.cl | 3 | Dual |
| rats.cl | 1 | Médicos referentes |
| videotoracoscopia.cl | 1 | VATS — dominio principal desde jul-2026 |
| vats.cl | 308 → videotoracoscopia.cl | Redirect |
| cirugiadetorax.cl | 308 → cirugiatoracica.cl | Redirect |

**Total: 33 páginas publicadas.**

### Despliegue — cómo funciona ahora

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

## 2. Identidad — datos canónicos

- **ORCID:** `0009-0007-0806-6679`
- **`@id` de la entidad:** `https://cirugiatoracica.cl/#david-lazo` — presente en las 33 páginas.
  **Nunca crear un `@id` local por dominio.**
- **Indexación del nombre:** SciELO → `Lazo P` · PubMed → **`Lazo P D`** · Elsevier → `P. David Lazo`.
  Buscar "Lazo D" o "David Lazo" devuelve cero; resuelto con "also known as" en ORCID.
- **Homonimia:** su hermano Diego es el "Lazo D" de PubMed. La huella real de David son 5 artículos ahí.
- **Afiliación vigente:** Clínica Las Condes (desde ene-2026) + Hospital Clínico San Borja Arriarán
  (desde oct-2022). **MEDS terminó en dic-2025** — sigue apareciendo en LinkedIn indexado y en la
  ficha del 94° Congreso Argentino.
- **Formación:** Médico-Cirujano PUC (2004) · Esp. Cirugía Torácica U. de Chile / INT (2009) ·
  Fellowship Trasplante Pulmonar, H.U. Puerta de Hierro Majadahonda (2010-2011).
- **Cargos internacionales:** Regente por Chile de **WABIP** (verificado en su Board of Regents) ·
  Director Depto. Cirugía Torácica **ALAT** (2020-2022) · Director **SER** (2016-2019).
- **Docencia:** Comité Académico de la subespecialidad en Cirugía de Tórax, **U. Finis Terrae**
  (verificado en medfinis.cl) · Director de perfeccionamiento en la **Escuela de Postgrado de la
  U. de Chile, 2014 – nov 2022** (terminó; no es vigente).

### Actividad verificada en fuentes de terceros (17-ago-2026)

Material encontrado al rastrear serchile.cl y savalnet.cl. **Todo abierto en la fuente.**

| Fecha | Qué | Fuente |
|---|---|---|
| 17-20 oct 2012 | Charla "Trasplante pulmonar en FQ. Experiencia chilena" — Congreso Soc. Latinoamericana de Neumología Pediátrica, Hotel del Mar | savalnet.cl `20121017_12354/17676` |
| 6-9 nov 2013 | Charla "Situación actual del trasplante pulmonar en Chile" — Congreso SER 2013, Viña del Mar | savalnet.cl `20131106_20393/20430` |
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

### Desde cuándo — lo que cada técnica puede fechar

| Técnica | Evidencia pública más antigua |
|---|---|
| Trasplante pulmonar | **2012** (charla en congreso) |
| Pleura / fístula broncopleural | **2015** |
| Hiperhidrosis | **2016** (notas CLC) |
| Broncoscopía intervencional / EBUS | **2018** (charla titulada "EBUS"); Comisión SER **2020** |
| **EBUS desde 2010** | **SIN FUENTE EXTERNA** |
| **RATS desde 2015** | **SIN FUENTE EXTERNA** — ver abajo |

**Corrección importante (error mío, 17-ago):** ofrecí el resumen *"análisis de 79 casos del primer
programa nacional"* como respaldo del claim de RATS. **No lo respalda.** David lo aclaró: ese es el
programa del **Hospital San Borja Arriarán, que partió en 2022**; el título dice literalmente *"en
hospital público docente"*. Acredita el primer programa **en un hospital público**, no su práctica
personal desde 2015. Es exactamente el tipo de conflación contra la que advierte la §3.1.

**Lo que sí podría fechar 2015:** el CV lista *"[Asis.] Da Vinci Console Surgeon Training — Florida
Hospital Celebration, Orlando"* como entrada #27, **entre** el 48° Congreso SEPAR (Gran Canaria,
2015) y el 11.º Simposio ISSS (Santiago, **15-16 oct 2015**, verificado en isss.net). La lista es
cronológica, así que la certificación cae en 2015. **El certificado de cirujano de consola es el
documento que zanjaría el asunto** — pendiente de que David lo aporte.

### Publicaciones: 31 verificadas (2004-2023)

**26 artículos revisados por pares:** 10 Rev Chil Enf Respir · 6 Rev Chil Cirugía · 4 Rev Med Chile ·
3 Rev Med Clin Condes · 1 Rev Chil Radiología · 1 Cir Cir · 1 Rev Chil Urología.

**5 resúmenes de congreso indexados** (DOI verificado en Crossref salvo el de 2014):
J Heart Lung Transplant 2023;42(4):S298 (×2) · Pediatr Crit Care Med 2021;22(Supl 1) (×2) ·
J Thorac Oncol 2014;9(9):S184-5 (sin DOI).

Identificadores: 21 PID SciELO · 11 DOI · 5 PMID · 1 LILACS · 1 sin ID.
Archivo para ORCID: `lazo_31_publicaciones.bib`.

**No confundir:** son **26 revisados por pares + 5 resúmenes**, no "31 revisadas por pares".
**Ninguna de las 26 es de RATS** — esa producción está en comunicaciones a congreso.

### CV

`CV_David_Lazo_2026.docx` / `.pdf` — 7 páginas. **86 congresos**, **36 resúmenes presentados
en congresos**, 31 publicaciones. Perfil: "más de 85 congresos".

---

## 3. Reglas que no se negocian

### 3.1 Verificar antes de afirmar (YMYL)

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

**También hay que verificar las fuentes ya verificadas:** la nota de CLC de 2016 dice "un día de
hospitalización" cuando hoy la cirugía es ambulatoria, y la nota de EBUS atribuye al Dr. Lazo una
cita que el texto pone en boca del paciente. **No reproducir ninguna de las dos.**

### 3.2 Registro sobrio

David marcó como **"poco serio"** el registro narrativo y pidió borrar todas las descripciones de
eventos que yo había añadido a `/docencia` (bajó de 1.460 a 500 palabras).

**Criterio:** cada entrada es **título · fecha · institución · enlace**. Se conserva la atribución
literal de terceros (`Citado como «…»`) porque es la prueba. Se eliminan valoraciones,
comparaciones con otras instituciones, superlativos y cualquier frase que explique por qué algo
importa. **Si un dato necesita que yo argumente su relevancia, probablemente no debería estar.**

Aplica a las seis webs y al CV. **No aplica a las afirmaciones que David hace sobre sí mismo:**
esas son suyas, se señalan una vez y se respeta su decisión.

### 3.3 Schema

Todo lo que va en JSON-LD **debe estar visible en la página**. Hubo un `FAQPage` oculto clonado en
4 dominios (infracción de Google); ya corregido, no reintroducir.

### 3.4 Contenido que no se toca

- **No tocar precios ni cobertura.** Hay un convenio en negociación.
- **No destacar la sudoración compensatoria** — es el principal motivo por el que la gente no se opera.
- **Rubor facial: cada vez se opera menos** por alta probabilidad de SC posoperatoria. No priorizar.
- **Sin claims de ranking** ("el mejor", "el número 1"). Las cifras de volumen sí se conservan.

---

## 4. Decisiones tomadas — no revisitar

- **NO partir rats.cl en subpáginas.** Tiene 1.104 palabras; partirlo daría ~220/pág. Primero contenido.
- **rats.cl NO cita publicaciones**: ninguno de los 26 artículos es de RATS. Presentarlo así sería inflar.
- **NO hay huella de PBN.** La duplicación real de prosa es 3-10%: solo el pie de contacto.
- **Categoría GBP "Cirujano torácico" NO EXISTE.** La única es "Cirujano cardiovascular y torácico",
  ya puesta. Compensar vía Servicios del GBP.
- **No soltar vats.cl:** un .cl de 4 letras, pagado hasta 2028, es el atajo que se dice en voz alta.
- **Los claims de «pionero» y «referente» se quedan** (decisión de David, 17-ago). Ver §7.
- **Graphify no aplica**: indexa grafos de dependencias de código; aquí es HTML estático.

---

## 5. Estado actual de la red (medido el 17-ago-2026)

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

### Search Console — última lectura (14-ago-2026, 3 meses)

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
Cuenta de GSC: **`dr.david.lazo@gmail.com`** (authuser=1); `dlazo.torax@` no tiene propiedades.

**Lo que no se movió, para no engañarse:** `cirugía de tórax` sigue en **82,9** pese al cambio
de vocabulario del 2-ago, y `/cirugia-hiperhidrosis/` en **60,7** pese a la reescritura completa.
Ahí el problema es autoridad, no on-page.

### GA4 — primera medición real

80 sesiones · 25 usuarios nuevos · 329 vistas. **Cuidado:** 70% "Direct" con 2 s de interacción y
reparto por país anómalo = **bots**. El tráfico real son las 15 sesiones de orgánica, que sí leen
(54 s, 5,73 páginas/sesión). Página más vista: **videotoracoscopia.cl**, la que menos impresiones
tiene. Conviene activar el filtro de bots.

### Peso de las homes (como las descarga un navegador moderno)

videotoracoscopia 1.375 KB · broncoscopia 1.376 KB · cirugiatoracica 1.434 KB · hiperhidrosis 788 KB ·
cancerpulmonar 668 KB · **rats 1.150 KB** (venía de 6.413 KB).

---

## 6. Pendientes

### De David — por impacto

| # | Qué | Por qué importa |
|---|---|---|
| 1 | **Pedir el enlace a WABIP, SOCICH y Finis Terrae** | Única vía de backlink institucional. Backlinks actuales: **cero**. Ya existe `/docencia` como URL concreta que pedirles que enlacen |
| 2 | **GBP: conseguir reseñas** | Tiene **0**; en Doctoralia tiene 58. Es la ficha que sale al googlear su nombre |
| 3 | **GA4: marcar conversiones** | `reserva_presencial` y `reserva_telemedicina` como eventos clave + los 6 dominios en Admin → Flujos de datos |
| 4 | **Fusionar las 2 fichas de Doctoralia** | 58 reseñas partidas |
| 5 | **ORCID: borrar el duplicado** "Resistencia a ciprofloxacino" (marca 32, son 31) | 2 minutos |
| 6 | **ORCID: cargar la regencia WABIP** | Su credencial internacional más fuerte, ausente del registro |
| 7 | **LinkedIn: sigue indexado como "Clínica MEDS"** | Aparece así en las respuestas de IA |
| 8 | **@hiperhidrosis.cl (IG): cambiar el enlace de beacons.page** | Debería ir a hiperhidrosis.cl o al perfil |
| 9 | GBP: cargar horario y categoría | Google lo pide en el panel |
| 10 | Cerrar el convenio para publicar la sección de cobertura | El hueco más grande de "cirugía hiperhidrosis" |
| 11 | CV: corregir coautores omitidos | #17 lista 4 de 14; #14 lista 4 de 9 ("Yévene" → **Yévenes**); #18 falta Clavero JM |
| 12 | TopDoctors: reactivar | "no es posible contactar" |

### De Claude

| # | Qué | Estado |
|---|---|---|
| 1 | Acordeón de FAQ en el resto de hiperhidrosis.cl | Verificado 17-ago: `rubor-facial-patologico` no tiene ni un `.faq-q` |
| 2 | `/rats-vs-vats` — contenido nuevo | Verificado 17-ago: `dist/rats/` solo tiene `index.html` |
| 3 | 7 páginas bajo 400 palabras (todas en hiperhidrosis.cl) | |
| 4 | `hiperhidrosis.cl` no nombra `OAI-SearchBot` ni `ChatGPT-User` en robots.txt | Cosmético: el comodín ya los cubre |
| 5 | No existe `llms.txt` en ningún dominio | |
| 6 | `videotoracoscopia.cl` es el único sin `FAQPage` | |

### Tres dudas del CV pendientes de David

1. ¿"Curso Latinoamericano Osteosíntesis Pared Torácica" (may-2023) es el mismo que el **#58**,
   "Curso Pared Torácica MedXpert LATAM — Bogotá"?
2. ¿"Webinar SBCT-GBOT-ALAT" (sep-2021) es el **#47**, "Webinar ALAT: Nuevas Modalidades Terapéuticas"?
3. **Discrepancia real:** el CV dice "#64 **3°** International SRS LATAM Robotic Surgery Congress —
   **Río de Janeiro**", pero su post del 25-ago-2023 dice "**2do** Congreso de la Society of Robotic
   Surgery LATAM y **COLCIR**". Ni el ordinal ni la sede coinciden.

---

## 7. Diagnóstico — el cuello de botella

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

**El on-page está resuelto.** Lo que falta son dominios externos que lo respalden. Por eso el
pendiente #1 de David es el único que mueve la aguja.

### Sobre el claim de EBUS y Clínica Alemana

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

## 8. Trampas de método — comprobado a base de equivocarse

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

## 9. Archivos de la carpeta

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

### `scripts/audit.py`

`python3 scripts/audit.py` desde la raíz. Comprueba las 33 páginas: anidado HTML, JSON-LD
parseable, cada pregunta y respuesta de `FAQPage` presente en el texto visible, recursos locales
existentes, GA4 una sola vez, `title` ≤60 y `description` 120-158 sin duplicados, y `@id` canónico.
Devuelve 1 si algo falla. **No detecta problemas de renderizado** — para eso hace falta navegador.

---

## 10. Estándar de la red

- Canonical **sin www** en toda la red · `cleanUrls: true` donde hay subpáginas `.html`.
- `robots.txt` permite GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-Web, PerplexityBot,
  Google-Extended, Applebot-Extended, CCBot. Sitemap por dominio, sin-www.
- `<meta robots>` con `max-snippet:-1, max-image-preview:large, max-video-preview:-1`.
- Estilo: Arial/Figtree, teal `#0891b2`, navy `#0c1526`, serif `DM Serif Display`.
- `lastReviewed` lleva la fecha del **último cambio clínico real** (`git log`), no la de hoy.
  El `<lastmod>` del sitemap sí lleva la fecha del cambio de archivo.
- `/links` no lleva `lastReviewed` a propósito: no tiene contenido clínico.
  `/publicaciones` tampoco: es bibliografía, no consejo médico.
