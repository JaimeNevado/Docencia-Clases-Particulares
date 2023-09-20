class Persona:
    def __init__(self, nombre_apellidos, dni, poblacion):
        self.nombre_apellidos = self.convertir_a_mayusculas_iniciales(nombre_apellidos)
        self.dni = self.validar_dni(dni)
        self.poblacion = self.convertir_a_mayusculas_iniciales(poblacion)
        self.pais = pais.upper()

    def convertir_a_mayusculas_iniciales(self, texto):
        return texto.title()

    def validar_dni(self, dni):
        if len(dni) == 9 and dni[0:7].isdigit() and dni[-1].isalpha():
            return dni.upper()
        else:
            raise ValueError("El DNI debe ser un valor alfanumérico de 9 caracteres con letra.")

class GustosMusicales:
    def __init__(self, cancion_favorita, grupo_favorito, estilo_musical):
        self.cancion_favorita = cancion_favorita
        self.grupo_favorito = grupo_favorito
        self.estilo_musical = estilo_musical.upper()

class Amigo(Persona, GustosMusicales):
    def __init__(self, nombre_apellidos, dni, poblacion, cancion_favorita, grupo_favorito, estilo_musical):
        Persona.__init__(self, nombre_apellidos, dni, poblacion)
        GustosMusicales.__init__(self, cancion_favorita, grupo_favorito, estilo_musical)

    def mostrar_datos(self):
        print("Nombre y apellidos:", self.nombre_apellidos)
        print("DNI:", self.dni)
        print("Población:", self.poblacion)
        print("Canción favorita:", self.cancion_favorita)
        print("Grupo favorito:", self.grupo_favorito)
        print("Estilo musical:", self.estilo_musical)

# Ejemplo de uso:
try:
    nombre_apellidos = input("Nombre y apellidos: ")
    dni = input("DNI: ")
    poblacion = input("Población: ")
    cancion_favorita = input("Canción favorita: ")
    grupo_favorito = input("Grupo favorito: ")
    estilo_musical = input("Estilo musical: ")
    pais = input("Pais de origen: ")

    amigo = Amigo(nombre_apellidos, dni, poblacion, cancion_favorita, grupo_favorito, estilo_musical)
    amigo.mostrar_datos()

except ValueError:
    print("Error")
