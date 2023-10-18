import matplotlib.pyplot as plt
import json

# Cargar datos desde el archivo JSON
archivo_json = open("Datos.json", "r", encoding="utf-8")
datos = json.load(archivo_json)

num_def_total = 0
new_cases_total = 0
num_hosp_total = 0
num_uci_total = 0

for elemento in datos:
    provincia = elemento["province"]
    dia_semana = elemento["dia_sem"]
    num_def_total = num_def_total + int(elemento["num_def"])
    new_cases_total = new_cases_total + int(elemento["new_cases"])
    num_hosp_total = num_hosp_total + int(elemento["num_hosp"])
    num_uci_total = num_uci_total + int(elemento["num_uci"])

while True:
    opcion = int(input("""¿Qué gráfica quieres visualizar?
    1. Defunciones
    2. Casos
    3. Hospitalizados
    4. UCI
    5. Salir
    """))

    if opcion == 1:
        plt.bar(provincia, num_def_total)
        plt.xlabel('Provincia')
        plt.ylabel('Número de Defunciones')
        plt.title(f'Número de Defunciones en {provincia} un {dia_semana}')
        plt.show()
    elif opcion == 2:
        plt.bar(provincia, new_cases_total)
        plt.xlabel('Provincia')
        plt.ylabel('Nuevos Casos')
        plt.title(f'Nuevos Casos en {provincia} un {dia_semana}')
        plt.show()
    elif opcion == 3:
        plt.bar(provincia, num_hosp_total)
        plt.xlabel('Provincia')
        plt.ylabel('Número de Hospitalizaciones')
        plt.title(f'Número de Hospitalizaciones en {provincia} un {dia_semana}')
        plt.show()
    elif opcion == 4:
        plt.bar(provincia, num_uci_total)
        plt.xlabel('Provincia')
        plt.ylabel('Número de Pacientes en UCI')
        plt.title(f'Número de Pacientes en UCI en {provincia} un {dia_semana}')
        plt.show()
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
