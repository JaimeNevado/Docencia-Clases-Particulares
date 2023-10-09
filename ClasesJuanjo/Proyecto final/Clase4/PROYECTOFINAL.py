import csv
from datetime import datetime

archivoCSV=open("prueba.csv", "r")

lineas=list(csv.DictReader(archivoCSV))

def buscar_elementos(provincia, dia_a_buscar):

	for elemento in lineas:
		fecha=elemento["date"]
		#fecha = "2021-05-04"
		fecha_obj = datetime.strptime(fecha,"%Y-%m-%d")
		numero_dia_semana = fecha_obj.weekday()
		dias_semana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
		nombreDiaEncontrado=dias_semana[numero_dia_semana]
		#nombreDiaEncontrado = "Lunes"
		if elemento["province"]==provincia and nombreDiaEncontrado == dia_a_buscar:
			print(nombreDiaEncontrado,elemento["province"],elemento["num_def"], elemento["new_cases"],elemento["num_hosp"],elemento["num_uci"])

# provincias = ["Málaga", "Jaén", ...]
dia_A_buscar = "Lunes"
provincia_A_buscar = "Málaga"

buscar_elementos(provincia_A_buscar, dia_A_buscar)
