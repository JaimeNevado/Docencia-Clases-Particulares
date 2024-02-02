package clase6;

import java.util.Scanner;

public class ej2 {

	public static double calcularAreaTriangulo(double b, double a) {
		double area = 0;
		if (b <= 0 || a <= 0) {
			System.out.println("Error, las longitudes deben ser positivas");
		} else {
			area = (b * a)/2;
		}
		return area;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Introduzca la base del triángulo: ");
		double base = sc.nextDouble();
		System.out.print("Introduzca la altura del triángulo: ");
		double altura = sc.nextDouble();
		
		double solucion = calcularAreaTriangulo(base, altura);
		
		System.out.println("El área del triángulo es: " + solucion);
	}

}
