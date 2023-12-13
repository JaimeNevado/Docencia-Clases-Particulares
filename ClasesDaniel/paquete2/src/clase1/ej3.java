package clase1;
import java.util.Scanner;

public class ej3 {

    public static final int N = 3;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Crear la matriz
        int[][] matriz = new int[N][N];

        System.out.println("Introduce " + (N * N) + " números enteros para llenar la matriz:");
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                matriz[i][j] = scanner.nextInt();

                // Verificar que los elementos sean no negativos y menores que 100
                if (matriz[i][j] < 0 || matriz[i][j] >= 100) {
                    System.out.println("Error: Los elementos deben ser no negativos y menores que 100.");
                    return;
                }
            }
        }

        // Mostrar la matriz
        System.out.println("Matriz:");
        imprimirMatriz(matriz);

        // Verificar si la matriz es doblemente estocástica normalizada
        if (esDobleEstocasticaNormalizada(matriz)) {
            System.out.println("La matriz es doblemente estocástica normalizada.");
        } else {
            System.out.println("La matriz NO es doblemente estocástica normalizada.");
        }
    }

    // Función para imprimir la matriz
    private static void imprimirMatriz(int[][] matriz) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Función para verificar si la matriz es doblemente estocástica normalizada
    private static boolean esDobleEstocasticaNormalizada(int[][] matriz) {
        // Verificar la suma de cada fila y columna
        for (int i = 0; i < N; i++) {
            int sumaFila = 0;
            int sumaColumna = 0;

            for (int j = 0; j < N; j++) {
                sumaFila += matriz[i][j];
                sumaColumna += matriz[j][i];
            }

            if (sumaFila != 100 || sumaColumna != 100) {
                return false;
            }
        }

        return true;
    }
}
