package clase3;
import java.util.Scanner;

public class ejercicio2 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
        int numeroAleatorio = 15;
        int intento;
        int intentosRealizados = 0;

        System.out.println("Bienvenido a Adivina el Número!");

        while (true) {
            System.out.print("Adivina el número (1-100) o ingresa 0 para salir: ");
            intento = scanner.nextInt();
            intentosRealizados++;

            if (intento == 0) {
                System.out.println("Saliendo del juego. ¡Hasta luego!");
                break;
            }

            if (intento < numeroAleatorio) {
                System.out.println("Más alto. Intento número: " + intentosRealizados);
            } else if (intento > numeroAleatorio) {
                System.out.println("Más bajo. Intento número: " + intentosRealizados);
            } else {
                System.out.println("¡Felicidades! Has adivinado el número en " + intentosRealizados + " intentos.");
                break;
            }
        }
        scanner.close();

	}

}
