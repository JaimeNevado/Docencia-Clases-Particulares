package RepasoPracticaHerencia;

class RobotLimpieza extends Robot {
    public RobotLimpieza(String nombre, int bateria, int[] posicion) {
        super(nombre, bateria, posicion, 4, 'L');
    }

    @Override
    void Avanzar() {
        posicion[0] += 3;
    }

    @Override
    void Retroceder() {
        if (posicion[0] >= 2) {
            posicion[0] -= 2;
        } else {
            System.out.println("No se puede retroceder más.");
        }
    }

    @Override
    void Mostrar() {
        System.out.println("Posición: [" + posicion[0] + "," + posicion[1] + "] - Batería: " + bateria);
    }

    @Override
    void EjecutarAccion() {
        if (bateria >= potencia) {
            bateria -= potencia;
            System.out.println("Aspirando...");
        } else {
            System.out.println("Batería insuficiente para ejecutar acción.");
        }
    }
}
