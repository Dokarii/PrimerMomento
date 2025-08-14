def clasificar_edad() -> str:
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
    except ValueError as e:
        return f"Error: {str(e)}"
    
    if edad < 12:
        return "Niño"
    elif edad <= 17:
        return "Adolescente"
    elif edad <= 64:
        return "Adulto"
    else:
        return "Adulto mayor"
    
print(clasificar_edad())