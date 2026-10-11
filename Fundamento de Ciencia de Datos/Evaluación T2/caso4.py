import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# A. Desarrollo del modelo
datos_c4 = {
    'Mes': [1, 2, 3, 4, 5, 6, 7, 8],
    'Inversion': [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500],
    'Ventas': [5000, 6500, 7000, 9000, 9500, 11000, 11500, 13000]
}
df_c4 = pd.DataFrame(datos_c4)

X = df_c4[['Inversion']] # Variable independiente
y = df_c4['Ventas']      # Variable dependiente

modelo_reg = LinearRegression()
modelo_reg.fit(X, y)

coeficiente = modelo_reg.coef_[0]
intercepto = modelo_reg.intercept_
r2 = modelo_reg.score(X, y)

print(f"Coeficiente: {coeficiente:.2f}")
print(f"Intercepto: {intercepto:.2f}")
print(f"R^2: {r2:.4f}")

# B. Visualización y predicción
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, modelo_reg.predict(X), color='red', label='Recta de regresión')
plt.title('Inversión Publicitaria vs Ventas')
plt.xlabel('Inversión Publicitaria (S/)')
plt.ylabel('Ventas (S/)')
plt.legend()
plt.show()

inversion_futura = pd.DataFrame({'Inversion': [5000]})
prediccion_ventas = modelo_reg.predict(inversion_futura)[0]
print(f"Ventas estimadas para S/ 5,000 de inversión: {prediccion_ventas:.2f}")