package clase3;

import java.util.Scanner;

public class ej3 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Escriba una palabra: ");
		String palabra = sc.next();
		String vocales = "";
		String consonantes = "";
		char c;
		
		
		for (int i = 0; i < palabra.length(); i++) {
			c = palabra.toLowerCase().charAt(i);
			if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
				vocales += c;
			} else {
				consonantes += c;
			}
		}
		
		System.out.println("Las vocales en la palabra son: " + vocales);
		System.out.println("Las consonantes en la palabra son: " + consonantes);
	}

}
