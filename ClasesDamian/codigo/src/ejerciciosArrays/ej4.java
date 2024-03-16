package ejerciciosArrays;

public class ej4 {
	public static boolean esPalindromo(String cadena) {
		String cadenaSinEspacios = "";
		for (int i = 0; i < cadena.length(); i++) {
			if (cadena.charAt(i) != ' ') {
				cadenaSinEspacios = cadenaSinEspacios + cadena.charAt(i);
			}
		}
		
		cadena = cadenaSinEspacios;

		// Comparar la cadena original con su inversa
		int i = 0;
		int j = cadena.length() - 1;
		boolean esPalindroma = true;
		while (esPalindroma && i < j) {
			if (cadena.charAt(i) != cadena.charAt(j)) {
				esPalindroma = false;
			}
			i++;
			j--;
		}
		return esPalindroma;
	}

	public static void main(String[] args) {
		String cadena1 = "se van sus naves";
		String cadena2 = "yo hago yoga hoy";
		String cadena3 = "no soy palindromo";

		System.out.println(cadena1 + ": " + esPalindromo(cadena1));
		System.out.println(cadena2 + ": " + esPalindromo(cadena2));
		System.out.println(cadena3 + ": " + esPalindromo(cadena3));
	}

}
