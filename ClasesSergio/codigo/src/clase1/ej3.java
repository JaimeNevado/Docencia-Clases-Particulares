package clase1;

import java.util.Scanner;

public class ej3 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("¿De que número quieres saber la tabla de multiplicar?: ");
		int numero = sc.nextInt();
		int total = 0;
		int i = 0;
		while (i < 11) {
			System.out.println(numero + " x " + i + " = " + total);
			total += numero;
			i++;
		}
		System.out.println("Terminado");

	}

}
