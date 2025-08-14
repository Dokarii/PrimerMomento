def ListaDecimales():
    lista = []
    for i in range(5):
        while True:
            num = float(input(f"Ingrese el número decimal #{i+1}: "))
            lista.append(num)
            break
    print(f'Promedio: {sum(lista)/len(lista)}')
    print(f'Numero máximo: {max(lista)}')
    print(f'Numero mínimo: {min(lista)}')

    sorteo = sorted(lista)
    print(f'Lista ordenada: {sorteo}')

ListaDecimales()