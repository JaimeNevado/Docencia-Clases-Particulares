package clase7;

import java.util.Scanner;

public class juegoAhorcado {
	
	public static void mostrarPista(String p, int i) {
		for (int j = 0; j < i+1; j++) {
			System.out.print(p.charAt(j));
		}
		System.out.println();
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		final String ADIVINAR = "Secreto";
		final int intentos = 5;

		
		System.out.println("Bienvenido al Juego del Ahorcado");
		System.out.print("Nombre del Jugador: ");
		String jugador = scanner.nextLine();
		
		int i = 0; 
		boolean acertada = false;
		String guess = "";

		do {
			System.out.println("Intento " + (i+1) + ":");
			guess = scanner.nextLine();
			if (guess.equalsIgnoreCase(ADIVINAR)) {
				acertada = true;
			} else {
				System.out.println("Palabra incorrecta, pista: ");
				mostrarPista(ADIVINAR, i);
			}
			i++;			
		}
		while (i < intentos && !acertada);
		
		
		if (acertada == true) {
			System.out.println("\nFelicidades, " + jugador +  " Eres el ganador!");
		} else {
			System.out.println("\nHas agotado los intentos, has perdido");
		}

		scanner.close();
	}
}
