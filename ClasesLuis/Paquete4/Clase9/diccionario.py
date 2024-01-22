def escribir_datos(corcho):
    # corcho es una LISTA!!
    # corcho = [persona1, persona2, persona3]
    persona1 = corcho[0]
    print(f"Hola, soy {persona1['Nombre']} tengo {persona1['Edad']} años y mido {persona1['Altura']}")


persona1 = {
    "Nombre" : "Luis",
    "Edad" : 13,
    "Altura" : 1.80
}

persona2 = {
    "Nombre" : "Jaime",
    "Edad" : 20,
    "Altura" : 1.80
}

persona3 = {
    "Nombre" : "Angel",
    "Edad" : 24,
    "Altura" : 1.80
}


lista = [persona1, persona2, persona3]

escribir_datos(lista)
