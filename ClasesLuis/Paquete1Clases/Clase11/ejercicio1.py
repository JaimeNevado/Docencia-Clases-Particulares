numero_carnet = input("Escribe tu carnet de empleado: ")
# f2354

primera_letra = numero_carnet[0]

letraCambiada = primera_letra.lower()

if (letraCambiada == "e"):
    print("El carnet es Español")
elif (primera_letra.lower() == "p"):
    print("El carnet es Portugues")
elif (primera_letra.lower() == "f"):
    print("El carnet es Francés")
else:
    print("No se puede identificar el carnet")

