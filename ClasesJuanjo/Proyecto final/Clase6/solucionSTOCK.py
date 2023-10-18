import json

import matplotlib.pyplot as plt


archivo = open("stock.json", "r")
datos = json.load(archivo)

etiquetas = ["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen"]
valores = [0, 0, 0, 0, 0]

for elemento in datos:
    valores[0] += elemento["Toyota"]
    valores[1] += elemento["Honda"]
    valores[2] += elemento["Ford"]
    valores[3] += elemento["Chevrolet"]
    valores[4] += elemento["Volkswagen"]

# Crear el gráfico de queso
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)

# Añadir título
plt.title('Ejemplo de gráfico de queso')

# Mostrar gráfico
plt.show()
