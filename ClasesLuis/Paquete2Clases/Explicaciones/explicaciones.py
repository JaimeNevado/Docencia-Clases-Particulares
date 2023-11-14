stock_productos = {
    "camisa": 50,
    "pantalon": 30,
    "zapatos": 20,
    "sombrero": 15,
    "bufanda": 25
}
producto = input("Dime el producto: ")
cantidad = int(input("Cuánto has traido?: "))

stock_productos[producto] = cantidad

print(stock_productos)