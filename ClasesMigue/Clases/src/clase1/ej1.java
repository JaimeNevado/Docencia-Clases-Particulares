package clase1;

public class ej1 {

	public static void main(String[] args) {
		int edad = 19;
		
		if (edad < 0) {
            System.out.println("ERROR: La edad ingresada no es válida.");
        } else if (edad <= 17) {
            System.out.println("Eres menor de edad.");
        } else if (edad <= 64) {
            System.out.println("Eres mayor de edad.");
        } else {
            System.out.println("Eres un jubilado.");
        }

	}

}
