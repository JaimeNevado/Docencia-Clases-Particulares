package clase2;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Jugador {
	private String nombre;
	private String posicion;
	private double precioFichaje;

	public Jugador(String nombre, String posicion, double precioFichaje) {
		this.nombre = nombre;
		this.posicion = posicion;
		this.precioFichaje = precioFichaje;
	}

	// Getters y Setters

	@Override
	public String toString() {
		return "Nombre -> " + nombre + ", posición -> " + posicion + ", precio -> " + precioFichaje / 1000000
				+ " millones";
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getPosicion() {
		return posicion;
	}

	public void setPosicion(String posicion) {
		this.posicion = posicion;
	}

	public double getPrecioFichaje() {
		return precioFichaje;
	}

	public void setPrecioFichaje(double precioFichaje) {
		this.precioFichaje = precioFichaje;
	}

	public static List<Jugador> getJugadores() {
		return jugadores;
	}

	public static void setJugadores(List<Jugador> jugadores) {
		Jugador.jugadores = jugadores;
	}

	public static Jugador[] getPlantilla() {
		return plantilla;
	}

	public static void setPlantilla(Jugador[] plantilla) {
		Jugador.plantilla = plantilla;
	}

	public static Scanner getScanner() {
		return scanner;
	}

	public static void setScanner(Scanner scanner) {
		Jugador.scanner = scanner;
	}

	private static List<Jugador> jugadores = new ArrayList<>();
	private static Jugador[] plantilla = new Jugador[11];
	private static Scanner scanner = new Scanner(System.in);

	public static void mostrarMenu() {
		System.out.println("Menu:");
		System.out.println("1. Mostrar plantilla");
		System.out.println("2. Cambiar jugador");
		System.out.println("3. Valor del Equipo");
		System.out.println("4. Salir");
		System.out.print("Ingrese su opción: ");
	}

	public static void mostrarPlantilla() {
		System.out.println("Jugadores disponibles:");
		for (int i = 0; i < jugadores.size(); i++) {
			if (jugadores.get(i) != null) {
				System.out.println("pos:" + i + " " + jugadores.get(i).toString());
			}
		}

		System.out.println("\nTu plantilla:");

		for (int i = 0; i < plantilla.length; i++) {
			if (plantilla[i] != null) {
				System.out.println("Pos = " + i + " " + plantilla[i].toString());
			} else {
				System.out.println("Pos = " + i + " VACIA");
			}
		}
		System.out.println();
	}

	public static void valorEquipo() {
		double valorTotal = 0;
		for (Jugador jugador : plantilla) {
			if (jugador != null) {
				valorTotal += jugador.getPrecioFichaje();
			}
		}
		System.out.println("El valor total de tu equipo es: " + valorTotal / 1000000 + " millones");
		System.out.println();
	}

	public static void cambiarJugador() {
		System.out.println("Elige la posición del jugador que quieres cambiar de la lista:");
		int posicionLista = scanner.nextInt();

		System.out.println("Elige la posición del jugador que quieres cambiar de tu plantilla:");
		int posicionPlantilla = scanner.nextInt();

		if (posicionLista < 0 || posicionLista >= jugadores.size() || posicionPlantilla < 0
				|| posicionPlantilla >= plantilla.length) {
			System.out.println("Posiciones inválidas. Intente de nuevo.");
			return;
		}

		Jugador jugadorNuevo = jugadores.get(posicionLista);
		Jugador jugadorAntiguo = plantilla[posicionPlantilla];

		// Verificar límite de jugadores por posición
		if (!cumpleLimitePorPosicion(jugadorNuevo, posicionPlantilla)) {
			System.out.println("No se puede agregar más jugadores de esa posición.");
			return;
		}

		plantilla[posicionPlantilla] = jugadorNuevo;
		jugadores.set(posicionLista, jugadorAntiguo);

		System.out.println("Tu nueva plantilla tendrá en la pos " + posicionPlantilla + " el jugador de la posición "
				+ posicionLista + " de la lista de jugadores.");
	}

	private static boolean cumpleLimitePorPosicion(Jugador jugador, int posicionPlantilla) {
		int countPorteros = 0;
		int countDefensas = 0;
		int countCentrocampistas = 0;
		int countDelanteros = 0;

		for (Jugador jugadorEnPlantilla : plantilla) {
			if (!(jugadorEnPlantilla == null)) {
				if (jugadorEnPlantilla.getPosicion().equals("Portero"))
					countPorteros++;
				else if (jugadorEnPlantilla.getPosicion().equals("Defensa"))
					countDefensas++;
				else if (jugadorEnPlantilla.getPosicion().equals("Centrocampista"))
					countCentrocampistas++;
				else if (jugadorEnPlantilla.getPosicion().equals("Delantero"))
					countDelanteros++;
			}
		}

		switch (jugador.getPosicion()) {
		case "Portero":
			return countPorteros < 2;
		case "Defensa":
			return countDefensas < 6;
		case "Centrocampista":
			return countCentrocampistas < 6;
		case "Delantero":
			return countDelanteros < 5;
		default:
			return false;
		}
	}

	public static void main(String[] args) {
		jugadores.add(new Jugador("Kroos", "Centrocampista", 37000000.0));
		jugadores.add(new Jugador("Isco", "Centrocampista", 65000000.0));
		jugadores.add(new Jugador("Gerard", "Delantero", 35000000.0));
		jugadores.add(new Jugador("Casillas", "Portero", 39000000.0));
		jugadores.add(new Jugador("Kaká", "Defensa", 40000000.0));
		jugadores.add(new Jugador("Messi", "Delantero", 100000000.0));
		// Agrega más pibes

		int opcion;
		do {
			mostrarMenu();
			opcion = scanner.nextInt();
			switch (opcion) {
			case 1:
				mostrarPlantilla();
				break;
			case 2:
				cambiarJugador();
				break;
			case 3:
				valorEquipo();
				break;
			case 4:
				System.out.println("¡Hasta luego!");
				break;
			default:
				System.out.println("Opción no válida. Intente de nuevo.");
			}
		} while (opcion != 4);
	}
}
