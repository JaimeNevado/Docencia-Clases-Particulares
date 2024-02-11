import matplotlib.pyplot as plt

# Datos
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el diagrama de dispersión
plt.bar(x, y)



# Personalizar el gráfico
plt.title('Diagrama de Dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()
