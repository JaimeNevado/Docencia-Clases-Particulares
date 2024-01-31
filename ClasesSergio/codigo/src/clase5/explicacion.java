package clase5;

import java.util.Scanner;

public class explicacion {

	public static double calcularMedia(int[] notas) {
		int cantidadDeNotas = notas.length;
		double suma = 0;
		
		for (int nota : notas) {
			suma += nota;
		}
		
		double media = suma / cantidadDeNotas;
		
		System.out.println("La media es: " + media);
		
		return media;
		
	}
	
	public static void main(String[] args) {

		int[] numeros = {4, 5, 6, 8, 10};
		
		double resultado = calcularMedia(numeros);
		

		if (comprobarParidadDeMatriz(matriz)) {
			System.out.println("Estás aprobado");
		} else {
			System.out.println("No estás aprobado");
		}
		
		
	}

}
