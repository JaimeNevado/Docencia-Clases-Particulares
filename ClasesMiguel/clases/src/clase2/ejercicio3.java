package clase2;

public class ejercicio3 {
	public static void main(String[] args) {
		// Definir la variable nombre
		String nombre = "Jaime";

		// Comprobar si el nombre termina en "e" o "l"
		if (nombre.charAt(nombre.length() - 1) == 'e' || nombre.charAt(nombre.length() - 1) == 'l') {
			System.out.println(nombre + " sabe programar en Java.");
		} else {
			System.out.println(nombre + " no sabe programar.");
		}
	}
}
