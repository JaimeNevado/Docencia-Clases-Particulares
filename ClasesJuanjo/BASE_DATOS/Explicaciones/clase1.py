import sqlite3

conexion = sqlite3.connect("datos.db")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS personas (
    Nombre TEXT,
    Apellido TEXT,
    Edad INTEGER
)
""")

# Primera forma
cursor.execute("""
INSERT INTO personas VALUES
    ('Jaime', 'Garcia', 19),
    ('Juan', 'Sanchez', 20),
    ('Paco', 'Luis', 20)
""")


# Segunda forma
nombre = "Alberto"
apellido = "Ramirez"
cursor.execute("""
INSERT INTO personas VALUES
    (?, ?, ?)
""", (nombre, apellido, 20)
)



cursor.execute("""
SELECT * FROM personas WHERE Edad = 20
""")
datos = cursor.fetchall()

print(datos)

conexion.commit()
conexion.close()


