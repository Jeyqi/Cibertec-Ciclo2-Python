import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Reporte Ejecutivo", page_icon="♥", layout="wide")

st.title("Reporte Ejecutivo de Ventas")
st.write(
    "Empresa Comercial ABC: Analisis de Ventas,"
    "ganancias y apoyo a la toma de decision"
)

datos = {
    "Producto": ["Laptop", "Teclado", "Mouse", "Monitor"],
    "Cantidad": [12, 35, 50, 10],
    "Precio": [2500, 80, 40, 700],
    "Costo": [2100, 45, 20, 500],
}

df = pd.DataFrame(datos)

df["Ventas"] = df["Cantidad"] * df["Precio"]

df["Costo_Total"] = df["Cantidad"] * df["Costo"]

df["Ganancia"] = df["Ventas"] - df["Costo_Total"]

# indicador para  EL REPORTE EJECUTIVO

total_ventas = df["Ventas"].sum()
total_ganancia = df["Ganancia"].sum()
total_unidades = df["Cantidad"].sum()

producto_mas_vendido = df.loc[df["Ventas"].idxmax(), "Producto"]

# MOSTRAR EL INDICADOR A ,A PAG. WEB
st.subheader("Indicadores principales")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Ventas totales", f"S/.{total_ventas:,.2f}")
col2.metric("Ganancia bruta", f"S/.{total_ganancia:,.2f}")
col3.metric("Unidades vendidas", f"{total_unidades}")
col4.metric("Mayor Ingreso", producto_mas_vendido)

# MOSTRAR LA TB DE RESULTADOS

st.subheader("Detalle de ventas pro producto")

st.dataframe(df, use_container_width=True)

# realizar  LOS GRAFICOS PARA COMPARAR LOS RESULTADOS

grafico1, grafico2 = st.columns(2)

with grafico1:
    st.subheader("Venta por producto")

    fig1, ax1 = plt.subplots()

    ax1.bar(df["Producto"], df["Ventas"])
    ax1.set_xlabel("Producto")
    ax1.set_ylabel("Ventas en soles")
    ax1.set_title("Ingresos del producto")

    fig1.tight_layout()

    st.pyplot(fig1)
    plt.close(fig1)

# GRAFICO 2
with grafico2:
    st.subheader("Ganancia por producto")

    fig2, ax2 = plt.subplots()

    ax2.bar(df["Producto"], df["Ganancia"])
    ax2.set_xlabel("Producto")
    ax2.set_ylabel("Ganancia en soles")
    ax2.set_title("Ganancia bruta por producto")

    fig2.tight_layout()

    st.pyplot(fig2)
    plt.close(fig2)


# generar RECOMENDACION PARA GERENCIA

st.subheader("Conclusiones para la toma de decisiones")

st.write(
    f"El producto que genero mas ingresos fue"
    f"{producto_mas_vendido},con ventas de "
    f"S/ {df.loc[df['Ventas'].idxmax(),'Ventas']:,.2f}."
)

st.write(f"La empresa obtuvo una ganancia bruta total de " f"S/ {total_ganancia:,.2f}.")

# producto menor cantidad de venta
producto_menor_cantidad = df.loc[df["Cantidad"].idxmin(), "Producto"]

st.write(
    f"El producto con menor cantidad de unidades vendidas"
    f"fue {producto_menor_cantidad}."
    "Se recomienda revisar su demanda antes de realizar "
    "nuevas compras."
)

st.success(
    "Reporte generado correctamente."
    "La gerencia puede utilizar estos reultados "
    "para orientar sus decisiones"
)
