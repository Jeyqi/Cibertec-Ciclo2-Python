from datetime import date
from pathlib import Path
from Servicios import modelo_ia

CARPETA_REPORTES = Path(__file__).parent.parent / "reportes"


def evaluar_universo(filas, resultados_ia):
    matriz = {
        "NEG": {"NEG": 0, "NEU": 0, "POS": 0},
        "NEU": {"NEG": 0, "NEU": 0, "POS": 0},
        "POS": {"NEG": 0, "NEU": 0, "POS": 0}
    }
    coincidencias = 0
    total = len(filas)
    
    if total == 0:
        return 0.0, matriz

    for estado_real, score, comentario, idx_global in filas:
        nota = int(score) if score is not None else 5
        
        if nota <= 4:
            m_real = "NEG"
        elif nota >= 9:
            m_real = "POS"
        else:
            m_real = "NEU"
            
        res_ia = resultados_ia[idx_global]
        label_ia = res_ia[0] if isinstance(res_ia, tuple) else res_ia
        m_ia = str(label_ia).strip().upper()
        
        if m_ia not in ["NEG", "NEU", "POS"]:
            m_ia = "NEU"
            
        matriz[m_real][m_ia] += 1
        if m_ia == m_real:
            coincidencias += 1
            
    acierto = (coincidencias / total * 100)
    return acierto, matriz


def generar_reporte(conn):
    CARPETA_REPORTES.mkdir(exist_ok=True)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*), IFNULL(AVG(score), 0.0) FROM dbconsolidado_3fn.ventas")
    total_registros, promedio_general = cursor.fetchone()
    
    cursor.execute("""
        SELECT v.estado, v.score, c.comentario, v.id_banco, v.monto_financiado
        FROM dbconsolidado_3fn.ventas v
        INNER JOIN dbconsolidado_3fn.clientes c ON v.dni = c.dni
    """)
    todas_las_filas = cursor.fetchall()
    
    cursor.execute("""
        SELECT v.anio, c.dni, v.estado, v.score, c.comentario 
        FROM dbconsolidado_3fn.ventas v
        INNER JOIN dbconsolidado_3fn.clientes c ON v.dni = c.dni
        WHERE v.score <= 4
        ORDER BY v.score ASC
    """)
    alertas = cursor.fetchall()
    cursor.close()

    completas = []
    incompletas = []
    universo_completo = []
    comentarios_para_ia = []

    for idx, fila in enumerate(todas_las_filas):
        estado_real, score, comentario, id_banco, monto_financiado = fila
        com_texto = str(comentario).strip() if comentario else ""
        if not com_texto or com_texto.upper() == "N/A":
            com_texto = "Sin comentario"
        comentarios_para_ia.append(com_texto)
        
        datos_fila = (estado_real, score, comentario, idx)
        universo_completo.append(datos_fila)
        
        es_incompleta = (
            score is None or 
            estado_real is None or str(estado_real).strip() in ["", "N/A"] or 
            comentario is None or str(comentario).strip() in ["", "N/A"] or
            id_banco is None or
            monto_financiado is None or str(monto_financiado).strip() in ["", "N/A"]
        )
        
        if es_incompleta:
            incompletas.append(datos_fila)
        else:
            completas.append(datos_fila)

    resultados_ia = modelo_ia.analizar(comentarios_para_ia) if comentarios_para_ia else []

    acierto_completas, matriz_comp = evaluar_universo(completas, resultados_ia)
    acierto_incompletas, matriz_incomp = evaluar_universo(incompletas, resultados_ia)
    acierto_total, matriz_total = evaluar_universo(universo_completo, resultados_ia)

    comentarios_alertas = [str(al[4]).strip() for al in alertas]
    analisis_alertas = modelo_ia.analizar(comentarios_alertas) if comentarios_alertas else []

    ruta_sat = CARPETA_REPORTES / f"reporte_satisfaccion_{date.today()}.txt"
    with open(ruta_sat, "w", encoding="utf-8") as f:
        f.write("============================================================\n")
        f.write("  CUSTOMERVOICE AI - EVALUACIÓN DEL MODELO MULTI-CRITERIO\n")
        f.write(f"  Generado: {date.today()}\n")
        f.write("============================================================\n\n")
        
        f.write(f"1) LÍNEAS COMPLETAS (MySQL):\n")
        f.write(f"   Muestra evaluada: {len(completas)} registros\n")
        f.write(f"   Acierto de sentimiento: {acierto_completas:.1f}%\n\n")
        
        f.write(f"2) LÍNEAS INCOMPLETAS (MySQL):\n")
        f.write(f"   Muestra evaluada: {len(incompletas)} registros\n")
        f.write(f"   Acierto de sentimiento: {acierto_incompletas:.1f}%\n\n")
        
        f.write(f"3) UNIVERSO TOTAL (MySQL):\n")
        f.write(f"   Muestra evaluada: {len(universo_completo)} registros\n")
        f.write(f"   Acierto de sentimiento: {acierto_total:.1f}% (Meta > 85%: {'CUMPLE' if acierto_total > 85 else 'NO CUMPLE'})\n\n")
        
        f.write("Matriz de confusión combinada (Universo Total):\n")
        f.write("           PREDICCIÓN IA\n")
        f.write("           NEG   NEU   POS\n")
        f.write(f"R NEG  |   {matriz_total['NEG']['NEG']:<6}{matriz_total['NEG']['NEU']:<6}{matriz_total['NEG']['POS']:<5}|\n")
        f.write(f"E NEU  |   {matriz_total['NEU']['NEG']:<6}{matriz_total['NEU']['NEU']:<6}{matriz_total['NEU']['POS']:<5}|\n")
        f.write(f"A POS  |   {matriz_total['POS']['NEG']:<6}{matriz_total['POS']['NEU']:<6}{matriz_total['POS']['POS']:<5}|\n")
        f.write("L\n")
      
        f.write("\n============================================================\n")
        f.write("  CUSTOMERVOICE AI - REPORTE DE SATISFACCIÓN GLOBAL (3FN)\n")
        f.write("============================================================\n\n")
        f.write(f"Total de registros evaluados: {total_registros}\n")
        f.write(f"Score promedio general: {promedio_general:.2f} / 10\n\n")
        f.write(f"ALERTAS POR INCONGRUENCIA O BAJO SCORE: {len(alertas)}\n")
        f.write("-" * 60 + "\n\n")
        
        f.write("============================================================\n")
        f.write("  AUDITORÍA IA - ANÁLISIS DE SENTIMIENTOS Y PUNTUACIÓN\n")
        f.write("============================================================\n")
        for idx, (anio, dni, estado, score, comentario) in enumerate(alertas):
            sentimiento_predicho, puntuacion_confianza = analisis_alertas[idx]
            f.write(f"[{anio}] DNI: {dni} | Estado: {estado} | Score: {score}/10\n")
            f.write(f"   Comentario: \"{comentario}\"\n")
            f.write(f"   [IA] Sentimiento: {str(sentimiento_predicho).upper()} | Puntuación de Confianza: {puntuacion_confianza:.2f}\n")
            f.write("-" * 60 + "\n")
            
    return ruta_sat
