def EjercicioTupla():
    nums = input("Ingresa 4 números separados por comas: ")
    num_tuple = tuple(int(num) for num in nums.split(','))
    print("Tupla original:", num_tuple)

    print("Numero mayor de la tupla:", max(num_tuple))
    print("Numero menor de la tupla:", min(num_tuple))
    print("Promedio de los números:", sum(num_tuple) / len(num_tuple))

EjercicioTupla()