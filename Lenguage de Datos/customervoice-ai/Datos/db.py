"""
Módulo de persistencia: base de datos MySQL y operaciones CRUD.
"""
import mysql.connector

CONFIG_CONEXION = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "customervoice_ai"
}

ESQUEMA_CLIENTES = """
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id VARCHAR(50) PRIMARY KEY
);
"""

ESQUEMA_EVALUACIONES = """
CREATE TABLE IF NOT EXISTS evaluaciones (
    id                 INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id         VARCHAR(50) NOT NULL,
    fecha              VARCHAR(20) NOT NULL,
    nota               INT NOT NULL,
    comentario         TEXT NOT NULL,
    sentimiento_real   VARCHAR(10),
    sentimiento_modelo VARCHAR(10),
    score              DOUBLE,
    flag               INT DEFAULT 0,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    CONSTRAINT chk_nota CHECK (nota BETWEEN 1 AND 10)
);
"""


def conectar():
    """Abre la conexión con el servidor MySQL configurado."""
    return mysql.connector.connect(**CONFIG_CONEXION)


def crear_tablas(conn):
    """DDL: crea las tablas utilizando un cursor de MySQL."""
    cursor = conn.cursor()
    cursor.execute(ESQUEMA_CLIENTES)
    cursor.execute(ESQUEMA_EVALUACIONES)
    conn.commit()
    cursor.close()


# ---------- CREATE ----------
def insertar_evaluaciones(conn, registros):
    """Inserta una lista de evaluaciones (diccionarios) y sus clientes en MySQL."""
    cursor = conn.cursor()
    
    query_clientes = "INSERT IGNORE INTO clientes (cliente_id) VALUES (%s)"
    datos_clientes = [(r["cliente_id"],) for r in registros]
    cursor.executemany(query_clientes, datos_clientes)
    
    query_evaluaciones = """
        INSERT INTO evaluaciones (cliente_id, fecha, nota, comentario, sentimiento_real)
        VALUES (%(cliente_id)s, %(fecha)s, %(nota)s, %(comentario)s, %(sentimiento_real)s)
    """
    cursor.executemany(query_evaluaciones, registros)
    
    conn.commit()
    cursor.close()
    return len(registros)


def insertar_val_manual(conn, registro):
    """Inserta una sola evaluación limpia desde el menú interactivo."""
    cursor = conn.cursor()
    query_cliente = "INSERT IGNORE INTO clientes (cliente_id) VALUES (%s)"
    cursor.execute(query_cliente, (registro["cliente_id"],))
    
    query_evaluacion = """
        INSERT INTO evaluaciones 
        (cliente_id, fecha, nota, comentario, sentimiento_real, sentimiento_modelo, score, flag)
        VALUES (%(cliente_id)s, %(fecha)s, %(nota)s, %(comentario)s, %(sentimiento_real)s,
                %(sentimiento_modelo)s, %(score)s, %(flag)s)
    """
    cursor.execute(query_evaluacion, registro)
    conn.commit()
    nuevo_id = cursor.lastrowid
    cursor.close()
    return nuevo_id


# ---------- READ ----------
def listar_evaluaciones(conn, limite=20):
    """Últimas evaluaciones registradas."""
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id, fecha, cliente_id, nota, sentimiento_modelo, flag, comentario
           FROM evaluaciones ORDER BY id DESC LIMIT %s""",
        (limite,),
    )
    filas = cursor.fetchall()
    cursor.close()
    return filas


def obtener_evaluacion(conn, id_evaluacion):
    """Una evaluación por ID."""
    cursor = conn.cursor()
    cursor.execute(
        """SELECT id, fecha, cliente_id, nota, sentimiento_modelo, flag, comentario
           FROM evaluaciones WHERE id = %s""",
        (id_evaluacion,),
    )
    fila = cursor.fetchone()
    cursor.close()
    return fila


def obtener_pendientes(conn):
    """Evaluaciones que todavía no pasaron por el modelo."""
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nota, comentario FROM evaluaciones WHERE sentimiento_modelo IS NULL"
    )
    filas = cursor.fetchall()
    cursor.close()
    return filas


def obtener_alertas(conn):
    """Evaluaciones con flag = 1, ordenadas por confianza."""
    cursor = conn.cursor()
    cursor.execute(
        """SELECT fecha, cliente_id, nota, sentimiento_modelo, score, comentario
           FROM evaluaciones WHERE flag = 1 ORDER BY score DESC"""
    )
    filas = cursor.fetchall()
    cursor.close()
    return filas


def obtener_resumen(conn):
    """Total, nota promedio y distribución de sentimiento."""
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM evaluaciones")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT AVG(nota) FROM evaluaciones")
    res_prom = cursor.fetchone()[0]
    promedio = float(res_prom) if res_prom is not None else 0.0
    
    cursor.execute(
        """SELECT sentimiento_modelo, COUNT(*) FROM evaluaciones
           GROUP BY sentimiento_modelo ORDER BY COUNT(*) DESC"""
    )
    distribucion = cursor.fetchall()
    
    cursor.close()
    return total, promedio, distribucion


# ---------- UPDATE ----------
def actualizar_analisis(conn, datos):
    """Guarda el resultado del modelo en lote."""
    cursor = conn.cursor()
    query = """
        UPDATE evaluaciones
        SET sentimiento_modelo = %s, score = %s, flag = %s
        WHERE id = %s
    """
    cursor.executemany(query, datos)
    conn.commit()
    cursor.close()


def actualizar_nota(conn, id_evaluacion, nota, flag):
    """Corrige la nota de una evaluación."""
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE evaluaciones SET nota = %s, flag = %s WHERE id = %s",
        (nota, flag, id_evaluacion),
    )
    conn.commit()
    cursor.close()


# ---------- DELETE ----------
def eliminar_evaluacion(conn, id_evaluacion):
    """Elimina una evaluación por su ID."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM evaluaciones WHERE id = %s", (id_evaluacion,))
    conn.commit()
    cursor.close()


def vaciar_evaluaciones(conn):
    """Elimina todas las evaluaciones y reinicia el AUTO_INCREMENT."""
    cursor = conn.cursor()
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("DELETE FROM evaluaciones")
    cursor.execute("ALTER TABLE evaluaciones AUTO_INCREMENT = 1")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    conn.commit()
    cursor.close()
