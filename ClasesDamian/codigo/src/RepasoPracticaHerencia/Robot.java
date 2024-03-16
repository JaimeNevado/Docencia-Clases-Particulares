package RepasoPracticaHerencia;

abstract class Robot {
    protected String nombre;
    protected int bateria;
    protected int[] posicion;
    protected int potencia;
    protected char letra;

    public Robot(String nombre, int bateria, int[] posicion, int potencia, char letra) {
        this.nombre = nombre;
        this.bateria = bateria;
        this.posicion = posicion;
        this.potencia = potencia;
        this.letra = letra;
    }

    public char getLetra() {
        return letra;
    }

    public int getBateria() {
        return bateria;
    }

    // Métodos abstractos
    abstract void Avanzar();
    abstract void Retroceder();
    abstract void Mostrar();
    abstract void EjecutarAccion();
}
