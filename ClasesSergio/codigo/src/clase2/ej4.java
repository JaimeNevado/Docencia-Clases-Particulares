package clase2;

public class ej4 {

	public static void main(String[] args) {
		String palabra = "Azul";
		int tamaño = palabra.length();
		int vocales = 0;
		char c;
		for (int i = 0; i < tamaño; i++) {
			c = palabra.toLowerCase().charAt(i);
			if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
				vocales++;
			}
		}
		System.out.println("La palabra: " + palabra + " tiene " + vocales + " vocales");

	}

}
