import matplotlib.pyplot as plt

# Datos
lista = [1, 2, 3, 4, 5, 6]
nombres = ["2ºA", "2ºB", "3ºA", "3ºB", "4ºA", "4ºB"]


plt.bar(lista, lista)



# Personalizar el gráfico
plt.title('Cantidad de alumnos en la ESO')
plt.xlabel('Curso')
plt.ylabel('Alumnos')

# Mostrar el gráfico
plt.show()

