"""
Implementación de IA en este archivo:
1. Estructuración del código: Organizó el código en secciones lógicas y bien comentadas
2. Manejo de errores: Implementó validaciones try-except para garantizar entradas correctas
3. Formato de salida: Sugirió una presentación clara de los resultados con mensajes descriptivos
4. Buenas prácticas: Implementó comentarios explicativos y una estructura modular del código
"""

def numero_enteros():
    # 5. Crear lista de 10 números enteros
    numeros = []
    print("Ingresa 10 números enteros:")
    for i in range(10):
        while True:
            try:
                num = int(input(f"Número #{i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor ingresa un número entero.")
    
    # 5.1 Imprimir todos los números uno por uno
    print("\nTodos los números ingresados:")
    for numero in numeros:
        print(numero)
    
    # 5.2 Imprimir solo los números mayores que 50
    print("\nNúmeros mayores que 50:")
    for numero in numeros:
        if numero > 50:
            print(numero)
    
    # 5.3 Añadir dos números decimales usando append y extend
    numeros.append(3.14)  # Añade un número decimal con append
    numeros.extend([2.718])  # Añade otro número decimal con extend
    
    # 5.4 Insertar 100.5 en la posición 3
    numeros.insert(2, 100.5)
    
    # 5.5 Eliminar el primer número por valor y el último por índice
    primer_numero = numeros[0]
    numeros.remove(primer_numero)  # Elimina el primer número por valor
    numeros.pop()  # Elimina el último número por índice
    
    # 5.6 Mostrar lista final y cantidad de elementos
    print("\nLista final:")
    print(numeros)
    print(f"Cantidad de elementos en la lista: {len(numeros)}")
    
    return numeros

# Ejecutar la función
print("\nEjecutando el programa:")
numero_enteros()