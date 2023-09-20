class Lista:
    def __init__(self, lista):
        self.lista = lista

    def sumar(self, lista):
        i = 0
        suma = 0
        while i < len(lista):
            suma += lista[i]
            i += 1
        return suma

    def mediaPar(self):
        numerosPares = []
        numerosImpares = []
        numeros = self.lista
        i = 0
        while i < len(numeros):
            if i % 2 == 0:
                numerosPares.append(int(numeros[i]))
            # Código para impares 
            else:
                numerosImpares.append(int(numeros[i]))
            i += 1

        mediaPar = self.sumar(numerosPares) / len(numerosPares)
        mediaInpar= self.sumar(numerosImpares) / len(numerosImpares)
        return mediaPar

    def mediaImpar(self):
        numerosPares = []
        numerosImpares = []
        numeros = self.lista
        i = 0
        while i < len(numeros):
            if i % 2 == 0:
                numerosPares.append(int(numeros[i]))
            # Código para impares 
            else:
                numerosImpares.append(int(numeros[i]))
            i += 1

        #mediaPar = self.sumar(numerosPares) / len(numerosPares)
        mediaInpar= self.sumar(numerosImpares) / len(numerosImpares)
        return mediaInpar
    
    def __str__ (self):
        return f"La lista es: {self.lista} \nLa media Par es: {self.mediaPar()} \nLa media Impar es: {self.mediaImpar()}"

lista1 = Lista([1, 8, 3, 1, 2, 3])

print(lista1)