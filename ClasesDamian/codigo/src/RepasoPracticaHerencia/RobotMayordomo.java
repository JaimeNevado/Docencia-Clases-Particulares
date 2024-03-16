package RepasoPracticaHerencia;

class RobotMayordomo extends Robot {
    public RobotMayordomo(String nombre, int bateria, int[] posicion) {
        super(nombre, bateria, posicion, 3, 'M');
    }

    @Override
    void Avanzar() {
        posicion[0] += 5;
    }

    @Override
    void Retroceder() {
        if (posicion[0] >= 4) {
            posicion[0] -= 4;
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
        if (bateria >= potencia * 2) {
            bateria -= potencia * 2;
            System.out.println("Cogiendo...");
        } else {
            System.out.println("Batería insuficiente para ejecutar acción.");
        }
    }
}