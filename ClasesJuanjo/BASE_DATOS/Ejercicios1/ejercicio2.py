import sqlite3

# Conexión a la base de datos (se crea automáticamente si no existe)
conexion = sqlite3.connect("empleados.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    nombre TEXT,
    apellido TEXT,
    carrera TEXT,
    salario INTEGER
)
""")

cursor.execute("""
INSERT INTO empleados VALUES
    ('Raul', 'Sanchez', 'Derecho', 34000),
    ("Alicia", "Martinez", "Ingeniería", 51000),
    ("David", "García", "Ventas", 48000)
""")

conexion.commit()

# Extraer y mostrar los nombres
cursor.execute("SELECT nombre FROM empleados WHERE salario > 50000")
nombres_extraidos = cursor.fetchall()

print("Nombres de personas que ganan más de 50000")
for nombre in nombres_extraidos:
    print(nombre[0])

# Cerrar la conexión a la base de datos
conexion.close()
