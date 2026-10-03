import matplotlib.pyplot as plt

institutos = ["SENATI", "CIBERTEC", "IDAT", "TECSUP"]

matricula = [300, 350, 300, 500]
mensualidad = [400, 500, 450, 750]

costo_4_meses = []

for precio in mensualidad:
    costo = precio * 4
    costo_4_meses.append(costo)

print("DASHBOARD DE LOS PAGOS DE INSTITUTOS")
print("===================================")

for i in range(len(institutos)):
    print (institutos[i])
    print("Matricula es : S/.", matricula[i])
    print("Mensualidad es : S/.", mensualidad[i])
    print("4 mensualidades son: S/.", costo_4_meses[i])

plt.bar(institutos,mensualidad)
plt.title("Comparación de mensualidades")
plt.xlabel("Institutos")
plt.ylabel("Mensualidad S/.")
plt.show()