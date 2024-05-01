stock_tienda = {
    "manzanas": 50,
    "plátanos": 30,
    "naranjas": 40,
    "peras": 20,
    "uvas": 35
}

for clave in stock_tienda.keys():
	print(clave)

for valor in stock_tienda.values():
	print(valor)

for clave, valor in stock_tienda.items():
	print(clave, valor)
	