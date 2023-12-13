package clase1;

public class ej1 {
	
	public static int[][] sumarMatrices(int[][] matriz1, int[][] matriz2) {
		int filas = matriz1.length;
		int columnas = matriz1[0].length;

		int[][] matrizResultado = new int[filas][columnas];

		for (int i = 0; i < filas; i++) {
			for (int j = 0; j < columnas; j++) {
				matrizResultado[i][j] = matriz1[i][j] + matriz2[i][j];
			}
		}

		return matrizResultado;
	}

	public static void main(String[] args) {
		// Ejemplo de uso
		int[][] matriz1 = {
		        { 1,  2,  3,  4,  5,  6},
		        { 7,  8,  9, 10, 11, 12},
		        {13, 14, 15, 16, 17, 18},
		        {19, 20, 21, 22, 23, 24},
		        {25, 26, 27, 28, 29, 30},
		        {31, 32, 33, 34, 35, 36}
		    };

		int[][] matriz2 =  {
		        { 9,  8,  7,  6,  5,  4},
		        { 3,  2,  1,  0, -1, -2},
		        {-3, -4, -5, -6, -7, -8},
		        {-9,-10,-11,-12,-13,-14},
		        {-15,-16,-17,-18,-19,-20},
		        {-21,-22,-23,-24,-25,-26}
		    };

		int[][] resultado = sumarMatrices(matriz1, matriz2);

		// Imprimir matriz resultado
		for (int i = 0; i < resultado.length; i++) {
			for (int j = 0; j < resultado[0].length; j++) {
				System.out.print(resultado[i][j] + " ");
			}
			System.out.println();
		}
	}
}
