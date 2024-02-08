package clase7;

import java.util.Scanner;

public class ej2 {
	
	public static boolean comprobarPalindromo(String pal) {
		boolean palindromo = false;
		String palabra = pal.toLowerCase();
		if (palabra.charAt(0) == palabra.charAt(palabra.length() - 1)) {
			palindromo = true;
		}
		return palindromo;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Introduzca una palabra: ");
		String palabra = sc.next();
		boolean palindromo = comprobarPalindromo(palabra);
		if (palindromo) {
			System.out.println("La palabra " + palabra + " SI es palíndroma");
		} else {
			System.out.println("La palabra " + palabra + " NO es palíndroma");			
		}
	}

}
