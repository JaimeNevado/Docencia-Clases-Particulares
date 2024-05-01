def asignar_grupos(lista_nombres):
    grupo_a = []
    grupo_b = []
    grupo_c = []

    for i, nombre in enumerate(lista_nombres):
        if i % 3 == 0:
            grupo_a.append(nombre)
        elif i % 3 == 1:
            grupo_b.append(nombre)
        else:
            grupo_c.append(nombre)

    return grupo_a, grupo_b, grupo_c

nombres_alumnos = ["Juan", "María", "Pedro", "Ana", "Luisa", "Carlos", "Eva", "Pablo", "Sofía"]

grupo_a, grupo_b, grupo_c = asignar_grupos(nombres_alumnos)

print("Grupo A:", grupo_a)
print("Grupo B:", grupo_b)
print("Grupo C:", grupo_c)
