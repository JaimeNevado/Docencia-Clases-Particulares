import matplotlib.pyplot as plt

# Datos
x = [0, 1, 2, 3, 4]
y = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

# Crear el diagrama de dispersión
plt.bar(x, y)



# Personalizar el gráfico
plt.title('Diagrama de Dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()

