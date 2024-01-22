package clase3;

import java.util.Scanner;

public class ej1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		try {
			System.out.print("Ingrese el primer número: ");
			double num1 = sc.nextDouble();

			System.out.print("Ingrese el segundo número: ");
			double num2 = sc.nextDouble();

			System.out.println("¿Qué quieres hacer?");
			System.out.println("1) Sumar");
			System.out.println("2) Restar");
			System.out.println("3) Multiplicar");
			System.out.println("4) Dividir");

			System.out.print("Ingrese el número de la opción (1-4): ");
			int opcion = sc.nextInt();

			if (opcion == 1) {
				System.out.println("Resultado de la suma: " + (num1 + num2));
			} else if (opcion == 2) {
				System.out.println("Resultado de la resta: " + (num1 - num2));
			} else if (opcion == 3) {
				System.out.println("Resultado de la multiplicación: " + (num1 * num2));
			} else if (opcion == 4) {
				if (num2 != 0) {
					System.out.println("Resultado de la división: " + (num1 / num2));
				} else {
					System.out.println("No se puede dividir por cero.");
				}
			} else {
				System.out.println("Opción no válida. Por favor, ingrese un número del 1 al 4.");
			}

		} catch (Exception e) {
			System.out.println("Error al leer la entrada. Asegúrese de ingresar números válidos.");
		}
	}

}
