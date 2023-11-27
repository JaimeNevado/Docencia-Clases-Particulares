package clase5;

import java.util.Scanner;

public class ejercicio2 {

    // Función para sumar dos números
    static void suma(double num1, double num2) {
        System.out.println("La suma es: " + (num1 + num2));
    }

    // Función para restar dos números
    static void resta(double num1, double num2) {
        System.out.println("La resta es: " + (num1 - num2));
    }

    // Función para multiplicar dos números
    static void multiplicacion(double num1, double num2) {
        System.out.println("La multiplicación es: " + (num1 * num2));
    }

    // Función para dividir dos números
    static void division(double num1, double num2) {
        if (num2 != 0) {
            System.out.println("La división es: " + (num1 / num2));
        } else {
            System.out.println("No se puede dividir por cero.");
        }
    }

    // Función para escribir el menú
    static void escribirMenu() {
        System.out.println("¿Qué quieres hacer?");
        System.out.println("1) Sumar");
        System.out.println("2) Restar");
        System.out.println("3) Multiplicar");
        System.out.println("4) Dividir");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Obtener los dos números del usuario
        System.out.print("Introduce el primer número: ");
        double num1 = scanner.nextDouble();

        System.out.print("Introduce el segundo número: ");
        double num2 = scanner.nextDouble();

        // Llamada a la función para escribir el menú
        escribirMenu();

        // Obtener la opción del usuario
        System.out.print("Introduce el número de la opción (1-4): ");
        int opcion = scanner.nextInt();

        // Realizar la operación correspondiente
        if (opcion == 1) {
            suma(num1, num2);
        } else if (opcion == 2) {
            resta(num1, num2);
        } else if (opcion == 3) {
            multiplicacion(num1, num2);
        } else if (opcion == 4) {
            division(num1, num2);
        } else {
            System.out.println("Opción no válida. Por favor, introduce un número del 1 al 4.");
        }

        // Cerrar el scanner
        scanner.close();
    }
}

