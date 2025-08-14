def mostrar_menu():
    print("\n=== GESTIÓN DE NÚMEROS ===")
    print("1. Añadir un número")
    print("2. Insertar un número en posición específica")
    print("3. Eliminar por valor")
    print("4. Eliminar por índice")
    print("5. Mostrar lista")
    print("6. Salir")

def añadir_numero(lista):
    while True:
        try:
            tipo = input("¿Qué tipo de número deseas añadir? (1: entero, 2: decimal): ")
            if tipo == "1":
                numero = int(input("Ingresa un número entero: "))
            elif tipo == "2":
                numero = float(input("Ingresa un número decimal: "))
            else:
                print("Opción no válida")
                continue
            lista.append(numero)
            print(f"Número {numero} añadido exitosamente")
            break
        except ValueError:
            print("Error: Ingresa un número válido")

def insertar_numero(lista):
    if not lista:
        print("La lista está vacía. Usa la opción 1 para añadir números primero.")
        return
    
    print(f"Posiciones disponibles: 0 a {len(lista)}")
    while True:
        try:
            posicion = int(input("Ingresa la posición donde deseas insertar: "))
            if posicion < 0 or posicion > len(lista):
                print(f"Error: La posición debe estar entre 0 y {len(lista)}")
                continue
            
            tipo = input("¿Qué tipo de número deseas insertar? (1: entero, 2: decimal): ")
            if tipo == "1":
                numero = int(input("Ingresa un número entero: "))
            elif tipo == "2":
                numero = float(input("Ingresa un número decimal: "))
            else:
                print("Opción no válida")
                continue
            
            lista.insert(posicion, numero)
            print(f"Número {numero} insertado en la posición {posicion}")
            break
        except ValueError:
            print("Error: Ingresa números válidos")

def eliminar_valor(lista):
    if not lista:
        print("La lista está vacía")
        return
    
    print("Lista actual:", lista)
    while True:
        try:
            valor = float(input("Ingresa el valor a eliminar: "))
            if valor in lista:
                lista.remove(valor)
                print(f"Valor {valor} eliminado exitosamente")
                break
            else:
                print("El valor no se encuentra en la lista")
                break
        except ValueError:
            print("Error: Ingresa un número válido")

def eliminar_indice(lista):
    if not lista:
        print("La lista está vacía")
        return
    
    print(f"Índices disponibles: 0 a {len(lista)-1}")
    print("Lista actual:", lista)
    while True:
        try:
            indice = int(input("Ingresa el índice del elemento a eliminar: "))
            if 0 <= indice < len(lista):
                valor = lista.pop(indice)
                print(f"Elemento {valor} en índice {indice} eliminado exitosamente")
                break
            else:
                print(f"Error: El índice debe estar entre 0 y {len(lista)-1}")
        except ValueError:
            print("Error: Ingresa un número válido")

def mostrar_lista(lista):
    if not lista:
        print("La lista está vacía")
    else:
        print("\nLista actual:")
        for i, valor in enumerate(lista):
            print(f"Índice {i}: {valor}")

def main():
    lista_numeros = []
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "1":
            añadir_numero(lista_numeros)
        elif opcion == "2":
            insertar_numero(lista_numeros)
        elif opcion == "3":
            eliminar_valor(lista_numeros)
        elif opcion == "4":
            eliminar_indice(lista_numeros)
        elif opcion == "5":
            mostrar_lista(lista_numeros)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

if __name__ == "__main__":
    main()