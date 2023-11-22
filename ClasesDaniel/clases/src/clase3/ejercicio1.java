package clase3;
import java.util.Scanner;

public class ejercicio1 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
        int opcion;

        while (true) {
            System.out.println("Calculadora Simple");
            System.out.println("1. Suma");
            System.out.println("2. Resta");
            System.out.println("3. Multiplicación");
            System.out.println("4. División");
            System.out.println("5. Salir");
            System.out.print("Seleccione una opción: ");

            opcion = scanner.nextInt();

            if (opcion == 5) {
                System.out.println("Saliendo de la calculadora. ¡Hasta luego!");
                break;
            }

            // Implementa la lógica para realizar operaciones según la opción seleccionada
            double resultado;
            System.out.print("Ingrese el primer número: ");
            double num1 = scanner.nextDouble();
            System.out.print("Ingrese el segundo número: ");
            double num2 = scanner.nextDouble();

            if (opcion == 1) {
                resultado = num1 + num2;
            } else if (opcion == 2) {
                resultado = num1 - num2;
            } else if (opcion == 3) {
                resultado = num1 * num2;
            } else if (opcion == 4) {
                if (num2 != 0) {
                    resultado = num1 / num2;
                } else {
                    System.out.println("No se puede dividir por cero.");
                    continue; // Vuelve al inicio del bucle
                }
            } else {
                System.out.println("Opción no válida. Por favor, elija una opción válida.");
                continue; // Vuelve al inicio del bucle
            }

            System.out.println("Resultado: " + resultado);
        }
        scanner.close();
	}

}
