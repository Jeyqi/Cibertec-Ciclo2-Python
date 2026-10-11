#Desarrollar un caso de aprendizaje supervisado para la empresa Coca Cola y mostrar la direferencia entre el modelo predictivo y el modelo descriptivo.

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# 1. GENERACIÓN DE DATOS SIMULADOS (Caso Coca-Cola Zero)
np.random.seed(42)
n_semanas = 100

# Características (X)
temperatura = np.random.uniform(15, 35, n_semanas)  # Entre 15°C y 35°C
publicidad = np.random.uniform(1000, 5000, n_semanas)  # Presupuesto en USD
partido_importante = np.random.choice([0, 1], size=n_semanas)  # 0=No, 1=Sí

# Variable Objetivo (Y): Litros vendidos (con algo de ruido aleatorio)
litros_vendidos = (
    5000
    + (temperatura * 150)
    + (publicidad * 0.8)
    + (partido_importante * 2000)
    + np.random.normal(0, 300, n_semanas)
)

# Crear el DataFrame de trabajo
df = pd.DataFrame(
    {
        "Temperatura": temperatura,
        "Publicidad_USD": publicidad,
        "Partido_Futbol": partido_importante,
        "Litros_Vendidos": litros_vendidos,
    }
)

X = df[["Temperatura", "Publicidad_USD", "Partido_Futbol"]]
y = df["Litros_Vendidos"]

# Dividir en entrenamiento y prueba (Crucial para el enfoque Predictivo)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)


# ==========================================
# 🔎 EVALUACIÓN ENFOQUE DESCRIPTIVO
# ==========================================
print("--- 🔎 EVALUACIÓN DESCRIPTIVA (Entender el impacto) ---")
# El enfoque descriptivo analiza la estructura interna del modelo ajustado
r2_entrenamiento = r2_score(y_train, modelo.predict(X_train))

print(f"Coeficiente de determinación (R²): {r2_entrenamiento:.4f}")
print("Impacto de cada variable (Coeficientes):")
print(f" -> Por cada 1°C más de Temperatura: +{modelo.coef_[0]:.2f} litros.")
print(f" -> Por cada 1 USD en Publicidad:    +{modelo.coef_[1]:.2f} litros.")
print(f" -> Si hay Partido de Fútbol (Sí):   +{modelo.coef_[2]:.2f} litros.")
print(f" Intercepto (Base fija de ventas):   {modelo.intercept_:.2f} litros.\n")


# ==========================================
# 🔮 EVALUACIÓN ENFOQUE PREDICTIVO
# ==========================================
print("--- 🔮 EVALUACIÓN PREDICTIVA (Capacidad de anticipar) ---")
# El enfoque predictivo evalúa el desempeño estrictamente con datos nuevos (Test)
predicciones_test = modelo.predict(X_test)
mae_test = mean_absolute_error(y_test, predicciones_test)

print(
    f"Error Absoluto Medio (MAE) en datos nuevos: {mae_test:.2f} litros de desfase promedio."
)

# Ejemplo de predicción para la próxima semana operativa
proxima_semana = pd.DataFrame(
    [{"Temperatura": 30, "Publicidad_USD": 2500, "Partido_Futbol": 1}]
)
prediccion_futura = modelo.predict(proxima_semana)
print(
    f"Predicción para la próxima semana (30°C, $2500 publicidad, Con partido): {prediccion_futura[0]:.2f} litros."
)
