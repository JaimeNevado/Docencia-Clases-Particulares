package clase3;

import java.util.Scanner;

public class explicacion {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] numeros = {0, 0, 0, 0, 0};
	
		for (int i = 0; i < numeros.length; i++) {
			System.out.print("Escribe un número en la posicion " + i + ": ");		
			numeros[i] = sc.nextInt();		
		}
		
		for (int i = 0; i < numeros.length; i++) {
			System.out.println(numeros[i]);		
		}
		
		
		
	}

}
