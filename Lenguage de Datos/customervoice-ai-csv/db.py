"""
Módulo de persistencia: base de datos SQLite3 y operaciones CRUD.
"""
import sqlite3
from pathlib import Path

RUTA_BD = Path(__file__).parent / "data" / "customervoice.db"

ESQUEMA = """
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS evaluaciones (
    id                 INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id         TEXT NOT NULL,
    fecha              TEXT NOT NULL,
    nota               INTEGER NOT NULL CHECK (nota BETWEEN 1 AND 10),
    comentario         TEXT NOT NULL,
    sentimiento_real   TEXT,
    sentimiento_modelo TEXT,
    score              REAL,
    flag               INTEGER DEFAULT 0,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);
"""


def conectar(ruta=RUTA_BD):
    """Abre (o crea) la base de datos y activa las claves foráneas."""
    conn = sqlite3.connect(ruta)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def crear_tablas(conn):
    """DDL: crea las tablas si no existen."""
    conn.executescript(ESQUEMA)
    conn.commit()


# ---------- CREATE ----------
def insertar_evaluaciones(conn, registros):
    """Inserta una lista de evaluaciones (diccionarios) y sus clientes."""
    conn.executemany(
        "INSERT OR IGNORE INTO clientes (cliente_id) VALUES (?)",
        [(r["cliente_id"],) for r in registros],
    )
    conn.executemany(
        """INSERT INTO evaluaciones (cliente_id, fecha, nota, comentario, sentimiento_real)
           VALUES (:cliente_id, :fecha, :nota, :comentario, :sentimiento_real)""",
        registros,
    )
    conn.commit()
    return len(registros)


def insertar_evaluacion(conn, registro):
    """Inserta una sola evaluación ya analizada (usada desde el menú) y devuelve su id."""
    conn.execute("INSERT OR IGNORE INTO clientes (cliente_id) VALUES (?)", (registro["cliente_id"],))
    cursor = conn.execute(
        """INSERT INTO evaluaciones
           (cliente_id, fecha, nota, comentario, sentimiento_real, sentimiento_modelo, score, flag)
           VALUES (:cliente_id, :fecha, :nota, :comentario, :sentimiento_real,
                   :sentimiento_modelo, :score, :flag)""",
        registro,
    )
    conn.commit()
    return cursor.lastrowid


# ---------- READ ----------
def listar_evaluaciones(conn, limite=20):
    """Últimas evaluaciones registradas."""
    return conn.execute(
        """SELECT id, fecha, cliente_id, nota, sentimiento_modelo, flag, comentario
           FROM evaluaciones ORDER BY id DESC LIMIT ?""",
        (limite,),
    ).fetchall()


def obtener_evaluacion(conn, id_evaluacion):
    """Una evaluación por id (o None si no existe)."""
    return conn.execute(
        """SELECT id, fecha, cliente_id, nota, sentimiento_modelo, flag, comentario
           FROM evaluaciones WHERE id = ?""",
        (id_evaluacion,),
    ).fetchone()


def obtener_pendientes(conn):
    """Evaluaciones que todavía no pasaron por el modelo."""
    return conn.execute(
        "SELECT id, nota, comentario FROM evaluaciones WHERE sentimiento_modelo IS NULL"
    ).fetchall()


def obtener_alertas(conn):
    """Evaluaciones con flag = 1, ordenadas por confianza del modelo."""
    return conn.execute(
        """SELECT fecha, cliente_id, nota, sentimiento_modelo, score, comentario
           FROM evaluaciones WHERE flag = 1 ORDER BY score DESC"""
    ).fetchall()


def obtener_resumen(conn):
    """Total, nota promedio y distribución de sentimiento."""
    total = conn.execute("SELECT COUNT(*) FROM evaluaciones").fetchone()[0]
    promedio = conn.execute("SELECT AVG(nota) FROM evaluaciones").fetchone()[0]
    distribucion = conn.execute(
        """SELECT sentimiento_modelo, COUNT(*) FROM evaluaciones
           GROUP BY sentimiento_modelo ORDER BY COUNT(*) DESC"""
    ).fetchall()
    return total, promedio, distribucion


# ---------- UPDATE ----------
def actualizar_analisis(conn, datos):
    """Guarda el resultado del modelo. datos = [(sentimiento, score, flag, id), ...]"""
    conn.executemany(
        """UPDATE evaluaciones
           SET sentimiento_modelo = ?, score = ?, flag = ?
           WHERE id = ?""",
        datos,
    )
    conn.commit()


def actualizar_nota(conn, id_evaluacion, nota, flag):
    """Corrige la nota de una evaluación y su flag recalculado."""
    conn.execute(
        "UPDATE evaluaciones SET nota = ?, flag = ? WHERE id = ?",
        (nota, flag, id_evaluacion),
    )
    conn.commit()


# ---------- DELETE ----------
def eliminar_evaluacion(conn, id_evaluacion):
    """Elimina una evaluación por su id."""
    conn.execute("DELETE FROM evaluaciones WHERE id = ?", (id_evaluacion,))
    conn.commit()


def vaciar_evaluaciones(conn):
    """Elimina todas las evaluaciones (para recargar desde cero)."""
    conn.execute("DELETE FROM evaluaciones")
    # reinicia la numeración de los id para que vuelvan a empezar en 1
    conn.execute("DELETE FROM sqlite_sequence WHERE name = 'evaluaciones'")
    conn.commit()
