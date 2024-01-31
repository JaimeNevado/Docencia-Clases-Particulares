package clase2;

import java.util.Scanner;

public class ej3 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Escribe el carnet: ");
		String carnet = sc.next();
		
		switch (carnet.charAt(0)) {
		case 'F':
			System.out.println("El empleado es Francés");
			break;
		case 'E':
			System.out.println("El empleado es Español");
			break;
		case 'P':
			System.out.println("El empleado es Portugués");
			break;
		default:
			System.out.println("Error en el código de carnet");
			break;
		}

	}

}
