from pytube import YouTube
import os

def descargarMP3(enlace, nombreArchivo):
	yt = YouTube(enlace)

	audio = yt.streams.filter(only_audio=True).first()

	ruta_archivo = audio.download(output_path="/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete7/Clase2", filename=nombreArchivo)

	print("Se ha guardado el archivo correctamente ✓")
