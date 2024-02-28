import random
import matplotlib.pyplot as plt

def suma_matrices(matriz1, matriz2):

    resultado = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    return resultado

def multiplicacion_matrices(matriz1, matriz2):
    """
    Función para multiplicar dos matrices.
    """
    resultado = []
    for i in range(3):
        fila = []
        for j in range(3):
            suma = 0
            for k in range(3):
                suma += matriz1[i][k] * matriz2[k][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

def generar_matriz():
    """
    Función para generar una matriz aleatoria.
    """
    matriz = []
    for _ in range(3):
        fila = [random.randint(1, 10) for _ in range(3)]
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    """
    Función para mostrar una matriz.
    """
    for fila in matriz:
        print(fila)

def grafico_suma_filas(matriz):
    """
    Función para graficar la suma de las filas de una matriz.
    """
    suma_filas = [sum(fila) for fila in matriz]

    plt.bar(range(3), suma_filas)
    plt.xlabel('Fila')
    plt.ylabel('Suma de elementos')
    plt.title('Suma de los elementos por fila')
    plt.show()

def generar_numero_aleatorio():
    """
    Función para generar un número aleatorio.
    """
    return random.randint(1, 100)

def menu():
    """
    Función que muestra el menú y permite al usuario seleccionar una opción.
    """
    print("\nMenú:")
    print("1. Sumar matrices")
    print("2. Multiplicar matrices")
    print("3. Representar gráficamente la suma de las filas de una matriz")
    print("4. Generar número aleatorio")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

# Bucle principal del programa
while True:
    opcion = menu()

    if opcion == "1":
        print("\nGenerando matrices aleatorias...")
        matriz1 = generar_matriz()
        matriz2 = generar_matriz()

        print("\nMatriz 1:")
        mostrar_matriz(matriz1)
        print("\nMatriz 2:")
        mostrar_matriz(matriz2)

        resultado = suma_matrices(matriz1, matriz2)
        print("\nResultado de la suma:")
        mostrar_matriz(resultado)

    elif opcion == "2":
        print("\nGenerando matrices aleatorias...")
        matriz1 = generar_matriz()
        matriz2 = generar_matriz()

        print("\nMatriz 1:")
        mostrar_matriz(matriz1)
        print("\nMatriz 2:")
        mostrar_matriz(matriz2)

        resultado = multiplicacion_matrices(matriz1, matriz2)
        print("\nResultado de la multiplicación:")
        mostrar_matriz(resultado)

    elif opcion == "3":
        print("\nGenerando matriz aleatoria...")
        matriz = generar_matriz()
        print("\nMatriz:")
        mostrar_matriz(matriz)

        grafico_suma_filas(matriz)

    elif opcion == "4":
        numero_aleatorio = generar_numero_aleatorio()
        print(f"\nNúmero aleatorio generado: {numero_aleatorio}")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
