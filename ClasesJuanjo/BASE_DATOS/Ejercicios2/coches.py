import sqlite3

# Conectarse a la base de datos (se creará si no existe)
conexion = sqlite3.connect('coches.db')

# Crear una tabla llamada "coches"
conexion.execute('''
    CREATE TABLE IF NOT EXISTS coches (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        marca TEXT,
        modelo TEXT,
        combustible TEXT,
        año INTEGER
    )
''')

# Datos de ejemplo sobre coches
datos_coches = [
    ("Civic", "Honda", "Civic LX", "Gasolina", 2022),
    ("Corolla", "Toyota", "Corolla SE", "Híbrido", 2021),
    ("Golf", "Volkswagen", "Golf GTI", "Gasolina", 2020),
    ("Prius", "Toyota", "Prius Hybrid", "Híbrido", 2019),
    ("Mustang", "Ford", "Mustang GT", "Gasolina", 2022),
    # ... (otros datos)
]

# Insertar los datos en la tabla
for coche in datos_coches:
    conexion.execute('''
        INSERT INTO coches (nombre, marca, modelo, combustible, año)
        VALUES (?, ?, ?, ?, ?)
    ''', coche)

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

# Realizar una búsqueda por año y tipo de combustible
conexion = sqlite3.connect('coches.db')
año_buscado = 2022
combustible_buscado = "Gasolina"

consulta = '''
    SELECT nombre, marca, modelo, combustible, año
    FROM coches
    WHERE año = ? AND combustible = ?
'''

resultados = conexion.execute(consulta, (año_buscado, combustible_buscado)).fetchall()

resultados = conexion.execute("SELECT MAX(año) AS fecha_mas_antigua FROM coches")

# Mostrar los resultados
print("Resultados de búsqueda:")
for resultado in resultados:
    print("Nombre:", resultado[0])
    #print("Marca:", resultado[1])
    #print("Modelo:", resultado[2])
    #print("Combustible:", resultado[3])
    #print("Año:", resultado[4])
    print("------")

# Cerrar la conexión
conexion.close()
