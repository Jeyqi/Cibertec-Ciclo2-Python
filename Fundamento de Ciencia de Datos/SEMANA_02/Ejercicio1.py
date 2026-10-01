import matplotlib.pyplot as plt

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

ventas = [120, 150, 100, 180, 250, 300, 200]

print("Ventas de la semana")
print("Venta máxima:", max(ventas))
print("Venta mínima:", min(ventas))
print("Venta Total:", sum(ventas))

print("Venta promedio:", sum(ventas) / len(ventas))
