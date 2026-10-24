import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página web (Debe ser la primera línea de Streamlit)
st.set_page_config(
    page_title="Dashboard Ejecutivo de Ventas",
    page_icon="📊",
    layout="wide"
)

# 1. Título principal de la aplicación web
st.title("📊 Reporte Ejecutivo de Ventas y Ganancias Mensuales")
st.markdown("Generado automáticamente para la toma de decisiones gerenciales.")
st.divider()

# 2. Carga y preparación de datos
df = pd.DataFrame({
    "Producto": ["Laptop", "Teclado", "Mouse", "Monitor", "Impresora"],
    "Ventas": [10000, 5000, 3000, 8000, 2000],
    "Ganancia": [3000, 2500, 1500, 4000, 1000],
    "Cantidad": [10, 20, 15, 8, 5]
})

# Cálculos de indicadores clave (KPIs)
producto_mas_vendido = df.loc[df["Cantidad"].idxmax()]["Producto"]
total_dinero_ingresado = df["Ventas"].sum()
total_ganancias = df["Ganancia"].sum()
producto_mayor_ganancia = df.loc[df["Ganancia"].idxmax()]["Producto"]
df["Margen_%"] = (df["Ganancia"] / df["Ventas"]) * 100

# ==========================================
# 3. SECCIÓN DE INDICADORES CLAVE (KPIs)
# ==========================================
st.subheader("📈 Indicadores Clave de Rendimiento (KPIs)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Ingresos", value=f"${total_dinero_ingresado:,.2f}")
with col2:
    st.metric(label="Total Ganancias", value=f"${total_ganancias:,.2f}")
with col3:
    st.metric(label="Líder en Ganancia", value=producto_mayor_ganancia, delta=f"${df['Ganancia'].max():,.2f}")
with col4:
    st.metric(label="Más Vendido (Volumen)", value=producto_mas_vendido, delta=f"{df['Cantidad'].max()} und")

st.divider()

# ==========================================
# 4. SECCIÓN VISUAL (GRÁFICOS)
# ==========================================
st.subheader("📊 Análisis Visual")
col_graf1, col_graf2 = st.columns(2)

sns.set_theme(style="whitegrid")

with col_graf1:
    st.markdown("### Comparativa de Ingresos vs. Ganancias ($)")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    df_melted = df.melt(id_vars="Producto", value_vars=["Ventas", "Ganancia"], var_name="Métrica", value_name="Monto")
    sns.barplot(data=df_melted, x="Producto", y="Monto", hue="Métrica", palette="Blues_r", ax=ax1)
    ax1.set_ylabel("Monto en USD")
    ax1.set_xlabel("Producto")
    st.pyplot(fig1)

with col_graf2:
    st.markdown("### Volumen de Unidades Vendidas")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df, x="Producto", y="Cantidad", palette="viridis", ax=ax2)
    ax2.set_ylabel("Unidades")
    ax2.set_xlabel("Producto")
    st.pyplot(fig2)

st.divider()

# ==========================================
# 5. TABLA DE DATOS Y RECOMENDACIONES
# ==========================================
st.subheader("📋 Detalle de Eficiencia y Recomendaciones")

col_tabla, col_recom = st.columns([2, 3]) # El segundo bloque es más ancho para el texto

with col_tabla:
    st.markdown("### Tabla de Rendimiento")
    # Formateamos la tabla para que se vea impecable en la web
    df_formatted = df.copy()
    df_formatted["Ventas"] = df_formatted["Ventas"].map("${:,.2f}".format)
    df_formatted["Ganancia"] = df_formatted["Ganancia"].map("${:,.2f}".format)
    df_formatted["Margen_%"] = df_formatted["Margen_%"].map("{:.1f}%".format)
    st.dataframe(df_formatted, use_container_width=True)

with col_recom:
    st.markdown("### 💡 Recomendaciones Estratégicas")
    st.info(f"**1. Impulsar el 'Teclado':** Tiene un margen de ganancia altísimo ({df.loc[df['Producto']=='Teclado', 'Margen_%'].values[0]:.1f}%) en relación a su costo. Campañas de marketing aquí dejarán mucho dinero.")
    st.success(f"**2. Estrategia Cross-Selling (Venta cruzada):** Aprovechar que el **'{producto_mas_vendido}'** es el más vendido en volumen para armar combos con **'Laptops'** (mayor ingreso) o **'Teclados'** (mayor margen).")
    st.warning(f"**3. Evaluar 'Impresora':** Es el producto que menos ingresos y ganancias aporta al negocio. Considerar si vale la pena mantener stock o renegociar costos con proveedores.")
