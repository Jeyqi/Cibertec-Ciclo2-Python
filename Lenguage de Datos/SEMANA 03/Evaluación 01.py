#SISTEMA DE ANÁLISIS DE VENTA

#Registro de productos

#Nombre del producto, precio y cantidad vendida

inventario = {}

while True:
    nombre_producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    if nombre_producto.lower() == 'salir':

        break
    
    precio_producto = float(input(f"Ingrese el precio del producto '{nombre_producto}': "))    

    cantidad_vendida = int(input(f"Ingrese la cantidad vendida del producto '{nombre_producto}': "))

    total_producto = precio_producto * cantidad_vendida

   
    inventario[nombre_producto] = {
    "precio": precio_producto,
    "cantidad": cantidad_vendida,
    "total": total_producto
        }

    
            
#Calcular total de ventas por producto
    total_ventas = precio_producto * cantidad_vendida
    print("Producto registrado correctamente.")
    print(f"Venta generada: S/.{total_ventas:.2f}\n")


#Calcular estadísticas de ventas

cantidad_productos = len(inventario)
total_unidades_vendidas = sum(producto["cantidad"] for producto in inventario.values())
total_ventas_generadas = sum(producto["total"] for producto in inventario.values())
promedio_venta_producto = total_ventas_generadas / cantidad_productos

#Producto con mayor venta
producto_mayor_venta= None
mayor_monto = 0

for producto, datos in inventario.items():
    if datos["total"] > mayor_monto:
        mayor_monto = datos["total"]
        producto_mayor_venta = producto

#Producto con menor venta
producto_menor_venta = None
menor_monto = float('inf')

for producto, datos in inventario.items():
    if datos["total"] < menor_monto:
        menor_monto = datos["total"]
        producto_menor_venta = producto

#Mostrar resultados
print("\n--- ESTADÍSTICAS GENERALES ---")
print(f"Cantidad de productos: {cantidad_productos}")
print(f"Total de unidades vendidas: {total_unidades_vendidas}")
print(f"Venta Total: S/.{total_ventas_generadas:.2f}")
print(f"Promedio por producto: S/.{promedio_venta_producto:.2f}\n")
print(f"Producto con mayor venta:\n {producto_mayor_venta}\nVenta: S/.{mayor_monto}")
print(f"Producto con menor venta:\n {producto_menor_venta}\nVenta: S/.{menor_monto}")


#Clasificar el rendimiento de la empresa según el total de monto de ventas generadas
if total_ventas_generadas > 10000:
    rendimiento = "Excelente Rendimiento"
elif total_ventas_generadas > 5000:
    rendimiento = "Rendimiento Aceptable"
else:
    rendimiento = "Rendimiento Bajo"

print("\n--- RENDIMIENTO DE LA EMPRESA---")
print(rendimiento)

#Buscar productos por nombre y mostrar sus estadísticas
while True:
    buscar_producto = input("\nIngrese el nombre del producto a buscar (o 'salir' para terminar): ")
    if buscar_producto.lower() == 'salir':
        break
    
    if buscar_producto in inventario:
        datos_producto = inventario[buscar_producto]
        print("\n--- BÚSQUEDA DE PRODUCTO ---")
        print("Producto encontrado:")
        print(f"Nombre: {buscar_producto}")
        print(f"Precio: S/.{datos_producto['precio']:.2f}")
        print(f"Cantidad: {datos_producto['cantidad']}")
        print(f"Venta: S/.{datos_producto['total']:.2f}")
    else:
        print("Producto no encontrado en el inventario.")

print("\n--- FIN DEL PROGRAMA ---")