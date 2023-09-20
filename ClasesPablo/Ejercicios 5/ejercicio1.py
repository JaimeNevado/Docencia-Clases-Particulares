# Club de Fútbol

class equipo_futbol:
    def __init__(self, nombre, fundacion, ligasGanadas, jugadores, lesionados):
        self.nombre = nombre
        self.fundacion = fundacion
        self.ligasGanadas = ligasGanadas
        self.lesionados = lesionados

    def sumarLiga(self):
        self.ligasGanadas += 1