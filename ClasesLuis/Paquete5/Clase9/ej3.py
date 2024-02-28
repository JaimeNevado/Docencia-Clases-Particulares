import matplotlib.pyplot as plt

y = [0, 0, 0, 0, 0, 0]
x = ["ojo", "nariz", "boca", "oreja", "cuello", "cabeza"]
texto = ["ojo", "nariz", "piojo", "nariz", "boca", "pie", "cuello", "cabeza", "ojo", "ojo", "boca"]

for elemento in texto:
	if (elemento == "ojo"):
		y[0] = y[0] + 1
	elif (elemento == "nariz"):
		y[1] = y[1] + 1
	elif (elemento == "boca"):
		y[2] = y[2] + 1
	elif (elemento == "oreja"):
		y[3] = y[3] + 1
	elif (elemento == "cuello"):
		y[4] = y[4] + 1
	elif (elemento == "cabeza"):
		y[5] = y[5] + 1
	

plt.bar(x, y)

# Personalizar el gráfico
plt.title("Cantidad de veces que aparece una parte del cuerpo en un texto")
plt.xlabel("Parte del cuerpo")
plt.ylabel("Cantidad de veces")

# Mostrar el gráfico
plt.show()

