package clase7;

public class ej1 {
	public static void main(String[] args) {
		String palabra = "Juana Antonia";
		int resultado = contar_letra_a(palabra);
		System.out.println("En la palabra '"+ palabra + "' la letra 'a' aparece: " + resultado + " veces");
	}


	public static int contar_letra_a(String palabra) {
		int contador = 0;

		for (int i = 0; i < palabra.length(); i++) {
			if (palabra.charAt(i) == 'a' || palabra.charAt(i) == 'A') {
				contador++;
			}
		}
		
		return contador;
	}

}
