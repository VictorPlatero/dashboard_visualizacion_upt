import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "ventas.csv"

st.set_page_config(
    page_title="Dashboard de Ventas UPT",
    page_icon="📊",
    layout="wide"
)

px.defaults.template = "plotly_white"
COLOR_PRINCIPAL = "#0f766e"
COLOR_SECUNDARIO = "#2563eb"


@st.cache_data
def cargar_datos():
    """Carga y prepara el archivo principal de ventas usado por el dashboard."""
    df = pd.read_csv(DATA_PATH, parse_dates=["fecha"])
    df["mes"] = df["fecha"].dt.to_period("M").astype(str)
    return df


df = cargar_datos()

st.markdown(
    """
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
    }
    div[data-testid="stMetricLabel"] p {color: #475569;}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Dashboard Interactivo de Ventas")
st.caption("Actividad Grupal 01 - Visualization Reports or Dashboard")

with st.sidebar:
    st.header("Filtros")
    st.caption("Selecciona los criterios para explorar las ventas registradas.")
    regiones = st.multiselect(
        "Región",
        sorted(df["region"].unique()),
        default=sorted(df["region"].unique())
    )
    categorias = st.multiselect(
        "Categoría",
        sorted(df["categoria"].unique()),
        default=sorted(df["categoria"].unique())
    )
    fecha_min = df["fecha"].min().date()
    fecha_max = df["fecha"].max().date()
    rango = st.date_input(
        "Rango de fechas",
        value=(fecha_min, fecha_max),
        min_value=fecha_min,
        max_value=fecha_max
    )

if isinstance(rango, tuple) and len(rango) == 2:
    inicio, fin = rango
else:
    inicio, fin = fecha_min, fecha_max

# El filtrado alimenta todas las métricas, gráficos y la tabla final.
f = df[
    (df["region"].isin(regiones)) &
    (df["categoria"].isin(categorias)) &
    (df["fecha"].dt.date >= inicio) &
    (df["fecha"].dt.date <= fin)
].copy()

if f.empty:
    st.warning("No hay registros para los filtros seleccionados. Ajusta la región, categoría o rango de fechas.")
    st.stop()

ventas = f["ventas"].sum()
utilidad = f["utilidad"].sum()
unidades = f["unidades"].sum()
margen = (utilidad / ventas * 100) if ventas else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Ventas", f"S/ {ventas:,.2f}")
c2.metric("Utilidad", f"S/ {utilidad:,.2f}")
c3.metric("Unidades", f"{unidades:,}")
c4.metric("Margen", f"{margen:.1f}%")

st.markdown("---")

mensual = (
    f.assign(mes=f["fecha"].dt.to_period("M").dt.to_timestamp())
     .groupby("mes", as_index=False)[["ventas", "utilidad"]].sum()
)

fig_linea = px.line(
    mensual, x="mes", y=["ventas", "utilidad"],
    markers=True,
    title="Evolución mensual de ventas y utilidad"
)
fig_linea.update_layout(legend_title_text="Indicador", hovermode="x unified")
st.plotly_chart(fig_linea, use_container_width=True)

c1, c2 = st.columns(2)

por_categoria = f.groupby("categoria", as_index=False)["ventas"].sum().sort_values("ventas", ascending=False)
fig_cat = px.bar(
    por_categoria, x="categoria", y="ventas",
    title="Ventas por categoría", text_auto=".2s",
    color_discrete_sequence=[COLOR_PRINCIPAL]
)
fig_cat.update_layout(xaxis_title="Categoría", yaxis_title="Ventas (S/)")
c1.plotly_chart(fig_cat, use_container_width=True)

por_region = f.groupby("region", as_index=False)["ventas"].sum().sort_values("ventas", ascending=False)
fig_reg = px.pie(
    por_region, names="region", values="ventas",
    hole=0.45,
    title="Participación de ventas por región"
)
fig_reg.update_traces(textposition="inside", textinfo="percent+label")
c2.plotly_chart(fig_reg, use_container_width=True)

c3, c4 = st.columns(2)

por_vendedor = f.groupby("vendedor", as_index=False).agg(
    ventas=("ventas", "sum"),
    utilidad=("utilidad", "sum")
).sort_values("ventas", ascending=False)

fig_vend = px.bar(
    por_vendedor, x="vendedor", y="ventas",
    color="utilidad", title="Rendimiento por vendedor",
    color_continuous_scale="Teal"
)
fig_vend.update_layout(xaxis_title="Vendedor", yaxis_title="Ventas (S/)")
c3.plotly_chart(fig_vend, use_container_width=True)

disp = f.groupby("categoria", as_index=False).agg(
    ventas=("ventas", "sum"),
    utilidad=("utilidad", "sum"),
    unidades=("unidades", "sum")
)
fig_disp = px.scatter(
    disp, x="ventas", y="utilidad", size="unidades",
    color="categoria", hover_name="categoria",
    title="Relación ventas vs. utilidad"
)
fig_disp.update_layout(xaxis_title="Ventas (S/)", yaxis_title="Utilidad (S/)")
c4.plotly_chart(fig_disp, use_container_width=True)

st.subheader("Detalle de registros")
st.dataframe(
    f.sort_values("fecha", ascending=False),
    use_container_width=True,
    hide_index=True
)

st.download_button(
    "Descargar datos filtrados en CSV",
    f.to_csv(index=False).encode("utf-8"),
    file_name="ventas_filtradas.csv",
    mime="text/csv"
)

st.caption("Actividad Grupal 01 – Inteligencia de Negocios – Universidad Privada de Tacna")
