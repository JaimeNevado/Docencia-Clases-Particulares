package clase8;

public class ej2 {
	
    public static int[][] construirMatrizCruz(int tamaño) {
        if (tamaño % 2 == 0) {
            throw new IllegalArgumentException("El tamaño debe ser un número impar");
        }

        int[][] matriz = new int[tamaño][tamaño];

        int mitad = tamaño / 2;
        for (int i = 0; i < tamaño; i++) {
            matriz[mitad][i] = 1; // Fila del medio
            matriz[i][mitad] = 1; // Columna del medio
        }

        return matriz;
    }
    

    public static void main(String[] args) {
        int tamaño = 5;

        int[][] matrizCruz = construirMatrizCruz(tamaño);

        // Imprimir la matriz
        for (int i = 0; i < tamaño; i++) {
            for (int j = 0; j < tamaño; j++) {
                System.out.print(matrizCruz[i][j] + " ");
            }
            System.out.println();
        }
    }
}
