# lazoweb — red de sitios del Dr. David Lazo Pérez

Monorepo de la red de dominios de cirugía torácica. **Sitios estáticos, sin build.**

## Léeme primero

**`ESTADO.md`** es el documento de referencia del proyecto: infraestructura, qué ya está
hecho, qué está pendiente, decisiones tomadas y los datos canónicos de identidad.
Consúltalo antes de proponer cualquier cambio — evita rehacer trabajo ya resuelto.

## Estructura

```
dist/<dominio>/     ← lo único que se publica. Un proyecto de Vercel por carpeta.
ESTADO.md           ← estado del proyecto (leer primero)
chats/              ← transcripciones del diseño original (histórico)
_design/            ← borradores sueltos (no se publica)
```

## Dominios

| Carpeta | Dominio | Rol |
|---|---|---|
| `cirugiatoracica` | cirugiatoracica.cl | Hub principal (+ `/perfil`, `/publicaciones`, `/links`) |
| `rats` | rats.cl | Cirugía robótica torácica |
| `cancerpulmonar` | cancerpulmonar.cl | Cáncer pulmonar (7 páginas) |
| `broncoscopia` | broncoscopia.cl | Broncoscopía intervencional |
| `hiperhidrosis` | hiperhidrosis.cl | Hiperhidrosis (16 páginas) |
| `videotoracoscopia` | videotoracoscopia.cl | VATS |
| `vats` | vats.cl | Redirige 308 → videotoracoscopia.cl |
| `cirugiadetorax` | cirugiadetorax.cl | Redirige 308 → cirugiatoracica.cl |

## Despliegue

Push a `main` = despliegue automático en Vercel. Un proyecto por carpeta, con
Root Directory = `dist/<carpeta>`. La propagación del CDN toma entre 40 y 90 segundos.

**La configuración del panel de Vercel gana sobre el `vercel.json` del repo.**

## Reglas que no se negocian

- **Contenido médico (YMYL).** Nunca publicar una autoría, cifra, credencial o afiliación
  sin abrirla en su fuente primaria. Ver la regla completa en `ESTADO.md` §6.
- **Todo `FAQPage` debe tener su contenido visible** en la página. Nunca marcado oculto.
- **`@id` único de la entidad:** `https://cirugiatoracica.cl/#david-lazo` en toda la red.
- **Canonical sin `www` y sin barra final.**
- **Sin claims de ranking.** Las cifras de volumen sí se conservan.
