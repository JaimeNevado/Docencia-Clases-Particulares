# Jaime Nevado Farfán
# 12 Septiembre 2023

import csv
import json
from datetime import datetime

import matplotlib.pyplot as plt


archivo = open("prueba.csv", "r")
archivo_json = open("Datos.json", "r+")
copia = list(csv.DictReader(archivo))
lineas = copia
provincias = []
datos = {}
listaDatos = []

def crear_lista_provincias():
	# Creamos la lista con las provincias no repetidas
	for elemento1 in lineas:
		if (elemento1["province"] not in provincias):
			provincias.append(elemento1["province"])

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
			datos = {
				"province" : elemento["province"],
				"num_def" : elemento["num_def"],
				"new_cases" : elemento["new_cases"],
				"num_hosp" : elemento["num_hosp"],
				"num_uci" : elemento["num_uci"]
			}
			listaDatos.append(datos)


dia_A_buscar = "Lunes"
provincia_A_buscar = "Málaga"

buscar_elementos(provincia_A_buscar, dia_A_buscar)

# Ensure_ascii hace que las tildes se escriban correctamente.
json.dump(listaDatos, archivo_json, ensure_ascii=False)

# Escribir en archivo y leer de archivo
lectura_archivo = archivo_json.readlines()
archivo_json.close()

# Gráficas
