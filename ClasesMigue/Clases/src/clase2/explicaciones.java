package clase2;

import java.util.Scanner;

public class explicaciones {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Escribe el primer número: ");
		int numero1 = sc.nextInt();
		
		System.out.print("Escribe el segundo número: ");
		int numero2 = sc.nextInt();
		
		System.out.println("Seleccione una operacion: ");
		System.out.println("1) Sumar");
		System.out.println("2) Restar");
		System.out.println("3) Multiplicar");
		System.out.println("4) Dividir");
		
		int eleccion = sc.nextInt();
		
		if (eleccion == 1) {
			int suma = numero1 + numero2;
			System.out.println("La suma es: " + suma);
		} else if (eleccion == 2){
			int resta = numero1 - numero2;
			System.out.println("La resta es: " + resta);
		} else if (eleccion == 3){
			int multiplicacion = numero1 * numero2;
			System.out.println("La multiplicacion es: " + multiplicacion);
		} else if (eleccion == 4){
			int division = numero1 / numero2;
			System.out.println("La division es: " + division);
		} else {
			System.out.println("Numero no válido");
		}
		
		
		

		

	}

}
