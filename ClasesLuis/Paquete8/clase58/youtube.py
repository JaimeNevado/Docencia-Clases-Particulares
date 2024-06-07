from pytube import YouTube

def descargarMP3(enlace, nombreArchivo):
	yt = YouTube(enlace)

	audio = yt.streams.filter(only_audio=True).first()

	ruta_archivo = audio.download(output_path="/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesLuis/Paquete8/clase58/Recursos/efectosDeSonido", filename=nombreArchivo + ".mp3")

	print("Se ha guardado el archivo correctamente ✓")

enlace = input("Dime el enlace: ")
nombre = input("Dime el nombre del archivo: ")
descargarMP3(enlace, nombre)