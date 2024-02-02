package clase6;

public class ej5 {
	
	public static boolean esPar(int n) {
		boolean par = false;
		if (n % 2 == 0) {
			par = true;
		}
		return par;
	}

	public static boolean paridadArray(int[] nums) {
		boolean paridad = true;
		for (int n : nums) {
			if (!esPar(n)) {
				paridad = false;
			}			
		}
		return paridad;
	}

	public static void escribirArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
        	if (i != array.length - 1) {
        		System.out.print(array[i] + ", ");        		
        	} else {
        		System.out.print(array[i]);        		        		
        	}
        }
        System.out.println();
    }
	
	public static void main(String[] args) {
		int[] numeros = {2, 4, 6, 8};
		System.out.print("El array: ");
		escribirArray(numeros);
		if (paridadArray(numeros)) {
			System.out.println("Es un array con paridad");
		} else {
			System.out.println("No es un array con paridad");
		}
	}

}
