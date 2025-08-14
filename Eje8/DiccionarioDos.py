DiccionarioDos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del producto {i+1}: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    cantidad = int(input(f"Ingrese la cantidad de {nombre}: "))
    DiccionarioDos[nombre] = (precio, cantidad)

print("\nLista de productos:")
for producto, datos in DiccionarioDos.items():
    print(f"Producto: {producto}")
    print(f"Precio: ${datos[0]:.2f}")
    print(f"Cantidad: {datos[1]}")
    print("-" * 30)

#Valor total del diccionario
valor_total = sum(datos[0] * datos[1] for datos in DiccionarioDos.values())
print(f"\nValor total del DiccionarioDos: ${valor_total:.2f}")