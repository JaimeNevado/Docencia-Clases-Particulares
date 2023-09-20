class Artista:
    def __init__(self, nombre, genero):
        self.nombre = nombre
        self.genero = genero
        self.va_al_concierto = False

    def asistir_concierto(self):
        self.va_al_concierto = True

    def cancelar_asistencia(self):
        self.va_al_concierto = False


# Crear una lista de artistas
artistas = [
    Artista("Adele", "Pop"),
    Artista("Ed Sheeran", "Pop"),
    Artista("Metallica", "Rock"),
    Artista("J Balvin", "Reggaeton"),
]

def imprimirArtistas():
    i = 0
    while (i < len(artistas)):
        if (artistas[i].va_al_concierto):
            print(artistas[i].nombre, "SI va al concierto")
        else:
            print(artistas[i].nombre, "NO va al concierto")
        i = i + 1
    
# Mostrar la lista de artistas y su asistencia actual al concierto
print("Lista de artistas y su asistencia al concierto:")
imprimirArtistas();

# Cambiar la asistencia de algunos artistas
artistas[0].asistir_concierto()
artistas[2].asistir_concierto()
artistas[3].asistir_concierto()

# Mostrar la lista actualizada de artistas y su asistencia al concierto
print("\nLista actualizada de artistas y su asistencia al concierto:")
imprimirArtistas();

