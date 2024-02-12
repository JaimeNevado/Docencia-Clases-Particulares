package clase9;

public class ej2 {

	public static String invertirCadena(String cadena) {
		String cadenaInversa = "";

		for (int i = cadena.length() - 1; i >= 0; i--) {
			cadenaInversa = cadenaInversa + cadena.charAt(i);
		}
		return cadenaInversa;
	}

	public static void main(String[] args) {
		String cadena = "ordenador";
		
		System.out.println("La cadena original es: " + cadena);
		System.out.println("La cadena invertida es: " + invertirCadena(cadena));
		

		
	}
	
}
