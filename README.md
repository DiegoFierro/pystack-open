# PyStack Open

Sitio del curso **PyStack Open**: un programa práctico para construir
aplicaciones Full Stack (Web, Móvil y Desktop) usando exclusivamente el
ecosistema de Python (Django, FastAPI, HTMX, Flet).

El sitio en sí también sigue esa filosofía: es un sitio estático generado
con **[Pelican](https://getpelican.com/)**, sin build step de JavaScript ni
frameworks de frontend.

🔗 **Sitio publicado:** https://diegofierro.github.io/pystack-open/

## Requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) para manejar el entorno y las dependencias

## Desarrollo local

```bash
uv sync                              # instala Pelican y dependencias
uv run pelican --listen -r           # sirve el sitio en localhost:8000 y reconstruye al guardar
```

Para simular el build de producción (el que corre en CI, con dominio absoluto,
feed y sitemap):

```bash
uv run pelican content -s publishconf.py -o output
```

## Estructura del proyecto

```
content/
  pages/
    index.md              → página de inicio
    syllabus.md            → índice del syllabus (intro + listado dinámico de módulos)
    syllabus/
      modulo-00.md          → un módulo por archivo, con metadata Order/Summary
      modulo-01.md
      ...
    404.md                  → página de error 404 (Status: hidden)

theme/pystack/              → tema propio (sin dependencias de terceros)
  templates/
    base.html                → layout compartido: header, footer, meta tags
    page.html                → template genérico de página (Inicio)
    syllabus.html             → arma el índice de módulos a partir de `pages`
    modulo.html                → template de cada módulo, con breadcrumb y pager
    error404.html              → template de la página 404
  static/
    css/style.css              → todo el CSS del sitio
    img/favicon.svg

plugins/                    → plugins propios de Pelican, sin dependencias externas
  sitemap.py                 → genera sitemap.xml y robots.txt en el build de producción
  module_nav.py               → ordena los módulos del syllabus y arma prev/next

pelicanconf.py               → configuración de desarrollo (SITEURL vacío)
publishconf.py                → configuración de producción (dominio absoluto, feed, sitemap)
.github/workflows/deploy.yml   → build y deploy a GitHub Pages en cada push a main
```

## Cómo agregar o editar un módulo del syllabus

Cada módulo es un archivo Markdown independiente en `content/pages/syllabus/`.
No hay que tocar ninguna plantilla ni ningún índice a mano: el listado en
`/syllabus.html` y la navegación anterior/siguiente se generan solos a partir
de la metadata.

```
Title: Módulo 13: Título del módulo
Date: 2026-09-02
Slug: modulo-13
Save_as: syllabus/modulo-13.html
URL: syllabus/modulo-13.html
Template: modulo
Order: 13
Summary: Una línea describiendo el módulo (se usa en el índice y en las meta tags).

* **13.1 Nombre de la lección:** Descripción breve.
* **13.2 Otra lección:** Descripción breve.
```

`Order` debe ser un número de dos dígitos (`00`, `01`, ... `13`) para que el
ordenamiento alfabético de los archivos coincida con el orden numérico.

## Despliegue

Cada push a `main` dispara `.github/workflows/deploy.yml`, que instala
dependencias con `uv`, compila el sitio con `publishconf.py` y publica el
resultado en GitHub Pages.

## Licencia

Sin especificar todavía — agregar un archivo `LICENSE` si el proyecto va a
recibir contribuciones externas.
