import csv


def validar_fila(fila):
    try:
        nota = int(fila["cliente_score"])
        if nota < 1: nota = 1
        if nota > 10: nota = 10
    except (ValueError, TypeError):
        return None, f"Nota no numérica"

    comentario = (fila.get("feedback_cliente") or "").strip()
    if not comentario:
        return None, "Feedback vacío"

    return {
        "cliente_dni": fila["cliente_dni"].strip(),
        "marca_interes": fila.get("marca_interes", "N/A").strip(),
        "modelo_interes": fila.get("modelo_interes", "N/A").strip(),
        "estado_comercial": fila.get("estado_comercial", "N/A").strip(),
        "precio_lista": float(fila.get("precio_lista") or 0),
        "nota": nota,
        "comentario": comentario
    }, None


def leer_csv(ruta):
    validos, errores = [], []
    with open(ruta, encoding="utf-8", newline="") as f:
        lector = csv.DictReader(f)
        for numero, fila in enumerate(lector, start=2):
            registro, motivo = validar_fila(fila)
            if registro:
                validos.append(registro)
            else:
                errores.append(f"Fila {numero}: {motivo}")
    return validos, errores
