package clase3Mayo2024;

import java.util.ArrayList;
import java.util.LinkedList;

public class listasEnlazadasExplicacion {

	public static void main(String[] args) {
		LinkedList<Integer> lista = new LinkedList<>();
        lista.add(1);
        lista.add(2);
        lista.add(3);
        
        lista.removeFirst();
        
        System.out.println(lista.contains(3));
	
	}

}
