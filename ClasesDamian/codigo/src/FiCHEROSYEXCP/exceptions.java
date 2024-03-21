package FiCHEROSYEXCP;

import java.util.InputMismatchException;
import java.util.Scanner;

public class exceptions {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Dime un nombre: ");
		
		
		
		try {
			byte edad = sc.nextByte();
			
			System.out.println("EL numero es: " + edad);
			
		} catch (InputMismatchException e) {
			System.out.println("Ha saltado una excepcion porque has introducido un dato que no es Entero");
			//e.printStackTrace();
		} catch (ArithmeticException e) {
			System.out.println("Excepcion por dividir entre cero!!");
		}
		
		
		System.out.println("CODIGO SUPER IMPORTANTE DE EJECUTAR");
	}

}
