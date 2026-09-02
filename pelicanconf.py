AUTHOR = 'Diego Fierro / PyStack Team'
SITENAME = 'PyStack Open'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'es'

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
    ('Inicio', '/index.html'),
    ('Syllabus', '/syllabus.html'),
)

# Blogroll
LINKS = [
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
]

# Social widget
SOCIAL = [
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
