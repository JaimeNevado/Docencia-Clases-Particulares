package clase5;

public class ejercicio6 {
	// Función para verificar si un array está vacío y mostrar un mensaje
    static void verificarArray(int[] arreglo) {
        if (arreglo == null || arreglo.length == 0) {
            System.out.println("Está vacío");
        } else {
            System.out.println("Tiene " + arreglo.length + " elementos");
        }
    }

    public static void main(String[] args) {
        // Ejemplos de uso de la función
        int[] arrayVacio = {};
        int[] arrayNoVacio = {1, 2, 3, 4, 5};

        verificarArray(arrayVacio);
        verificarArray(arrayNoVacio);
    }
}
