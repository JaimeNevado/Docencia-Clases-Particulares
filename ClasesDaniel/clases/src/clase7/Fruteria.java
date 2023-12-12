package clase7;

import java.util.Scanner;

public class Fruteria {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		final int TOTAL_FRUTAS = 10;

		String[] nombresFrutas = new String[] { "Naranjas", "Limones", "Peras", "", "", "", "", "", "", "" };
		// int[] cantidadFrutas = new int[TOTAL_FRUTAS];
		float[] precioKgFrutas = new float[] { 1.55f, 1.35f, 0.80f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f };

		String opcion = "";
		do {
			opcion = menu(scanner);
			switch (opcion.toUpperCase()) {
			case "A":
				insertarFruta(nombresFrutas, precioKgFrutas);
				break;
			case "B":
				break;
			case "C":
				modificarPrecioFruta(nombresFrutas, precioKgFrutas);
				break;
			case "D":
				break;
			case "E":
				mostrarInforme(nombresFrutas, precioKgFrutas);
				break;
			}
		} while (!opcion.toUpperCase().equals("X"));

		scanner.close();
	}

	public static String menu(Scanner scanner) {
		System.out.println("a - Insertar fruta");
		// System.out.println("b - Comprar fruta");
		System.out.println("c - Modificar precio fruta");
		// System.out.println("d - Modificar todos los precios");
		System.out.println("e - Mostrar informe");
		System.out.println("x - Salir");
		System.out.println("---------------------------------------------");
		System.out.print("Indique opción... ");
		String opcion = scanner.nextLine();
		System.out.println();
		return opcion;
	}

	public static void insertarFruta(String[] nombresFrutas, float[] precioKgFrutas) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Ingrese el nombre de la fruta: ");
        String nombreFruta = scanner.nextLine();
        System.out.print("Ingrese el precio por kilogramo: ");
        float precio = scanner.nextFloat();

        // Buscar la primera posición disponible para insertar la nueva fruta
        for (int i = 0; i < nombresFrutas.length; i++) {
            if (nombresFrutas[i].isEmpty()) {
                nombresFrutas[i] = nombreFruta;
                precioKgFrutas[i] = precio;
                System.out.println("Fruta insertada correctamente.\n");
                return;
            }
        }
        System.out.println("No hay espacio para más frutas.\n");
	}

	public static void modificarPrecioFruta(String[] nombresFrutas, float[] precioKgFrutas) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Ingrese el nombre de la fruta a modificar: ");
        String nombreFruta = scanner.nextLine();
        for (int i = 0; i < nombresFrutas.length; i++) {
            if (nombresFrutas[i].equalsIgnoreCase(nombreFruta)) {
                System.out.print("Ingrese el nuevo precio por kilogramo: ");
                float nuevoPrecio = scanner.nextFloat();
                precioKgFrutas[i] = nuevoPrecio;
                System.out.println("Precio de la fruta modificado correctamente.\n");
                return;
            }
        }
        System.out.println("La fruta no fue encontrada.\n");
	}

	public static void mostrarInforme(String[] nombresFrutas, float[] precioKgFrutas) {
		System.out.println("Informe de frutas:");
		for (int i = 0; i < nombresFrutas.length; i++) {
			if (!nombresFrutas[i].isEmpty()) {
				System.out.println(nombresFrutas[i] + ": $" + precioKgFrutas[i] + " por kg");
			}
		}
		System.out.println();
	}
}