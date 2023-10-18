import matplotlib.pyplot as plt

# Datos de ejemplo
etiquetas = ['Manzanas', 'Plátanos', 'Cerezas', 'Dátiles']
valores = [15, 30, 45, 10]  # Valores que representan el tamaño de cada sector

# Crear el gráfico de queso
plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)

# Añadir título
plt.title('Ejemplo de gráfico de queso')

# Mostrar gráfico
plt.show()
