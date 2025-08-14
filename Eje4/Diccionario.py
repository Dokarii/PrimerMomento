def dict():
    diccionario = {}
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    curso = input("Ingrese su curso: ")
    diccionario['Nombre'] = nombre
    diccionario['Edad'] = edad
    diccionario['Curso'] = curso

    print("\nDiccionario:")
    for clave, valor in diccionario.items():
        print(f'{clave}: {valor}')
dict()