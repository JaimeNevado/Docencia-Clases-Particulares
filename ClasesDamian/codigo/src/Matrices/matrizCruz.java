package Matrices;

public class matrizCruz {
	public static void main(String[] args) {
		int[][] matriz = construir_matriz_cruz(5);
		imprimirMatriz(matriz);
	}

	public static int[][] construir_matriz_cruz(int tamaño) {
		int[][] matriz = new int[tamaño][tamaño];

		// Construir la cruz con unos
		for (int i = 0; i < tamaño; i++) {
			matriz[i][tamaño / 2] = 1; // Columna central
			matriz[tamaño / 2][i] = 1; // Fila central
		}

		return matriz;
	}

	public static void imprimirMatriz(int[][] matriz) {
		for (int i = 0; i < matriz.length; i++) {
			for (int j = 0; j < matriz[i].length; j++) {
				System.out.print(matriz[i][j] + " ");
			}
			System.out.println();
		}
	}
}
