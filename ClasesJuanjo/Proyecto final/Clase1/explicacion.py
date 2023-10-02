import csv 
  
results = [] 
archivo = open("prueba.csv", "r")
linea = csv.DictReader(archivo) 
for row in linea: 
    results.append(row) 
print(results)