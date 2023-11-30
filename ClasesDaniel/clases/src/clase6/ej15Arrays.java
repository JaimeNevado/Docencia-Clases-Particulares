package clase6;

import java.util.Random;
import java.util.Scanner;

public class ej15Arrays {
	
	// Método para mostrar el estado de las mesas
	private static void mostrarEstadoMesas(int[] mesas) {
		for (int i = 0; i < mesas.length; i++) {
			System.out.println("Mesa " + (i + 1) + ": " + mesas[i] + " personas");
		}
		System.out.println("----------------------");
	}
	
	public static void main(String[] args) {
		int numeroMesas = 10;
		int[] mesas = new int[numeroMesas];

		Random random = new Random();
		for (int i = 0; i < numeroMesas; i++) {
			mesas[i] = random.nextInt(5); // Números aleatorios de 0 a 4
		}

		System.out.println("Estado inicial de las mesas:");
		mostrarEstadoMesas(mesas);

		// Simular la llegada de clientes
		Scanner scanner = new Scanner(System.in);
		System.out.print("¿Cuántos son en su grupo?: ");
		int clientesEnGrupo = scanner.nextInt();

		// Verificar si el grupo es válido
		if (clientesEnGrupo > 4) {
			System.out.println("Lo siento, no admitimos grupos de " + clientesEnGrupo
					+ ", haga grupos de 4 personas como máximo e intente de nuevo.");
		} else {
			// Buscar una mesa para el grupo
			boolean mesaEncontrada = false;
			for (int i = 0; i < numeroMesas; i++) {
				if ((mesas[i] + clientesEnGrupo) <= 4) {
					mesas[i] += clientesEnGrupo;
					System.out.println("Por favor, siéntense en la mesa número " + i + 1);
					mesaEncontrada = true;
					break;
				}
			}

			// Si no se encontró una mesa, mostrar mensaje
			if (!mesaEncontrada) {
				System.out.println("Lo siento, no hay mesas disponibles para su grupo en este momento.");
			}

			// Mostrar el estado actualizado de las mesas
			System.out.println("Estado actualizado de las mesas:");
			mostrarEstadoMesas(mesas);
		}
	}

}
