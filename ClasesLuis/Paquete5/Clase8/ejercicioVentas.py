import matplotlib.pyplot as plt

# Datos de ejemplo: ventas mensuales de un producto
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
ventas_producto_A = [100, 120, 90, 110, 95]
ventas_producto_B = [110, 100, 105, 115, 120]

# Crear gráfico de barras
plt.bar(meses, ventas_producto_A, color='blue', label='Producto A')
plt.bar(meses, ventas_producto_B, color='red', label='Producto B', alpha=0.5)  # Usar transparencia

# Personalizar gráfico
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.title('Ventas mensuales por producto')
plt.legend()

# Mostrar gráfico
plt.show()
