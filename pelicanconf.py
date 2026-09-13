AUTHOR = 'Diego Fierro / PyStack Team'
SITENAME = 'PyStack Open'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'es'

# Tema propio (theme/pystack) en vez del tema "simple" por defecto de Pelican
THEME = "theme/pystack"

# Plugin propio, sin dependencias: genera sitemap.xml y robots.txt
# (ver plugins/sitemap.py). Solo actúa si SITEURL es una URL absoluta,
# así que en local (pelicanconf.py) no genera nada; en publishconf.py sí.
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["sitemap", "module_nav"]

# El extension "toc" no genera un índice visible por sí sola, pero le da
# a cada encabezado (incluidos los "Módulo N" del syllabus) un id estable
# para poder enlazarlos directamente, p. ej. syllabus.html#modulo-3
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Permitir que index.md sobreescriba la raíz del sitio (index.html)
INDEX_SAVE_AS = 'blog_index.html'  # Mueve el listado de blog secundario si existiera

# Configuración de URLs para Páginas
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

# Desactivar la generación automática del menú predeterminado de Pelican
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Crear el menú principal de navegación de forma explícita
MENUITEMS = (
    ('Inicio', '/pystack-open/index.html'),
    ('Syllabus', '/pystack-open/syllabus.html'),
)

# Enlaces del proyecto (se muestran en el footer, ver theme/pystack)
LINKS = [
    ("Diego Fierro", "https://diegofierro.github.io/"),
    ("Código en GitHub", "https://github.com/DiegoFierro/pystack-open"),
    #("Pelican", "https://getpelican.com/"),
    #("Python.org", "https://www.python.org/"),
]

DEFAULT_PAGINATION = False

# Este sitio es solo páginas (sin blog), así que no generamos los listados
# automáticos de artículos/categorías/tags/autores que Pelican crea por
# defecto (evita archivos vacíos como blog_index.html, tags.html, etc.)
DIRECT_TEMPLATES = []

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
