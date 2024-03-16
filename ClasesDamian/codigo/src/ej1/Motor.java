package ej1;


// Ejercicio 1
public class Motor {
    // Atributos
    private String tipoCombustible;
    private int cilindros;
    private double potencia;

    // Constructor
    public Motor(String tipoCombustible, int cilindros, double potencia) {
        this.tipoCombustible = tipoCombustible;
        this.cilindros = cilindros;
        this.potencia = potencia;
    }

    // Métodos
    public void encender() {
        System.out.println("Motor encendido");
    }

    public void apagar() {
        System.out.println("Motor apagado");
    }

    public void informacion() {
        System.out.println("Tipo de combustible: " + tipoCombustible);
        System.out.println("Número de cilindros: " + cilindros);
        System.out.println("Potencia: " + potencia + " HP");
    }
    
    
    @Override
    public String toString() {
    	return "Tipo de combustible: " + tipoCombustible + "\n" + 
				"Número de cilindros: " + cilindros + "\n" +
				"Potencia " + potencia + " HP" + "\n";
    }
    
    

    // Método main para probar la clase
    public static void main(String[] args) {
        // Crear una instancia de Motor
        Motor motor1 = new Motor("Gasolina", 4, 200.0);

        // Probar los métodos
        motor1.encender();
        motor1.informacion();
        motor1.apagar();
    }
}
