"""
CustomerVoice AI - punto de entrada.
Flujo: CSV -> validación -> SQLite -> modelo de IA -> SQLite -> reporte TXT -> evaluación
"""
from pathlib import Path

import db
import evaluacion
import ingesta
import modelo_ia
import reportes

RUTA_CSV = Path(__file__).parent / "data" / "evaluaciones_clientes.csv"


def main():
    print("1. Conectando a la base de datos...")
    conn = db.conectar()
    db.crear_tablas(conn)
    db.vaciar_evaluaciones(conn)  # recarga desde cero en cada ejecución

    print("2. Leyendo y validando el CSV...")
    validos, errores = ingesta.leer_csv(RUTA_CSV)
    for error in errores:
        print("   [descartado]", error)
    insertados = db.insertar_evaluaciones(conn, validos)
    print(f"   {insertados} registros cargados, {len(errores)} descartados")

    print("3. Analizando sentimiento (la primera vez descarga el modelo)...")
    pendientes = db.obtener_pendientes(conn)
    resultados = modelo_ia.analizar(comentario for _, _, comentario in pendientes)
    datos = [
        (sentimiento, score, modelo_ia.calcular_flag(nota, sentimiento), id_)
        for (id_, nota, _), (sentimiento, score) in zip(pendientes, resultados)
    ]
    db.actualizar_analisis(conn, datos)
    print(f"   {len(datos)} comentarios analizados, {sum(d[2] for d in datos)} alertas")

    print("4. Generando reporte...")
    ruta = reportes.generar_reporte(conn)
    print(f"   Reporte guardado en: {ruta}")

    print("5. Evaluando el modelo contra las etiquetas manuales...")
    ruta_eval, metricas = evaluacion.generar_reporte_evaluacion(conn)
    if metricas:
        print(f"   Acierto: {metricas['acierto']:.1%} | "
              f"incongruencias detectadas: {metricas['detectados']} | "
              f"alertas falsas: {metricas['falsos']}")
        print(f"   Evaluación guardada en: {ruta_eval}")
    else:
        print("   No hay etiquetas manuales para evaluar")

    conn.close()


if __name__ == "__main__":
    main()
