def TuplaDos():
    while True:
        nums = input("Ingresa 5 números separados por comas: ")
        num_list = nums.split(',')
        if len(num_list) == 5:
            num_tupla = tuple(int(num) for num in num_list)
            break
        else:
            print("Por favor ingresa exactamente 5 números")
    
    #Tupla a lista
    tupla_lista = list(num_tupla)
    nums = int(input("Ingresa un número para agregar a la tupla: "))
    tupla_lista.append(nums)
    
    #Lista a tupla de nuevo
    num_tupla = tuple(tupla_lista)

    print("Posisión 4 de la tupla:", num_tupla[4], "\nTotal elementos:", len(num_tupla))
TuplaDos()