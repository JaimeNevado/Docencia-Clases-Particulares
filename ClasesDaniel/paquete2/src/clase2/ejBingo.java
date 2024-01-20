package clase2;

import java.util.Arrays;
import java.util.Random;
import java.util.Scanner;

public class ejBingo {

	public static void main(String[] args) {
		//int[][] carton = generarCarton();
		int[] numerosSacados = new int[15];
		int sacadosCount = 0;

		
		//imprimirCarton(carton);

		System.out.println("Hola");
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

	private static int sacarNumero(int[] numerosSacados) {
		Random random = new Random();
		int numero;
		do {
			numero = random.nextInt(99) + 1;
		} while (Arrays.stream(numerosSacados).anyMatch(n -> n == numero));
		return numero;
	}

	private static void marcarNumero(int[][] carton, int numero) {
		for (int fila = 0; fila < 3; fila++) {
			for (int columna = 0; columna < 9; columna++) {
				if (carton[fila][columna] == numero) {
					carton[fila][columna] = -1; // Marcar con -1
					return;
				}
			}
		}
	}

	private static boolean esBingo(int[][] carton) {
		for (int columna = 0; columna < 9; columna++) {
			boolean columnaCompleta = true;
			for (int fila = 0; fila < 3; fila++) {
				if (carton[fila][columna] != -1) {
					columnaCompleta = false;
					break;
				}
			}
			if (columnaCompleta) {
				return true;
			}
		}

		for (int fila = 0; fila < 3; fila++) {
			boolean filaCompleta = true;
			for (int columna = 0; columna < 9; columna++) {
				if (carton[fila][columna] != -1) {
					filaCompleta = false;
					break;
				}
			}
			if (filaCompleta) {
				return true;
			}
		}

		// Revisar diagonales
		if (carton[0][0] == -1 && carton[1][1] == -1 && carton[2][2] == -1) {
			return true;
		}

		if (carton[0][2] == -1 && carton[1][1] == -1 && carton[2][0] == -1) {
			return true;
		}

		return false;
	}
}
