package clase10;

import java.util.Scanner;

public class boleano {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean salida = false;
		char opcion = ' ';
		Scanner sc = new Scanner(System.in);
		
		while (!salida) {
			System.out.println("Dime la letra: ");
            opcion = sc.next().toUpperCase().charAt(0);
            System.out.println(opcion);
            if (opcion == 'S' || opcion == 's') {
            	salida = true;            	
            }
		}
		
		System.out.println("Hemos salido del bucle");
	}

}
