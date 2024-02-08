def escribirMatriz(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			print(matriz[i][j], end=' ')
		print()


def es_no_negativa_y_menor_que_100(matriz):
	estado = True
	for fila in matriz:
		for elemento in fila:
			if elemento < 0 or elemento >= 100:
				estado = False
	return estado

def suma_fila_igual_a_100(matriz):
    estado = True
    for fila in matriz:
        suma_fila = sum(fila)
        if suma_fila != 100:
            estado = False
    return estado

def suma_columna_igual_a_100(matriz):
	estado = True
	for i in range(len(matriz)):
		suma_columna = 0
		for fila in matriz:
			suma_columna += fila[i]
		if suma_columna != 100:
			estado = False
	return estado

def verificar_doblemente_estocastica_normalizada(matriz):
    estado = False
    if es_no_negativa_y_menor_que_100(matriz) and suma_fila_igual_a_100(matriz) and suma_columna_igual_a_100(matriz):	
        estado = True
    return estado

# Ejemplo de uso:
matriz_ejemplo = [
    [20, 30, 50], 
    [50, 0, 50], 
    [30, 70, 0]
]

matriz_ejemplo2 = [
    [20, 30, 50], 
    [50, -5, 50], 
    [25, 75, 0]
]

resultado = verificar_doblemente_estocastica_normalizada(matriz_ejemplo)

print("La matriz de ejemplo es:")
escribirMatriz(matriz_ejemplo)

if (resultado):
	print("La matriz SI es doblemente estocástica normalizada")
else:
	print("La matriz NO es doblemente estocástica normalizada")
     
