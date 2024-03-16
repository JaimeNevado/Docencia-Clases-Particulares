package clase5;

class Motocicleta extends Vehiculo {
    // Constructor
    public Motocicleta(String marca, String modelo, String color) {
        super(marca, modelo, color);
    }

    // Método adicional
    public void hacerAcrobacias() {
        System.out.println(marca + " " + modelo + " está haciendo una acrobacia.");
    }
}