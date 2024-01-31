stock = [
    {"Producto": "Camisa", "Precio": 20},
    {"Producto": "Pantalón", "Precio": 30},
    {"Producto": "Zapatos", "Precio": 50},
    {"Producto": "Bolso", "Precio": 40},
    {"Producto": "Bufanda", "Precio": 10}
]

for elemento in stock:
    print(f"{elemento['Producto'].upper()} {elemento['Precio']} euros")


    