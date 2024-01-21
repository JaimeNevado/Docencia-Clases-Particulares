package clase2;

import java.util.Scanner;

public class ej2 {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		
		// Definir los límites del intervalo
		double limiteInferior = 2;
		double limiteSuperior = 5;
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Escriba un número: ");
		double numero = sc.nextDouble();
	
		
		if (numero >= limiteInferior && numero <= limiteSuperior) {
			System.out.println("Está en el intervalo");
		} else {
			System.out.println("No está en el intervalo");
		}

	}

}
