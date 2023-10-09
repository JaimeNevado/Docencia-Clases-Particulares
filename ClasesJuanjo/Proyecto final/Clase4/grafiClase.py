import matplotlib.pyplot as plt

# Datos de ejemplo (reemplaza esto con tus propios datos)

listaClases = [
    {
        "clase1" : [8, 7, 9, 10, 6],
        "clase2" : [8, 7, 9, 10, 6],
        "clase3" : [8, 7, 9, 10, 6],
        "clase4" : [8, 7, 9, 10, 6],
        "clase5" : [8, 7, 9, 10, 6]
}
]

def media (notas):
    suma = 0
    for elemento in notas:
        suma = suma + elemento
    media = suma / len(notas)
    return media

etiquetas = ["clase1", "clase2", "clase3", "clase4", "clase5"]
valores = [media(listaClases[0]["clase1"]), 24, 18, 32, 7]

# Crear el gráfico de barras
plt.bar(etiquetas, valores)

# Agregar etiquetas y título
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras Ejemplo')

# Mostrar el gráfico
plt.show()
