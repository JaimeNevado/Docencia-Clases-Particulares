package ejClase5;

public class ej2 {
	public static void main(String[] args) {
        int[][] matriz1 = {
            { 1,  2,  3,  4,  5,  6},
            { 7,  8,  9, 10, 11, 12},
            {13, 14, 15, 16, 17, 18},
            {19, 20, 21, 22, 23, 24},
            {25, 26, 27, 28, 29, 30},
            {31, 32, 33, 34, 35, 36}
        };

        int[][] matriz2 = {
            { 9,  8,  7,  6,  5,  4},
            { 3,  2,  1,  0, -1, -2},
            {-3, -4, -5, -6, -7, -8},
            {-9,-10,-11,-12,-13,-14},
            {-15,-16,-17,-18,-19,-20},
            {-21,-22,-23,-24,-25,-26}
        };

        try {
            int[][] resultado = dividirMatrices(matriz1, matriz2);
            imprimirMatriz(resultado);
        } catch (ArithmeticException e) {
            System.out.println("Error: No se puede dividir por cero.");
        } catch (Exception e) {
            System.out.println("Error inesperado: " + e.getMessage());
        }
    }

    public static int[][] dividirMatrices(int[][] matriz1, int[][] matriz2) {
        int filas = matriz1.length;
        int columnas = matriz1[0].length;
        int[][] resultado = new int[filas][columnas];

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                resultado[i][j] = matriz1[i][j] / matriz2[i][j];
            }
        }

        return resultado;
    }

    public static void imprimirMatriz(int[][] matriz) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[1].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
