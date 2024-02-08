def escribirTriangulo2(tam):
    for i in range(tam):
        for j in range(tam):
            if i <= j:
                print("*", end=" ")
        print()

tamano_cuadrado = int(input("Ingrese el tamaño del triángulo: "))

escribirTriangulo2(tamano_cuadrado)
