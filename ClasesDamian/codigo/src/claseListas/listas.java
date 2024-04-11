package claseListas;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class listas {

	public static void main(String[] args) {
		Map<String, Integer> miMapa = new HashMap<>();

		ArrayList<Map<String, Integer>> lista = new ArrayList<>();

	

			//		  Key  , Value
		miMapa.put("MANZANAS", 5);
		miMapa.put("PERAS", 3);
		miMapa.put("MELONES", 7);
		miMapa.put("SANDIA", 2);
		miMapa.put("FRESAS", 13);
		miMapa.put("MCDONALDS", 70);

		// miMapa.remove("MCDONALDS");

		for (Map.Entry<String, Integer> elemento : miMapa.entrySet()) {
			String nombre = elemento.getKey();
			int valor = elemento.getValue();
			if (valor < 5) {
				System.out.println(nombre + " -> " + valor + " COMPRAR!!");
			} else {
				System.out.println(nombre + " -> " + valor);
			}
		}
		
		
		lista.add(miMapa); // Posicion 0

		System.out.println(lista);
		
		

	}

}
