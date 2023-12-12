def mostrar_menu():
    print("\n=== Menú ===")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver lista de tareas")
    print("4. Salir")

def agregar_tarea(tareas, nueva_tarea):
    tareas.append(nueva_tarea)
    print("Tarea agregada correctamente.")

def eliminar_tarea(tareas):
    tarea_eliminar = input("Ingrese la tarea que quieres eliminar: ")
    if (tarea_eliminar in tareas):
        tareas.remove(tarea_eliminar)
        print("Tarea eliminada correctamente.")
        estaEnLaLista = True
    else:
        print("La tarea no está en la lista")
        estaEnLaLista = False
    return estaEnLaLista
        


def ver_lista_tareas(tareas):
    print("\n=== Lista de Tareas ===")
    for elemento in tareas:
        print(elemento)


tareas = []

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        nueva_tarea = input("Ingrese la nueva tarea: ")
        agregar_tarea(tareas, nueva_tarea)
    elif opcion == "2":
        valor = eliminar_tarea(tareas)
        if (valor == False):
            break
    elif opcion == "3":
        ver_lista_tareas(tareas)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elija una opción válida.")
