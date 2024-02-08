package clase2;

import java.util.Scanner;

public class ej2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Ingresa su nota: ");
		double num1 = sc.nextInt();
		System.out.print("Ingresa su nota: ");
		double num2 = sc.nextInt();
		System.out.print("Ingresa su nota: ");
		double num3 = sc.nextInt();
		
		double media = (num1 + num2 + num3) / 3;
		
		System.out.println("La media es: " + media);

	}

}
