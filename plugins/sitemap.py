"""
sitemap
~~~~~~~

Plugin mínimo (sin dependencias externas) que genera sitemap.xml y
robots.txt después de que Pelican termina de escribir el sitio.

Se activó un paquete de terceros solo para esto no se justificaba con
dos páginas de contenido, así que va directo con las señales de Pelican.

Solo escribe el sitemap si SITEURL es una URL absoluta (para no generar
un sitemap apuntando a "" durante `pelican -lr` en desarrollo local).
"""

import os

from pelican import signals

_pages = []


def _collect_pages(generator):
    _pages[:] = list(generator.pages)


def _write_sitemap(pelican_object):
    siteurl = pelican_object.settings.get("SITEURL", "").rstrip("/")
    output_path = pelican_object.settings.get("OUTPUT_PATH")

    if not siteurl.startswith("http"):
        return

    urls = [siteurl + "/"]
    for page in _pages:
        if page.url in ("index.html", ""):
            continue  # ya cubierto por la raíz del sitio
        loc = f"{siteurl}/{page.url}"
        if loc not in urls:
            urls.append(loc)

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url in urls:
        xml_lines.append(f"  <url><loc>{url}</loc></url>")
    xml_lines.append("</urlset>")

    with open(os.path.join(output_path, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines) + "\n")

    with open(os.path.join(output_path, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {siteurl}/sitemap.xml\n")


def register():
    signals.page_generator_finalized.connect(_collect_pages)
    signals.finalized.connect(_write_sitemap)
