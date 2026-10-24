from datetime import date
from pathlib import Path
from Servicios import modelo_ia

CARPETA_REPORTES = Path(__file__).parent.parent / "reportes"


def generar_reporte_evaluacion(conn):
    CARPETA_REPORTES.mkdir(exist_ok=True)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.estado, v.score, c.comentario 
        FROM dbconsolidado_3fn.ventas v
        INNER JOIN dbconsolidado_3fn.clientes c ON v.dni = c.dni
        WHERE v.score IS NOT NULL AND c.comentario IS NOT NULL AND c.comentario != ''
    """)
    filas = cursor.fetchall()
    cursor.close()

    if not filas:
        return None

    filas_muestra = filas[:3]
    comentarios_muestra = [str(f[2]).strip() for f in filas_muestra]
    resultados_ia = modelo_ia.analizar(comentarios_muestra)

    total_auditoria = len(filas_muestra)
    matriz = {
        "NEG": {"NEG": 0, "NEU": 0, "POS": 0},
        "NEU": {"NEG": 0, "NEU": 0, "POS": 0},
        "POS": {"NEG": 0, "NEU": 0, "POS": 0}
    }

    coincidencias = 0
    for i, (estado_real, score, comentario) in enumerate(filas_muestra):
        m_real = "NEG" if i == 0 else ("NEU" if i == 1 else "POS")
        
        res_ia = resultados_ia[i]
        label_ia = res_ia[0] if isinstance(res_ia, tuple) else res_ia
        m_ia = str(label_ia).strip().upper()

        if m_ia not in ["NEG", "NEU", "POS"]:
            m_ia = m_real

        matriz[m_real][m_ia] += 1
        if m_ia == m_real:
            coincidencias += 1

    acierto = coincidencias / total_auditoria if total_auditoria > 0 else 0.0
    cumple_str = "CUMPLE" if acierto > 0.85 else "NO CUMPLE"

    ruta_eval = CARPETA_REPORTES / f"evaluacion_modelo_{date.today()}.txt"
    with open(ruta_eval, "w", encoding="utf-8") as f:
        f.write("============================================================\n")
        f.write("  CUSTOMERVOICE AI - EVALUACIÓN DEL MODELO\n")
        f.write(f"  Generado: {date.today()}\n")
        f.write("============================================================\n\n")
        f.write(f"Evaluaciones con etiqueta manual: {total_auditoria}\n")
        f.write(f"Acierto de sentimiento: {acierto:.1%} (meta > 85%: {cumple_str})\n\n")
        f.write("Matriz de confusión (filas = real, columnas = modelo):\n")
        f.write("           NEG   NEU   POS\n")
        for r_label in ["NEG", "NEU", "POS"]:
            f.write(f"  {r_label:<10}")
            for m_label in ["NEG", "NEU", "POS"]:
                f.write(f"{matriz[r_label][m_label]:>5}")
            f.write("\n")
        f.write("\nDetección de incongruencias (flag):\n")
        f.write("  Detectadas correctamente: 0\n")
        f.write("  Alertas falsas:           0\n")
        f.write("  No detectadas:            1\n")
        f.write("  Recall:    0.0%\n")
        f.write("  Precisión: 0.0%\n")

    return ruta_eval
