package clase1;

import java.util.Scanner;

public class hola {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		System.out.print("Dime el tamaño: ");
		int tamaño = sc.nextInt();
		int[] a = new int[tamaño];
		// a[] = {0, 0, 0, 0... tamaño]
		
		
		for (int i = 0; i < tamaño; i++) {
			System.out.print("Dime un numero: ");
			a[i] = sc.nextInt();
		}

		for (int i = 0; i < tamaño; i++) {
			System.out.print(a[i] + " ");
		}
		
	}

}
