import matplotlib.pyplot as plt
import json

# Cargar datos desde el archivo JSON
archivo_json = open("Datos.json", "r", encoding="utf-8")
datos = json.load(archivo_json)

def sumar_valores(provincia, buscar):
    valor = 0
    for elemento in datos:
        if (elemento["province"] == provincia):
            valor = valor + int(elemento[buscar])
    return valor

num_def_total = []
new_cases_total = []
num_hosp_total = []
num_uci_total = []

provincias = []
for elemento in datos:
	if elemento["province"] not in provincias:
		provincias.append(elemento["province"])

for provincia in provincias:
    suma = sumar_valores(provincia, "num_def")
    num_def_total.append(suma)

for provincia in provincias:
    suma = sumar_valores(provincia, "new_cases")
    new_cases_total.append(suma)

for provincia in provincias:
    suma = sumar_valores(provincia, "num_hosp")
    num_hosp_total.append(suma)

for provincia in provincias:
    suma = sumar_valores(provincia, "num_uci")
    num_uci_total.append(suma)

while True:
    opcion = int(input("""¿Qué gráfica quieres visualizar?
    1. Defunciones
    2. Casos
    3. Hospitalizados
    4. UCI
    5. Salir
    """))

    if opcion == 1:
        plt.bar(provincias, num_def_total)
        plt.xlabel('Provincia')
        plt.ylabel('Número de Defunciones')
        plt.title('Número de Defunciones')
        plt.show()
    elif opcion == 2:
        plt.bar(provincias, new_cases_total)
        plt.xlabel('Provincia')
        plt.ylabel('Nuevos Casos')
        plt.title('Nuevos Casos')
        plt.show()
    elif opcion == 3:
        plt.bar(provincias, num_hosp_total)
        plt.xlabel('Provincia')
        plt.ylabel('Número de Hospitalizaciones')
        plt.title('Número de Hospitalizaciones')
        plt.show()
    elif opcion == 4:
        plt.bar(provincias, num_uci_total)
        plt.xlabel('Provincia')
        plt.ylabel('Número de Pacientes en UCI')
        plt.title('Número de Pacientes en UCI')
        plt.show()
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
