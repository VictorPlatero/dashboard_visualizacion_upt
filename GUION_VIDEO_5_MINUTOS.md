# Guion para video (duración máxima: 5 minutos)

## 0:00 – 0:25 | Presentación
Hola. En este video presentaré un dashboard interactivo de ventas desarrollado con Python, Streamlit y Plotly para la actividad de visualización de datos del curso de Inteligencia de Negocios.

## 0:25 – 1:05 | Repositorio
Mostrar el repositorio público en GitHub.

Explicar:
- `app.py`: aplicación principal.
- `data/ventas.csv`: datos.
- `requirements.txt`: dependencias.
- `render.yaml`: configuración de nube.
- `.github/workflows/deploy.yml`: automatización.

## 1:05 – 2:40 | Dashboard
Abrir la aplicación publicada.

Mostrar:
- Filtro por región.
- Filtro por categoría.
- Rango de fechas.
- KPIs: ventas, utilidad, unidades y margen.
- Evolución mensual.
- Ventas por categoría.
- Participación por región.
- Rendimiento por vendedor.
- Tabla de registros.
- Botón para descargar CSV.

## 2:40 – 3:35 | Automatización
Regresar a GitHub y abrir `.github/workflows/deploy.yml`.

Explicar que cada push a `main`:
1. Configura Python.
2. Instala dependencias.
3. Valida la aplicación.
4. Ejecuta el Deploy Hook de Render.

Mostrar, si está disponible, una ejecución exitosa en la pestaña Actions.

## 3:35 – 4:25 | Nube
Abrir Render y/o la URL pública.

Explicar que `render.yaml` contiene el comando de construcción y el comando con el que Streamlit se publica.

## 4:25 – 4:50 | Conclusión
Este proyecto integra visualización de datos, repositorio público, automatización y despliegue en la nube. La aplicación permite explorar indicadores de ventas de forma interactiva y puede actualizarse automáticamente cuando se realizan cambios en GitHub.

## 4:50 – 5:00 | Cierre
Gracias por ver el video.
