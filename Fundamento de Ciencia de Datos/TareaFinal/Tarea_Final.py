import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configuración de datos
df = pd.DataFrame({
    "Producto": ["Laptop", "Teclado", "Mouse", "Monitor", "Impresora"],
    "Ventas": [10000, 5000, 3000, 8000, 2000],
    "Ganancia": [3000, 2500, 1500, 4000, 1000],
    "Cantidad": [10, 20, 15, 8, 5]
})

# 2. Cálculos de indicadores clave (KPIs)
producto_mas_vendido = df.loc[df["Cantidad"].idxmax()]["Producto"] 
total_dinero_ingresado = df["Ventas"].sum()
total_ganancias = df["Ganancia"].sum()
producto_mayor_ganancia = df.loc[df["Ganancia"].idxmax()]["Producto"]

# Calcular margen de ganancia por producto para el análisis
df["Margen_%"] = (df["Ganancia"] / df["Ventas"]) * 100

# 3. Reporte visual

sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle("REPORTE EJECUTIVO DE VENTAS Y GANANCIAS MENSUALES", fontsize=16, fontweight="bold", y=1.02)

# Gráfico 1: Ventas vs Ganancias por Producto
df_melted = df.melt(id_vars="Producto", value_vars=["Ventas", "Ganancia"], var_name="Métrica", value_name="Monto")
sns.barplot(data=df_melted, x="Producto", y="Monto", hue="Métrica", palette="Blues_r", ax=axes[0])
axes[0].set_title("Comparativa de Ingresos vs. Ganancias ($)", fontsize=12, fontweight="bold")
axes[0].set_ylabel("Monto en USD")
axes[0].set_xlabel("Producto")

# Gráfico 2: Cantidades vendidas por Producto (Volumen)
sns.barplot(data=df, x="Producto", y="Cantidad", palette="viridis", ax=axes[1])
axes[1].set_title("Volumen de Unidades Vendidas", fontsize=12, fontweight="bold")
axes[1].set_ylabel("Unidades")
axes[1].set_xlabel("Producto")

plt.tight_layout()
plt.show()

# 4. Reporte Ejecutivo - Recomendaciones Estratégicas
print("=" * 60)
print("             REPORTE EJECUTIVO - RESUMEN MENSUAL            ")
print("=" * 60)
print(f"• Total Ingresos Mensuales:    ${total_dinero_ingresado:,.2f}")
print(f"• Total Ganancias Mensuales:   ${total_ganancias:,.2f}")
print(f"• Producto Líder en Margen:    {producto_mayor_ganancia} (${df['Ganancia'].max():,.2f})")
print(f"• Producto Más Vendido (Vol):  {producto_mas_vendido} ({df['Cantidad'].max()} unidades)")
print("-" * 60)
print("ANÁLISIS DE EFICIENCIA POR PRODUCTO:")
print(df[["Producto", "Cantidad", "Ventas", "Ganancia", "Margen_%"]].to_string(index=False))
print("-" * 60)
print("RECOMENDACIONES ESTRATÉGICAS PARA EL GERENTE:")

# Generación de recomendaciones dinámicas basadas en los datos
print(f"1. Impulsar el 'Teclado': Tiene un margen de ganancia altísimo ({df.loc[df['Producto']=='Teclado', 'Margen_%'].values[0]:.1f}%) en relación a su costo. Campañas de marketing aquí dejarán mucho dinero.")
print(f"2. Estrategia Cross-Selling (Venta cruzada): Aprovechar que el '{producto_mas_vendido}' es el más vendido en volumen para armar combos con 'Laptops' (mayor ingreso) o 'Teclados' (mayor margen).")
print(f"3. Evaluar 'Impresora': Es el producto que menos ingresos y ganancias aporta al negocio. Considerar si vale la pena mantener stock o renegociar costos con proveedores.")
print("=" * 60)


'''Debido a que son pocos los datos se hace de esta manera para poner en práctica lo aprendido en clases. Si fuesen
más datos, como una base de datos de, por ejemplo, 10 mil productos, podríamos usar la IA para que analice
toda la data usando APIs o las librerías de machine learning de Python, y nos genere un reporte ejecutivo 
más completo y detallado, con recomendaciones estratégicas más precisas y personalizadas.'''

