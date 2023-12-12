package clase7;

import java.util.Scanner;

public class explicacion {
	
	
	public static void imprimirMatriz(int[][] m) {
		for (int i = 0; i < m.length; i++) {
			for (int j = 0; j < m[i].length; j++) {
				System.out.print(m[i][j] + " ");
			}
			System.out.println();
		}
	}
	
	public static void main(String[] args) {
		int[][] m = {
				{1, 2, 3, 4}, 
				{1, 2, 3, 4}, 
				{1, 2, 3, 4},
				{1, 2, 3, 4}
			};
		
		
		for (int i = 0; i < m.length; i++) {
			for (int j = 0; j < m[i].length; j++) {
				if (i == j) {
					m[i][j] = 1;
				} else {
					m[i][j] = 0;
				}
			}
		}
		
		imprimirMatriz(m);
		
	}
	
}
