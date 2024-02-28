package clase10;

public class Motor {
    private String tipoCombustible;
    private int cilindros;
    private double potencia; 

    // Constructor
    public Motor(String tipoCombustible, int cilindros, double potencia) {
        this.tipoCombustible = tipoCombustible;
        this.cilindros = cilindros;
        this.potencia = potencia;
    }

    public void encender() {
        System.out.println("Motor encendido");
    }

    public void apagar() {
        System.out.println("Motor apagado");
    }
    
    public void informacion() {
    	System.out.println("Información del motor: ");
        System.out.println("Tipo de combustible: " + tipoCombustible);
        System.out.println("Número de cilindros: " + cilindros);
        System.out.println("Potencia: " + potencia + " HP");
        System.out.println("--------------------");
    }

    // Getters y setters
    public String getTipoCombustible() {
        return tipoCombustible;
    }

    public void setTipoCombustible(String tipoCombustible) {
        this.tipoCombustible = tipoCombustible;
    }

    public int getCilindros() {
        return cilindros;
    }

    public void setCilindros(int cilindros) {
        this.cilindros = cilindros;
    }

    public double getPotencia() {
        return potencia;
    }

    public void setPotencia(double potencia) {
        this.potencia = potencia;
    }

    public static void main(String[] args) {
        Motor motor = new Motor("Gasolina", 4, 200.0);

        motor.informacion();
        
        motor.encender();

        motor.apagar();
    }
}
