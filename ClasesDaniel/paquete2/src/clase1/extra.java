package clase1;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class extra {

    private static final int TAM = 5;  // Puedes ajustar el tamaño según tus necesidades

    public static List<Integer> mayorLongitud(List<Integer> array) {
        if (array == null || array.isEmpty()) {
            return null;
        }
        List<Integer> sol = new ArrayList<>();
   
        for (int i = 1; i < array.size(); i++) {
            if (array.get(i) >= array.get(i - 1)) {
                sol.add(array.get(i - 1));
            } 
        }

        return sol;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Integer> sequence = new ArrayList<>();

        System.out.println("Ingrese una secuencia de " + TAM + " números enteros:");

        for (int i = 0; i < TAM; i++) {
            System.out.print("Número " + (i + 1) + ": ");
            int number = scanner.nextInt();
            sequence.add(number);
        }

        List<Integer> result = mayorLongitud(sequence);
        System.out.println("La longitud de la mayor subsecuencia ordenada es: " + result);
    }
}
