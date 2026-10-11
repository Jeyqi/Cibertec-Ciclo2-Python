import pandas as pd
import matplotlib.pyplot as plt

# A. Construcción del análisis
datos_c6 = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Ingresos': [25000, 28000, 26000, 32000, 35000, 30000],
    'Gastos': [18000, 19000, 21000, 22000, 24000, 27000],
    'Clientes_nuevos': [80, 95, 90, 110, 125, 100],
    'Reclamos': [12, 10, 18, 9, 7, 22]
}
df_c6 = pd.DataFrame(datos_c6)

# Cálculos
df_c6['Utilidad'] = df_c6['Ingresos'] - df_c6['Gastos']
df_c6['Variacion_Ingresos_%'] = df_c6['Ingresos'].pct_change() * 100

mes_mayor_utilidad = df_c6.loc[df_c6['Utilidad'].idxmax(), 'Mes']
mes_mas_reclamos = df_c6.loc[df_c6['Reclamos'].idxmax(), 'Mes']

print(f"Mes con mayor utilidad: {mes_mayor_utilidad}")
print(f"Mes con más reclamos: {mes_mas_reclamos}")

# B. Dashboard
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Dashboard Operativo Mensual')

# 1. Ingresos
axs[0, 0].plot(df_c6['Mes'], df_c6['Ingresos'], marker='o', color='green')
axs[0, 0].set_title('Evolución de Ingresos')
axs[0, 0].set_ylabel('S/')

# 2. Utilidades
axs[0, 1].bar(df_c6['Mes'], df_c6['Utilidad'], color='blue')
axs[0, 1].set_title('Utilidades Mensuales')
axs[0, 1].set_ylabel('S/')

# 3. Reclamos
axs[1, 0].bar(df_c6['Mes'], df_c6['Reclamos'], color='red')
axs[1, 0].set_title('Reclamos por Mes')
axs[1, 0].set_ylabel('Cantidad')

# 4. Resumen
total_ingresos = df_c6['Ingresos'].sum()
total_utilidad = df_c6['Utilidad'].sum()
total_reclamos = df_c6['Reclamos'].sum()
texto_resumen = f"Total Ingresos: S/ {total_ingresos}\nTotal Utilidad: S/ {total_utilidad}\nTotal Reclamos: {total_reclamos}"
axs[1, 1].text(0.5, 0.5, texto_resumen, fontsize=14, ha='center', va='center')
axs[1, 1].axis('off')

plt.tight_layout()
plt.show()