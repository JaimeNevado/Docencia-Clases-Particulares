mesas = []  # Inicializa la lista de mesas vacía

def mostrar_estado_mesas():
    print("\nEstado de las mesas:")
    i = 1
    for personas in mesas:
        estado = f"Mesa {i}: {personas}"
        print(estado)
        i += 1

def agregar_clientes(num_personas):
    if num_personas <= 4:
        nueva_mesa = {}
        i = 0
        while (i < num_personas):
            nombre = input("Ingrese el nombre de la persona: ")
            edad = int(input("Ingrese la edad de la persona: "))
            nueva_mesa[nombre] = edad
            i = i + 1
        mesas.append(nueva_mesa)
        print(f"Clientes añadidos a la Mesa {len(mesas)}.")
    else:
        print("Número de personas excede la capacidad máxima de la mesa (4).")

while True:
    print("\nMenú:")
    print("1. Mostrar estado de las mesas")
    print("2. Añadir clientes a una mesa")
    print("3. Salir")

    opcion = input("Selecciona una opción (1/2/3): ")

    if opcion == "1":
        mostrar_estado_mesas()
    elif opcion == "2":
        num_personas = int(input("Ingrese el número de personas para la mesa: "))
        agregar_clientes(num_personas)
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
