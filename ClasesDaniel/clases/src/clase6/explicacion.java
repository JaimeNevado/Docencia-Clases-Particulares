package clase6;

import java.util.Scanner;

public class explicacion {

	public static boolean arrayVacio(int[] array) {
		boolean vacio = false;
		if (array.length == 0) {
			vacio = true;
		}
		return vacio;
	}
	
	public static int suma(int a, int b) {
		int suma = a + b;
		return suma;
	}
	
	public static void main(String[] args) {
		int resultado = suma(10, 2);
		System.out.println(resultado);
	}
	
}
