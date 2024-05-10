package clase3Mayo2024;

import java.util.ArrayList;
import java.util.LinkedList;

public class listasEnlazadasExplicacion {

	public static void main(String[] args) {
		LinkedList <Integer> miLista = new LinkedList<>();
		
		miLista.add(19);
		miLista.add(20);
		miLista.add(21);
		miLista.add(22);
		
		miLista.add(2, 10);
		
		int valor = miLista.get(0);
		
		//int ultDato = miLista.getLast();
		
		int tamaño = miLista.size();
		
		int ultDato = miLista.get(tamaño - 1);

		
		//miLista.clear();
		
		if (miLista.isEmpty() == false) {
			System.out.println("El primer elemento de la lista es: " + valor);
			System.out.println("El último elemento de la lista es: " + ultDato);
			System.out.println(miLista);
		} else {
			System.out.println("La lista esta vacia");
		}
		
		
		
	
	}

}
