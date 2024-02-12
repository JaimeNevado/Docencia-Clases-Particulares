

	/*
	 * Miguel Ángel Ruiz Miranda
	 * dni 26792593P
	 * 11/02/2024 
	 * Examen (Parte Práctica) Fundamentos de Programación */ 

import java.util.Scanner;

public class Ejercicio1 {

	public static void main(String[] args) {
		/*
		 * Personalmete me gusta dejar la entrada de el codigo para la creacion de todas
		 * las variables que necesitemos
		 */
		String nombre = ""; // nombre del alumno
		int numeroID = 0; // numero de identidad del alumno
		float nota1 = 0; // primera nota del alumno
		float nota2 = 0; // segunda nota del alumno
		float nota3 = 0; // tercera nota del alumno
		int opcion = 1; // variables para los bucles
		int opcion2 = 0;

		// A continuacion creamos un scanner para poder escribir por pantalla los datos
		// del alumno
		Scanner sc = new Scanner(System.in);

		/*
		 * creamos un while donde preguntamos al usuario ponga en bucle si quiere seguir
		 * introduciendo alumnos en caso de elegir la primera opcion o quiere salir en
		 * caso de elegir la segunda opcion para ello igualamos la variable opcion al
		 * scanner por el que introduce la opcion el usuario
		 */
		while (opcion == 1) {
			System.out.println("¿Desea introducir alumno?");
			System.out.println("Pulse 1 para afirmar ");
			System.out.println("Pulse 2 para negar ");
			opcion = sc.nextInt();

			/*
			 * Creamos un if para el caso de que el usuario haya decidido seguir
			 * introduciendo alumnos y en este le preguntamos sys datos, los igualamos a sus
			 * respectivas variables y se lo imprimimos por pantalla ademas, le damos la
			 * opion de calcular la nota media
			 */
			if (opcion == 1) {
				System.out.println("introduce el nombre :");
				nombre = sc.next();
				System.out.println("intoduce el numero de identidad : ");
				numeroID = sc.nextInt();
				System.out.println("introduce la 1º nota : ");
				nota1 = sc.nextInt();
				System.out.println("introduce la 2º nota : ");
				nota2 = sc.nextInt();
				System.out.println("introduce la 3º nota : ");
				nota3 = sc.nextInt();

				System.out.println("el nombre introduido es : " + nombre);
				System.out.println("el numero de identidad introduido es : " + numeroID);
				System.out.println("la primera nota es : " + nota1);
				System.out.println("la segunda nota es : " + nota2);
				System.out.println("la tercera nota es : " + nota3);

				System.out.println("¿desea calcular la nota media?");
				System.out.println("Pulse 1 para afirmar ");
				System.out.println("Pulse 2 para negar ");
				opcion2 = sc.nextInt();
				/*
				 * En caso de solicitar la nota media se abre el if, se calcula esa nota media,
				 * se le imprime por pantalla y se sigue realizando el bucle volviendole a
				 * preguntar al usuario si quiere introduir a otro alumno
				 */
				if (opcion2 == 1) {
					float notaMedia = (nota1 + nota2 + nota3) / 3;
					System.out.println("La nota media de " + nombre + " es : " + notaMedia);
				}
				/*
				 * En caso de no solicitar la nota media se sigue leyendo el codigo igualmente y
				 * le volvemos a preguntar si quiere introducir a otro alumno
				 */

			} else if (opcion == 2) {
				// finalizamos el while junto con el programa en caso de que el usuario lo haya
				// solicitado
				break;
			} else {
				// curamos el codigo de errores en este caso de que el usuario introduzca un
				// numero aleatorio diferente al que se le ha pedido
				System.out.println(" La opcion introducida no es valida ");
			}

		}

	}

}
