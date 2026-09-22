# ESTADO — Red web Dr. David Lazo Pérez

> **Última actualización: 22 sep 2026.** Documento de trabajo: reglas, decisiones, datos canónicos,
> métricas vigentes y pendientes. Todo lo narrativo (sesiones, razonamientos, cómo se llegó a cada
> dato) está en **`ESTADO-historico.md`**; la versión larga de este archivo, tal como estaba al
> 22-sep-2026, está al final de ese histórico.

## 0. Cómo mantener este archivo

- **Se reemplaza, no se añade.** Al cerrar una sesión: actualizar §6 (métricas) y §7 (pendientes)
  **sobrescribiendo** lo viejo. Un pendiente hecho se borra; si su historia importa, va al histórico.
- **Sin narrativa aquí.** Nada de «error mío», «pasadas», ni relatos de sesión: eso va al histórico.
  Aquí solo queda la regla o el dato que resultó.
- Tope orientativo: **~300 líneas**. Si se pasa, algo narrativo se coló.
- Cada cifra lleva su fecha de medición. Un dato sin fecha no se reusa.

---

## 1. Reglas que no se negocian

**1.1 Verificar antes de afirmar (YMYL).** Nunca publicar autoría, cifras, credenciales, afiliaciones
ni citas desde un resumen de buscador o de IA: abrir la fuente primaria y confirmar el dato literal.
Si no se puede verificar, no se publica. **Afirmar una ausencia exige la misma verificación que una
presencia** (un `grep` antes de decir «no está»).

**1.2 Registro sobrio.** Cada entrada es **título · fecha · institución · enlace**. Sin valoraciones,
comparaciones ni superlativos; no explicar por qué algo importa. Se conserva la atribución literal de
terceros (`Citado como «…»`) porque es la prueba. No aplica a lo que David afirma de sí mismo (§2).

**1.3 Schema.** Todo lo que va en JSON-LD **debe estar visible** en la página. No reintroducir
`FAQPage` ocultos.

**1.4 Contenido que no se toca.**
- Precios y cobertura: **no** (convenio en negociación).
- **No destacar la sudoración compensatoria** ni priorizar el **rubor facial**.
- Sin claims de ranking («el mejor», «el número 1»). Las cifras de volumen sí se conservan.

**1.5 Contenido clínico nuevo:** nada sin bibliografía verificada (regla de David, 12-sep).
**Preguntar a David antes de publicar afirmaciones nuevas sobre su trayectoria.**

**1.6 Secciones:** no abrir una sección con menos de 3-4 entradas verificadas. Una sección de una
línea comunica escasez.

**1.7 Git:** antes de commitear, `git config user.email noreply@anthropic.com && git config user.name Claude`.
Correr `python3 scripts/audit.py` y **no pushear con hallazgos**.

---

## 2. Decisiones cerradas — no revisitar

| Decisión | Fecha |
|---|---|
| **NO pedir backlinks a sociedades científicas ni instituciones** (WABIP, SOCICH, Finis Terrae, HCSBA ni otra). Que una sociedad enlace a un médico es recomendarlo, y es impropio. **No reproponer en ninguna forma** (ni correos, ni plantillas, ni «notas institucionales») | 20-sep-2026 |
| **No desmentir la nota de FALP** («primera cirugía robótica de tórax del país», 2022). Cronología real en el doc del Project `cronologia-robotica-toracica-chile.md` | 20-sep-2026 |
| **No consolidar los seis dominios en uno.** rats.cl (menos páginas) es el que mejor rankea: la variable es la competencia de la consulta, no la arquitectura | 24-ago-2026 |
| Los claims **«pionero en CryoEBUS»**, H1 de `/perfil` «Referente en Cirugía Torácica en Latinoamérica» y H2 «Cirugía Torácica de Vanguardia» **se quedan** | 17-ago-2026 |
| **No partir rats.cl** (portada) en subpáginas. La sección opérculo es aparte y ya existe | ago-2026 |
| **rats.cl no cita publicaciones**: ninguno de los 26 artículos es de RATS | ago-2026 |
| **No soltar vats.cl** (redirige a videotoracoscopia.cl; pagado hasta 2028) | jul-2026 |
| neumotorax.cl y derramepleural.cl **fuera** del set: llegan por urgencia, no por búsqueda | — |
| Categoría GBP «Cirujano torácico» **no existe**; se usa «Cirujano cardiovascular y torácico» + Servicios | ago-2026 |
| No hay huella de PBN (duplicación real de prosa 3-10%, solo el pie) | ago-2026 |
| Hero de `/publicaciones` (imagen IA con taza STS) **se mantiene** por decisión de David hasta tener foto real de congreso | ago-2026 |

---

## 3. Infraestructura y flujo

- **Repo:** `dlazotorax/lazoweb`, rama `main`. Sitios estáticos sin build en `dist/<dominio>/`.
  **El repo manda**; la carpeta local `Projects/Paginas web` es respaldo y **puede estar desfasada**:
  antes de decir que algo «no está publicado», mirarlo en `dist/`.
- **Token:** `Paginas web/.github-token` (fine-grained, solo lazoweb). **Nunca commitearlo.**
- **Flujo:** clonar fresco → editar → `audit.py` → commit → push a `main`.
- **Vercel Hobby**, 7 proyectos sobre el mismo repo, cada uno con **Ignored Build Step**
  `git diff --quiet HEAD^ HEAD ./` (se ejecuta desde el Root Directory). Un commit a un dominio da
  1 READY + 6 CANCELED; commits a la raíz (`ESTADO.md`, `scripts/`) no despliegan. Tope Hobby: 100
  despliegues/día.
- **CDN:** 40-90 s. Revalidar con `?v=N`. **«Redeploy» del panel no publica código nuevo** (reconstruye
  el mismo commit).
- **`scripts/audit.py`:** anidado HTML, JSON-LD parseable, cada Q/A de `FAQPage` visible, recursos
  locales, GA4 una vez, `title` ≤60 y `description` 120-158 sin duplicados, `@id` canónico. Sale 1 si
  falla. **No detecta problemas de renderizado.**
- **Opérculo:** la fuente es `_design/maquetas/operculo/_build/lienzo-design-v2.dc.html`; se regenera con
  `python3 _design/maquetas/operculo/_build/convert_dc.py --publicar`. **No editar los HTML generados.**

---

## 4. La red

| Dominio | Páginas | Rol |
|---|---|---|
| cirugiatoracica.cl | 6 (`/`, `/perfil`, `/cv`, `/publicaciones`, `/docencia`, `/links`) | Hub |
| rats.cl | 6 (`/` + `/operculo-toracico` y 4 subpáginas) | Médicos referentes |
| cancerpulmonar.cl | 7 | Pacientes |
| broncoscopia.cl | 3 | Dual |
| hiperhidrosis.cl | 16 | Pacientes |
| videotoracoscopia.cl | 1 | VATS |
| vats.cl · cirugiadetorax.cl | 308 → videotoracoscopia.cl · 308 → cirugiatoracica.cl | Redirects |

**39 páginas.** Auditoría en producción (20-sep-2026): 39/39 limpias — sitemaps cuadran, UTF-8 sin BOM,
un `h1`, canonical sin www, 0 JSON-LD inválidos, contenido sin JS, 89 pares FAQ todos visibles,
`robots.txt` y `llms.txt` en los 6. `audit.py` al 22-sep: 0 hallazgos.

**Estándar técnico:**
- Canonical **sin www**; `cleanUrls: true` donde hay subpáginas `.html`; `www` → apex con **308**
  (en Vercel, desmarcar «Redirect apex to www» y cambiar 307 → 308).
- `robots.txt` permite GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-Web, PerplexityBot,
  Google-Extended, Applebot-Extended, CCBot; declara sitemap y `llms.txt`. `llms.txt` del hub dice que
  la fuente de trayectoria es `/cv` y que las cifras de volumen vienen del registro personal del autor.
- `<meta robots>`: `max-snippet:-1, max-image-preview:large, max-video-preview:-1`.
- GA4 `G-X3GX2HCVZL`: aparece **2 veces** por página (loader + config) y está bien.
- `lastReviewed` = fecha del último cambio clínico real (`git log`), no la de hoy. `/links` y
  `/publicaciones` no lo llevan a propósito. `<lastmod>` del sitemap = fecha del cambio de archivo.
- `img { height: auto; }` obligatorio si `<img>` lleva `width`/`height`. WebP en fondos vía `image-set()`.
- Estilo: Arial/Figtree, teal `#0891b2`, navy `#0c1526`, serif `DM Serif Display`.

**`/cv` es la fuente de trayectoria.** `Physician` de las demás páginas apunta a ella con
`subjectOf → /cv#page`; `/perfil` es `mainEntityOfPage`. Enlace visible bajo el bloque de cifras en
5 dominios. Sin datos personales (RUT, nacimiento, correo, móvil).

---

## 5. Identidad — datos canónicos

**Entidad:** `@id` `https://cirugiatoracica.cl/#david-lazo` en todos los `Physician` de la red.
**Nunca crear un `@id` local.** Los datos colgados del `@id` deben coincidir en los 6 dominios
(hiperhidrosis.cl alineado el 20-sep; `hasCredential` omitido ahí porque no está visible).

| Campo | Valor |
|---|---|
| Nombre | **Dr. David Lazo Pérez** · ORCID `0009-0007-0806-6679` |
| Indexación bibliográfica | SciELO `Lazo P` · PubMed **`Lazo P D`** · Elsevier `P. David Lazo`. «Lazo D» en PubMed es su hermano **Diego** (no colisionan) |
| Afiliación vigente | **Clínica Las Condes** (desde ene-2026) + **Hospital Clínico San Borja Arriarán** (desde oct-2022). **MEDS terminó dic-2025** — no presentarla como vigente |
| Formación | Médico-Cirujano PUC (2004) · Cirugía Torácica U. de Chile / INT (2009) · Fellowship Trasplante Pulmonar, H.U. Puerta de Hierro (2010-2011) |
| Cargos internacionales | **Regente por Chile de WABIP** · Director Depto. Cirugía Torácica **ALAT** (2020-2022) · Director **SER** (2016-2019) |
| Docencia | Comité Académico subespecialidad Cirugía de Tórax, **U. Finis Terrae** (vigente) · Director de perfeccionamiento, Postgrado U. de Chile, **2014 – nov 2022** (no vigente) |
| Credenciales | **FACS desde 2020** (`honorificSuffix` en los 6 dominios; visible como «Fellow» en `/perfil`; «miembro del ACS» no aparece en la red, grep 22-sep) · IASLC 2014 · ERS 2015 · ISHLT 2020 · Soc. Cirujanos de Chile 2016 |
| Cifras de volumen (coherentes en toda la red) | **+5.700** cirugías torácicas · **+3.200** EBUS · **+200** RATS · **19 años** |
| Inicios acreditados | **EBUS desde dic-2010** (Workshop EBUS-TBNA, Thoraxklinik Heidelberg, CV 2024 V.12) · **RATS desde 11-jun-2015** (da Vinci Console Surgeon, Orlando, CV 2024 V.29) |
| Publicaciones | **31 = 26 revisadas por pares + 5 resúmenes indexados** (no «31 revisadas»). Ninguna de RATS. Archivo ORCID: `lazo_31_publicaciones.bib` |
| CV | `CV_David_Lazo_2026.docx/.pdf`, 7 págs. **86 congresos, 86/86 fechados**, orden ascendente estricto nov-2003 → jul-2026. **Fuente de fechas: `CV David Lazo 2024 (con fechas).pdf`** |

**Evidencia en fuentes de terceros (abierta en la fuente):**
- Rev Med Clin Condes 2015;26(3):387-392, «Avances en videobroncoscopía», **primer autor**,
  DOI 10.1016/j.rmclc.2015.06.013.
- Rev Chil Enferm Respir 2020;36(2):135-137, DOI 10.4067/S0717-73482020000200135: afiliación declarada
  **Comisión de Broncoscopía y Neumología Intervencionista de la SER**.
- Revista *Vivir Más* (CLC), **mayo 2014**, nota de EBUS. **Citar esta, no la republicación de nov-2017**
  (que borró datos y atribuye mal una cita del paciente).
- Programa del *Sixth International Joint Meeting on Thoracic Surgery* / 30° AIACT, Barcelona,
  20-nov-2024: «David Lazo Pérez (Chile)».
- Diplomado de Cirugía ACS Chile 2024: dos clases (Mediastinitis; Cirugía torácica robótica) como «Dr. David Lazo P., FACS».
- Coordinador de Cirugía, 49° Congreso Chileno de Enfermedades Respiratorias (nov-2016, serchile.cl).
- El resumen «79 casos del primer programa nacional» es el programa del **HCSBA (2022) en hospital
  público**: no respalda su práctica RATS desde 2015.

**Perfiles:**
- LinkedIn bueno: `linkedin.com/in/david-lazo-pérez-7b194748/` (verificado, 1,4K seguidores).
  Duplicado vacío: `/in/david-lazo-272a82317/`. La sesión de Chrome de David abre el **duplicado**.
- Doctoralia: `/perfil/david-rene-lazo-perez-3` (la completa, 0 opiniones) y `/perfil/david-rene-lazo-perez`
  (antigua, 1 opinión). **Total 1, no 58** (dato de origen desconocido: no reusar).
- Instagram `@dr.david.lazo.p` (Metricool brand `6878090`). Cuenta del sitio: `@hiperhidrosis.cl`.
- Search Console: `dr.david.lazo@gmail.com`, que hoy es **`authuser=0`** (`dlazo.torax@` no tiene acceso).

---

## 6. Métricas vigentes (reemplazar en cada medición)

**Search Console — 3 meses al 18-sep-2026** (impr / clics / posición / impresiones en IA de Google):

| Dominio | Impr | Clics | Pos | IA |
|---|---|---|---|---|
| cirugiatoracica.cl | 802 | 18 | 20,6 | 66 |
| rats.cl | 705 | 21 | **6,7** | **153** |
| cancerpulmonar.cl | 690 | 15 | 29,1 | 40 |
| hiperhidrosis.cl | 507 | 5 | 42,2 | 28 |
| videotoracoscopia.cl | 371 | 3 | 7,8 | 34 |
| broncoscopia.cl | 330 | 6 | 13,6 | 49 |
| **Red** | **3.405** | **68** | | **370** |

Hub por página: `/perfil` 331/15/5,9 · `/` 511/3/18,4 · `/cv` 10/0/5,9. «cirugía de tórax» sigue ~80.
Opérculo: indexado solo; consultas anatómicas con 0 clics.

**SERP google.cl (20-sep):** videotoracoscopía Chile **#1** · EBUS Chile **#5** (broncoscopia.cl) ·
cirugía robótica torácica Chile **#3** · «David Lazo cirujano torácico» 4 propios en top 10, MEDS ya no
aparece · cirujano torácico Santiago y cirugía hiperhidrosis Chile: **ausente** (Doctoralia #1 lo nombra).

**IA (13 y 20-sep):** citan rats.cl, el hub y, desde el 20-sep, broncoscopia.cl (nódulo/EBUS).
**Nunca** han citado cancerpulmonar.cl ni hiperhidrosis.cl. Gemini sin sesión: sin medir.

**Fichas (20-sep):** GBP **0 reseñas** (129 vistas/mes) · Doctoralia **1**.

**Instagram (Metricool, 7-sep → 21-sep):** 2.437 seguidores, planos (+4). 4 reels jul-sep, 0 historias.
Cada reel alcanza 440-975 cuentas; entre reels, <15/día.

**GA4:** ~70% del tráfico «Direct» es bot (2 s de interacción). Filtro de bots y conversiones pendientes.

**Diagnóstico:** el on-page está resuelto. El cuello de botella es **autoridad externa** (0 dominios de
terceros enlazan la red). La vía institucional está cerrada (§2). Lo que queda, sin pedir nada a nadie:
**ORCID, Wikidata, fichas propias con reseñas de pacientes, producción indexada con DOI**, y aceptar
que el resto es lento.

---

## 7. Pendientes

### De David

| # | Qué | Nota |
|---|---|---|
| 1 | **ORCID:** borrar el duplicado «Resistencia a ciprofloxacino» (marca 32, son 31) y **cargar la regencia WABIP** | Autoridad externa que controla él entero |
| 2 | **Reseñas de pacientes** en GBP y Doctoralia; **fusionar las 2 fichas de Doctoralia** | Doctoralia es #1 en «cirujano torácico Santiago» |
| 3 | **GA4:** marcar `reserva_presencial` y `reserva_telemedicina` como eventos clave; los 6 dominios en Flujos de datos; filtro de bots | |
| 4 | **LinkedIn:** cerrar el duplicado, URL personalizada del bueno, comprobar desde qué cuenta publica | |
| 5 | **Instagram:** cadencia (≈2 reels/mes + historias), enlace de bio al hub; `@hiperhidrosis.cl`: cambiar el enlace de beacons.page | |
| 6 | GBP: horario y categoría | |
| 7 | Cerrar el convenio → sección de cobertura en hiperhidrosis.cl | Bloqueado por §1.4 hasta entonces |
| 8 | TopDoctors: reactivar («no es posible contactar») | |
| 9 | Vídeo del autor para `rats.cl/operculo-toracico/tratamiento` (irá con `VideoObject`) | En producción |
| 10 | CV: coautores omitidos (#17 lista 4 de 14; #14 4 de 9, «Yévene» → **Yévenes**; #18 falta Clavero JM); nombre completo «AIRE 2024»; #79 MedXpert `[Rel./Mod.]`; revisar roles del CV 2026 contra el 2024 | |
| 11 | Tres dudas del CV: ¿«Osteosíntesis Pared Torácica» (may-2023) = #58? · ¿«Webinar SBCT-GBOT-ALAT» (sep-2021) = #47? · #64: CV dice «3° SRS LATAM, Río» y su post dice «2do… COLCIR» | |
| 12 | Guardar copia del brochure de la V Jornada Clínica Alemana (oct-2023) | Está en un servidor de cursos |

### De Claude

| # | Qué | Nota |
|---|---|---|
| 1 | Verificar si **`/docencia`** entró en Google (indexación solicitada 20-sep). Si a 2-3 semanas sigue fuera: enlazado interno | Revisar ~4-oct |
| 2 | **Medir IA** de nuevo (incluido Gemini sin sesión) para ver efecto de la entidad unificada | |
| 3 | **cancerpulmonar.cl:** FAQ publicadas el 4-sep (7 páginas) y aun así no citado. Propuesta: preguntas quirúrgicas que solo responde un cirujano torácico (operabilidad, lobectomía vs segmentectomía, VATS/RATS en cáncer, recuperación, EBUS en la decisión). Con bibliografía y validación de David | Borrador por hacer |
| 4 | **hiperhidrosis.cl:** decidir si se invierte. Si sí: páginas por **tratamiento** (toxina botulínica, iontoforesis, medicación oral), reescribir `/hiperhidrosis-localizada-leve/` y pasar los 7 posts 2020-21 a registro sobrio (tutean y exclaman). **No ampliar** `/blog/`, `/test…/`, `/`, ni los posts de SC y rubor (§1.4) | Decisión de David |
| 5 | `videotoracoscopia.cl`: único sin `FAQPage`; CTR 0,8% en pos 7,8 → revisar `title`/`description` | |
| 6 | Opérculo: orientar `title`/`description` a intención de paciente (síntomas, tratamiento) | |
| 7 | `/rats-vs-vats` — contenido nuevo | |
| 8 | Acordeón de FAQ en `rubor-facial-patologico` (tiene `FAQPage` visible, falta la interfaz) | |
| 9 | Eyebrows: 7 `class="eyebrow"` en `cirugiatoracica/index.html` (una **es** el `h2` «Enfermedades que tratamos»); familias `cta-/sec-/bio-/hero-/page-nav-eyebrow` sin decidir | Criterio en el histórico |
| 10 | Menores: `url` del `Physician` con/sin barra final (hiperhidrosis vs hub); post SC en `/2020/11/13/` con `datePublished` 2020-11-14 (no tocar sin saber cuál es la buena) | |

---

## 8. Trampas de método

| Trampa | Qué hacer |
|---|---|
| Archivos de la carpeta local desfasados | El repo manda. Verificar en `dist/` antes de afirmar que algo no está publicado |
| Resumen de buscador/IA como fuente | Abrir la fuente primaria (se atribuyó un paper de Bellvitge sin «Lazo»; se inventó una paginación) |
| Cifra propia repetida hasta volverse «dato» | Contar en la fuente (eran 7 notas de CLC, no «unas diez»; eran 1 reseña, no 58) |
| Fechar por la republicación | El CMS muestra la reedición; buscar el original |
| `docx` leído solo con `paragraphs` | Las tablas no están ahí: leer también `tables` |
| Perfil que aparece vacío | Hipótesis por defecto: **duplicado**. Mirar primero qué enlaza ya la red |
| LinkedIn «1 año» | Redondea a la baja (23 meses = «1 año») |
| Método derivado que falla el control | Se descarta, no se calibra contra el resultado deseado |
| WebFetch en redirecciones | Miente (302 por 308). Códigos HTTP: panel de Vercel |
| Duplicación entre dominios | Medir prosa, no HTML (el 46% era CSS) |
| GA4 por `sendBeacon` | Mirar `en=` del último hit `/g/collect` |
| Posición de GSC | La media del dominio ≠ la de la consulta; activar la métrica Posición |
| Instagram sin sesión | Ilegible. Con sesión en Chrome: `/api/v1/feed/user/1486809562/` + `x-ig-app-id`, de 33 en 33, trocear (corte a 45 s). Preferir Metricool |
| Schema vs texto visible | Normalizar acentos y puntuación (`<strong>`/`<a>` meten espacios) |
| Tablas de operabilidad por estadio | Distinguir técnica (prescindible) de condición clínica («con evaluación») |
| Buscar fechas rastreando IG/LinkedIn | No funciona (scroll infinito). **Pedir a David el enlace o la captura** |
| La nota de CLC de 2016 dice «un día de hospitalización» | Hoy es ambulatoria: no reproducir |

---

## 9. Archivos

| Archivo | Para qué |
|---|---|
| `ESTADO.md` | Este documento |
| `ESTADO-historico.md` | Registro cronológico completo y la versión larga de ESTADO al 22-sep-2026 |
| `scripts/audit.py` | Auditoría previa a cada push |
| Carpeta local: `CV_David_Lazo_2026.docx/.pdf`, `CV David Lazo 2024 (con fechas).pdf`, `lazo_31_publicaciones.bib`, `ORCID-*.md`, `apply_orcid.py`, `GBP-servicios.md` | Respaldo y fuentes. **`.github-token`: nunca commitear** |
| Docs del Project en claude.ai (`claude/…`) | Informes fechados: reanálisis, auditorías, decisiones (p. ej. `decision-no-pedir-backlinks.md`) |
