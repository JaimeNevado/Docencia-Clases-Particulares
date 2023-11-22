package clase6;

import java.util.Scanner;

public class ejercicioRPT {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

        char jugador1 = ' ';
        char jugador2 = ' ';

        // Jugador 1 ingresa su jugada
        while (jugador1 != 'T' && jugador1 != 'R' && jugador1 != 'P') {
            System.out.print("Jugador 1, elige T, R o P: ");
            jugador1 = scanner.next().toUpperCase().charAt(0);
        }

        // Jugador 2 ingresa su jugada
        while (jugador2 != 'T' && jugador2 != 'R' && jugador2 != 'P') {
            System.out.print("Jugador 2, elige T, R o P: ");
            jugador2 = scanner.next().toUpperCase().charAt(0);
        }

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
                break;
            case 1:
                System.out.println(jugador1 + "-" + jugador2 + " Roca rompe Tijeras. Gana el jugador 1");
                break;
            case -1:
                System.out.println(jugador1 + "-" + jugador2 + " Roca rompe Tijeras. Gana el jugador 2");
                break;
            case 2:
                System.out.println(jugador1 + "-" + jugador2 + " Tijeras cortan Papel. Gana el jugador 1");
                break;
            case -2:
                System.out.println(jugador1 + "-" + jugador2 + " Tijeras cortan Papel. Gana el jugador 2");
                break;
            case 3:
                System.out.println(jugador1 + "-" + jugador2 + " Papel cubre Roca. Gana el jugador 1");
                break;
            case -3:
                System.out.println(jugador1 + "-" + jugador2 + " Papel cubre Roca. Gana el jugador 2");
                break;
            default:
                System.out.println("Jugada no válida");
                break;
        }
	}

}
