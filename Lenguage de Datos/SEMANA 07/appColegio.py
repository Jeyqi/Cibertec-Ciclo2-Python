from google import genai

API_KEY = "TU_API_KEY_AQUI"

client = genai.Client(api_key=API_KEY)

estudiantes = []

for i in range(3):
    print(f"=== ESTUDIANTES ===")

    nombre = input("Nombre del estudiante: ")
    promedio = float(input("Promedio final (0 - 20): "))

    estudiantes.append({
        "nombre":nombre,
        "promedio":promedio
    })

datos = ""

for estudiante in estudiantes:
    datos +=(
        f"Nombre: {estudiante['nombre']},"
        f"Promedio: {estudiante['promedio']}"
    )


prompt = f"""
Actúa como un gerente educativo experto en mejora académica.
Analiza los resultados de estos 5 estudiantes:
{datos}
Realiza lo siguiente:
1. Identifica a los estudiantes que necesitan mayor apoyo.
2. Interpreta los resultados del grupo.
3. Propón soluciones concretas para mejorar el rendimiento.
4. Recomienda acciones para docentes y padres.
5. Sugiere cómo evaluar las mejoras.
Usa un lenguaje sencillo, profesional y práctico.
No inventes causas personales que no aparecen en los datos.
Considera que la escala de notas es de 0 a 20.
"""

response = client.models.generate_content(
        model = "gemini-3.8-flash",
        contents = prompt
    )

print("=== Analisis por la IA ===")
print(response.text)