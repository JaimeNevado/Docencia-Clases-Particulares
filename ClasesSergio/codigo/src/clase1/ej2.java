package clase1;

import java.util.Scanner;

public class ej2 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
        System.out.print("Por favor, ingresa tu edad: ");

        if (scanner.hasNextInt()) {
            int edad = scanner.nextInt();

            if (edad < 0) {
                System.out.println("ERROR La edad ingresada no es válida.");
            } else if (edad >= 0 && edad <= 17) {
                System.out.println("Eres menor de edad.");
            } else if (edad >= 18 && edad <= 64) {
                System.out.println("Eres mayor de edad.");
            } else {
                System.out.println("Eres un jubilado.");
            }
        } else {
            System.out.println("ERROR: Ingresa un valor numérico válido para la edad.");
        }

        scanner.close();

	}

}
