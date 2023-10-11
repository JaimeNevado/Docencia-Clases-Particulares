import matplotlib.pyplot as plt

# Datos de ejemplo (reemplaza esto con tus propios datos)

listaClases = [
    {
        "clase1" : [8, 7, 2, 10, 6],
        "clase2" : [1, 4, 9, 3, 8],
        "clase3" : [3, 6, 9, 6, 10],
        "clase4" : [9, 7, 9, 10, 6],
        "clase5" : [5, 9, 9, 7, 5]
    }
]

def media (notas):
    suma = 0
    for elemento in notas:
        suma = suma + elemento
    media = suma / len(notas)
    return media

etiquetas = ["clase1", "clase2", "clase3", "clase4", "clase5"]
valores = [media(listaClases[0]["clase1"]), media(listaClases[0]["clase2"]) , media(listaClases[0]["clase3"]), media(listaClases[0]["clase4"]), media(listaClases[0]["clase5"])]

# Crear el gráfico de barras
plt.bar(etiquetas, valores)

# Agregar etiquetas y título
plt.xlabel('Nombre clases')
plt.ylabel('Nota Media')
plt.title('Gráfico de Notas Medias')

# Mostrar el gráfico
plt.show()
