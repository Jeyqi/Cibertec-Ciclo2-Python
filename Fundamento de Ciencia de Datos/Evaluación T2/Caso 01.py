import matplotlib.pyplot as plt

# Lista de productos disponibles en la tienda
productos = [
    {"Venta": "V001", "Producto": "Laptop", "Sucursal": "Lima", "Unidades": 2, "Precio unitario S/.": 2500},
    {"Venta": "V002", "Producto": "Mouse", "Sucursal": "Lima", "Unidades": 10, "Precio unitario S/.": 1500},
    {"Venta": "V003", "Producto": "Laptop", "Sucursal": "Callao", "Unidades": 1, "Precio unitario S/.": 1200},
    {"Venta": "V004", "Producto": "Teclado", "Sucursal": "Lima", "Unidades": 5, "Precio unitario S/.": 2500},
    {"Venta": "V005", "Producto": "Mouse", "Sucursal": "Callao", "Unidades": 8, "Precio unitario S/.": 1500},
    {"Venta": "V006", "Producto": "Monitor", "Sucursal": "Lima", "Unidades": 3, "Precio unitario S/.": 1200},
    {"Venta": "V007", "Producto": "Teclado", "Sucursal": "Callao", "Unidades": 4, "Precio unitario S/.": 2500},
    {"Venta": "V008", "Producto": "Monitor", "Sucursal": "Callao", "Unidades": 2, "Precio unitario S/.": 1500},
    {"Venta": "V009", "Producto": "Laptop", "Sucursal": "Lima", "Unidades": 1, "Precio unitario S/.": 1200},
    {"Venta": "V010", "Producto": "Mouse", "Sucursal": "Lima", "Unidades": 15, "Precio unitario S/.": 2500}
]

# 1. Calcular el ingreso de cada venta
for producto in productos:
    producto["Ingreso"] = producto["Unidades"] * producto["Precio unitario S/."]

#Obtener los ingresos totales por producto y sucursal
ingresos_por_producto = {}
ingresos_por_sucursal = {}

for producto in productos:
    prod = producto["Producto"]
    suc = producto["Sucursal"]
    ingreso = producto["Ingreso"]

    # Acumular por producto
    if prod not in ingresos_por_producto:
        ingresos_por_producto[prod] = 0
    ingresos_por_producto[prod] += ingreso

    # Acumular por sucursal
    if suc not in ingresos_por_sucursal:
        ingresos_por_sucursal[suc] = 0
    ingresos_por_sucursal[suc] += ingreso

# 3. Iidentificar el producto que genera más ingresos y la sucursal con más facturación
producto_mas_ingresos = max(ingresos_por_producto.items(), key=lambda x: x[1])
sucursal_mas_ingresos = max(ingresos_por_sucursal.items(), key=lambda x: x[1])

print(f"Producto con más ingresos: {producto_mas_ingresos[0]} (S/. {producto_mas_ingresos[1]})")
print(f"Sucursal con más ingresos: {sucursal_mas_ingresos[0]} (S/. {sucursal_mas_ingresos[1]})")

# 4. Generar el gráfico de barras usando únicamente el diccionario de productos
plt.figure(figsize=(10, 6))
plt.bar(ingresos_por_producto.keys(), ingresos_por_producto.values(), color='royalblue')
plt.xlabel("Producto")
plt.ylabel("Ingreso Total (S/.)")
plt.title("Comparación de Ingresos por Producto")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()