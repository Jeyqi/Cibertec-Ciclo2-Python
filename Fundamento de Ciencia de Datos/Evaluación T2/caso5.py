import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, confusion_matrix, accuracy_score

# Datos
datos_c5 = {
    'Compras_previas': [8, 2, 10, 3, 7, 1, 9, 4, 6, 2, 11, 3],
    'Gasto_promedio': [120, 60, 200, 75, 140, 40, 180, 90, 130, 55, 220, 80],
    'Dias_sin_comprar': [5, 40, 3, 35, 8, 55, 6, 25, 12, 48, 4, 32],
    'Gasto_proxima_compra': [150, 50, 230, 65, 160, 30, 210, 85, 145, 45, 250, 70],
    'Abandona': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] # 0: No, 1: Sí
}
df_c5 = pd.DataFrame(datos_c5)

X = df_c5[['Compras_previas', 'Gasto_promedio', 'Dias_sin_comprar']]
y_reg = df_c5['Gasto_proxima_compra']
y_clf = df_c5['Abandona']

# División de datos (tamaño reducido)
X_train, X_test, yr_train, yr_test, yc_train, yc_test = train_test_split(X, y_reg, y_clf, test_size=0.3, random_state=42)

# Regresión
mod_reg = LinearRegression()
mod_reg.fit(X_train, yr_train)
pred_reg = mod_reg.predict(X_test)
print(f"MAE (Regresión): {mean_absolute_error(yr_test, pred_reg):.2f}")

# Clasificación
mod_clf = LogisticRegression()
mod_clf.fit(X_train, yc_train)
pred_clf = mod_clf.predict(X_test)
print("Matriz de confusión:\n", confusion_matrix(yc_test, pred_clf))
print(f"Exactitud (Accuracy): {accuracy_score(yc_test, pred_clf):.2f}")

#Presenta las predicciones generadas para los clientes del conjunto de prueba.

print("\nPredicciones de gasto para el conjunto de prueba:")
for i, pred in enumerate(pred_reg):
    print(f"Cliente {X_test.index[i]}: Predicción de gasto = {pred:.2f}, Abandona = {'Sí' if pred_clf[i] == 1 else 'No'}")