"""
calcular_promedio()
determinar_estado() # Aprobado o Desaprobado
mostrar_resultados

ejemplo:
Ingresar 3 notas
Nota 01: 15
Nota 02: 18
Nota 03: 14

Promedio: 15.67
Estado: Aprobado
"""
from promedio import (calcular_promedio,
                      determinar_estado,
                      mostrar_resultados
                      )

nombre = "Juan"
prom = calcular_promedio(15,18,14)
esta = determinar_estado(prom)
mostrar_resultados(nombre,prom,esta)