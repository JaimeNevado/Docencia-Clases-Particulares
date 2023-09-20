import sqlite3

# Conexión a la base de datos (se crea automáticamente si no existe)
conexion = sqlite3.connect("usuarios.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear la tabla de usuarios si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER,
    nombre TEXT,
    edad INTEGER
)
""")

cursor.execute("""
INSERT INTO usuarios VALUES
    (1, 'Pablo', 19),
    (2, 'Juan', 20),
    (3, 'Paco', 20)
""")

conexion.commit()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print("ID:", usuario[0])
    print("Nombre:", usuario[1])
    print("Edad:", usuario[2])
    print("---------------")

conexion.close()
