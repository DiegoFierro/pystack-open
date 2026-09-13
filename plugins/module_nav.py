"""
module_nav
~~~~~~~~~~

Las páginas de Pelican no tienen un orden implícito como los artículos
(que se ordenan por fecha). Este plugin toma todas las páginas que
definen metadata `Order` (los módulos del syllabus, ver
content/pages/syllabus/), las ordena, y le cuelga a cada una
`.prev_module` / `.next_module` para que el template pueda armar el
paginador "← Módulo anterior / Módulo siguiente →" sin lógica extra
en Jinja.
"""

from pelican import signals


def link_modules(generator):
    modules = sorted(
        (p for p in generator.pages if hasattr(p, "order")),
        key=lambda p: p.order,
    )
    for i, page in enumerate(modules):
        page.prev_module = modules[i - 1] if i > 0 else None
        page.next_module = modules[i + 1] if i < len(modules) - 1 else None
        page.module_position = i + 1
        page.module_count = len(modules)


def register():
    signals.page_generator_finalized.connect(link_modules)
