def contarLetra(palabra, letra):
    cantidad = 0;
    for elemento in palabra:
        if (elemento.lower() == letra.lower()):
            cantidad = cantidad + 1
    return cantidad



print(contarLetra("Juana Antonia", "p"))
# Escribe 0 porque no hay ninguna p




