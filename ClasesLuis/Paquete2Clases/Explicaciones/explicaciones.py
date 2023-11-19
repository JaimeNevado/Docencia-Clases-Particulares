diccionario = {
    
}

diccionario["nombre"] = input("Dime tu nombre")
diccionario["edad"] = int(input("Dime tu edad"))


# delete
cosa_a_eliminar = input("Dime la cosa a eliminar: ")

del diccionario[cosa_a_eliminar.lower()]

print(diccionario)