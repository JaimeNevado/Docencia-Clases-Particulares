import matplotlib.pyplot as plt


datosx = ["Peras", "Manzanas","Melocotones", "Fresas", "Sandias","Palinca"]

datosy = [7, 6, 9, 3, 4, 3]


plt.bar(datosx, datosy, color='red')
plt.title("Stock de frutas en la tienda")
plt.xlabel("Frutas")
plt.ylabel("Cantidad")

plt.yticks(rotation=45)

plt.grid(True)

plt.show()


