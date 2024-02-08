package clase8;

public class ej2 {

	public static boolean esPalindromo(String cadena) {
        // Eliminar espacios en blanco y convertir a minúsculas
        cadena = cadena.replaceAll("\\s+", "").toLowerCase();
        
        // Inicializar los índices para comparar los caracteres
        int i = 0;
        int j = cadena.length() - 1;
        
        // Verificar si la cadena es un palíndromo
        while (i < j) {
            if (cadena.charAt(i) != cadena.charAt(j)) {
                // Si los caracteres en los índices i y j no coinciden, no es un palíndromo
                return false;
            }
            // Mover los índices hacia el centro de la cadena
            i++;
            j--;
        }
        
        // Si llegamos hasta aquí, la cadena es un palíndromo
        return true;
    }

    public static void main(String[] args) {
        // Ejemplo de uso
        String cadena1 = "reconocer";
        String cadena2 = "Hola";
        
        System.out.println("¿Es " + cadena1 + " un palíndromo? " + esPalindromo(cadena1)); // Output: true
        System.out.println("¿Es " + cadena2 + " un palíndromo? " + esPalindromo(cadena2)); // Output: false
    }

}
