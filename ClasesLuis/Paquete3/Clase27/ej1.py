def contar_letra_a(palabra):
    cantidad = 0;
    for letra in palabra:
        if (letra.lower() == "a"):
            cantidad = cantidad + 1
    return cantidad



print(contar_letra_a("Juana Antonia"))
# Escribe 4


