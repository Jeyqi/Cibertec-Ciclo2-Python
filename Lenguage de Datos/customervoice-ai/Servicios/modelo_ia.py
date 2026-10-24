from transformers import pipeline

MODELO = "pysentimiento/robertuito-sentiment-analysis"
_clasificador = None


def cargar_modelo():
    global _clasificador
    if _clasificador is None:
        _clasificador = pipeline("sentiment-analysis", model=MODELO)
    return _clasificador


def analizar(textos, tamano_lote=32):
    clf = cargar_modelo()
    resultados = []
    lista_textos = list(textos)
    for i in range(0, len(lista_textos), tamano_lote):
        lote = lista_textos[i:i + tamano_lote]
        lote_resultados = clf(lote, truncation=True)
        for r in lote_resultados:
            resultados.append((r["label"], round(r["score"], 2)))
    return resultados


def calcular_flag(nota, sentimiento):
    return int((nota >= 9 and sentimiento == "NEG") or (nota <= 4 and sentimiento == "POS"))
