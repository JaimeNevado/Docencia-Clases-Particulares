import sqlite3
import os

os.remove("pueblos_personas.db")

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

#Manera 2
lista_personas = [persona1, persona2, persona3]
cursor.executemany("INSERT INTO pueblos_personas (nombre, edad, pueblo) VALUES (?, ?, ?)", lista_personas)

conexion.commit()

print("----Menú----")
print("Selecciona una opción:")
print("1) Mostrar los habitantes de un pueblo ")
print("2) Mostrar las personas mayores de edad ")

eleccion = int(input())
pueblo = False

if (eleccion == 1):
    print("¿Qué pueblo desea investigar?")
    pueblo = input()
    if (pueblo.lower() == "pueblo a"):
        print("Las personas que habitan en el Pueblo A son:")
        cursor.execute("SELECT nombre, edad, pueblo FROM pueblos_personas WHERE pueblo = 'Pueblo A'")
        pueblo = True
    elif (pueblo.lower() == "pueblo b"):
        print("Las personas que habitan en el Pueblo B son:")
        cursor.execute("SELECT nombre, edad, pueblo FROM pueblos_personas WHERE pueblo = 'Pueblo B'")
        pueblo = True
    else:
        print("ERROR, el pueblo no existe")
elif (eleccion == 2):
    print("Las personas mayores de edad son:")
    cursor.execute("SELECT nombre, edad, pueblo FROM pueblos_personas WHERE edad > 18")
else:
    print("Eleccion inválida")

# Extraer y mostrar información de personas y sus pueblos
info_personas = cursor.fetchall()

# IMPORTANTE!!!
if (pueblo == True):
    cursor.execute("SELECT COUNT(*) FROM pueblos_personas WHERE pueblo = 'Pueblo A'")
    habitantes = cursor.fetchall()[0][0]
# IMPORTANTE!!!



print("Información de personas y sus pueblos:")
print("El pueblo tiene", habitantes, "habitantes")
for info in info_personas:
    print("Nombre:", info[0])
    print("Edad:", info[1])
    print("Pueblo:", info[2])
    print("---------------")

# Cerrar la conexión a la base de datos
conexion.close()
