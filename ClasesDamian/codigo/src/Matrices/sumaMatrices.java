package Matrices;

public class sumaMatrices {
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

        int[][] matrizResultado = sumar_matrices(matriz1, matriz2);
        escribir_matriz(matrizResultado);
    }

    public static int[][] sumar_matrices(int[][] matriz1, int[][] matriz2) {
        int[][] matrizResultado = new int[6][6];

        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                matrizResultado[i][j] = matriz1[i][j] + matriz2[i][j];
            }
        }

        return matrizResultado;
    }

    public static void escribir_matriz(int[][] matriz) {
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }

}
