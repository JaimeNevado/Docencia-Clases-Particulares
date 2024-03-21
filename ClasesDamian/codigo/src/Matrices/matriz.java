package Matrices;

import java.util.Scanner;

public class matriz {

	public static void escribirMatriz(int[][] m) {
		for (int i = 0; i < m.length; i++) {
			for (int j = 0; j < m[i].length; j++) {
				System.out.print(m[i][j] + " ");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.println("Ingrese el tamaño de la matriz cuadrada:");
		int n = scanner.nextInt();

		int[][] matriz = new int[n][n];

		System.out.println("Ingrese los elementos de la matriz:");
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				matriz[i][j] = scanner.nextInt();
			}
		}

		escribirMatriz(matriz);

	}
}
