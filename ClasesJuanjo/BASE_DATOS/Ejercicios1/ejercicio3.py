import sqlite3

# Conexión a la base de datos (se crea automáticamente si no existe)
conexion = sqlite3.connect("pueblos_personas.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS pueblos_personas (
    nombre TEXT,
    edad INTEGER,
    pueblo TEXT
)
""")

# Agregar algunas personas a la base de datos
persona1 = ("Alicia", 25, "Pueblo A")
persona2 = ("Bárbara", 30, "Pueblo B")
persona3 = ("Carlos", 28, "Pueblo A")

##########
# Manera 1
cursor.execute("""
INSERT INTO pueblos_personas VALUES
    (?, ?, ?)
""", persona1
)
cursor.execute("""
INSERT INTO pueblos_personas VALUES
    (?, ?, ?)
""", persona2
)
cursor.execute("""
INSERT INTO pueblos_personas VALUES
    (?, ?, ?)
""", persona3
)

#################

#Manera 2
lista_personas = [persona1, persona2, persona3]
cursor.executemany("INSERT INTO pueblos_personas (nombre, edad, pueblo) VALUES (?, ?, ?)", lista_personas)

conexion.commit()

# Extraer y mostrar información de personas y sus pueblos
cursor.execute("SELECT nombre, edad, pueblo FROM pueblos_personas")
info_personas = cursor.fetchall()

print("Información de personas y sus pueblos:")
for info in info_personas:
    print("Nombre:", info[0])
    print("Edad:", info[1])
    print("Pueblo:", info[2])
    print("---------------")

# Cerrar la conexión a la base de datos
conexion.close()
