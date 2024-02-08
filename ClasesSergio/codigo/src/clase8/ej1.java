package clase8;

public class ej1 {

	public static void escribirMatriz(int[][] matriz) {
		for (int i = 0; i < matriz.length; i++) {
			for (int j = 0; j < matriz[i].length; j++) {
				System.out.print(matriz[i][j] + " ");
			}
			System.out.println();
		}
	}

	public static boolean esNoNegativaYMenorQue100(int[][] matriz) {
		boolean estado = true;
		for (int[] fila : matriz) {
			for (int elemento : fila) {
				if (elemento < 0 || elemento >= 100) {
					estado = false;
					break;
				}
			}
			if (!estado)
				break;
		}
		return estado;
	}

	public static boolean sumaFilaIgualA100(int[][] matriz) {
		boolean estado = true;
		for (int[] fila : matriz) {
			int sumaFila = 0;
			for (int elemento : fila) {
				sumaFila += elemento;
			}
			if (sumaFila != 100) {
				estado = false;
				break;
			}
		}
		return estado;
	}

	public static boolean sumaColumnaIgualA100(int[][] matriz) {
		boolean estado = true;
		for (int i = 0; i < matriz[0].length; i++) {
			int sumaColumna = 0;
			for (int[] fila : matriz) {
				sumaColumna += fila[i];
			}
			if (sumaColumna != 100) {
				estado = false;
				break;
			}
		}
		return estado;
	}

	public static boolean verificarDoblementeEstocasticaNormalizada(int[][] matriz) {
		boolean estado = false;
		if (esNoNegativaYMenorQue100(matriz) && sumaFilaIgualA100(matriz) && sumaColumnaIgualA100(matriz)) {
			estado = true;
		}
		return estado;
	}

	public static void main(String[] args) {
		int[][] matrizEjemplo = { { 20, 30, 50 }, { 50, 0, 50 }, { 30, 70, 0 } };

		int[][] matrizEjemplo2 = { { 20, 30, 50 }, { 50, -5, 50 }, { 25, 75, 0 } };

		boolean resultado = verificarDoblementeEstocasticaNormalizada(matrizEjemplo);

		System.out.println("La matriz de ejemplo es:");
		escribirMatriz(matrizEjemplo);

		if (resultado) {
			System.out.println("La matriz SI es doblemente estocástica normalizada");
		} else {
			System.out.println("La matriz NO es doblemente estocástica normalizada");
		}
	}

}
