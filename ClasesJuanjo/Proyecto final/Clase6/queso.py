import matplotlib.pyplot as plt
import json 


archivo = open("stock.json","r")
lineas=json.load(archivo)


suma_toyota=0
suma_honda=0
suma_ford=0
suma_Chevrolet=0
suma_volkswagen=0

for elemento in lineas:
    suma_toyota = suma_toyota + elemento["Toyota"]
    suma_honda = suma_honda + elemento["Honda"]
    suma_ford = suma_ford + elemento["Ford"]
    suma_Chevrolet = suma_Chevrolet + elemento["Chevrolet"]
    suma_volkswagen = suma_volkswagen + elemento["Volkswagen"]


etiquetas = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen"]
valores = [suma_toyota, suma_honda, suma_ford, suma_Chevrolet, suma_volkswagen]


# Crear el grafico de queso
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)

# Añadir titulo
plt.title("Marca")


plt.show()
