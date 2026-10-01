#Fábrica registró la cantidad de productos defectuosos durante 8 días
import matplotlib.pyplot as plt

productos_defectuosos = [5, 4, 6, 5, 7, 4, 30, 6]
dias_defectuosos = list(range(1,9))


#Calcular Promedio, Mínimo, Máximo
promedio = sum(productos_defectuosos) / len(productos_defectuosos)
minimo = min(productos_defectuosos)
maximo = max(productos_defectuosos)

#Detectar los valores mayores a 10
outliers = []
for cantidad in productos_defectuosos:
    if cantidad > 10:
        outliers.append(cantidad)


#Imprimir outliers
print("Valores atípicos (productos defectuosos > 10):", outliers)

#Crear gráfico de productos defectuosos
plt.bar(dias_defectuosos, productos_defectuosos, color='red')
plt.title('Productos defectuosos durante 8 días')
plt.xlabel('Días')
plt.ylabel('Cantidad de productos defectuosos')
plt.xticks(dias_defectuosos)
plt.show()



'''
¿Existe un valor que se aleja considerablemente de los demás?
Sí.

¿Qué podría haber ocurrido en la fábrica ese día?
Podría haber ocurrido un problema en la línea de producción, como una falla en la maquinaria, un error humano, o un lote defectuoso 
de materiales que resultó en un aumento significativo de productos defectuosos ese día.

¿Se debería eliminar automáticamente ese dato? ¿Por qué?
No se debería eliminar automáticamente ese dato sin un análisis más profundo. Aunque es un valor atípico, podría proporcionar 
información valiosa sobre problemas en el proceso de producción. Es importante investigar la causa del aumento de productos defectuosos 
antes de decidir si se debe excluir el dato del análisis.
'''
