package clase4;

public class ej2 {

	public static void main(String[] args) {
		int[] array1 = {1, 2, 3, 4, 5, 6};
		int[] array2 = {3, 4, 2, 5, 7, 8};
		
		boolean iguales = true;
		
		for (int i = 0; i < array1.length; i++) {
			if (array1[i] != array2[i]) {
				iguales = false;
			}
			System.out.println("Estoy en bucle");
		}
		
		if (iguales) {
			System.out.println("Son iguales");
		} else {
			System.out.println("No son iguales");
		}

	}

}
