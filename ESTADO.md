# ESTADO — Red web Dr. David Lazo Pérez

> **Léeme primero.** Este archivo evita proponer cosas ya hechas o rehacer trabajo.
> Última actualización: **25 jul 2026**.

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

## 3. PENDIENTE DE VERDAD

| # | Qué | De quién |
|---|---|---|
| 1 | **Fusionar las 2 fichas de Doctoralia** (`-3/…/santiago` y `/…/las-condes`) — reseñas partidas; Doctoralia es el resultado #1 en "cirujano torácico Santiago" | David |
| 2 | **GBP: falta teléfono y horario** (lo dice Google en el panel) | David |
| 3 | **ORCID: keywords y país vacíos** (2 min) | David |
| 4 | `/rats-vs-vats` — mejor apuesta de contenido nuevo | Claude |
| 5 | `dist/uploads/` — 47 archivos basura (copias viejas). No se publica (404), pero conviene limpiar | Claude |
| 6 | CV: corregir coautores omitidos (ver §6) | David |

---

## 4. DIAGNÓSTICO — el cuello de botella real

**No es indexación, no es estructura. Es autoridad.**

Datos de Search Console (jul-2026, 3 meses):

| | broncoscopia.cl | hiperhidrosis.cl |
|---|---|---|
| Impresiones | 37 | 75 |
| **Clics** | **0** | **0** |
| **Posición media** | **18,9** (pág. 2) | **42** (pág. 4-5) |
| Consultas | 6 | 22 |

- Toda la red **está indexada** (verificado con `site:` en Google).
- La consulta #1 de broncoscopia es **"david lazo"** → solo te encuentra quien ya te conoce.
- hiperhidrosis capta la demanda correcta ("sudor compensatorio", "rubor facial") pero en posición 42.
- Los datos de hiperhidrosis parten el **4/7/26**, con la migración a Vercel. **No vemos su historial previo** — revisar en ago-2026 si la migración costó posiciones.

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
