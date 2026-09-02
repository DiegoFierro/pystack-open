Title: Programa de Estudios (Syllabus)
Date: 2026-09-02
Slug: syllabus
Save_as: syllabus.html

# Programa de Estudios Oficial

El curso está estructurado en **12 módulos progresivos**. Cada módulo contiene lecciones cortas y enfocadas en un objetivo técnico directo.

---

### Módulo 0: Entorno de Desarrollo Pythonico Moderno
* **0.1 Gestor de dependencias:** Instalación y flujos de trabajo deterministas con **`uv`**.
* **0.2 Calidad de código:** Linting y formateo estricto en tiempo real con **Ruff**.
* **0.3 Verificación de tipos:** Análisis estático de código con **`mypy`**.
* **0.4 Configuración tipada:** Variables de entorno y ajustes con **Pydantic Settings**.

### Módulo 1: Fundamentos Web & Hypermedia
* **1.1 Arquitectura HTTP:** Protocolo, verbos, cabeceras y ciclo de vida de peticiones.
* **1.2 Filosofía Hypermedia:** Diferencias clave entre aplicaciones impulsadas por hipertexto y SPAs.
* **1.3 Motor de plantillas:** Renderizado de vistas dinámicas con **Jinja2**.
* **1.4 Vistas asíncronas:** Creación de endpoints y validación de esquemas con **FastAPI**.

### Módulo 2: Interfaz Interactiva sin JavaScript
* **2.1 Contrato Hypermedia:** Atributos core de **HTMX** (`hx-get`, `hx-post`, `hx-target`, `hx-swap`).
* **2.2 Modales nativos:** Implementación de diálogos y popups con la etiqueta `<dialog>` de HTML5.
* **2.3 Acordeones y menús:** Componentes desplegables mediante `<details>` y `<summary>`.
* **2.4 Animaciones fluidas:** Transiciones de estado con la API *View Transitions* de CSS.

### Módulo 3: Arquitectura Backend & Base de Datos
* **3.1 Modelado relacional:** Definición de esquemas y relaciones con **Django ORM**.
* **3.2 Persistencia de datos:** Configuración e integración con **PostgreSQL**.
* **3.3 Control de esquemas:** Creación y gestión de migraciones de base de datos.
* **3.4 Backoffice central:** Personalización del Panel de Administración de Django.

### Módulo 4: Arquitectura Híbrida (Django + FastAPI)
* **4.1 Fuente de verdad:** Estrategia de modelos compartidos usando Django ORM.
* **4.2 Consultas asíncronas:** Ejecución de operaciones ORM desde FastAPI mediante `sync_to_async`.
* **4.3 Emisión Dual:** Configuración de endpoints para retornar fragmentos HTML o JSON según el cliente.

### Módulo 5: Formularios Dinámicos & Manejo de Estado
* **5.1 Validación en tiempo real:** Procesamiento de formularios en el servidor sin recargar.
* **5.2 Actualización múltiple:** Componentes distantes usando *Out-of-Band Swaps* (OOB) de HTMX.
* **5.3 Tablas reactivas:** Paginación, ordenamiento y búsquedas al vuelo.

### Módulo 6: Autenticación & Seguridad
* **6.1 Autenticación dual:** Manejo de sesiones por Cookies (`HttpOnly`) y Tokens JWT.
* **6.2 Control de acceso:** Autenticación y autorización basada en roles (RBAC).
* **6.3 Protección web:** Mitigación de riesgos CSRF, XSS e Inyección SQL.
* **6.4 Seguridad de credenciales:** Hashing de contraseñas con Argon2.

### Módulo 7: Especialización de Cliente (A Elección)
* **Ruta A (Web/PWA):** Tailwind CLI Standalone, DaisyUI y empaquetado TWA.
* **Ruta B (Nativa/Offline):** Flet, persistencia local con SQLite y motor de sincronización offline.

### Módulo 8: Rendimiento & Caché
* **8.1 Almacenamiento en caché:** Estrategias de caché con **Redis**.
* **8.2 Compresión de red:** Optimización de respuestas HTTP mediante **Brotli**.
* **8.3 Carga diferida:** Implementación de *Lazy Loading* de recursos con HTMX.
* **8.4 Optimización de consultas:** Eliminación de problemas $N+1$ en el ORM.

### Módulo 9: Comunicación en Tiempo Real
* **9.1 Conexiones bidireccionales:** Implementación de WebSockets en **FastAPI**.
* **9.2 Eventos en vivo:** Notificaciones push y mensajería en tiempo real.
* **9.3 Integración de sockets:** Conexión de WebSockets con HTMX (`hx-ws`) y Flet.

### Módulo 10: Tareas en Segundo Plano
* **10.1 Cola asíncrona:** Procesamiento de tareas diferidas con **TaskIQ**.
* **10.2 Broker de mensajes:** Gestión de colas de ejecución respaldadas por **Redis**.
* **10.3 Estado de tareas:** Polling y actualización del progreso en la UI.

### Módulo 11: Testing & Calidad de Software
* **11.1 Pruebas unitarias:** Tests de modelos y lógica de negocio con **Pytest**.
* **11.2 Pruebas de integración:** Testing de endpoints HTTP asíncronos con **HTTPX**.
* **11.3 Automatización:** Configuración de hooks de pre-commit para ejecuciones con Ruff y MyPy.

### Módulo 12: Despliegue & Producción
* **12.1 Contenerización:** Imágenes livianas (*multi-stage*) con **Docker**.
* **12.2 Orquestación:** Entorno completo en **Docker Compose** (Django + FastAPI + PostgreSQL + Redis).
* **12.3 Servidor ASGI:** Despliegue de alto rendimiento con **Granian**.
* **12.4 Producción:** Configuración de **Caddy** como proxy inverso con SSL automático.