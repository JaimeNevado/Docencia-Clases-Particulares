# Ejercicio 1: Manipulación básica de una lista

# Crea una lista vacía
mi_lista = []

# Agrega tres elementos a la lista utilizando append()
mi_lista.append("manzana")
mi_lista.append("naranja")
mi_lista.append("plátano")

# Accede al segundo elemento de la lista e imprímelo
print("Segundo elemento de la lista:", mi_lista[1])

# Elimina el primer elemento de la lista utilizando remove()
mi_lista.remove("manzana")

# Limpia la lista utilizando clear()
mi_lista.clear()

# Imprime la lista para verificar si está vacía
print("Lista después de usar clear():", mi_lista)
