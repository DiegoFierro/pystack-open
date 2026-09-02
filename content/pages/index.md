Title: Inicio — PyStack Open
Date: 2026-09-02
Slug: index
Save_as: index.html
URL: index.html

# PyStack Open

> **Aprende a construir aplicaciones de nivel de producción (Web, Móvil y Desktop) usando exclusivamente el ecosistema de Python.**

Inspirado en la metodología práctica de [*Full Stack Open*](https://fullstackopen.com/es/) (proporcinado por la **Universidad de Helsinki**), este curso te guía desde los fundamentos de la web moderna hasta el despliegue de sistemas capaces de funcionar offline durante días y sincronizarse automáticamente con un backend central.

---

## 🎯 Objetivo del Curso

Diseñar, desarrollar y desplegar una arquitectura completa **Full Stack** utilizando un único lenguaje de programación: **Python**. Al finalizar, serás capaz de:

1. **Construir aplicaciones web modernas** basadas en el estándar Hypermedia (*HTML Over the Wire*) sin frameworks pesados de JavaScript.
2. **Crear clientes nativos multiplataforma** (Android `.apk` y PC `.exe`) con persistencia local en **SQLite**.
3. **Diseñar sistemas Local-First** capaces de operar sin señal de internet y sincronizar datos asíncronamente.
4. **Desplegar arquitecturas de alto rendimiento** orquestadas con Docker, servidores ASGI en Rust (**Granian**) y proxy inverso **Caddy**.

---

## 🛠️ Stack Tecnológico Oficial (PyStack)

Para evitar la parálisis por análisis, el curso utiliza un **stack acotado y estándar de la industria**:

| Capa | Tecnología | Función Principal |
| --- | --- | --- |
| **Entorno & Tooling** | `uv` + `Ruff` + `mypy` | Gestión ultra rápida de paquetes, calidad y tipado estático. |
| **Backend Core** | Django ORM + PostgreSQL | Fuente única de verdad para datos, migraciones y backoffice. |
| **API & Asincronía** | FastAPI + Granian | Endpoints de alta velocidad, WebSockets y servidor ASGI. |
| **Frontend Web** | HTMX + HTML5 Nativo + DaisyUI | Interactividad cliente directa sin JavaScript. |
| **Cliente Nativo** | Flet (Python) + SQLite | Interfaz multiplataforma (Mobile/Desktop) con soporte offline. |
| **Procesos en Segundo Plano** | TaskIQ + Redis | Cola de tareas asíncronas y almacenamiento en caché. |
| **Infraestructura** | Docker Compose + Caddy | Contenerización y despliegue con SSL automático. |

---

## 🛣️ Las Dos Rutas de Especialización

El programa ofrece una base común de backend (Módulos 0 a 6) y se bifurca en el **Módulo 7** según el producto que necesites construir:

* **Ruta A (Web Responsiva & PWA):** Para aplicaciones web tradicionales, paneles administrativos y SaaS. Utiliza HTMX y Tailwind CLI empaquetado mediante **TWA** (Trusted Web Activity).
* **Ruta B (Cliente Nativo & Local-First):** Para aplicaciones con uso offline prolongado (ej. apps de aprendizaje de idiomas). Utiliza Flet con SQLite local y un motor de sincronización asíncrono.

---

## 📋 Requisitos Previos

Para aprovechar al máximo este curso, es recomendable contar con:

* **Conocimientos intermedios de Python:** Manejo de Funciones, Clases (POO), Excepciones y Estructuras de Datos.
* **Fundamentos de Terminal:** Uso básico de la línea de comandos en PowerShell o CMD.
* **Conceptos básicos de Web:** Entender qué es una petición HTTP (GET, POST) y marcado básico en HTML.