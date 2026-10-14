"""
Módulo de ingesta: lectura y validación del archivo CSV.
"""
import csv
from datetime import datetime

COLUMNAS = ["cliente_id", "fecha", "nota", "comentario", "sentimiento_real"]
ETIQUETAS = {"POS", "NEG", "NEU"}


def validar_fila(fila):
    """Devuelve (registro_limpio, None) si la fila es válida, o (None, motivo) si no."""
    try:
        nota = int(fila["nota"])
    except (ValueError, TypeError):
        return None, f"nota no numérica: {fila['nota']!r}"
    if not 1 <= nota <= 10:
        return None, f"nota fuera de rango: {nota}"

    try:
        datetime.strptime(fila["fecha"], "%Y-%m-%d")
    except (ValueError, TypeError):
        return None, f"fecha inválida: {fila['fecha']!r}"

    comentario = (fila["comentario"] or "").strip()
    if not comentario:
        return None, "comentario vacío"

    sentimiento = (fila["sentimiento_real"] or "").strip().upper() or None
    if sentimiento and sentimiento not in ETIQUETAS:
        return None, f"etiqueta desconocida: {sentimiento!r}"

    return {
        "cliente_id": fila["cliente_id"].strip(),
        "fecha": fila["fecha"],
        "nota": nota,
        "comentario": comentario,
        "sentimiento_real": sentimiento,
    }, None


def leer_csv(ruta):
    """Lee el CSV y separa los registros válidos de los errores."""
    validos, errores = [], []
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        lector = csv.DictReader(f)
        faltantes = set(COLUMNAS) - set(lector.fieldnames or [])
        if faltantes:
            raise ValueError(f"Faltan columnas en el CSV: {sorted(faltantes)}")

        for numero, fila in enumerate(lector, start=2):
            registro, motivo = validar_fila(fila)
            if registro:
                validos.append(registro)
            else:
                errores.append(f"Fila {numero}: {motivo}")
    return validos, errores
