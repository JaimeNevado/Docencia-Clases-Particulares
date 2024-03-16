package ejerciciosArrays;

public class ej1 {

	public static void main(String[] args) {
		int[] array1 = { 1, 2, 3, 4, 5 };
		int[] array2 = { 1, 2, 3, 4, 6 };

		escribirArray(array1);
		escribirArray(array2);

		boolean sonIguales = true;

		// Verificar si los arrays tienen la misma longitud
		if (array1.length != array2.length) {
			sonIguales = false;
		} else {
			// Comparar elementos uno por uno
			for (int i = 0; i < array1.length; i++) {
				if (array1[i] != array2[i]) {
					sonIguales = false;
					break;
				}
			}
		}

		// Imprimir el resultado
		if (sonIguales) {
			System.out.println("Los arrays son iguales");
		} else {
			System.out.println("Los arrays no son iguales");
		}
	}

	public static void escribirArray(int[] array) {
		System.out.print("Array: ");
		for (int i = 0; i < array.length; i++) {
			System.out.print(array[i]);
			if (i < array.length - 1) {
				System.out.print(", ");
			}
		}
		System.out.println();
	}

}
