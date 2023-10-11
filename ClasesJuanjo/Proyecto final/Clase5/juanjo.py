import matplotlib.pyplot as plt
etiquetas = ['clase1','clase2','clase3','clase4']

plt.xlabel("etiquetas")
plt.ylabel("valores")


listaClases = [
    {
        "clase1" : [8, 7, 2, 10, 6],
        "clase2" : [1, 4, 9, 3, 8],
        "clase3" : [3, 6, 9, 6, 10],
        "clase4" : [9, 7, 9, 10, 6],
        "clase5" : [5, 9, 9, 7, 5]
    }
]


media1= sum (listaClases[0]["clase1"])/len("clase1")
media2= sum (listaClases[0]["clase2"])/len("clase2")
media3= sum (listaClases[0]["clase3"])/len("clase3")
media4= sum (listaClases[0]["clase4"])/len("clase4")


valores = [media1,media2,media3,media4]
plt.bar(etiquetas, valores)

plt.show()

