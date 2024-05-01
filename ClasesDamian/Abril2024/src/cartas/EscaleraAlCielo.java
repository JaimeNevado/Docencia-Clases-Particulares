package cartas;

public class EscaleraAlCielo {
    public static void main(String[] args) {
        for (int i = 0; i < 3; i++) {
            System.out.println("Ejecución " + (i + 1) + ":");
            Main juego = new Main();
            juego.jugar();
            System.out.println();
        }
    }
}
