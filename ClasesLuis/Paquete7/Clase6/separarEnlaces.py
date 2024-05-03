
from pytube import YouTube

def descargarMP3(enlace, nombreArchivo):
	yt = YouTube(enlace)

	audio = yt.streams.filter(only_audio=True).first()

	ruta_archivo = audio.download(output_path="/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete7/Clase6/Musica", filename=nombreArchivo + ".mp3")

	print("Se ha guardado el archivo correctamente ✓")

archivo = open("enlaces.txt", "r")

lineas = archivo.readlines()

archivo.close()

for elemento in lineas:
	separado = elemento.split(",")
	descargarMP3(separado[0].strip(),separado[1])
	print(f"Se ha descargado la cancion {separado[1]}")



