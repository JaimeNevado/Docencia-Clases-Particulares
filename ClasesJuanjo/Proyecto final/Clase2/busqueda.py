import csv

archivoCSV=open("prueba.csv", "r")

lineas=list(csv.DictReader(archivoCSV))

def buscar_elementos(provincia):
    for elemento in lineas:
        if elemento["province"]==provincia:
            print(elemento["province"],elemento["num_def"], elemento["new_cases"],elemento["num_hosp"],elemento["num_uci"])

provincias = []
for elemento in lineas:
	if elemento["province"] not in provincias:
		provincias.append(elemento["province"])

print(provincias)

# provincias = ["Málaga", "Jaén", ...]
for provincia in provincias:
	buscar_elementos(provincia)
