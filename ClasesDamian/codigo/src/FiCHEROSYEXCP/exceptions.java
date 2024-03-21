package FiCHEROSYEXCP;

import java.util.InputMismatchException;
import java.util.Scanner;

public class exceptions {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		try {
			int num = sc.nextInt();
			System.out.println("El numero es: " + num);			
		} catch (InputMismatchException e) {
			System.out.println("Ha ocurrido una excepción");
		} finally {
			System.out.println("Finally");
		}
		

	}

}
