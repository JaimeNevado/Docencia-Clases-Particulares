package clase2;

import java.util.Scanner;

public class ej1 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.print("Ingrese el primer número: ");
		double num1 = scanner.nextDouble();
		System.out.print("Ingrese el segundo número: ");
		double num2 = scanner.nextDouble();

		System.out.println("Qué operación quieres hacer??");
		System.out.println("1. Suma");
		System.out.println("2. Resta");
		System.out.println("3. Multiplicación");
		System.out.println("4. División");
		System.out.print("Ingrese el número de la operación: ");

		try {
			int opcion = scanner.nextInt();

			switch (opcion) {
			case 1:
				System.out.println("El resultado de la suma es: " + (num1 + num2));
				break;
			case 2:
				System.out.println("El resultado de la resta es: " + (num1 - num2));
				break;
			case 3:
				System.out.println("El resultado de la multiplicación es: " + (num1 * num2));
				break;
			case 4:
				if (num2 == 0) {
					System.out.println("Error: No se puede dividir por cero.");
				} else {
					System.out.println("El resultado de la división es: " + (num1 / num2));
				}
				break;
			default:
				System.out.println("Opción no válida");
			}
		} catch (Exception e) {
			System.out.println("Has introducido algo que no es un numero");
		}
	}

}
