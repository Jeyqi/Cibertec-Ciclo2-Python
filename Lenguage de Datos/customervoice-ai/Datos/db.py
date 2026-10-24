import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbconsolidado_3fn"
    )


def listar_evaluaciones(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.anio, v.dni, a.marca, a.modelo, v.score, v.estado
        FROM dbconsolidado_3fn.ventas v
        INNER JOIN dbconsolidado_3fn.autos a ON v.id_auto = a.id_auto
        ORDER BY v.id_venta DESC LIMIT 10
    """)
    registros = cursor.fetchall()
    cursor.close()
    return registros


def obtener_alertas(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT v.anio, v.dni, v.score, v.estado, c.comentario 
        FROM dbconsolidado_3fn.ventas v
        INNER JOIN dbconsolidado_3fn.clientes c ON v.dni = c.dni
        WHERE v.score <= 4
    """)
    alertas = cursor.fetchall()
    cursor.close()
    return alertas


def registrar_nueva_evaluacion_manual(conn, d):
    cursor = conn.cursor(buffered=True)
    try:
        cursor.execute(
            "INSERT IGNORE INTO dbconsolidado_3fn.clientes (dni, comentario) VALUES (%s, %s)", 
            (d["dni"], d["comentario"])
        )
        
        cursor.execute(
            "INSERT IGNORE INTO dbconsolidado_3fn.autos (marca, modelo, categoria, precio_lista) VALUES (%s, %s, 'N/A', %s)", 
            (d["marca"], d["modelo"], d["precio_lista"])
        )
        conn.commit()
        
        cursor.execute(
            "SELECT id_auto FROM dbconsolidado_3fn.autos WHERE marca=%s AND modelo=%s", 
            (d["marca"], d["modelo"])
        )
        resultado = cursor.fetchone()
        
        if resultado is None:
            return False
            
        id_auto = resultado[0]
        
        cursor.execute("""
            INSERT INTO dbconsolidado_3fn.ventas (dni, id_auto, estado, origen, anio, score) 
            VALUES (%s, %s, %s, 'Manual', 2026, %s)
        """, (d["dni"], id_auto, d["estado_comercial"], d["nota"]))
        conn.commit()
        return True
    except Exception as e:
        print(f"   [ERROR SQL] {e}")
        return False
    finally:
        cursor.close()


def modificar_nota_evaluacion(conn, dni, nueva_nota):
    cursor = conn.cursor(buffered=True)
    cursor.execute("UPDATE dbconsolidado_3fn.ventas SET score = %s WHERE dni = %s", (nueva_nota, dni))
    afectados = cursor.rowcount
    conn.commit()
    cursor.close()
    return afectados > 0


def eliminar_evaluacion_por_lead(conn, dni):
    cursor = conn.cursor(buffered=True)
    cursor.execute("DELETE FROM dbconsolidado_3fn.ventas WHERE dni = %s", (dni,))
    afectados = cursor.rowcount
    conn.commit()
    cursor.close()
    return afectados > 0
