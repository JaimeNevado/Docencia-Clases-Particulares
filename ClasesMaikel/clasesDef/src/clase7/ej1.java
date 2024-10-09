package clase7;

import java.util.Scanner;

public class ej1 {

	// Función para calcular el área de un triángulo
		static double calcularAreaTriangulo(double base, double altura) {
			return (base * altura) / 2;
		}

		public static void main(String[] args) {
			Scanner scanner = new Scanner(System.in);

			// Obtener la base del triángulo del usuario
			System.out.print("Introduce la base del triángulo: ");
			double base = scanner.nextDouble();

			// Obtener la altura del triángulo del usuario
			System.out.print("Introduce la altura del triángulo: ");
			double altura = scanner.nextDouble();

			// Llamada a la función para calcular el área
			double area = calcularAreaTriangulo(base, altura);

			// Mostrar el resultado
			System.out.println("El área del triángulo es: " + area);

			// Cerrar el scanner
			scanner.close();
		}

}
