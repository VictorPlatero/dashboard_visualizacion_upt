# Creación y despliegue automatizado de un dashboard interactivo con Streamlit y Plotly

## Introducción

La visualización de datos permite transformar grandes volúmenes de información en indicadores comprensibles para apoyar la toma de decisiones. En este proyecto se desarrolló un **dashboard interactivo de ventas** empleando Python, Streamlit, Plotly y Pandas. Además, se implementó un flujo de despliegue automatizado utilizando GitHub Actions y Render.

El objetivo fue construir una aplicación web capaz de presentar indicadores clave, permitir la exploración de datos mediante filtros y demostrar un proceso reproducible de publicación en la nube.

## 1. Tecnologías utilizadas

**Streamlit** permite crear aplicaciones de datos con Python sin desarrollar manualmente una interfaz web completa. **Plotly** se utilizó para generar gráficos interactivos, mientras que **Pandas** se encargó del procesamiento y agregación de la información.

Para el control de versiones se utilizó **GitHub**, y para automatizar el despliegue se configuró **GitHub Actions**. Finalmente, la aplicación se publica como servicio web en **Render**.

## 2. Conjunto de datos

El dashboard trabaja con un conjunto de datos de ventas que contiene las siguientes variables:

- Fecha de la operación.
- Categoría del producto.
- Región.
- Vendedor.
- Unidades vendidas.
- Importe de ventas.
- Costos.
- Utilidad.

A partir de estas variables se calculan indicadores como ventas totales, utilidad, margen porcentual y unidades vendidas.

## 3. Diseño del dashboard

La aplicación se diseñó con un panel lateral de filtros. El usuario puede elegir regiones, categorías y un rango de fechas.

En la parte superior se muestran cuatro indicadores principales:

1. Ventas acumuladas.
2. Utilidad acumulada.
3. Unidades vendidas.
4. Margen de utilidad.

Luego se incluyen diferentes visualizaciones:

- Gráfico de líneas para analizar la evolución mensual.
- Gráfico de barras para comparar ventas por categoría.
- Gráfico de dona para observar la participación de cada región.
- Gráfico por vendedor para comparar rendimiento.
- Diagrama de dispersión para estudiar la relación entre ventas y utilidad.

Además, el usuario puede visualizar los registros detallados y descargar en CSV únicamente los datos correspondientes a los filtros seleccionados.

## 4. Desarrollo con Streamlit

La estructura principal del proyecto es sencilla:

```text
dashboard_visualizacion_upt/
├── app.py
├── data/
│   └── ventas.csv
├── requirements.txt
├── render.yaml
├── README.md
└── .github/
    └── workflows/
        └── deploy.yml
```

El archivo `app.py` contiene la interfaz, el procesamiento y las visualizaciones. Las dependencias se especifican en `requirements.txt`.

La aplicación se puede ejecutar localmente con:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 5. Repositorio público

El código fuente se aloja en un repositorio público de GitHub. Esto permite documentar el proyecto, mantener un historial de cambios y conectar el repositorio con el servicio de despliegue.

**Repositorio público:**  
`https://github.com/VictorPlatero/dashboard_visualizacion_upt.git`

## 6. Publicación en la nube con Render

Para la publicación se utiliza Render. El archivo `render.yaml` define automáticamente el servicio web, el comando de instalación y el comando de inicio.

El servicio ejecuta:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

Una vez creado el servicio, la aplicación queda disponible públicamente desde Internet.

**Aplicación publicada:**  
`PEGAR_AQUI_URL_DE_RENDER`

## 7. Despliegue automatizado

La automatización se realizó mediante GitHub Actions. Cada vez que se realiza un `push` a la rama `main`, el workflow ejecuta las siguientes tareas:

1. Descarga el repositorio.
2. Configura Python.
3. Instala las dependencias.
4. Comprueba la sintaxis de la aplicación.
5. Llama al Deploy Hook de Render.

La URL del Deploy Hook se almacena de forma segura en GitHub como el secreto:

```text
RENDER_DEPLOY_HOOK_URL
```

De esta manera, una modificación enviada a `main` puede activar automáticamente una nueva versión de la aplicación sin realizar el despliegue manualmente.

## 8. Resultados

El proyecto demuestra que Streamlit permite construir dashboards interactivos de manera rápida y que la combinación de GitHub Actions y un proveedor de nube permite incorporar prácticas básicas de integración y despliegue continuo.

El resultado es una aplicación accesible desde un navegador, con filtros y gráficos interactivos que ayudan a interpretar la información de ventas.

## 9. Video demostrativo

Se preparó un video breve en el que se muestran el repositorio, el funcionamiento del dashboard, la automatización y la aplicación publicada.

**Video:**  
`PEGAR_AQUI_URL_DEL_VIDEO`

## Conclusiones

La construcción del dashboard permitió integrar diferentes componentes de un flujo moderno de inteligencia de negocios: preparación de datos, construcción de indicadores, visualización, control de versiones, automatización y publicación en la nube.

Streamlit y Plotly proporcionan una alternativa práctica para la creación de dashboards en Python, mientras que GitHub Actions permite automatizar tareas técnicas y Render facilita la publicación de la aplicación como un servicio web público.

---

**Curso:** Inteligencia de Negocios  
**Actividad:** Actividad Grupal 01 – Visualization Reports or Dashboard  
**Universidad:** Universidad Privada de Tacna
