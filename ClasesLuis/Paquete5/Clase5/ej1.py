def escribirCuadrado(tam):
    for i in range(tam):
        for j in range(tam):
            if (i == 0 or j == 0 or i == tam - 1 or j == tam - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
                
        print()

tamano_cuadrado = int(input("Ingrese el tamaño del cuadrado: "))

escribirCuadrado(tamano_cuadrado)
