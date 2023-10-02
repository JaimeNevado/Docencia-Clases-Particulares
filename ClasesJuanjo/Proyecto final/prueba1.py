import csv
import json
from collections import defaultdict

# Abre el archivo CSV y crea un lector de CSV
with open('prueba.csv') as File:
    reader = csv.DictReader(File)
    
    # Crea un diccionario para almacenar los datos agrupados
    data_by_day_province = defaultdict(lambda: defaultdict(int))
    
    # Itera a través de las filas del archivo CSV
    for row in reader:
        day_of_week = row['date']
        province = row['province'] 
        
        # Suma los valores para cada clave (día de la semana y provincia)
        data_by_day_province[day_of_week][province] += int(row['num_def'])
        data_by_day_province[day_of_week][province] += int(row['new_cases'])
        data_by_day_province[day_of_week][province] += int(row['num_hosp'])
        data_by_day_province[day_of_week][province] += int(row['num_uci'])

# Convierte el diccionario a una lista de objetos JSON
results = [{'day_of_week': day, 'province_data': province_data} for day, province_data in data_by_day_province.items()]

# Almacena los resultados en un archivo JSON
with open('result.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

print("Datos agrupados y almacenados en 'result.json'")
