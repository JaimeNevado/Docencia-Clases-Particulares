archivo = open("escritura.txt", "w")

texto = ["juan", "manuel", "luis"]
for elemento in texto:
    archivo.write(elemento + "\n")

archivo.close()