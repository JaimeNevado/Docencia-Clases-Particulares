from pytube import YouTube

def descargarMP3(enlace, nombreArchivo):
	yt = YouTube(enlace)

	audio = yt.streams.filter(only_audio=False).first()

	# Obtener el stream de video con la mejor calidad disponible
	#video = yt.streams.get_highest_resolution()

	ruta_archivo = audio.download(output_path="/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesNacho/IA/Clase3/", filename=nombreArchivo)

	print("Se ha guardado el archivo correctamente ✓")



link = input("Dime el enlace del video que quieres descargar: ")
nombre = input("Con que nombre quieres guardar el archivo: ")
descargarMP3(link, nombre + ".mp4")