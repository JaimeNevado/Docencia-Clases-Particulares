package clase6;

import java.util.Scanner;

public class explicacion {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Dime tu eleccion (R/P/T): ");
		

		
		char letra = sc.next().charAt(0);
		
		if (letra == 'R') {
			System.out.println("Has elegido roca");
		} else if (letra == 'P') {
			System.out.println("Has elegido papel");
		} else if (letra == 'T') {
			System.out.println("Has elegido tijeras");
		}
		
		
	}

}
