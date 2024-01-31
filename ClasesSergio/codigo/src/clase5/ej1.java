package clase5;

public class ej1 {

	public static int[][] construirMatrizCruz(int tamaño) {

		int[][] matriz = new int[tamaño][tamaño];

		int mitad = tamaño / 2;
		for (int i = 0; i < tamaño; i++) {
			matriz[mitad][i] = 1; // Fila del medio
			matriz[i][mitad] = 1; // Columna del medio
		}

		return matriz;
	}

	public static void imprimirMatriz(int[][] matrizCruz) {
		for (int i = 0; i < matrizCruz.length; i++) {
			for (int j = 0; j < matrizCruz[i].length; j++) {
				System.out.print(matrizCruz[i][j] + " ");
			}
			System.out.println();
		}
	}
	
	public static void main(String[] args) {
		int tamaño = 5;

		int[][] matrizCruz = construirMatrizCruz(tamaño);

		imprimirMatriz(matrizCruz);
	}

}
