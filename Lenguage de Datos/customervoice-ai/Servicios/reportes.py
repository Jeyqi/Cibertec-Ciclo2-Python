"""
Módulo de reportes: genera el reporte ejecutivo en TXT.
"""
from datetime import date
from pathlib import Path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Datos import db

CARPETA_REPORTES = Path(__file__).parent.parent / "reportes"


def generar_reporte(conn, carpeta=CARPETA_REPORTES):
    """Escribe reporte_AAAA-MM-DD.txt y devuelve su ruta."""
    carpeta.mkdir(exist_ok=True)
    total, promedio, distribucion = db.obtener_resumen(conn)
    alertas = db.obtener_alertas(conn)

    ruta = carpeta / f"reporte_{date.today()}.txt"
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("  CUSTOMERVOICE AI - REPORTE DE SATISFACCIÓN\n")
        f.write(f"  Generado: {date.today()}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total de evaluaciones: {total}\n")
        f.write(f"Nota promedio: {promedio:.2f} / 10\n\n")
        f.write("Distribución de sentimiento:\n")
        for sentimiento, cantidad in distribucion:
            sentimiento_str = sentimiento if sentimiento else "Sin analizar"
            f.write(f"  {sentimiento_str}: {cantidad} ({cantidad / total:.1%})\n")
        f.write(f"\nALERTAS POR INCONGRUENCIA: {len(alertas)}\n")
        f.write("(ordenadas por confianza del modelo, de mayor a menor)\n")
        f.write("-" * 60 + "\n")
        for fecha, cliente, nota, sentimiento, score, comentario in alertas:
            f.write(f"[{fecha}] {cliente} | nota {nota} | {sentimiento} ({score:.2f})\n")
            f.write(f'   "{comentario}"\n')
    return ruta
