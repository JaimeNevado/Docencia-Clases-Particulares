package clase4;

public class ejercicio2 {

	public static void main(String[] args) {
        int[] array1 = {1, 2, 3, 4, 5};
        int[] array2 = {1, 2, 3, 1, 5};
     
        boolean sonIguales = true;

        if (array1.length != array2.length) {
            sonIguales = false;
        } else {
            for (int i = 0; i < array1.length; i++) {
                if (array1[i] != array2[i]) {
                    sonIguales = false;
                }
            }
        }

        // Imprimir el resultado
        if (sonIguales) {
            System.out.println("Los arrays son iguales.");
        } else {
            System.out.println("Los arrays no son iguales.");
        }
	}	

}
