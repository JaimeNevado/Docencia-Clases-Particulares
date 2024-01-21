package clase2;

public class ej3 {

	public static void main(String[] args) {
		String palabra = "Teléfono";
		int tamaño = palabra.length();
		System.out.println("La palabra: " + palabra + " tiene estas letras");
		for (int i = 0; i < tamaño; i++) {
			System.out.println(palabra.charAt(i));
		}
	}

}
