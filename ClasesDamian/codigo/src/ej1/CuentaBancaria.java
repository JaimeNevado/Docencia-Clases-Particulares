package ej1;

// Ejercicio 2
public class CuentaBancaria {
    // Atributos
    private String titular;
    private double saldo;

    // Constructor
    public CuentaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    // Método para depositar dinero en la cuenta
    public void depositar(double cantidad) {
        saldo += cantidad;
        System.out.println("Se depositaron " + cantidad + " en la cuenta de " + titular);
    }

    // Método para retirar dinero de la cuenta
    public void retirar(double cantidad) {
        if (cantidad <= saldo) {
            saldo -= cantidad;
            System.out.println("Se retiraron " + cantidad + " de la cuenta de " + titular);
        } else {
            System.out.println("No se puede retirar " + cantidad + ", saldo insuficiente en la cuenta de " + titular);
        }
    }

    // Método para obtener el saldo actual de la cuenta
    public double obtenerSaldo() {
        return saldo;
    }

    // Método main para probar la clase
    public static void main(String[] args) {
        // Crear dos instancias de CuentaBancaria
        CuentaBancaria cuenta1 = new CuentaBancaria("Juan", 1000);
        CuentaBancaria cuenta2 = new CuentaBancaria("María", 2000);

        // Realizar operaciones de depósito y retiro
        cuenta1.depositar(500);
        cuenta2.retirar(1000);
        cuenta1.retirar(1500); // Intentar retirar más dinero del saldo disponible en cuenta1

        // Mostrar la información de las cuentas
        System.out.println("Saldo de la cuenta de " + cuenta1.titular + ": " + cuenta1.obtenerSaldo());
        System.out.println("Saldo de la cuenta de " + cuenta2.titular + ": " + cuenta2.obtenerSaldo());
    }
}
