#!/usr/bin/env python3
"""Auditoría de la red de sitios del Dr. David Lazo.

Comprueba, sobre las páginas publicadas de dist/<dominio>/:

  1. HTML bien anidado (pila de etiquetas, con lista de elementos void).
  2. Todo bloque JSON-LD parsea con json.loads.
  3. Cada pregunta y respuesta de cada FAQPage aparece en el texto visible.
  4. Ningún recurso local roto (src/href relativos apuntan a archivos que existen).
  5. G-X3GX2HCVZL presente exactamente una vez por página.
  6. title <= 60, description entre 120 y 158, sin duplicados.
  7. @id canónico presente y sin @id locales alternativos.

Uso:  python3 scripts/audit.py            (desde la raíz del repo)
      python3 scripts/audit.py --verbose

Salida: código 0 si todo pasa, 1 si hay algún fallo.
"""

import argparse
import html as htmllib
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DIST = REPO / "dist"

# Dominios publicados. dist/index.html es la "Vista General" y no se publica
# (los roots de Vercel son dist/<dominio>), por eso queda fuera.
DOMINIOS = [
    "cirugiatoracica",
    "hiperhidrosis",
    "cancerpulmonar",
    "broncoscopia",
    "rats",
    "videotoracoscopia",
]

GA4_ID = "G-X3GX2HCVZL"
ID_CANONICO = "https://cirugiatoracica.cl/#david-lazo"

# Elementos sin etiqueta de cierre. La lista del encargo (meta, link, img, br,
# hr, input, source, path, circle, rect, use, col, area) más el resto de voids
# de HTML y las formas de SVG que también son vacías por definición.
VOID = {
    "meta", "link", "img", "br", "hr", "input", "source",
    "path", "circle", "rect", "use", "col", "area",
    "base", "embed", "param", "track", "wbr",
    "line", "polyline", "polygon", "ellipse", "stop",
}

# Etiquetas cuyo contenido no es texto visible.
NO_VISIBLE = {"script", "style", "noscript", "template"}


def normalizar(texto):
    """Minúsculas, sin acentos, espacios colapsados. Para comparar textos."""
    texto = htmllib.unescape(texto or "")
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    # Unifica los distintos guiones y comillas que se mezclan en el HTML.
    texto = texto.replace("—", "-").replace("–", "-").replace("‑", "-")
    texto = texto.replace("“", '"').replace("”", '"')
    texto = texto.replace("‘", "'").replace("’", "'").replace(" ", " ")
    return re.sub(r"\s+", " ", texto).strip().lower()


def sin_etiquetas(texto):
    return re.sub(r"<[^>]+>", " ", texto or "")


def solo_palabras(texto):
    """Normaliza y descarta la puntuación, dejando solo palabras y espacios.

    Necesario para comparar el texto del schema con el visible: en la página
    el texto viene partido por etiquetas (<strong>, <a>…), lo que introduce
    espacios sueltos junto a comas y puntos que no existen en el JSON-LD.
    """
    limpio = normalizar(texto)
    limpio = re.sub(r"[^0-9a-zñ ]+", " ", limpio)
    return re.sub(r"\s+", " ", limpio).strip()


class Anidado(HTMLParser):
    """Verifica el anidado con una pila. Reporta el primer desajuste."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pila = []
        self.errores = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.pila.append((tag, self.getpos()))

    def handle_startendtag(self, tag, attrs):
        pass  # <tag /> se abre y cierra en el sitio.

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.pila:
            self.errores.append(f"</{tag}> de más en línea {self.getpos()[0]}")
            return
        if self.pila[-1][0] == tag:
            self.pila.pop()
            return
        # Puede cerrar una etiqueta más abajo en la pila: todo lo que quede
        # por encima está sin cerrar.
        for i in range(len(self.pila) - 1, -1, -1):
            if self.pila[i][0] == tag:
                sueltas = [t for t, _ in self.pila[i + 1:]]
                self.errores.append(
                    f"</{tag}> en línea {self.getpos()[0]} cierra sobre "
                    f"etiquetas sin cerrar: {', '.join(sueltas)}"
                )
                del self.pila[i:]
                return
        self.errores.append(f"</{tag}> sin apertura en línea {self.getpos()[0]}")


class TextoVisible(HTMLParser):
    """Extrae el texto visible: fuera de script, style, noscript y template."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.trozos = []
        self.ocultar = 0

    def handle_starttag(self, tag, attrs):
        if tag in NO_VISIBLE:
            self.ocultar += 1

    def handle_endtag(self, tag):
        if tag in NO_VISIBLE and self.ocultar:
            self.ocultar -= 1

    def handle_data(self, data):
        if not self.ocultar:
            self.trozos.append(data)

    def texto(self):
        return " ".join(self.trozos)


def paginas():
    encontradas = []
    for dominio in DOMINIOS:
        raiz = DIST / dominio
        if raiz.is_dir():
            encontradas.extend(sorted(raiz.rglob("*.html")))
    return encontradas


def bloques_jsonld(contenido):
    """Devuelve [(texto_bruto, objeto_o_None, error_o_None), ...]."""
    patron = re.compile(
        r'<script[^>]+type\s*=\s*["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        re.S | re.I,
    )
    salida = []
    for bruto in patron.findall(contenido):
        try:
            salida.append((bruto, json.loads(bruto), None))
        except json.JSONDecodeError as exc:
            salida.append((bruto, None, str(exc)))
    return salida


def recorrer(nodo):
    """Recorre recursivamente dicts y listas del JSON-LD."""
    if isinstance(nodo, dict):
        yield nodo
        for valor in nodo.values():
            yield from recorrer(valor)
    elif isinstance(nodo, list):
        for item in nodo:
            yield from recorrer(item)


def tipos(nodo):
    t = nodo.get("@type")
    if isinstance(t, str):
        return {t}
    if isinstance(t, list):
        return {x for x in t if isinstance(x, str)}
    return set()


def resolver_recurso(pagina, destino):
    """Resuelve un src/href relativo a un archivo del repo.

    Con cleanUrls activo, /perfil sirve perfil.html y /links sirve
    links/index.html, así que se prueban las tres formas.
    """
    destino = destino.split("#")[0].split("?")[0]
    if not destino:
        return True
    if re.match(r"^(https?:)?//", destino) or destino.startswith(
        ("mailto:", "tel:", "data:", "javascript:", "#")
    ):
        return True

    raiz_dominio = pagina
    while raiz_dominio.parent != DIST:
        raiz_dominio = raiz_dominio.parent
    raiz_dominio = raiz_dominio if raiz_dominio.is_dir() else pagina.parent

    for dominio in DOMINIOS:
        if str(pagina.relative_to(DIST)).startswith(dominio + "/"):
            raiz_dominio = DIST / dominio
            break

    base = raiz_dominio if destino.startswith("/") else pagina.parent
    limpio = destino.lstrip("/")
    if not limpio:
        return True

    candidatos = [
        base / limpio,
        base / (limpio + ".html"),
        base / limpio / "index.html",
    ]
    return any(c.exists() for c in candidatos)


def auditar(verbose=False):
    fallos = []
    avisos = []
    titles = {}
    descripciones = {}
    archivos = paginas()

    if not archivos:
        print("No se encontró ninguna página en dist/. ¿Estás en la raíz del repo?")
        return 1

    for pagina in archivos:
        rel = pagina.relative_to(REPO)
        contenido = pagina.read_text(encoding="utf-8", errors="replace")

        # 1. Anidado
        parser = Anidado()
        try:
            parser.feed(contenido)
            parser.close()
        except Exception as exc:  # noqa: BLE001
            fallos.append(f"[anidado] {rel}: el parser falló: {exc}")
        else:
            for error in parser.errores:
                fallos.append(f"[anidado] {rel}: {error}")
            sueltas = [t for t, _ in parser.pila if t not in ("html", "body", "head")]
            if sueltas:
                fallos.append(f"[anidado] {rel}: sin cerrar: {', '.join(sueltas)}")

        # 2. JSON-LD parsea
        bloques = bloques_jsonld(contenido)
        for _, objeto, error in bloques:
            if error:
                fallos.append(f"[json-ld] {rel}: no parsea: {error}")

        # Texto visible, para los chequeos 3 y 7
        extractor = TextoVisible()
        try:
            extractor.feed(contenido)
            extractor.close()
        except Exception:  # noqa: BLE001
            pass
        visible = solo_palabras(extractor.texto())

        # 3. FAQPage con contenido visible
        for _, objeto, error in bloques:
            if error or objeto is None:
                continue
            for nodo in recorrer(objeto):
                if "FAQPage" not in tipos(nodo):
                    continue
                preguntas = nodo.get("mainEntity") or []
                if isinstance(preguntas, dict):
                    preguntas = [preguntas]
                for pregunta in preguntas:
                    if not isinstance(pregunta, dict):
                        continue
                    nombre = solo_palabras(sin_etiquetas(pregunta.get("name", "")))
                    if nombre and nombre not in visible:
                        fallos.append(
                            f"[faq] {rel}: la pregunta no está visible: "
                            f"«{pregunta.get('name', '')[:70]}»"
                        )
                    respuesta = pregunta.get("acceptedAnswer") or {}
                    if isinstance(respuesta, list):
                        respuesta = respuesta[0] if respuesta else {}
                    cuerpo = solo_palabras(sin_etiquetas(respuesta.get("text", "")))
                    if cuerpo and cuerpo not in visible:
                        fallos.append(
                            f"[faq] {rel}: la respuesta no está visible: "
                            f"«{sin_etiquetas(respuesta.get('text', ''))[:70]}…»"
                        )

        # 4. Recursos locales
        for atributo, valor in re.findall(
            r'\b(src|href)\s*=\s*["\']([^"\']+)["\']', contenido, re.I
        ):
            if not resolver_recurso(pagina, valor):
                fallos.append(f"[recurso] {rel}: {atributo}=\"{valor}\" no existe")

        # También srcset, que lleva varias URLs.
        for valor in re.findall(r'\bsrcset\s*=\s*["\']([^"\']+)["\']', contenido, re.I):
            for parte in valor.split(","):
                url = parte.strip().split(" ")[0]
                if url and not resolver_recurso(pagina, url):
                    fallos.append(f"[recurso] {rel}: srcset \"{url}\" no existe")

        # 5. GA4 instalado exactamente una vez.
        # El snippet estándar nombra el ID dos veces —en el src del loader y en
        # gtag('config', …)— así que lo que debe ser único es cada una de esas
        # dos piezas, no la cadena suelta.
        loaders = len(re.findall(r"gtag/js\?id=" + re.escape(GA4_ID), contenido))
        configs = len(
            re.findall(
                r"gtag\s*\(\s*['\"]config['\"]\s*,\s*['\"]" + re.escape(GA4_ID) + r"['\"]",
                contenido,
            )
        )
        if loaders != 1 or configs != 1:
            fallos.append(
                f"[ga4] {rel}: {loaders} loader(s) y {configs} config(s) "
                f"de {GA4_ID} (debe ser 1 y 1)"
            )

        # 6. title y description
        m = re.search(r"<title[^>]*>(.*?)</title>", contenido, re.S | re.I)
        if not m:
            fallos.append(f"[title] {rel}: falta <title>")
        else:
            titulo = htmllib.unescape(re.sub(r"\s+", " ", m.group(1)).strip())
            if len(titulo) > 60:
                fallos.append(f"[title] {rel}: {len(titulo)} caracteres (máx 60): «{titulo}»")
            titles.setdefault(titulo, []).append(str(rel))

        m = re.search(
            r'<meta[^>]+name\s*=\s*["\']description["\'][^>]*content\s*=\s*["\']([^"\']*)["\']',
            contenido, re.I,
        )
        if not m:
            fallos.append(f"[description] {rel}: falta meta description")
        else:
            desc = htmllib.unescape(re.sub(r"\s+", " ", m.group(1)).strip())
            if not (120 <= len(desc) <= 158):
                fallos.append(
                    f"[description] {rel}: {len(desc)} caracteres (debe ser 120-158)"
                )
            descripciones.setdefault(desc, []).append(str(rel))

        # og/twitter sincronizados con title y description
        def meta_prop(patron):
            m2 = re.search(patron, contenido, re.I)
            return htmllib.unescape(re.sub(r"\s+", " ", m2.group(1)).strip()) if m2 else None

        titulo_actual = (
            htmllib.unescape(
                re.sub(r"\s+", " ", re.search(r"<title[^>]*>(.*?)</title>", contenido, re.S | re.I).group(1)).strip()
            )
            if re.search(r"<title[^>]*>(.*?)</title>", contenido, re.S | re.I)
            else None
        )
        for etiqueta, patron in (
            ("og:title", r'<meta[^>]+property\s*=\s*["\']og:title["\'][^>]*content\s*=\s*["\']([^"\']*)["\']'),
            ("twitter:title", r'<meta[^>]+name\s*=\s*["\']twitter:title["\'][^>]*content\s*=\s*["\']([^"\']*)["\']'),
        ):
            valor = meta_prop(patron)
            if valor is not None and titulo_actual is not None and valor != titulo_actual:
                avisos.append(f"[sync] {rel}: {etiqueta} no coincide con <title>")

        desc_actual = meta_prop(
            r'<meta[^>]+name\s*=\s*["\']description["\'][^>]*content\s*=\s*["\']([^"\']*)["\']'
        )
        for etiqueta, patron in (
            ("og:description", r'<meta[^>]+property\s*=\s*["\']og:description["\'][^>]*content\s*=\s*["\']([^"\']*)["\']'),
            ("twitter:description", r'<meta[^>]+name\s*=\s*["\']twitter:description["\'][^>]*content\s*=\s*["\']([^"\']*)["\']'),
        ):
            valor = meta_prop(patron)
            if valor is not None and desc_actual is not None and valor != desc_actual:
                avisos.append(f"[sync] {rel}: {etiqueta} no coincide con la description")

        # 7. @id canónico
        ids_persona = set()
        hay_physician = False
        for _, objeto, error in bloques:
            if error or objeto is None:
                continue
            for nodo in recorrer(objeto):
                t = tipos(nodo)
                if {"Physician", "Person"} & t:
                    hay_physician = True
                    nid = nodo.get("@id")
                    if nid:
                        ids_persona.add(nid)
                nid = nodo.get("@id")
                if isinstance(nid, str) and nid.endswith("#david-lazo"):
                    ids_persona.add(nid)
        for nid in ids_persona:
            if nid != ID_CANONICO:
                fallos.append(
                    f"[@id] {rel}: @id local «{nid}» (debe ser {ID_CANONICO})"
                )
        if hay_physician and ID_CANONICO not in ids_persona:
            fallos.append(f"[@id] {rel}: nodo Physician/Person sin el @id canónico")

        if verbose:
            print(f"  revisada {rel}")

    # Duplicados
    for titulo, donde in titles.items():
        if len(donde) > 1:
            fallos.append(f"[duplicado] title repetido en {', '.join(donde)}: «{titulo}»")
    for desc, donde in descripciones.items():
        if len(donde) > 1:
            fallos.append(f"[duplicado] description repetida en {', '.join(donde)}")

    print(f"Auditadas {len(archivos)} páginas de {len(DOMINIOS)} dominios.\n")
    if avisos:
        print(f"AVISOS ({len(avisos)}):")
        for aviso in avisos:
            print(f"  · {aviso}")
        print()
    if fallos:
        print(f"FALLOS ({len(fallos)}):")
        for fallo in fallos:
            print(f"  ✗ {fallo}")
        return 1
    print("Todo correcto.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()
    sys.exit(auditar(verbose=args.verbose))
