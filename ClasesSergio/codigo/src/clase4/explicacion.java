package clase4;

import java.util.Scanner;

public class explicacion {
	
	public static void escribirArray(int[] a) {
		for (int i = 0; i < a.length; i++) {
			System.out.print(a[i] + " ");
		}
		System.out.println();
	}

	public static void main(String[] args) {		
		int[][] matriz = {
				{1, 2, 3}, 
				{2, 4, 6}, 
				{7, 8, 9}
			};
		
		for (int[] fila : matriz) {
			for (int columna : fila) {
				System.out.print(columna + " ");
			}
			System.out.println();
		}
		
	}

}
