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
| cirugiatoracica.cl | 6 (`/`, `/perfil`, `/cv`, `/publicaciones`, `/docencia`, `/links`) | Hub |
| hiperhidrosis.cl | 16 | Pacientes |
| cancerpulmonar.cl | 7 | Pacientes |
| broncoscopia.cl | 3 | Dual |
| rats.cl | 1 | Médicos referentes |
| videotoracoscopia.cl | 1 | VATS — dominio principal desde jul-2026 |
| vats.cl | 308 → videotoracoscopia.cl | Redirect |
| cirugiadetorax.cl | 308 → cirugiatoracica.cl | Redirect |

**Total: 34 páginas publicadas.**

## 1.b `/cv` — la fuente de trayectoria (publicado 20-ago-2026)

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

> **Pendiente detectado, no tocado:** `broncoscopia/index.html` tiene el mismo problema — dos
> `bio-text` seguidos que repiten "EBUS desde 2010 (+3.200 procedimientos)". Revisar si se repite
> en los otros dominios.

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

### Desde cuándo — fechas exactas de formación por técnica

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

### EBUS — la cadena documental completa (19-ago-2026)

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

### CV 2026 — fechas repobladas (19-ago-2026)

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

### FACS — confirmado por David. Y un error mío de bulto

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

**Arreglo pendiente:** `honorificSuffix: "FACS"` en el `Physician`, y cambiar *"miembro del American
College of Surgeons"* por *"Fellow del American College of Surgeons (FACS), desde 2020"* donde
aparezca visible. También revisar el resto de la tabla del CV por si hay más membresías con fecha
que la red no refleja (ISHLT 2020, IASLC 2014, ERS 2015, Soc. de Cirujanos de Chile 2016).

**Novena pasada — #71, aportada por David.** *2° Curso de Actualización en Cirugía Torácica*,
Clínica MEDS / IMP, Santiago, **26 de julio de 2024** (reel en su Instagram). Encaja en el hueco de
trece días entre el 17° ALAT (10-13 jul) y el Diplomado ACS.

**Décima pasada — #67, aportada por David.** *Curso Internacional de Broncoscopía*, Santiago,
**4 de abril de 2024**, como Director.

## ✅ CV CERRADO: 86 / 86 fechadas · 0 inversiones cronológicas

De **1 entrada con año** a **las 86**, en orden ascendente estricto de **nov-2003 a jul-2026**.
La lista es ahora autoverificable: cualquier fecha futura mal puesta romperá el orden.

### Cómo se resolvieron las 85 (para repetir el método)

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

### LinkedIn: hay DOS perfiles, y el que revisé era el vacío (corregido 19-ago-2026)

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

### No abrir secciones con una sola entrada (19-ago-2026)

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
5. Fechar una nota por su **republicación**. La de EBUS quedó como "22-nov-2017" porque esa es la
   fecha que muestra el blog de CLC. El original es de **mayo de 2014** (revista *Vivir Más*), y lo
   encontró David, no yo. **Antes de fechar una nota, buscar si es una republicación** — el CMS
   muestra la fecha de la reedición, no la de la primera publicación.

**También hay que verificar las fuentes ya verificadas:** la nota de CLC de 2016 dice "un día de
hospitalización" cuando hoy la cirugía es ambulatoria. **No reproducir esa frase.** El error de
atribución de la cita del paciente en la nota de EBUS **solo está en la versión de 2017**; la de
mayo de 2014 es correcta y además más completa.

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
