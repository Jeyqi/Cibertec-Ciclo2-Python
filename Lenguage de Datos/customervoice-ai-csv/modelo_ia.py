"""
Módulo de IA: análisis de sentimiento con Hugging Face y regla de incongruencia.
"""
from transformers import pipeline

MODELO = "pysentimiento/robertuito-sentiment-analysis"
_clasificador = None


def cargar_modelo():
    """Carga el modelo una sola vez (la primera vez lo descarga)."""
    global _clasificador
    if _clasificador is None:
        _clasificador = pipeline("sentiment-analysis", model=MODELO)
    return _clasificador


def analizar(textos):
    """Devuelve una lista de (etiqueta, score) para cada texto."""
    clf = cargar_modelo()
    resultados = clf(list(textos), truncation=True)
    return [(r["label"], round(r["score"], 2)) for r in resultados]


def calcular_flag(nota, sentimiento):
    """1 si la nota contradice el sentimiento del comentario, 0 si no."""
    return int((nota >= 9 and sentimiento == "NEG") or (nota <= 4 and sentimiento == "POS"))
