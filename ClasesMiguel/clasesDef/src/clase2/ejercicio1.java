package clase2;

public class ejercicio1 {

	public static void main(String[] args) {
		int edad = 17;

		if (edad < 0) {
			System.out.println("ERROR: La edad ingresada no es válida.");
		} else if (edad >= 0 && edad <= 17) {
			System.out.println("Eres menor de edad.");
		} else if (edad >= 18 && edad <= 64) {
			System.out.println("Eres mayor de edad.");
		} else {
			System.out.println("Eres un jubilado.");
		}
	}

}
