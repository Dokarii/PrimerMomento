frutas = []

print("Ingresa 5 frutas:")
for i in range(5):
    fruta = input(f"Ingresa la fruta #{i+1}: ")
    frutas.append(fruta)

# Convertir a mayúsculas y sortear
frutas_ordenadas = sorted([fruta.upper() for fruta in frutas])

# Mostrar la lista sorteda
print("\nLista de frutas en mayúsculas y orden:")
for fruta in frutas_ordenadas:
    print(fruta)

import os
if not os.path.exists('Saves'):
    os.makedirs('Saves')

# Guardar la lista el archivo
with open('Ejej2/Saves/frutas.txt', 'w') as archivo:
    for fruta in frutas_ordenadas:
        archivo.write(fruta + '\n')

print("\nListo. La lista (valga la redundancia) de frutas ha sido guardada.")
