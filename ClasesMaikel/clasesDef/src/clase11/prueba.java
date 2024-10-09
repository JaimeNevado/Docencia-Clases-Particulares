package clase11;

import java.util.Scanner;

public class prueba {

	public static int[][] leerMatriz(){
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Dime el tamaño de la matriz: ");
		int tamaño = sc.nextInt();
		
		int matrizX[][] = new int[tamaño][tamaño];
		for (int i = 0; i < tamaño; i++) {
			for (int j = 0; j < tamaño; j++) {
	            System.out.print("Introduce el número en [" +i+"][" + j+"]: " );
				matrizX[i][j] = sc.nextInt();
			}
		}
		sc.close();
		return matrizX;
	}
	
	public static void main(String[] args) {
		int tamaño = 1;
		int matriz1[][] = new int[tamaño][tamaño];
		
		matriz1 = leerMatriz();
		
		for (int i = 0; i < matriz1.length; i++) {
			for (int j = 0; j < matriz1[i].length; j++) {
	            System.out.print(matriz1[i][j] + " ");
			}
			System.out.println();
		}

	}

}
