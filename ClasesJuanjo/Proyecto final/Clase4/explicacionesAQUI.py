import matplotlib.pyplot as plt

etiquetas = ["num_def", "num_cases", "num_hosp", "num_uci"]
valores = [num1, 15, 20, 13]

plt.bar(etiquetas, valores)

plt.xlabel("Tipo de casos") 
plt.ylabel("Numero de enfermos")
plt.title("Casos en Malaga los lunes")

plt.show()