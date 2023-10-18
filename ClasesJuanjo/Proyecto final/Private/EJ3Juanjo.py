import matplotlib.pyplot as plt
import json

archivo= open("datos.json","r")
lineas= json.load(archivo)

# Máximo
max_num_def = 0
provincia_max_num_def = ""

max_new_cases = 0
provincia_max_new_cases = ""

max_num_hosp = 0
provincia_max_num_hosp = ""

max_num_UCI = 0
provincia_max_UCI = ""

# Mínimo
min_num_def = 1000
provincia_mim_num_def = ""

min_nuew_cases = 1000
provincia_min_new_cases = ""

min_num_hosp = 1000
provincia_min_num_hosp = ""

min_num_UCI = 1000
provincia_min_UCI = ""



for elemento in lineas:
    # Máximo
    if max_num_def < int(elemento["num_def"]):
        max_num_def=int(elemento["num_def"])
        provincia_max_num_def=elemento["province"]
    
    if max_new_cases < int(elemento["new_cases"]):
        max_new_cases=int(elemento["new_cases"])
        provincia_max_new_cases=elemento["province"]
    
    if max_num_hosp < int(elemento["num_hosp"]):
        max_num_hosp=int(elemento["num_hosp"])
        provincia_max_num_hosp=elemento["province"]
    
    if max_num_UCI < int(elemento["num_uci"]):
        max_num_UCI=int(elemento["num_uci"])
        provincia_max_num_UCI=elemento["province"]
    # Mínimo

    

etiquetas = ["Num Uci"]
valores = [max_num_UCI]

while True:
    opcion = int(input("""¿Qué gráfica quieres visualizar?
    1. Defunciones
    2. Casos
    3. Hospitalizados
    4. UCI
    5. Salir
    """))

    if opcion == 1:
        etiquetas = ["num_def"]
        valores = [12]
        plt.pie(valores, labels=etiquetas, autopct='%1.1f%%', startangle=90)
        plt.title(f'Número de Defunciones')
        plt.show()
    elif opcion == 2:

    elif opcion == 3:
       
    elif opcion == 4:
        
    elif opcion == 5:
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
