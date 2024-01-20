package clase10;

import java.util.Scanner;

public class JuegoPro {
	
	public static void mostrarResultadosFinales(int totalPartidas, int puntajeJugador1, int puntajeJugador2, int empates) {
        // Muestra los resultados finales del juego
        System.out.println("\nResultados finales:");
        System.out.println("Total de partidas: " + totalPartidas);
        System.out.println("Puntuación Jugador 1: " + puntajeJugador1);
        System.out.println("Puntuación Jugador 2: " + puntajeJugador2);
        System.out.println("Empates: " + empates);

        // Puedes agregar más detalles según tu preferencia
    }

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

        boolean salida = false;
        
        int totalPartidas = 0;
        int puntajeJugador1 = 0;
        int puntajeJugador2 = 0;
        int empates = 0;
        
        
        while (!salida) {
            char jugador1 = ' ';
            char jugador2 = ' ';
	        // Jugador 1 ingresa su jugada
	        while (jugador1 != 'T' && jugador1 != 'R' && jugador1 != 'P' && jugador1 != 'S') {
	            System.out.print("Jugador 1, elige T, R o P: (S para salir) ");
	            jugador1 = scanner.next().toUpperCase().charAt(0);
	            if (jugador1 == 'S') {
	            	System.out.println("Saliendo del Programa");
	            	salida = true;
	            	break;
	            }
	            
	        }
	
	        // Jugador 2 ingresa su jugada   
	        while (jugador2 != 'T' && jugador2 != 'R' && jugador2 != 'P' && jugador2 != 'S' && !salida) {
	            System.out.print("Jugador 2, elige T, R o P: (S para salir) ");
	            jugador2 = scanner.next().toUpperCase().charAt(0);
	            if (jugador2 == 'S') {
	            	System.out.println("Saliendo del Programa");
	            	salida = true;
	            	break;
	            }
	        }
	        
	        if (!salida) {
	    		// Determinar resultado
	    		int resultado;
	    		switch (jugador1) {
	    		case 'T':
	    			switch (jugador2) {
	    			case 'T':
	    				resultado = 0; // Empate
	    				break;
	    			case 'R':
	    				resultado = -1; // Gana el jugador 2
	    				break;
	    			case 'P':
	    				resultado = 2; // Gana el jugador 1
	    				break;
	    			default:
	    				resultado = 0; // Default, en caso de jugadas no válidas
	    				break;
	    			}
	    			break;
	    		case 'R':
	    			switch (jugador2) {
	    			case 'T':
	    				resultado = 1; // Gana el jugador 1
	    				break;
	    			case 'R':
	    				resultado = 0; // Empate
	    				break;
	    			case 'P':
	    				resultado = -3; // Gana el jugador 2
	    				break;
	    			default:
	    				resultado = 0; // Default, en caso de jugadas no válidas
	    				break;
	    			}
	    			break;
	    		case 'P':
	    			switch (jugador2) {
	    			case 'T':
	    				resultado = -2; // Gana el jugador 2
	    				break;
	    			case 'R':
	    				resultado = 3; // Gana el jugador 1
	    				break;
	    			case 'P':
	    				resultado = 0; // Empate
	    				break;
	    			default:
	    				resultado = 0; // Default, en caso de jugadas no válidas
	    				break;
	    			}
	    			break;
	    		default:
	    			resultado = 0; // Default, en caso de jugadas no válidas
	    			break;
	    		}

	    		// Mostrar resultado
	    		switch (resultado) {
	    		case 0:
	    			System.out.println(jugador1 + "-" + jugador2 + " Empate");
	    			empates++;
	    			break;
	    		case 1:
	    			System.out.println(jugador1 + "-" + jugador2 + " Roca rompe Tijeras. Gana el jugador 1");
	    			puntajeJugador1++;
	    			break;
	    		case -1:
	    			System.out.println(jugador1 + "-" + jugador2 + " Roca rompe Tijeras. Gana el jugador 2");
	    			puntajeJugador2++;
	    			break;
	    		case 2:
	    			System.out.println(jugador1 + "-" + jugador2 + " Tijeras cortan Papel. Gana el jugador 1");
	    			puntajeJugador1++;
	    			break;
	    		case -2:
	    			System.out.println(jugador1 + "-" + jugador2 + " Tijeras cortan Papel. Gana el jugador 2");
	    			puntajeJugador2++;
	    			break;
	    		case 3:
	    			System.out.println(jugador1 + "-" + jugador2 + " Papel cubre Roca. Gana el jugador 1");
	    			puntajeJugador1++;
	    			break;
	    		case -3:
	    			System.out.println(jugador1 + "-" + jugador2 + " Papel cubre Roca. Gana el jugador 2");
	    			puntajeJugador2++;
	    			break;
	    		default:
	    			System.out.println("Jugada no válida");
	    			break;
	    		}
	            totalPartidas++;
	            mostrarResultadosFinales(totalPartidas, puntajeJugador1, puntajeJugador2, empates);
	        }
        }
	}
}
