package clase9;

public class ej1 {

	public static boolean esPalindromo(String cadena) {
		String cadenaSinEspacios = "";
		for (int i = 0; i < cadena.length(); i++) {
			if (cadena.charAt(i) != ' ') {
				cadenaSinEspacios = cadenaSinEspacios + cadena.charAt(i);
			}
		}
		
		// Comparar la cadena original con su inversa
		int longitud = cadenaSinEspacios.length();
		for (int i = 0; i < longitud / 2; i++) {
			if (cadenaSinEspacios.charAt(i) != cadenaSinEspacios.charAt(longitud - i - 1)) {
				return false;
			}
		}
		return true;
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
