import sqlite3
import os

def escribir(resultado):
    for elemento in resultado:
        print(elemento)

os.remove("canciones.db")

# Conectarse a la base de datos (se creará si no existe)
conexion = sqlite3.connect('canciones.db')

cursor = conexion.cursor()

# Crear una tabla llamada "canciones"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS canciones (
        tema TEXT,
        interprete TEXT,
        año INTEGER,
        semanas INTEGER,
        país TEXT,
        idioma TEXT,
        continente TEXT
    )
''')

# Datos proporcionados
datos_canciones = [
    ("Colgando en tus manos", "Carlos Baute con Marta Sánchez", 2009, 27, "Venezuela", "Español", "América del Sur"),
    ("Despacito", "Luis Fonsi y Daddy Yankee", 2017, 26, "Puerto Rico", "Español", "América del Sur"),
    ("You're the One That I Want", "John Travolta & Olivia Newton-John", 1978, 20, "Estados Unidos", "Inglés", "Norteamérica"),
    ("Bailando", "Enrique Iglesias con Descemer Bueno y Gente de Zona", 2014, 20, "España", "Español", "Europa"),
    ("El Perdón", "Enrique Iglesias y Nicky Jam", 2015, 18, "España", "Español", "Europa"),
    ("Sorry", "Justin Bieber", 2015, 17, "Canadá", "Inglés", "Norteamérica"),
    ("Waka Waka (Esto es África)", "Shakira", 2010, 17, "Colombia", "Español", "América del Sur"),
    ("Tusa", "Karol G y Nicki Minaj", 2019, 16, "Colombia y Trinidad y Tobago", "Español", "América del Sur"),
    ("Gimme Hope Jo'anna", "Eddy Grant", 1988, 15, "Guyana", "Inglés", "América del Sur"),
    ("On the Floor", "Jennifer López y Pitbull", 2011, 15, "Estados Unidos", "Inglés", "Norteamérica"),
    ("Voyage, Voyage", "Desireless", 1987, 15, "Francia", "Francés", "Europa"),
    ("Yo Te Esperaré", "Cali y El Dandee", 2012, 15, "Colombia", "Español", "América del Sur"),
    ("Ai Se Eu Te Pego", "Michel Teló", 2011, 14, "Brasil", "Portugués", "América del Sur"),
    ("Candle in the wind", "Elton John", 1987, 14, "Reino Unido", "Inglés", "Europa"),
    ("Quevedo: BZRP Music Sessions, Vol. 52", "Bizarrap y Quevedo", 2022, 13, "Argentina y España", "Español", "América del Sur y Europa"),
    ("La Bicicleta", "Carlos Vives y Shakira", 2016, 13, "Colombia", "Español", "América del Sur"),
    ("Lambada", "Kaoma", 1989, 13, "Brasil", "Portugués", "América del Sur"),
    ("Duele El Corazón", "Enrique Iglesias y Wisin", 2016, 12, "España", "Español", "Europa"),
    ("Mambo No. 5", "Lou Bega", 1999, 12, "Alemania", "Inglés", "Europa"),
    ("Loca", "Shakira", 2010, 12, "Colombia", "Español", "América del Sur"),
    ("Always on My Mind", "Pet Shop Boys", 1988, 11, "Reino Unido", "Inglés", "Europa"),
    ("La Gozadera", "Gente de Zona y Marc Anthony", 2015, 11, "Cuba", "Español", "América del Norte"),
    ("Infinity", "Guru Josh", 1990, 10, "Reino Unido", "Inglés", "Europa"),
    ("Te Voy A Esperar", "Juan Magán y Belinda", 2012, 10, "España", "Español", "Europa"),
    ("The Final Countdown", "Europe", 1987, 10, "Suecia", "Inglés", "Europa")
]


# Insertar los datos en la tabla
for cancion in datos_canciones:
    conexion.execute('''
        INSERT INTO canciones (tema, interprete, año, semanas, país, idioma, continente)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', cancion)



# Confirmar los cambios y cerrar la conexión
conexion.commit()



# ¿Cuál es la canción más antigua de la lista?
cursor.execute("SELECT MIN(año) FROM canciones")
resultado = cursor.fetchall()[0]
print("La canción más antigua en la lista es del año: ", resultado[0])



# ¿Qué artista aparece más veces en esta lista?
cursor.execute('''
    SELECT Interprete, COUNT(*) as Count
    FROM canciones
    GROUP BY Interprete
    ORDER BY Count DESC
''')
resultado = cursor.fetchall()
# Imprimir el artista que aparece más veces
if resultado:
    artista_mas_frecuente = resultado[0][0]
    veces_aparece = resultado[0][1]
    print(f"El artista que aparece más veces en la lista es '{artista_mas_frecuente}' con {veces_aparece} canciones.")
else:
    print("No se encontraron resultados.")


# ¿Qué país tiene más artistas en esta lista?
cursor.execute('''
    SELECT país, COUNT(DISTINCT Interprete) as ArtistCount
    FROM canciones
    GROUP BY país
    ORDER BY ArtistCount DESC
''')

resultado = cursor.fetchall()
# Imprimir el país con más artistas
if resultado:
    pais_con_mas_artistas = resultado[0][0]
    cantidad_de_artistas = resultado[0][1]
    print(f"El país con más artistas en la lista es '{pais_con_mas_artistas}' con {cantidad_de_artistas} artistas.")
else:
    print("No se encontraron resultados.")

# Consulta SQL para contar la cantidad de canciones distintas por idioma
cursor.execute('''
    SELECT idioma, COUNT(DISTINCT Tema) as CancionesPorIdioma
    FROM canciones
    GROUP BY idioma
''')

# Consulta SQL para contar la cantidad de canciones por continente
cursor.execute('''
    SELECT continente, COUNT(*) as Count
    FROM canciones
    GROUP BY continente
    ORDER BY Count DESC
''')
               

         
print(resultado[0])

conexion.close()