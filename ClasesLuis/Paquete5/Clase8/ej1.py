def separar_numeros(matriz):
    lista_par = []
    lista_impar = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero = matriz[i][j]
            if numero % 2 == 0:
                lista_par.append(numero)
            else:
                lista_impar.append(numero)

    print("Lista de números pares:", lista_par)
    print("Lista de números impares:", lista_impar)

# Ejemplo de uso:
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

separar_numeros(matriz_ejemplo)
