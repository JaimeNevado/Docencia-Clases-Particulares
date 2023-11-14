stock_productos = {
    "camisa": 50,
    "pantalon": 30,
    "zapatos": 20,
    "sombrero": 15,
    "bufanda": 25
}

print("Bienvenido al sistema de administracion de stock")


numero = 2
while (numero > 0):
    print("1.Mostar cantidad en stock")
    print("2.Agregar nuevo producto")
    print("3. Salir")

    respuesta= int(input("Que quieres hacer? "))

    if (respuesta==1):
        print(stock_productos)
    elif (respuesta==2):
        producto=input(("Que has traido?"))
        cantidad=int(input("Que cantidad has traido? "))
        stock_productos[producto]=cantidad
    elif (respuesta == 3):
        break
    else:
        print("Error")