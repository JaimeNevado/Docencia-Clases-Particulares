package clase6;

public class ej1 {

	public static void main(String[] args) {
        int[] numeros = {1, 3, 5, 7, 9};

        escribirArray(numeros);
    }

    public static void escribirArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
        	if (i != array.length - 1) {
        		System.out.print(array[i] + ", ");        		
        	} else {
        		System.out.print(array[i]);        		        		
        	}
        }
    }

}
