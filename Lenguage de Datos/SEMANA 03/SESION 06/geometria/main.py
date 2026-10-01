from figuras import(
    area_rectangulo,
    area_triangulo,
    area_circulo
)

rectangulo = area_rectangulo(10,5)
triangulo = area_triangulo(20,4)
circulo = area_circulo(10)


print(f"El área de un rectangulo es: {rectangulo}")
print(f"El área de un triangulo es: {triangulo}")
print(f"El área del círculo es: {circulo:.2f}")