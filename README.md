# procreartes.com

Web estática servida como Cloudflare Worker con assets (`wrangler.jsonc`). Se publica sola al subir cambios a `main`.

## Cómo se edita

Desde el **Gestor de webs** del portal (portal.grupolivon.com) o a mano en estos ficheros:

- `data/proyectos.json`: proyectos (título, categoría, año, texto y enlace opcional). Las categorías crean los filtros automáticamente.

Al cambiar `data/`, `scripts/` o `css/tema.css`, la Action **Publicar la web** ejecuta `python3 scripts/generar.py`, guarda las páginas y Cloudflare las publica.

No edites los `.html` ni `css/estilos.css` a mano: se sobrescriben.

## Estructura

- `scripts/web.py`: plantilla común (cabecera, pie, páginas legales, sitemap).
- `scripts/generar.py`: contenido de esta web.
- `css/base.css` + `css/tema.css` → `css/estilos.css`.
- Fuentes propias en `fonts/` (sin Google Fonts ni cookies).
