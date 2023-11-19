# Diccionario para almacenar la información de los empleados
datos_empleados = []

# Menú principal
while True:
    print("\nMenú de uso:")
    print("1) Añadir más empleados")
    print("2) Escribir TODOS los empleados")
    print("3) Escribir los empleados con una edad > 30 años")
    print("4) Salir del programa")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del empleado: ")
        edad = int(input("Ingrese la edad del empleado: "))
        empleado = {"nombre": nombre, "edad": edad}
        datos_empleados.append(empleado)
        print("Empleado agregado exitosamente.")
    elif opcion == '2':
        print("Listado de todos los empleados:")
        for empleado in datos_empleados:
            print("Nombre: {}, Edad: {}".format(empleado['nombre'], empleado['edad']))
    elif opcion == '3':
        print("Listado de empleados con edad mayor a 30:")
        for empleado in datos_empleados:
            if empleado['edad'] > 30:
                print("Nombre: {}, Edad: {}".format(empleado['nombre'], empleado['edad']))
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
