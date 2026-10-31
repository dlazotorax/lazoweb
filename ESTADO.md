# ESTADO — Red web Dr. David Lazo Pérez

> **Última actualización: 31 oct 2026.** Documento de trabajo: reglas, decisiones, datos canónicos,
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
| cancerpulmonar `/tratamiento`: **«sotorasib en Chile está disponible desde 2024» se queda** tal cual. Respaldo interno (no publicar): LUMAKRAS, ISP `F-28265/24` | 28-sep-2026 |
| cancerpulmonar `/tratamiento`: **sin columna de frecuencias** en la tabla de biomarcadores (14 filas). No reintroducirla | 28-sep-2026 |
| cancerpulmonar.cl: **diseño F2 Índigo + coral** (Bricolage Grotesque + DM Sans, `/estilo.css` compartido). Sin círculos en los hero. El texto existente no se tocó salvo lo pedido por David | 17-oct-2026 |
| cancerpulmonar.cl: **sin cifras en la bio** (+5.700 cirugías, +3.200 EBUS, 19 años) en las 8 páginas. Las frases del párrafo de la bio («19 años de experiencia», «mejores resultados oncológicos», «mayor experiencia en EBUS en Chile» en la portada) **se quedan** | 17-oct-2026 |
| cancerpulmonar `/nodulo-pulmonar`: cirugía de nódulos pequeños **no va aquí**: marcación con lipiodol → videotoracoscopia.cl; con ICG → rats.cl (material reservado en `Paginas web/reservado-cirugia-nodulos.html`). Sin menciones a CLC en el contenido | 17-oct-2026 |
| videotoracoscopia.cl **`/cirugia-nodulo-pulmonar`** (publicada 27-oct-2026): resección (cuña, segmentectomía, lobectomía), localización con lipiodol y, en forma breve, con ICG; FAQ visible. **El ICG en profundidad, con videos, irá en rats.cl** (decisión de David, 27-oct) | 27-oct-2026 |
| rats.cl **`/verde-indocianina`** (publicada 31-oct-2026): portada + `/nodulos`, `/segmentectomia`, `/conducto-toracico`, cada una con su video de YouTube (@david-lazo-torax) que parte solo y sin sonido al llegar a él (API de YouTube + IntersectionObserver). `VideoObject` en nódulos y segmentectomía; `VideoObject` también en conducto torácico. Imágenes propias hechas con Gemini y corregidas (molécula de ICG real, rótulos anatómicos). Fuente: `_design/rats-verde-indocianina/build3.py` (genera los 4 HTML desde la plantilla del opérculo: `python3 _design/rats-verde-indocianina/build3.py . dist/rats/verde-indocianina final`); editar el script, no los HTML | 31-oct-2026 |
| **hiperhidrosis.cl sin HCSBA**: en HCSBA no hay capacidad para operar patología no grave. Afiliación solo CLC en ese dominio (JSON-LD, `llms.txt` y texto); excepción a la coincidencia del `@id` (§5) | 12-oct-2026 |
| Hero de `/publicaciones` (imagen IA con taza STS) **se mantiene** por decisión de David hasta tener foto real de congreso | ago-2026 |
| **Nombre visible: siempre «Dr. David Lazo Pérez»** en títulos, metas, marca, pies, FAQ y `alt`. «el Dr. Lazo» solo como segunda mención en prosa; donde aparece, el `Physician` lleva `"alternateName": "Dr. Lazo"`. Fuentes generadas (opérculo, hiperhidrosis, cancerpulmonar F2) corregidas en `_design/` | 20-oct-2026 |
| broncoscopia.cl: **tipografía y paleta del hub** (Red Hat Display + JetBrains Mono para etiquetas; azul `#1F6FEB`, grafito `#0E1012`, gris `#F4F4F4`). Estructura, fotos y texto sin cambios. Se aplicó con `retipo.py` (copia en la carpeta local `maqueta-broncoscopia/sitio-actual-tipo-a/`). Las maquetas de rediseño A-F de esa carpeta quedaron descartadas | 21-oct-2026 |
| **Barra de red sin hiperhidrosis.cl en cancerpulmonar, broncoscopia y rats** (barra superior y pie; opérculo vía su fuente en `_design/`). Se mantiene en el hub y en videotoracoscopia.cl («no es solo cáncer»). `sameAs` sin cambios. Interlinking contextual: rats.cl → cancerpulmonar `/tratamiento` y `/nodulo-pulmonar`, videotoracoscopia, broncoscopia `/ebus`. Frase «mayor experiencia en EBUS en Chile» de rats.cl se mantiene por decisión de David | 31-oct-2026 |

---

## 3. Infraestructura y flujo

- **Repo:** `dlazotorax/lazoweb`, rama `main`. Sitios estáticos sin build en `dist/<dominio>/`.
  **El repo manda**; la carpeta local `Projects/Paginas web` es respaldo y **puede estar desfasada**:
  antes de decir que algo «no está publicado», mirarlo en `dist/`.
- **Token:** `Paginas web/.github-token` (fine-grained, solo lazoweb). **Nunca commitearlo.**
- **Flujo:** clonar fresco → editar → `audit.py` → commit → push a `main`.
- **Vercel Hobby**, 7 proyectos sobre el mismo repo. Ignored Build Step: **`ignoreCommand` en cada
  `dist/*/vercel.json`: `git diff --quiet ${VERCEL_GIT_PREVIOUS_SHA:-HEAD^} HEAD ./`** (compara contra el
  último despliegue exitoso; sobrescribe el campo del panel), envuelto en `if git cat-file -e …; else exit 1`:
  si ese SHA no está en el clon superficial de Vercel, despliega en vez de fallar (vats falló así el 12-oct).
  Se ejecuta desde el Root Directory. Un commit a un dominio da
  1 READY + 6 CANCELED; commits a la raíz (`ESTADO.md`, `scripts/`) no despliegan. Tope Hobby: 100
  despliegues/día.
- **CDN:** 40-90 s. Revalidar con `?v=N`. **«Redeploy» del panel no publica código nuevo** (reconstruye
  el mismo commit).
- **`scripts/audit.py`:** anidado HTML, JSON-LD parseable, cada Q/A de `FAQPage` visible, recursos
  locales, GA4 una vez, `title` ≤60 y `description` 120-158 sin duplicados, `@id` canónico. Sale 1 si
  falla. **No detecta problemas de renderizado.**
- **Opérculo:** la fuente es `_design/maquetas/operculo/_build/lienzo-design-v2.dc.html`; se regenera con
  `python3 _design/maquetas/operculo/_build/convert_dc.py --publicar`. **No editar los HTML generados.**
- **cancerpulmonar.cl (desde 17-oct-2026):** cada página = `/estilo.css` (diseño F2) + su `<style>` propio acotado a `.lg`
  (contenido antiguo recoloreado). **Se editan los HTML de `dist/` directamente.** Los scripts de la migración
  están en `_design/cancerpulmonar-f2/` solo como referencia (`build3.py` parte de los HTML anteriores).
- **IndexNow** (Bing, Yandex, Seznam, Naver; Google no lo usa): clave `6563e7c4261c09942fb4341c9d6b5312`,
  archivo `<clave>.txt` en la raíz de los 6 dominios con contenido (vats y cirugiadetorax solo redirigen).
  Tras cada push, **cuando Vercel ya desplegó**: `python3 scripts/indexnow.py` (avisa solo URLs del sitemap
  cuyo HTML cambió en `HEAD^..HEAD`; `--desde SHA`, `--todo`, `--dry-run`).
  **Corre desde el Mac de David** (la nube y el shell remoto no tienen salida a `api.indexnow.org`).
  Envío inicial `--todo` el 14-oct-2026: 39 URLs, HTTP 200 en los 6.
- **Bing Webmaster Tools** (cuenta `dr.david.lazo@`): 7 propiedades importadas de Search Console el
  14-oct-2026 (falta cirugiadetorax, solo redirige). Sitemaps de los 6 enviados a mano ese día.

---

## 4. La red

| Dominio | Páginas | Rol |
|---|---|---|
| cirugiatoracica.cl | 6 (`/`, `/perfil`, `/cv`, `/publicaciones`, `/docencia`, `/links`) | Hub |
| rats.cl | 10 (`/` + `/operculo-toracico` y 4 subpáginas + `/verde-indocianina` y 3 subpáginas) | Médicos referentes |
| cancerpulmonar.cl | 8 (incl. `/nodulo-pulmonar`, 17-oct-2026) | Pacientes |
| broncoscopia.cl | 3 | Dual |
| hiperhidrosis.cl | 16 | Pacientes |
| videotoracoscopia.cl | 2 (`/` + `/cirugia-nodulo-pulmonar`, 27-oct-2026) | VATS |
| vats.cl · cirugiadetorax.cl | 308 → videotoracoscopia.cl · 308 → cirugiatoracica.cl | Redirects |

**45 páginas** (desde 31-oct-2026). Auditoría en producción (20-sep-2026): 39/39 limpias — sitemaps cuadran, UTF-8 sin BOM,
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
- Estilo: Arial/Figtree, teal `#0891b2`, navy `#0c1526`, serif `DM Serif Display`. **Excepción: broncoscopia.cl** (desde 21-oct-2026) usa el sistema del hub: Red Hat Display + JetBrains Mono, azul `#1F6FEB`, grafito `#0E1012`. **Excepción: rats.cl** (portada y
  opérculo) usa el sistema editorial del opérculo: Bebas Neue + Public Sans, hueso `#F6F5F1`, negro `#0B0B0B`.
  Acento: portada teal azul `#0E7490` (`#67D3E8` sobre negro); opérculo óxido `#C4500E`.

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

Detalle de esta medición: doc del Project `claude/posicionamiento-revision-2026-10-22.md`.

**Search Console — 3 meses al 23-oct-2026** (24-jul → 23-oct; impr / clics / posición). Medido 25-oct.
IA de Google no se volvió a medir (última: 20-oct, 1.815 en la red). GSC redondea sobre 1.000.

| Dominio | Impr | Clics | Pos |
|---|---|---|---|
| cancerpulmonar.cl | ~3.950 | 50 | 13,4 |
| rats.cl | ~2.800 | 45 | **5,6** |
| cirugiatoracica.cl | ~1.250 | 52 | 9,8 |
| broncoscopia.cl | ~1.060 | 23 | 9,1 |
| videotoracoscopia.cl | 807 | 10 | 6,8 |
| hiperhidrosis.cl | 668 | 8 | 36,4 |
| **Red** | **~10.540** | **188** | |

(20-oct: ~9.630 / 174.) (18-sep: 3.405 / 68 / IA 370.) Crecimiento por cancerpulmonar `/sobrevida`+`/etapificacion` y por el opérculo.
Hub por página: `/perfil` 614/37/5,4 · `/` 755/4/13,9. «cirugía de tórax» sigue ~84; «hiperhidrosis» ~82.
**Cuello de botella = CTR:** «adenocarcinoma pulmonar sobrevida» 242 impr pos 6,2 **0 clics** · «videotoracoscopia»
278 pos 6,0 2 clics · «ebus» 219 pos 7,9 2 clics · «operculo toracico» 110 pos 11,9 0 clics.

**SERP google.cl (25-oct, `pws=0`):** videotoracoscopía Chile **#1** · cirugía robótica torácica Chile **#2** (oncotorax #1) ·
EBUS Chile **#5** · adenocarcinoma pulmonar sobrevida **#3** (22-oct: AI Overview lo nombra en EBUS) · «David Lazo cirujano torácico» 5 de 9 propios, sin MEDS ·
cirujano torácico Santiago y cirugía hiperhidrosis Chile: **ausente**. Títulos aún sin «Pérez» (recrawl pendiente).

**IA (22-oct), categoría / marca:** ChatGPT **sin sesión** 4/6 · 3/3 · Perplexity con sesión 4/6 · 3/3 · Modo IA
con sesión 3/6 · 3/3 · Gemini Flash con sesión 2/6 · 3/3 (5-sep: 3/6; pierde cáncer de pulmón). Cáncer de pulmón entra en ChatGPT (vía Doctoralia) y
Perplexity (vía hub). Hiperhidrosis y trasplante: ausente en todos. «Primer programa sistemático de RATS» y
«mayor experiencia del país» se reproducen literal desde la bio de rats.cl (l. 630). MEDS residual en Modo IA
y Perplexity, desde contenido de MEDS. ChatGPT cita un trabajo «16 pacientes HCSBA dic-2022–jul-2023» que no
está en la red: **no reutilizar sin abrir la fuente**.

**Fichas (22-oct):** GBP **0 reseñas** (142 vistas/mes) · Doctoralia **1** (dos fichas).

**Instagram (Metricool, 22-sep → 21-oct):** 2.443 seguidores (+6 en un mes). 2 reels, 0 historias, 0 feed.
Alcance medio por reel 827; entre reels 2-21 cuentas/día.

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
| 13 | cancerpulmonar `/sobrevida`, bloque «El impacto del diagnóstico precoz»: «más del 60 % de los cánceres pulmonares en Chile se diagnostican en estadio III o IV» **no tiene fuente**. ¿Retirar o dar fuente? | No tocar hasta que decida (§1.1) |
| 14 | ¿Añadir en `/sobrevida` la tabla de sobrevida **patológica** 9.ª ed. (Rami-Porta 2024, Fig. 4)? Cifras en `ESTADO-historico.md` §19 | Por defecto no; tabla aparte si la pide |
| 15 | `/nodulo-pulmonar`, por confirmar: licencia de las figuras de Vega 2021 (SciELO); que los casos de las láminas 20/22 son suyos; origen de las miniaturas de bordes (lámina 13) | Publicada el 17-oct con ellas |

### De Claude

| # | Qué | Nota |
|---|---|---|
| 1 | **cancerpulmonar.cl:** reindexación de 4 páginas solicitada el 12-oct | Verificar |
| 2 | **CTR:** `title`/`description` de cancerpulmonar `/sobrevida`, broncoscopia `/ebus`, videotoracoscopia `/` y rats `/operculo-toracico` (página 1, 200+ impr, 0-2 clics). Maqueta para David antes de publicar | Medición 22-oct. Absorbe el antiguo nº 5 y nº 6 |
| 2b | Próxima medición IA: Modo IA y Gemini **sin sesión**. Gemini con el panel oculto tarda 2-3 min/respuesta y parte del texto va en nodos que `innerText` de `main` no lee: recorrer shadow DOM | |
| 3 | **cancerpulmonar.cl:** FAQ publicadas el 4-sep (7 páginas) y aun así no citado. Propuesta: preguntas quirúrgicas que solo responde un cirujano torácico (operabilidad, lobectomía vs segmentectomía, VATS/RATS en cáncer, recuperación, EBUS en la decisión). Con bibliografía y validación de David | Borrador por hacer |
| 4 | **hiperhidrosis.cl:** decidir si se invierte. Si sí: páginas por **tratamiento** (toxina botulínica, iontoforesis, medicación oral), reescribir `/hiperhidrosis-localizada-leve/` y pasar los 7 posts 2020-21 a registro sobrio (tutean y exclaman). **No ampliar** `/blog/`, `/test…/`, `/`, ni los posts de SC y rubor (§1.4) | Decisión de David |
| 5 | `videotoracoscopia.cl` portada: sin `FAQPage` (la subpágina `/cirugia-nodulo-pulmonar` ya lo tiene) | |
| 7 | `/rats-vs-vats` — contenido nuevo | |
| 8 | Acordeón de FAQ en `rubor-facial-patologico` (tiene `FAQPage` visible, falta la interfaz) | |
| 9 | Eyebrows: 7 `class="eyebrow"` en `cirugiatoracica/index.html` (una **es** el `h2` «Enfermedades que tratamos»); familias `cta-/sec-/bio-/hero-/page-nav-eyebrow` sin decidir | Criterio en el histórico |
| 10 | Menores: `url` del `Physician` con/sin barra final (hiperhidrosis vs hub); post SC en `/2020/11/13/` con `datePublished` 2020-11-14 (no tocar sin saber cuál es la buena) | |

El antiguo nº 1 (`/docencia` en Google) se cerró el 12-oct-2026: indexada.

El antiguo nº 11 (cancerpulmonar.cl tras NCCN v9.2026) se cerró completo el 28-sep-2026: sobrevida con las
cifras reales de la 9.ª ed. (Rami-Porta 2024, DOI 10.1016/j.jtho.2024.02.011), sotorasib y columna de
frecuencias por decisión de David (§2; la tabla tenía 14 filas, no 11). Detalle en `ESTADO-historico.md` §19.

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
