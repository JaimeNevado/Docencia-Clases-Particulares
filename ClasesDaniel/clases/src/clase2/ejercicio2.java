package clase2;

public class ejercicio2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// Definir dos arrays
        int[] array1 = {1, 2, 3, 4, 5};
        int[] array2 = {1, 2, 3, 4, 5};  // Puedes cambiar los elementos para probar diferentes casos

        // Verificar si los arrays son iguales
        boolean sonIguales = true;
        
        // Verificar elemento por elemento
        for (int i = 0; i < array1.length; i++) {
            if (array1[i] != array2[i]) {
                sonIguales = false;
            }
        }

        // Mostrar el resultado
        if (sonIguales) {
            System.out.println("Los arrays son iguales.");
        } else {
            System.out.println("Los arrays no son iguales.");
        }
	}

}
