import csv
import json
from datetime import datetime

archivo = open("prueba.csv", "r")
archivo_json = open("Datos.json", "w")
copia = list(csv.DictReader(archivo))
lineas = copia
provincias = []
resultados = []

def crear_lista_provincias():
	# Creamos la lista con las provincias no repetidas
	for elemento1 in lineas:
		if (elemento1["province"] not in provincias):
			provincias.append(elemento1["province"])

def buscar_elementos(provincia, diaParametro):
	for elemento in lineas:
		fecha_str = elemento["date"]
		fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d")
		numero_dia_semana = fecha_obj.weekday()
		dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
		nombre_dia_semana = dias_semana[numero_dia_semana]
		if (elemento["province"] == provincia and nombre_dia_semana == diaParametro):
			resultados.append([elemento["province"].upper(), nombre_dia_semana, elemento["num_def"], elemento["new_cases"], elemento["num_hosp"], elemento["num_uci"]])
	


crear_lista_provincias()
buscar_elementos("Málaga", "Martes")

# Ensure_ascii hace que las tildes se escriban correctamente.
json.dump(resultados, archivo_json, ensure_ascii=False)


