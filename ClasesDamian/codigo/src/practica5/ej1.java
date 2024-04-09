package practica5;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

class Paciente {
	int id;
	String nombre;
	String apellido;
	int edad;

	public Paciente(int id, String nombre, String apellido, int edad) {
		this.id = id;
		this.nombre = nombre;
		this.apellido = apellido;
		this.edad = edad;
	}

	public String toString() {
		return "ID: " + id + " NOMBRE Y APELLIDO: " + nombre + " " + apellido + " EDAD: " + edad;
	}
}

public class ej1 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int opcion = 0;

		String ruta_base = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesDamian/codigo/src/practica5/";

		while (opcion != 4) {
			mostrarMenu();
			opcion = scanner.nextInt();
			scanner.nextLine();

			switch (opcion) {
			case 1:
				crearPaciente(ruta_base);
				break;
			case 2:
				verPacientes(ruta_base);
				break;
			case 3:
				sondaje(ruta_base);
				break;
			case 4:
				System.out.println("Programa terminado con éxito");
				break;
			default:
				System.out.println("Opción no válida.");
				break;
			}
		}
		scanner.close();
	}

	private static void mostrarMenu() {
		System.out.println("Elige una opción:");
		System.out.println("1. Crear paciente");
		System.out.println("2. Ver pacientes");
		System.out.println("3. Sondaje");
		System.out.println("4. Salir");
	}

	private static void crearPaciente(String ruta_base) {
		try (BufferedReader reader = new BufferedReader(new FileReader(ruta_base + "config.txt"))) {
			int size = Integer.parseInt(reader.readLine().trim());
			reader.close();

			Scanner scanner = new Scanner(System.in);
			System.out.print("Introduce el nombre del paciente: ");
			String nombre = scanner.nextLine();
			System.out.print("Introduce el primer apellido del paciente: ");
			String apellido = scanner.nextLine();
			System.out.print("Introduce la edad del paciente: ");
			int edad = Integer.parseInt(scanner.nextLine());

			Paciente paciente = new Paciente(size + 1, nombre, apellido, edad);

			BufferedWriter writer = new BufferedWriter(new FileWriter(ruta_base + "pacientes.txt", true));
			writer.write(paciente.id + " " + paciente.nombre + " " + paciente.apellido + " " + paciente.edad + "\n");
			writer.close();

			BufferedWriter configWriter = new BufferedWriter(new FileWriter(ruta_base + "config.txt"));
			configWriter.write(String.valueOf(size + 1));
			configWriter.close();

			System.out.println("Paciente creado exitosamente.");
		} catch (IOException e) {
			System.out.println("Error al leer/escribir en archivo. " + e.getMessage());
		} catch (NumberFormatException ne) {
			System.out.println("No has convertido la edad a un entero.");
		}
	}

	private static void verPacientes(String ruta_base) {
		BufferedReader reader = null;
		BufferedReader configReader = null;
		try {
			reader = new BufferedReader(new FileReader(ruta_base + "pacientes.txt"));
			configReader = new BufferedReader(new FileReader(ruta_base + "config.txt"));
			int size = Integer.parseInt(configReader.readLine().trim());
			configReader.close();
			Paciente[] pacientes = new Paciente[size];

			String line;
			int i = 0;
			while ((line = reader.readLine()) != null) {
				String[] data = line.split(" ");
				int id = Integer.parseInt(data[0]);
				String nombre = data[1];
				String apellido = data[2];
				int edad = Integer.parseInt(data[3]);
				pacientes[i] = new Paciente(id, nombre, apellido, edad);
				i++;
			}

			for (Paciente paciente : pacientes) {
				if (paciente != null) {
					System.out.println(paciente.toString());
				}
			}
		} catch (IOException e) {
			System.out.println("Error al leer/escribir en archivo. " + e.getMessage());
		}
	}

	private static void sondaje(String ruta_base) {
		try (BufferedReader reader = new BufferedReader(new FileReader(ruta_base + "sondaje.txt"))) {
	        String line = reader.readLine();
	        reader.close();

	        String resultado = "";
	        for (int i = 0; i < line.length(); i++) {
	            char currentChar = line.charAt(i);
	            if (currentChar == '+') {
	                // Leer los dos caracteres siguientes como parte del número del diente
	                resultado += line.substring(i + 1, i + 3) + ", ";
	            }
	        }
	        if (!resultado.isEmpty()) {
	            // Eliminar la coma y el espacio extra al final
	            resultado = resultado.substring(0, resultado.length() - 2);
	            System.out.println("Han sangrado los dientes: " + resultado);
	        } else {
	            System.out.println("Ningún diente ha sangrado durante el sondaje.");
	        }
	    } catch (IOException e) {
	        System.out.println("Error al leer/escribir en archivo. " + e.getMessage());
	    }
	}
}