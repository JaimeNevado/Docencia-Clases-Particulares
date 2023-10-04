import matplotlib.pyplot as plt

# Datos de ejemplo (reemplaza esto con tus propios datos)
etiquetas = ['A', 'B', 'C', 'D', 'E']
valores = [10, 24, 18, 32, 12]

# Crear el gráfico de barras
plt.bar(etiquetas, valores)

# Agregar etiquetas y título
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de Barras Ejemplo')

# Mostrar el gráfico
plt.show()
