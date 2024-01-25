package clase5;

public class explicacion {

	public static void main(String[] args) {
		int[] array1 = {1, 2, 3, 4, 5, 6};
		int[] array2 = {1, 4, 2, 5, 7, 8};
		
		boolean iguales = true;
		String nombre = "Sergio";
		int i = 0;
		
		while(i < array1.length && iguales == true) {
			if (array1[i] != array2[i]) {
				iguales = false;
			}
			System.out.println("Estoy en bucle");
			i++;
		}
		
		if (iguales) {
			System.out.println("Son iguales");
		} else {
			System.out.println("No son iguales");
		}

	}

}
