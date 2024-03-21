package ejerciciosArrays;

public class clase {

	public static void main(String[] args) {
		String cadena = "se van sus naves";
		
		String cadenaSinEspacios = "";
		char espacio = ' ';
		
		for (int i = 0; i < cadena.length(); i++) {
			if (cadena.charAt(i) != espacio) {
				cadenaSinEspacios = cadenaSinEspacios + cadena.charAt(i);				
			}
		}
		
		System.out.println("------0");
		System.out.println(cadenaSinEspacios);
		
		String cadenaInversa = cadenaSinEspacios;

		System.out.println("La cadena inversa es: " + cadenaInversa);
		
		if (cadena.equals(cadenaInversa)) {
			System.out.println("Son palíndromas");
		} else {
			System.out.println("No lo son");
		}

	}

}
