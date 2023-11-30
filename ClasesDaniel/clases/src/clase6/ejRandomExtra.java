package clase6;

import java.util.Random;

public class ejRandomExtra {
	
	public static final int tamaño = 10;
	
	public static void printArray(int[] array) {
		for (int num : array) {
			if (num != -1) {
				System.out.print(num + " ");				
			}
        }
		System.out.println();
	}
	
	public static void parImpar(int[] array) {
		int[] pares = new int[array.length];
		int[] impares = new int[array.length];
		
		for (int i = 0; i < pares.length; i++) {
			pares[i] = -1;
			impares[i] = -1;
		}
		
		
		int p = 0;
		int i = 0;
		
		for (int elemento : array) {
			if (elemento % 2 == 0) {
				pares[p] = elemento;
				p++;
			} else {
				impares[i] = elemento;
				i++;
			}
		}
		
		System.out.println("Array de pares: ");
		printArray(pares);
		System.out.println("Array de impares: ");
		printArray(impares);
	}

	public static void main(String[] args) {
        Random r = new Random();
        int[] miArray = new int[tamaño];

        for (int i = 0; i < tamaño; i++) {
            miArray[i] = r.nextInt(100);
        }
        
        

        // Imprime el array
        System.out.println("Array de números aleatorios:");
        printArray(miArray);
        
        parImpar(miArray);
	}

}
