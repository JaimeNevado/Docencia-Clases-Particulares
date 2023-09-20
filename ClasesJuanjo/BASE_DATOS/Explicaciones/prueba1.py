import sqlite3

conexion = sqlite3.connect("datos.db")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
               first_name TEXT,
               last_name TEXT,
               age INTEGER
)
""")

#Primera manera
cursor.execute("""
INSERT INTO persons VALUES
('Pablo', 'GIL', 26),
('Guillermo', 'gil', 18)
""")

# Segunda manera
cursor.execute("""
INSERT INTO persons VALUES
(?, ?, ?)
"""
, ("juan", "gil", 13))

cursor.execute("""
SELECT * FROM persons
WHERE last_name LIKE 'gil'
""")
               
salidas = cursor.fetchall()
print(salidas)

for elemento in salidas:
    print("Nombre: ", elemento[0])

conexion.commit()
conexion.close()
