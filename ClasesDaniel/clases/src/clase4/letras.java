package clase4;

import java.util.Scanner;

public class letras {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		char letra = ' ';

		// Solicitar al usuario que ingrese una letra

		System.out.print("Ingresa una letra: ");
		while (letra != 'Z' && letra != 'A') {
			System.out.println("Por favor, ingresa una letra válida.");
			letra = scanner.next().charAt(0);
			letra.u
		}
		
		if (letra == 'Z') {
			System.out.println("La letra Z es la última del abecedario");
		} else {
			System.out.println("La letra A es la primera del abecedario");
			
		}

		// Mostrar la letra ingresada
		System.out.println("Ingresaste la letra: " + letra);

	}

}
