#!/usr/bin/env python3
"""Sincroniza <lastmod> de los sitemaps con la fecha real de cambio de cada HTML.

Regla (Google, «Build and submit a sitemap»): lastmod = fecha del último cambio
significativo (contenido, datos estructurados o enlaces). Aquí se toma la fecha
del último commit que tocó el archivo; si el archivo tiene cambios sin commitear,
la fecha de hoy (así el commit que se está preparando queda bien fechado).

Uso:
  python3 scripts/lastmod.py          # corrige los sitemaps en dist/*/sitemap.xml
  python3 scripts/lastmod.py --check  # solo informa; sale 1 si hay desfases
audit.py llama a desfases() y lo trata como fallo.
"""
import datetime
import os
import re
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(RAIZ, "dist")
DOMINIOS = {
    "cirugiatoracica": "cirugiatoracica.cl",
    "rats": "rats.cl",
    "cancerpulmonar": "cancerpulmonar.cl",
    "broncoscopia": "broncoscopia.cl",
    "hiperhidrosis": "hiperhidrosis.cl",
    "videotoracoscopia": "videotoracoscopia.cl",
}
BLOQUE = re.compile(r"(<url>\s*<loc>)([^<]+)(</loc>\s*<lastmod>)([^<]+)(</lastmod>)")


def archivo_de(carpeta, host, loc):
    ruta = loc.split(host, 1)[1].split("#")[0].split("?")[0].lstrip("/")
    base = os.path.join(DIST, carpeta)
    candidatos = ["index.html"] if ruta == "" else [
        ruta, ruta + ".html", ruta.rstrip("/") + "/index.html", ruta.rstrip("/") + ".html"]
    for c in candidatos:
        f = os.path.join(base, c)
        if os.path.isfile(f):
            return f
    return None


def fecha_de(archivo):
    rel = os.path.relpath(archivo, RAIZ)
    sucio = subprocess.run(["git", "-C", RAIZ, "status", "--porcelain", "--", rel],
                           capture_output=True, text=True).stdout.strip()
    if sucio:
        return datetime.date.today().isoformat()
    return subprocess.run(["git", "-C", RAIZ, "log", "-1", "--format=%cs", "--", rel],
                          capture_output=True, text=True).stdout.strip()


def recorrer(corregir):
    desfases = []
    for carpeta, host in DOMINIOS.items():
        ruta_sm = os.path.join(DIST, carpeta, "sitemap.xml")
        with open(ruta_sm, encoding="utf-8") as fh:
            xml = fh.read()

        def cambiar(m):
            loc, actual = m.group(2), m.group(4)
            archivo = archivo_de(carpeta, host, loc)
            if not archivo:
                desfases.append(f"{loc}: sin archivo en dist/")
                return m.group(0)
            real = fecha_de(archivo)
            if real and real != actual:
                desfases.append(f"{loc}: lastmod {actual} ≠ cambio real {real}")
                if corregir:
                    return m.group(1) + loc + m.group(3) + real + m.group(5)
            return m.group(0)

        nuevo = BLOQUE.sub(cambiar, xml)
        if corregir and nuevo != xml:
            with open(ruta_sm, "w", encoding="utf-8") as fh:
                fh.write(nuevo)
    return desfases


def desfases():
    return recorrer(corregir=False)


if __name__ == "__main__":
    solo_revisar = "--check" in sys.argv
    lista = recorrer(corregir=not solo_revisar)
    for linea in lista:
        print(("  ✗ " if solo_revisar else "  ✓ corregido: ") + linea)
    print(f"{len(lista)} desfases" + ("" if solo_revisar else " corregidos"))
    sys.exit(1 if (solo_revisar and lista) else 0)
