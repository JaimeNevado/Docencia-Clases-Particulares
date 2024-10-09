package clase4;

public class ejercicio1 {

	public static void main(String[] args) {
        int[] array1 = {1, 2, 3, 4, 5, 6};
        int[] array2 = {3, 4, 2, 5, 7, 8};

        int[] arrayResultado = {0, 0, 0, 0, 0, 0};

        for (int i = 0; i < array1.length; i++) {
            arrayResultado[i] = array1[i] + array2[i];
        }

        System.out.println("Resultado de la suma:");

        for (int i = 0; i < arrayResultado.length; i++) {
            System.out.print(arrayResultado[i] + " ");
        }
	}

}
