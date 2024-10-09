package clase11;

import java.util.Scanner;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class listas {

	public static void mostrarMenu() {
		System.out.println("--- Bienvenido a gestión de matrices ---");
		System.out.println("Operaciones disponibles");
		System.out.println("1. Introducir Matriz");
		System.out.println("2. Cargar Matriz");
		System.out.println("3. Guardar Matriz");
		System.out.println("4. Listar Matriz");
		System.out.println("5. Comparar Matrices");
		System.out.println("6. Sumar Matrices");
		System.out.println("7. Restar Matrices");
		System.out.println("8. Multiplicar por un escalar");
		System.out.println("9. Transponer");
		System.out.println("10. Multiplicar matrices");
		System.out.println("11. Salir");
		System.out.println("Indique la operación que desea realiza");

	}

	public static void introducirMatriz() {

	}

	public static void cargarMatriz() {

	}

	public static void guargarMatriz() {

	}

	public static void listarMatriz(int[][] a) {
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[i].length; j++) {
				System.out.print(a[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}

	public static boolean compararMatriz (int[][] a, int [][] b){
        boolean verificar = true;
        int i = 0;
        int j = 0;
        
        while (i<a.length && verificar == true) {
        	j = 0;
            while (j < a.length && verificar == true) {
                if (a[i][j] != b[i][j]) {
                    verificar = false ; 
                }
                System.out.println("hola");
                j++;
            }
            i++;
        }
        return verificar; 
    }
	public static int[][] sumarMatrices(int[][] a, int[][] b) {
		int matrizsuma[][] = new int[3][3];
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a.length; j++) {
				matrizsuma[i][j] = a[i][j] + b[i][j];
			}
		}
		return matrizsuma;
	}

	public static int[][] restarMatrices(int[][] a, int[][] b) {
		
		// Comprobar tamaños
		int matrizresta[][] = new int[3][3];
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a.length; j++) {
				matrizresta[i][j] = a[i][j] - b[i][j];
			}
		}
		return matrizresta;
	}

	public static int[][] multiplicarEscalar(int[][] a, Scanner sc) {
		int escalar = sc.nextInt();
		int matrizresultado[][] = new int[3][3];
		for (int i = 0; i < a.length; i++) {
			for (int j = 0; j < a[0].length; j++) {
				matrizresultado[i][j] = a[i][j] * escalar;
			}
		}
		return matrizresultado;
	}

	public static int[][] transponerMatriz(int[][] matriz) {
        int filas = matriz.length;
        int columnas = matriz[0].length;

        int[][] matrizTranspuesta = new int[columnas][filas];

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                matrizTranspuesta[j][i] = matriz[i][j];
            }
        }

        return matrizTranspuesta;
    }

	public static int[][] multiplicarMatrices(int[][] matrizA, int[][] matrizB) {
		int filasA = matrizA.length;
        int columnasA = matrizA[0].length;
        int columnasB = matrizB[0].length;

        int[][] resultado = new int[filasA][columnasB];

        for (int i = 0; i < filasA; i++) {
            for (int j = 0; j < columnasB; j++) {
                for (int k = 0; k < columnasA; k++) {
                    resultado[i][j] += matrizA[i][k] * matrizB[k][j];
                }
            }
        }

        return resultado;

	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		boolean continuar = true;
		
		System.out.println("Dime el tamaño de la matriz: ");
		int tamaño = sc.nextInt();
		
		int matriz1[][] = new int[tamaño][tamaño];
		int matriz2[][] = new int[tamaño][tamaño];
		
		
		int matrizResultado[][] = new int[matriz1.length][matriz1[0].length];

		while (continuar) {
			mostrarMenu();
			int opcion = sc.nextInt();
			System.out.println("Has elegido la " + opcion + "ª opcion");
			System.out.println();
			System.out.println();

			switch (opcion) {
			case 1:
				introducirMatriz();
				break;
			case 2:
				cargarMatriz();
				break;
			case 3:
				guargarMatriz();
				break;
			case 4:
				listarMatriz(matrizResultado);
				break;
			case 5:
				if (compararMatriz(matriz1, matriz2)) {
					System.out.println("Son iguales");
				} else {
					System.out.println("Son diferentes");
				}
				break;
			case 6:
				matrizResultado = sumarMatrices(matriz1, matriz2);
				break;
			case 7:
				matrizResultado = restarMatrices(matriz1, matriz2);
				break;
			case 8:
				matrizResultado = multiplicarEscalar(matriz1, sc);
				break;
			case 9:
				//transponer();
				break;
			case 10:
				matrizResultado = multiplicarMatrices(matriz1, matriz2);
				break;
			case 11:
				continuar = false;
				System.out.println("Saliendo del programa ... ");
				break;
			default:
				System.out.println("Esa opcion no existe ");
				System.out.println();
				System.out.println();
				break;
			}
		}

	}
}