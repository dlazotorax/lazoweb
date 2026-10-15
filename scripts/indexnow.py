#!/usr/bin/env python3
"""Aviso IndexNow (Bing, Yandex, Seznam, Naver) de las URLs que cambiaron.

Correr DESPUÉS de que Vercel termine de desplegar: el buscador descarga el
archivo de clave desde cada dominio para validar el aviso.

Solo envía URLs que figuran en el sitemap del dominio, así nunca se avisa una
URL no canónica. Los dominios que solo redirigen (vats, cirugiadetorax) no
llevan clave y quedan fuera.

Uso (desde la raíz del repo):
  python3 scripts/indexnow.py                 cambios de HEAD^..HEAD
  python3 scripts/indexnow.py --desde b3f0c89 cambios desde ese commit
  python3 scripts/indexnow.py --todo          todas las URLs de los sitemaps
  python3 scripts/indexnow.py --dry-run       muestra lo que enviaría

Salida: 0 si todos los envíos devolvieron 200/202, 1 si alguno falló.
"""

import argparse
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DIST = REPO / "dist"

CLAVE = "6563e7c4261c09942fb4341c9d6b5312"
ENDPOINT = "https://api.indexnow.org/indexnow"

# Carpeta de dist/ -> host publicado. Mismos dominios que scripts/audit.py.
DOMINIOS = {
    "cirugiatoracica": "cirugiatoracica.cl",
    "hiperhidrosis": "hiperhidrosis.cl",
    "cancerpulmonar": "cancerpulmonar.cl",
    "broncoscopia": "broncoscopia.cl",
    "rats": "rats.cl",
    "videotoracoscopia": "videotoracoscopia.cl",
}


def urls_sitemap(carpeta):
    xml = (DIST / carpeta / "sitemap.xml").read_text(encoding="utf-8")
    return re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)


def ruta_de_archivo(relativa):
    """dist/<d>/a/b/index.html -> /a/b ; x.html -> /x ; index.html -> /"""
    if not relativa.endswith(".html"):
        return None
    ruta = relativa[: -len(".html")]
    if ruta == "index":
        return "/"
    if ruta.endswith("/index"):
        ruta = ruta[: -len("/index")]
    return "/" + ruta


def sin_barra(url_o_ruta):
    return url_o_ruta.rstrip("/") or "/"


def cambiados(desde):
    r = subprocess.run(
        ["git", "diff", "--name-only", desde, "HEAD", "--", "dist/"],
        cwd=REPO, capture_output=True, text=True,
    )
    if r.returncode:
        sys.exit(f"git diff {desde}..HEAD falló: {r.stderr.strip()}")
    return [l for l in r.stdout.splitlines() if l.strip()]


def seleccionar(desde, todo):
    """Devuelve {carpeta: [urls]} solo con URLs presentes en el sitemap."""
    por_dominio = {}
    archivos = [] if todo else cambiados(desde)
    for carpeta, host in DOMINIOS.items():
        locs = urls_sitemap(carpeta)
        if todo:
            elegidas = locs
        else:
            rutas = set()
            prefijo = f"dist/{carpeta}/"
            for f in archivos:
                if f.startswith(prefijo):
                    r = ruta_de_archivo(f[len(prefijo):])
                    if r:
                        rutas.add(sin_barra(r))
            elegidas = [
                u for u in locs
                if sin_barra(u.split(host, 1)[1] or "/") in rutas
            ]
        if elegidas:
            por_dominio[carpeta] = elegidas
    return por_dominio


def enviar(host, urls):
    cuerpo = json.dumps({
        "host": host,
        "key": CLAVE,
        "keyLocation": f"https://{host}/{CLAVE}.txt",
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT, data=cuerpo, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--desde", default="HEAD^", help="commit base (def. HEAD^)")
    p.add_argument("--todo", action="store_true", help="todas las URLs")
    p.add_argument("--dry-run", action="store_true", help="no envía")
    a = p.parse_args()

    for carpeta in DOMINIOS:
        archivo = DIST / carpeta / f"{CLAVE}.txt"
        if not archivo.is_file() or archivo.read_text().strip() != CLAVE:
            sys.exit(f"Falta o no cuadra el archivo de clave: {archivo}")

    seleccion = seleccionar(a.desde, a.todo)
    if not seleccion:
        print("Ninguna URL de sitemap cambió; nada que avisar.")
        return 0

    fallos = 0
    for carpeta, urls in seleccion.items():
        host = DOMINIOS[carpeta]
        print(f"{host}: {len(urls)} URL(s)")
        for u in urls:
            print(f"  {u}")
        if a.dry_run:
            continue
        estado = enviar(host, urls)
        # 200 = aceptado; 202 = recibido, clave pendiente de validar.
        ok = estado in (200, 202)
        print(f"  -> HTTP {estado}{'' if ok else '  FALLO'}")
        fallos += not ok
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
