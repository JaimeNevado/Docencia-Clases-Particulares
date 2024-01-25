package clase5;

import java.util.Random;

public class ej1 {

	public static void main(String[] args) {
		Random rd = new Random();
		int[] array1 = new int[23];
		
		for (int i = 0; i < array1.length; i++) {
			int numero = rd.nextInt()%4;
			if (numero < 0) {
				numero = numero * -1;
			}
			array1[i] = numero;
			
		}
		
		
		for (int i = 0; i < array1.length; i++) {
			System.out.print(array1[i] + " ");
		}
		
		
	}

}
