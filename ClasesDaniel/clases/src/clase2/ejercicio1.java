package clase2;

import java.util.Scanner;

public class ejercicio1 {

	public static void main(String[] args) {
		// Definir los dos arrays
        int[] array1 = {1, 2, 3, 4, 5, 6};
        int[] array2 = {3, 4, 2, 5, 7, 8};

        // Inicializar el array resultado
        int[] arrayResultado = new int[6];

        // Sumar los elementos correspondientes de array1 y array2 y guardar el resultado en arrayResultado
        for (int i = 0; i < 6; i++) {
            arrayResultado[i] = array1[i] + array2[i];
        }

        // Imprimir los elementos de arrayResultado
        System.out.println("Array Resultado:");
        for (int elemento : arrayResultado) {
            System.out.println(elemento);
        }
		
	}

}
