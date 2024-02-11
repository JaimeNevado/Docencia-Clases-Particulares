package clase8;

public class ej2 {

	public static boolean esPalindromo(String cadena) {
        cadena = cadena.toLowerCase();
        
        int i = 0;
        int j = cadena.length() - 1;
        
        while (i < j) {
            if (cadena.charAt(i) != cadena.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        
        return true;
    }

    public static void main(String[] args) {
a        String cadena1 = "reconocer";
        String cadena2 = "Hola";
        
        System.out.println("¿Es " + cadena1 + " un palíndromo? " + esPalindromo(cadena1)); // Output: true
        System.out.println("¿Es " + cadena2 + " un palíndromo? " + esPalindromo(cadena2)); // Output: false
    }

}
