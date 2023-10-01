# Solicitar al usuario que ingrese su edad
edad = int(input("Por favor, ingresa tu edad: "))

# Determinar en qué grupo de edad se encuentra la persona y mostrar el mensaje correspondiente
if edad < 0:
    print("ERROR: La edad ingresada no es válida.")
else:
    if edad <= 17:
        print("Eres menor de edad.")
    else:
        if edad <= 64:
            print("Eres mayor de edad.")
        else:
            print("Eres un jubilado.")
