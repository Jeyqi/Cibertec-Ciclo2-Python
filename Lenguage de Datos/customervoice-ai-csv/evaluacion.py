"""
Módulo de evaluación: mide qué tan bien funciona el modelo contra las etiquetas manuales.
"""
from datetime import date
from pathlib import Path

from modelo_ia import calcular_flag

ETIQUETAS = ["NEG", "NEU", "POS"]
META_ACIERTO = 0.85
CARPETA_REPORTES = Path(__file__).parent / "reportes"


def calcular_metricas(conn):
    """Acierto, matriz de confusión y métricas del flag."""
    filas = conn.execute(
        """SELECT nota, sentimiento_real, sentimiento_modelo FROM evaluaciones
           WHERE sentimiento_real IS NOT NULL AND sentimiento_modelo IS NOT NULL"""
    ).fetchall()
    total = len(filas)
    if total == 0:
        return None

    matriz = {real: {pred: 0 for pred in ETIQUETAS} for real in ETIQUETAS}
    aciertos = detectados = falsos = perdidos = 0

    for nota, real, pred in filas:
        matriz[real][pred] += 1
        aciertos += real == pred
        flag_real = calcular_flag(nota, real)
        flag_modelo = calcular_flag(nota, pred)
        detectados += flag_real and flag_modelo
        falsos += (not flag_real) and flag_modelo
        perdidos += flag_real and not flag_modelo

    alertas = detectados + falsos
    incongruencias = detectados + perdidos
    return {
        "total": total,
        "acierto": aciertos / total,
        "matriz": matriz,
        "detectados": detectados,
        "falsos": falsos,
        "perdidos": perdidos,
        "recall_flag": detectados / incongruencias if incongruencias else None,
        "precision_flag": detectados / alertas if alertas else None,
    }


def generar_reporte_evaluacion(conn, carpeta=CARPETA_REPORTES):
    """Escribe evaluacion_AAAA-MM-DD.txt y devuelve (ruta, métricas)."""
    m = calcular_metricas(conn)
    if m is None:
        return None, None

    carpeta.mkdir(exist_ok=True)
    ruta = carpeta / f"evaluacion_{date.today()}.txt"
    cumple = "CUMPLE" if m["acierto"] > META_ACIERTO else "NO CUMPLE"

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("  CUSTOMERVOICE AI - EVALUACIÓN DEL MODELO\n")
        f.write(f"  Generado: {date.today()}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Evaluaciones con etiqueta manual: {m['total']}\n")
        f.write(f"Acierto de sentimiento: {m['acierto']:.1%} "
                f"(meta > {META_ACIERTO:.0%}: {cumple})\n\n")

        f.write("Matriz de confusión (filas = real, columnas = modelo):\n")
        f.write("        " + "".join(f"{e:>6}" for e in ETIQUETAS) + "\n")
        for real in ETIQUETAS:
            f.write(f"  {real:<6}" + "".join(f"{m['matriz'][real][p]:>6}" for p in ETIQUETAS) + "\n")

        f.write("\nDetección de incongruencias (flag):\n")
        f.write(f"  Detectadas correctamente: {m['detectados']}\n")
        f.write(f"  Alertas falsas:           {m['falsos']}\n")
        f.write(f"  No detectadas:            {m['perdidos']}\n")
        if m["recall_flag"] is not None:
            f.write(f"  Recall:    {m['recall_flag']:.1%}  (de las incongruencias reales, cuántas detecta)\n")
        if m["precision_flag"] is not None:
            f.write(f"  Precisión: {m['precision_flag']:.1%}  (de las alertas emitidas, cuántas son reales)\n")
    return ruta, m
