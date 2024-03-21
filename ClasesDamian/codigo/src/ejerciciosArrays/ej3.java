package ejerciciosArrays;

public class ej3 {

	public static void main(String[] args) {
		String cadena = "reconnocer";
		String cadenaInversa = "";
		
		
		for (int i = 0; i < cadena.length(); i++) {
			// cadenaInversa = e + "dro";
			cadenaInversa = cadena.charAt(i) + cadenaInversa;
		}

		System.out.println("La cadena inversa es: " + cadenaInversa);
	}

	
}
