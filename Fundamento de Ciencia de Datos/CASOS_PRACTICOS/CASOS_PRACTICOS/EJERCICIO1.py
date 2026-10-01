ventas=[]

for i in range(5):
    venta=float(input(f"Ingrese la venta del dia:{i+1}: S/."))
    ventas.append(venta)
    
total=sum(ventas)
promedio=total/len(ventas)
mayor=max(ventas)
menor=min(ventas)

print("\n resultados")
print(f"Total de ventas:S/. {total:.2f}")
print(f"Promedio de ventas: S/. {promedio:.2f}")
print(f"Venta mayor : S/. {mayor:.2f}")
print(f"Venta menor : S/. {menor:.2f}")

if promedio >=200:
    print("Conclusion:Buen nivel de ventas")
else:
    print("Conclusion: Se deben mejorar las ventas")