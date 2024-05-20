def imprimir_cuadrado(tamano):
    for i in range(tamano):
        for j in range(tamano):
            print('*', end=' ')
        print()  # Nueva línea después de cada fila

# Ejemplo de uso
tamano = 3
imprimir_cuadrado(tamano)
