package clase3;

import java.util.InputMismatchException;
import java.util.Scanner;

public class ej1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		try {
		int num = sc.nextInt();
		
		System.out.println("El numero es: " + num);
		} catch (InputMismatchException e) {
			System.out.println("Error");
		}
	}

}
