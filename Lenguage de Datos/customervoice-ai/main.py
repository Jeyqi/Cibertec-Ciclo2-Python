import sys
import os

DIRECTORIO_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
if DIRECTORIO_RAIZ not in sys.path:
    sys.path.insert(0, DIRECTORIO_RAIZ)

from Datos import db
from Servicios import reportes


def menu_listar(conn):
    print("\n--- ÚLTIMAS EVALUACIONES REGISTRADAS (3FN) ---")
    registros = db.listar_evaluaciones(conn)
    if not registros:
        print("   (sin actualización reciente)")
        return
    for anio, dni, marca, modelo, score, estado in registros:
        print(f"[{anio}] Cliente DNI: {dni} | {marca} {modelo} | Score: {score}/10 | Estado: {estado}")


def menu_alertas(conn):
    print("\n--- ALERTAS POR BAJO SCORE REGISTRADAS ---")
    alertas = db.obtener_alertas(conn)
    if not alertas:
        print("   (sin resultados)")
        return
    for anio, dni, score, estado, comentario in alertas:
        print(f"[{anio}] DNI: {dni} | Score: {score}/10 | Estado: {estado}")
        print(f"   Comentario: \"{comentario}\"")


def main():
    try:
        conn = db.conectar()
    except Exception as e:
        print(f"[ERROR] Conexión fallida a MySQL: {e}")
        return
        
    while True:
        print("\n=== CUSTOMERVOICE AI - REPOSITORIO 3FN ===")
        print("1. Listar últimas evaluaciones")
        print("2. Ver alertas")
        print("3. Registrar nueva evaluación")
        print("4. Modificar nota")
        print("5. Eliminar evaluación")
        print("6. Generar reporte consolidado TXT (3 Criterios)")
        print("0. Salir")
        opcion = input("Opción: ").strip()
        
        if opcion == "1": 
            menu_listar(conn)
        elif opcion == "2": 
            menu_alertas(conn)
        elif opcion == "3":
            print("\n--- REGISTRAR NUEVA EVALUACIÓN MANUAL ---")
            try:
                datos = {
                    "dni": input("Ingrese DNI del Cliente: ").strip(),
                    "marca": input("Ingrese Marca del Auto: ").strip(),
                    "modelo": input("Ingrese Modelo del Auto: ").strip(),
                    "estado_comercial": input("Ingrese Estado Comercial: ").strip(),
                    "precio_lista": float(input("Ingrese Precio de Lista ($): ") or 0),
                    "nota": int(input("Ingrese Nota NPS (1 al 10): ")),
                    "comentario": input("Ingrese Comentario/Feedback: ").strip()
                }
                if db.registrar_nueva_evaluacion_manual(conn, datos):
                    print("   ¡Evaluación guardada exitosamente en MySQL!")
            except ValueError:
                print("   [ERROR] Entrada inválida.")
        elif opcion == "4":
            print("\n--- MODIFICAR NOTA DE EVALUACIÓN ---")
            if db.modificar_nota_evaluacion(conn, input("DNI Cliente: "), int(input("Nueva Nota (1-10): "))):
                print("   ¡Nota actualizada con éxito!")
        elif opcion == "5":
            print("\n--- ELIMINAR EVALUACIÓN ---")
            if db.eliminar_evaluacion_por_lead(conn, input("DNI Cliente a eliminar: ")):
                print("   ¡Registro eliminado correctamente!")
        elif opcion == "6":
            print("\n[PROCESANDO IA] Analizando el repositorio completo bajo los 3 criterios. Por favor espere...")
            r_sat = reportes.generar_reporte(conn)
            print(f"\n[ÉXITO] Datos consolidados extraídos de MySQL:")
            print(f"  -> Reporte Unificado (3 Criterios): {r_sat}")
        elif opcion == "0": 
            break
    conn.close()


if __name__ == "__main__":
    main()
