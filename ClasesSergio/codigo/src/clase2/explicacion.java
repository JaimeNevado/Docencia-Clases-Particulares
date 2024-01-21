package clase2;

public class explicacion {

	public static void main(String[] args) {
		String nombre = "Ana";
		int tamaño = nombre.length();
		
		
		if (tamaño > 4) {
			System.out.println("El cuarto caracter es: " + nombre.charAt(4));			
		} else {
			System.out.println("Error, cadena muy corta");
		}

   
	}

}
