# Dashboard Interactivo de Ventas – UPT

Proyecto desarrollado para la **Actividad Grupal 01: Visualization Reports or Dashboard** del curso de Inteligencia de Negocios.

Repositorio público: <https://github.com/VictorPlatero/dashboard_visualizacion_upt.git>

## Tecnologías
- Python
- Streamlit
- Plotly
- Pandas
- GitHub Actions
- Render

## Estructura del proyecto

```text
dashboard_visualizacion_upt/
├── app.py
├── data/
│   └── ventas.csv
├── requirements.txt
├── render.yaml
├── README.md
├── ARTICULO_MEDIUM_DEVTO_HASHNODE.md
├── GUION_VIDEO_5_MINUTOS.md
└── .github/
    └── workflows/
        └── deploy.yml
```

## Funcionalidades
- Filtros por región, categoría y fechas.
- KPIs de ventas, utilidad, unidades y margen.
- Evolución mensual.
- Ventas por categoría.
- Participación por región.
- Rendimiento por vendedor.
- Análisis ventas vs. utilidad.
- Descarga de datos filtrados.

## Ejecutar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

El dashboard lee los datos desde `data/ventas.csv`. No cambies la ubicación de ese archivo al subir el proyecto.

## Automatización con GitHub Actions

El workflow `.github/workflows/deploy.yml` se ejecuta al hacer `push` a la rama `main` y también puede ejecutarse manualmente desde la pestaña Actions.

Pasos automatizados:

1. Descarga el repositorio.
2. Configura Python 3.12.
3. Instala las dependencias de `requirements.txt`.
4. Valida la sintaxis de `app.py` con `python -m py_compile app.py`.
5. Llama al Deploy Hook de Render usando el secreto `RENDER_DEPLOY_HOOK_URL`.

## Despliegue en Render

1. Crear un repositorio **público** en GitHub y subir este proyecto.
2. En Render: **New > Blueprint** y seleccionar el repositorio.
3. Render detectará `render.yaml`.
4. Crear el servicio.
5. En Render abrir **Settings > Deploy Hook** y copiar la URL.
6. En GitHub: **Settings > Secrets and variables > Actions > New repository secret**.
7. Crear el secreto `RENDER_DEPLOY_HOOK_URL`.
8. Hacer un nuevo push a `main`.

Cada push a `main` ejecutará GitHub Actions, validará el proyecto y solicitará automáticamente un nuevo despliegue en Render.

## Entregables
- Repositorio público.
- Aplicación publicada.
- Artículo técnico.
- Automatización mediante GitHub Actions.
- Video de máximo 5 minutos.
- Archivo ZIP con los enlaces finales.
