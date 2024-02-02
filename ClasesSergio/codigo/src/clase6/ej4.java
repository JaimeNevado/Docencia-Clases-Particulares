package clase6;

import java.util.Scanner;

public class ej4 {
	
	public static boolean esPar(int n) {
		boolean par = false;
		if (n % 2 == 0) {
			par = true;
		}
		return par;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Escribe el número: ");
		int numero = sc.nextInt();
		
		if (esPar(numero)) {
			System.out.println("Es par");
		} else {
			System.out.println("No es par");
		}
		sc.close();
	}

}
