package clase3;

import java.util.Scanner;

public class ej2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("De qué número quieres saber el factorial: ");
		int num = sc.nextInt();
		int factorial = 1;
		while (num > 0) {
			factorial = factorial * num;
			num--;
		}
		
		System.out.println("El factorial es: " + factorial);
	}

}
