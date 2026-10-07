# presentacion/menu.py

from servicios.producto_service import (
    obtener_productos,
    agregar_producto,
    eliminar_producto
)


def mostrar_encabezado():
    """Muestra el título del sistema."""
    print("\n========================================")
    print("         SISTEMA DE PRODUCTOS           ")
    print("========================================")


def mostrar_opciones():
    """Imprime el menú principal de opciones."""
    print("\n1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Eliminar producto")
    print("0. Salir")


def opcion_agregar_producto():
    """Solicita los datos del producto al usuario y llama al servicio."""
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    codigo = input("Ingrese el código del producto: ").strip()

    if not codigo:
        print(" Error: El código no puede estar vacío.")
        return

    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print(" Error: El nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese la cantidad en stock: "))
    except ValueError:
        print(" Error: El precio debe ser decimal y el stock un número entero.")
        return

    exito = agregar_producto(codigo, nombre, precio, stock)
    if exito:
        print(f" Producto '{nombre}' agregado exitosamente.")
    else:
        print(f" Error: Ya existe un producto registrado con el código '{codigo}'.")


def opcion_mostrar_productos():
    """Lista todos los productos registrados."""
    print("\n--- LISTA DE PRODUCTOS ---")
    lista = obtener_productos()

    if not lista:
        print("No hay productos registrados en el sistema.")
        return

    print(f"{'CÓDIGO':<10} | {'NOMBRE':<20} | {'PRECIO (S/)':<12} | {'STOCK':<10}")
    print("-" * 60)
    for producto in lista:
        print(f"{producto['codigo']:<10} | {producto['nombre']:<20} | S/{producto['precio']:<10.2f} | {producto['stock']:<10}")

     #Cuando ponemos :<10 o :<20 es para alinear el texto a la izquierda y reservar un espacio de 10 o 20 caracteres respectivamente. 
     # Esto ayuda a que la salida sea más legible y organizada, especialmente cuando se muestran listas de datos en columnas.   
     #Es para darle una impresión más profesional y ordenada.


def opcion_eliminar_producto():
    """Pide el código al usuario y elimina el producto."""
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()

    if eliminar_producto(codigo):
        print(f" Producto con código '{codigo}' eliminado correctamente.")
    else:
        print(f" Error: No se encontró ningún producto con el código '{codigo}'.")


def ejecutar_menu():
    """Bucle principal de ejecución del menú."""
    mostrar_encabezado()
    while True:
        mostrar_opciones()
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            opcion_agregar_producto()
        elif opcion == "2":
            opcion_mostrar_productos()
        elif opcion == "3":
            opcion_eliminar_producto()
        elif opcion == "0":
            print("\n¡Gracias por usar el Sistema de Productos! Hasta luego.")
            break
        else:
            print(" Opción no válida. Por favor, intente de nuevo.")