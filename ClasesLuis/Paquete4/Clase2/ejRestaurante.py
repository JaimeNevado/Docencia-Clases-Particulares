mesas = [0, 0, 0, 0, 0]  # Representa las mesas, donde 0 significa mesa libre


def mostrar_estado_mesas():
    print("\nEstado de las mesas:")
    i = 0
    for elemento in mesas:
        personas = elemento
        estado = f"Mesa {i + 1}: {personas} personas"
        print(estado)
        i = i + 1

def agregar_clientes(num_personas):
    i = 0
    while i < len(mesas):
        if mesas[i] == 0:  # La mesa está libre
            if num_personas <= 4:
                mesas[i] = num_personas
                print(f"Clientes añadidos a la Mesa {i + 1}.")
                return
            else:
                print("Número de personas excede la capacidad máxima de la mesa (4).")
                return
        i += 1
    print("Lo siento, no hay mesas disponibles en este momento.")



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
