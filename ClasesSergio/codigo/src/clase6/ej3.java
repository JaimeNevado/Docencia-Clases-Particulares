package clase6;

import java.util.Scanner;

public class ej3 {
    static void saludar(String nombre) {
        System.out.println("¡Hola, " + nombre + "! ¿Cómo estás?");
    }

    static void despedir(String nombre) {
        System.out.println("¡Hasta luego, " + nombre + "! Que tengas un buen día.");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa tu nombre: ");
        String nombreUsuario = scanner.nextLine();

        saludar(nombreUsuario);

        despedir(nombreUsuario);

        scanner.close();
    }
   

}
