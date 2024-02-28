package clase10;

public class CuentaBancaria {
    private String titular;
    private double saldo;

    public CuentaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public void depositar(double cantidad) {
        saldo += cantidad;
        System.out.println("Se depositaron " + cantidad + " euros. Saldo actual: " + saldo);
    }

    public void retirar(double cantidad) {
        if (cantidad <= saldo) {
            saldo -= cantidad;
            System.out.println("Se retiraron " + cantidad + " euros. Saldo actual: " + saldo);
        } else {
            System.out.println("No se puede retirar más dinero del saldo disponible.");
        }
    }

    public double obtenerSaldo() {
        return saldo;
    }

    public static void main(String[] args) {
        CuentaBancaria cuenta1 = new CuentaBancaria("Jaime", 1000.0);
        CuentaBancaria cuenta2 = new CuentaBancaria("Luis", 2000.0);

        System.out.println("Saldo de la cuenta de " + cuenta1.titular + ": " + cuenta1.obtenerSaldo());
        System.out.println("Saldo de la cuenta de " + cuenta2.titular + ": " + cuenta2.obtenerSaldo());
    }
}
