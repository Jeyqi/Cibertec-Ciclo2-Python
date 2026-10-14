"""
CustomerVoice AI - menú interactivo para operar el sistema (CRUD manual).
Ejecutar primero main.py para cargar los datos iniciales.
"""
from datetime import date
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Datos import db
from Servicios import ingesta, modelo_ia, reportes


def mostrar(filas):
    if not filas:
        print("   (sin resultados)")
        return
    for id_, fecha, cliente, nota, sentimiento, flag, comentario in filas:
        alerta = " ⚠" if flag else ""
        texto = comentario if len(comentario) <= 55 else comentario[:52] + "..."
        print(f"   #{id_:<4} {fecha}  {cliente}  nota {nota:>2}  {sentimiento or '---':<3}{alerta}  {texto}")


def pedir_id(mensaje):
    valor = input(mensaje).strip()
    return int(valor) if valor.isdigit() else None


def registrar(conn):
    cliente = input("   Código de cliente (ej. C041): ").strip().upper()
    nota = input("   Nota (1-10): ").strip()
    comentario = input("   Comentario: ").strip()

    registro, error = ingesta.validar_fila({
        "cliente_id": cliente, "fecha": str(date.today()), "nota": nota,
        "comentario": comentario, "sentimiento_real": "",
    })
    if error or not cliente:
        print(f"   No se registró: {error or 'cliente vacío'}")
        return

    print("   Analizando comentario...")
    sentimiento, score = modelo_ia.analizar([registro["comentario"]])[0]
    registro.update(
        sentimiento_modelo=sentimiento, score=float(score),
        flag=int(modelo_ia.calcular_flag(registro["nota"], sentimiento)),
    )
    nuevo_id = db.insertar_val_manual(conn, registro)
    print(f"   Registrada #{nuevo_id}: {sentimiento} ({score:.2f})"
          + ("  ⚠ ALERTA: la nota contradice el comentario" if registro["flag"] else ""))


def modificar_nota(conn):
    id_ = pedir_id("   Id de la evaluación: ")
    fila = db.obtener_evaluacion(conn, id_) if id_ else None
    if not fila:
        print("   No existe esa evaluación")
        return
    mostrar([fila])
    nota = input("   Nueva nota (1-10): ").strip()
    if not nota.isdigit() or not 1 <= int(nota) <= 10:
        print("   Nota inválida")
        return
    flag = modelo_ia.calcular_flag(int(nota), fila[4])
    db.actualizar_nota(conn, id_, int(nota), int(flag))
    print("   Nota actualizada" + ("  ⚠ ahora genera alerta" if flag else ""))


def eliminar(conn):
    id_ = pedir_id("   Id de la evaluación: ")
    fila = db.obtener_evaluacion(conn, id_) if id_ else None
    if not fila:
        print("   No existe esa evaluación")
        return
    mostrar([fila])
    if input("   ¿Eliminar? (s/n): ").strip().lower() == "s":
        db.eliminar_evaluacion(conn, id_)
        print("   Eliminada")


def main():
    try:
        conn = db.conectar()
    except Exception as e:
        print(f"No se pudo conectar a MySQL: {e}")
        return
        
    db.crear_tablas(conn)
    opciones = {
        "1": ("Listar últimas evaluaciones", lambda: mostrar(db.listar_evaluaciones(conn))),
        "2": ("Ver alertas", lambda: mostrar([f for f in db.listar_evaluaciones(conn, 10000) if f[5]])),
        "3": ("Registrar nueva evaluación", lambda: registrar(conn)),
        "4": ("Modificar nota", lambda: modificar_nota(conn)),
        "5": ("Eliminar evaluación", lambda: eliminar(conn)),
        "6": ("Generar reporte TXT", lambda: print(f"   Guardado en: {reportes.generar_reporte(conn)}")),
    }
    while True:
        print("\n=== CUSTOMERVOICE AI ===")
        for clave, (texto, _) in opciones.items():
            print(f" {clave}. {texto}")
        print(" 0. Salir")
        opcion = input("Opción: ").strip()
        if opcion == "0":
            break
        if opcion in opciones:
            opciones[opcion][1]()
        else:
            print("   Opción no válida")
    conn.close()


if __name__ == "__main__":
    main()
