package clase5;

class Coche extends Vehiculo {
    // Constructor
    public Coche(String marca, String modelo, String color) {
        super(marca, modelo, color);
    }

    // Método adicional
    public void abrirPuertas() {
        System.out.println(marca + " " + modelo + " está abriendo las puertas.");
    }
}