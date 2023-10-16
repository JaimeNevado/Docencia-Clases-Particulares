import matplotlib.pyplot as plt
import json

# Cargar datos desde el archivo JSON
archivo_json = open("Datos.json", "r", encoding="utf-8")
datos = json.load(archivo_json)

max_num_def = 0
max_new_cases = 0
max_num_hosp = 0
max_num_uci = 0

for elemento in datos:
    if (int(elemento["num_def"]) > max_num_def):
        #Declaramos máximo como el actual
        max_num_def = int(elemento["num_def"])
        # Declaramos la provincia donde está el valor mayor
        provincia_max_def = elemento["province"]
    if (int(elemento["new_cases"]) > max_new_cases):
        max_new_cases = int(elemento["new_cases"])
        provincia_max_new_cases = elemento["province"]
    if (int(elemento["num_hosp"]) > max_num_hosp):
        max_num_hosp = int(elemento["num_hosp"])
        provincia_max_num_hosp = elemento["province"]
    if (int(elemento["num_uci"]) > max_num_uci):
        max_num_uci = int(elemento["num_uci"])
        provincia_max_num_uci = elemento["province"]

while True:
    opcion = int(input("""¿Qué gráfica quieres visualizar?
    1. Defunciones
    2. Casos
    3. Hospitalizados
    4. UCI
    5. Salir
    """))

    if opcion == 1:
        etiquetas = ["Número defunciones"]
        tamaños = [max_num_def]  # Valores que representan el tamaño de cada sector
        plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        plt.title("Gráfica con los Número de defunciones")
        plt.show()
    elif opcion == 2:
        etiquetas = ["Nuevos casos"]
        tamaños = [max_new_cases]  # Valores que representan el tamaño de cada sector
        plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        plt.title("Gráfica con los Nuevos Casos")
        plt.show()
    elif opcion == 3:
        etiquetas = ["Número de Hospitalizados"]
        tamaños = [max_new_cases]  # Valores que representan el tamaño de cada sector
        plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        plt.title("Gráfica con el Número de Hospitalizados")
        plt.show()
    elif opcion == 4:
        etiquetas = ["Número en UCI"]
        tamaños = [max_new_cases]  # Valores que representan el tamaño de cada sector
        plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        plt.title("Gráfica con el Número de UCI")
        plt.show()
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
