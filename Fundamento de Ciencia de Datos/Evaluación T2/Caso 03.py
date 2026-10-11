'''Una institución educativa desea predecir qué estudiantes podrían necesitar apoyo académico. Sin embargo, 
la información almacenada presenta campos incompletos, registros duplicados y valores inconsistentes. 
Antes de entrenar un modelo, el equipo debe evaluar y preparar los datos.'''

#El archivo contiene los siguientes registros:
import numpy as np
import pandas as pd


estudiantes = [
    {"ID": "E01", "Horas de estudio": 2, "Asistencia %": 60, "Nota final": 10, "Requiere apoyo": "Sí"},
    {"ID": "E02", "Horas de estudio": 5, "Asistencia %": 90, "Nota final": 16, "Requiere apoyo": "No"},
    {"ID": "E03", "Horas de estudio": 1, "Asistencia %": 50, "Nota final": 8, "Requiere apoyo": "Sí"},
    {"ID": "E04", "Horas de estudio": 4, "Asistencia %": 85, "Nota final": 15, "Requiere apoyo": "No"},
    {"ID": "E05", "Horas de estudio": np.nan, "Asistencia %": 70, "Nota final": 12, "Requiere apoyo": "Sí"},
    {"ID": "E06", "Horas de estudio": 3, "Asistencia %": np.nan, "Nota final": 11, "Requiere apoyo": "Sí"},
    {"ID": "E07", "Horas de estudio": 1, "Asistencia %": 95, "Nota final": 18, "Requiere apoyo": "No"},
    {"ID": "E08", "Horas de estudio": 2, "Asistencia %": 65, "Nota final": np.nan, "Requiere apoyo": "Sí"},
    {"ID": "E08", "Horas de estudio": 2, "Asistencia %": 65, "Nota final": np.nan, "Requiere apoyo": "Sí"},
    {"ID": "E09", "Horas de estudio": 6, "Asistencia %": 110, "Nota final": 17, "Requiere apoyo": "No"},
]

#Cargar los datos en un DataFrame de pandas
df = pd.DataFrame(estudiantes)

#Identificar los valores faltantes, duplicados y valores fuera de los rangos esperados
print("--- 1. DIAGNÓSTICO DE VALORES FALTANTES ---")
# .isna().sum() cuenta cuántos valores nulos hay por columna
print(df.isna().sum())

print("\n--- 2. DIAGNÓSTICO DE DUPLICADOS ---")
# .duplicated() encuentra filas idénticas repetidas
filas_duplicadas = df[df.duplicated(keep=False)]
print(filas_duplicadas)

print("\n--- 3. DIAGNÓSTICO DE VALORES FUERA DE RANGO ---")
fuera_de_rango = df[
    (df["Asistencia %"] > 100) | (df["Asistencia %"] < 0) | 
    (df["Nota final"] > 20) | (df["Nota final"] < 0)
]

print(fuera_de_rango)

'''Hasta aquí profesor, me retorna la fila completa donde está el dato fuera de rango. Aquí funciona bien, pero si la fila tiene cientos de datos, no podemos
andar buscando el dato fuera de rango uno por uno, así que lo trataremos de ubicar en el siguiente código.'''

for indice, fila in fuera_de_rango.iterrows():
    estudiante_id = fila["ID"]
    asistencia = fila["Asistencia %"]
    nota = fila["Nota final"]
    
    # Evaluamos si el problema específico es la asistencia
    if asistencia > 100 or asistencia < 0:
        print("El item fuera de rango es la asistencia del id", estudiante_id, "con un valor de", asistencia)
        
    # Evaluamos si el problema específico es la nota final
    if nota > 20 or nota < 0:
        print("El item fuera de rango es la nota final del id", estudiante_id, "con un valor de", nota)

#Elimina los registros duplicados con un criterio justificado.

df = df.drop_duplicates(keep='first')

#Estrategia para tratar los valores faltantes.
#Borramos el error de rango
df["Asistencia %"] = df["Asistencia %"].clip(upper=100)

mediana_horas = df["Horas de estudio"].median()
mediana_asistencia = df["Asistencia %"].median()
mediana_notas = df["Nota final"].median()

#Aplicamos la imputación de datos usando fillna() para reemplazar los valores faltantes con la mediana de cada columna
df["Horas de estudio"] = df["Horas de estudio"].fillna(mediana_horas)
df["Asistencia %"] = df["Asistencia %"].fillna(mediana_asistencia)
df["Nota final"] = df["Nota final"].fillna(mediana_notas)

print("\nDataFrame después del tratamiento de valores faltantes:")
print(df)

print("\n--- 1. COMPROBACIÓN DE RANGOS DE ASISTENCIA ---")
# Verificamos si queda algún dato fuera del límite de seguridad en tu df actual
errores_asistencia = df[(df["Asistencia %"] < 0) | (df["Asistencia %"] > 100)]

if errores_asistencia.empty:
    print("Validación exitosa: Todos los registros de asistencia se encuentran correctamente en el rango de 0 a 100%")
else:
    print("Alerta: Se encontraron registros fuera de rango")

print("\n--- 2. SEPARACIÓN DE VARIABLES PARA LA IA ---")

#Excluimos ID por ser un texto irrelevante para nuestros propósitos de predicción.
X = df[["Horas de estudio", "Asistencia %"]]

#Lo que queremos que la IA aprenda a predecir
y = df["Requiere apoyo"]

print("Variables Predictoras (X) - Listas para la IA:")
print(X)

print("\nVariable Objetivo (y) - Lista para la IA:")
print(y)