package clase2;

import java.util.Random;
import java.util.Scanner;

public class bingo2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[][] carton = generarCarton();
		int[] numerosSacados = new int[100];
		int sacadosCount = 0;

		imprimirCarton(carton);
		while (true) {
			System.out.println("Que desea hacer?: ");
			System.out.println("0) Salir");
			System.out.println("1) Sacar número");
			int opcion = sc.nextInt();
			if (opcion == 0) {
				break;
			} else if (opcion == 1) {
				System.out.println("Generando Cartón");
				carton = generarCarton();
				imprimirCarton(carton);

			} else {
				System.out.println("Error, num inválido");
			}
		}

	}

	private static int[][] generarCarton() {
		int[][] carton = new int[3][9];

		// Posicionamiento de blancos
		Random random = new Random();
		for (int fila = 0; fila < 3; fila++) {
			int blancosRestantes = 4;
			while (blancosRestantes > 0) {
				int columna = random.nextInt(9);
				if (carton[fila][columna] != -1) {
					carton[fila][columna] = -1;
					blancosRestantes--;
				}
			}
		}

		// Posicionamiento de números
		for (int columna = 0; columna < 9; columna++) {
			int[] numeros = new int[] { columna * 10 + 1, columna * 10 + 2, columna * 10 + 3, columna * 10 + 4,
					columna * 10 + 5, columna * 10 + 6, columna * 10 + 7, columna * 10 + 8, columna * 10 + 9 };
			for (int fila = 0; fila < 3; fila++) {
				if (carton[fila][columna] != -1) {
					carton[fila][columna] = numeros[fila];
				}
			}
		}

		return carton;
	}

	private static void imprimirCarton(int[][] carton) {
		System.out.println("Cartón de Bingo:");
		for (int fila = 0; fila < 3; fila++) {
			for (int columna = 0; columna < 9; columna++) {
				if (carton[fila][columna] == -1) {
					System.out.print("   ");
				} else {
					System.out.printf("%2d ", carton[fila][columna]);
				}
			}
			System.out.println();
		}
		System.out.println();
	}
}
