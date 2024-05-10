package clase3Mayo2024;

import java.util.ArrayList;
import java.util.LinkedList;

public class tiempoListasEnlazadas {

	public static void main(String[] args) {
		// Creamos una lista enlazada
        LinkedList<Integer> listaEnlazada = new LinkedList<>();

        // Lista enlazada
        for (int i = 0; i < 100000; i++) {
            listaEnlazada.add(i);
        }
        
        long startTime = System.nanoTime(); // 19:00
        Integer elementoEnlazada = listaEnlazada.get(50000);
        long endTime = System.nanoTime(); // 19:01
        long tiempoEnlazada = endTime - startTime; // 00:01
        System.out.println("Tiempo de acceso en lista enlazada: " + tiempoEnlazada + " nanosegundos");

        
        
        // ArrayList
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (int i = 0; i < 100000; i++) {
            arrayList.add(i);
        }

        startTime = System.nanoTime();
        Integer elementoArrayList = arrayList.get(50000);
        endTime = System.nanoTime();
        long tiempoArrayList = endTime - startTime;
        System.out.println("Tiempo de acceso en ArrayList: " + tiempoArrayList + " nanosegundos");
        
        System.out.println("El ArrayList es: " + tiempoEnlazada / tiempoArrayList + " veces más eficiente");
    }

}
