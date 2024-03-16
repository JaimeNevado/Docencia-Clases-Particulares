package RepasoPracticaHerencia;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Crear robots
        RobotLimpieza robotLimpieza = new RobotLimpieza("Limpieza1", 20, new int[]{0, 0});
        RobotMayordomo robotMayordomo = new RobotMayordomo("Mayordomo1", 15, new int[]{0, 0});

        // Array bidimensional de char para representar los robots en el plano
        char[][] plano = new char[10][10];

        // Menú
        while (robotLimpieza.getBateria() > 0 || robotMayordomo.getBateria() > 0) {
            System.out.println("Seleccione el tipo de robot: ");
            System.out.println("1. Robot Limpieza");
            System.out.println("2. Robot Mayordomo");
            int tipoRobot = scanner.nextInt();
            scanner.nextLine(); // Limpiar buffer

            Robot robotSeleccionado = null;
            if (tipoRobot == 1) {
                robotSeleccionado = robotLimpieza;
            } else if (tipoRobot == 2) {
                robotSeleccionado = robotMayordomo;
            } else {
                System.out.println("Opción inválida.");
                continue;
            }

            System.out.println("Seleccione una acción: ");
            System.out.println("1. Avanzar");
            System.out.println("2. Retroceder");
            System.out.println("3. Acción");
            System.out.println("4. Mostrar");
            System.out.println("5. Mostrar en plano");
            int accion = scanner.nextInt();
            scanner.nextLine(); // Limpiar buffer

            switch (accion) {
                case 1:
                    robotSeleccionado.Avanzar();
                    break;
                case 2:
                    robotSeleccionado.Retroceder();
                    break;
                case 3:
                    robotSeleccionado.EjecutarAccion();
                    break;
                case 4:
                    robotSeleccionado.Mostrar();
                    break;
                case 5:
                    // Actualizar plano
                    for (int i = 0; i < plano.length; i++) {
                        for (int j = 0; j < plano[i].length; j++) {
                            plano[i][j] = '-';
                        }
                    }
                    plano[robotLimpieza.posicion[0]][robotLimpieza.posicion[1]] = robotLimpieza.getLetra();
                    plano[robotMayordomo.posicion[0]][robotMayordomo.posicion[1]] = robotMayordomo.getLetra();

                    // Mostrar plano
                    for (int i = 0; i < plano.length; i++) {
                        for (int j = 0; j < plano[i].length; j++) {
                            System.out.print(plano[i][j] + " ");
                        }
                        System.out.println();
                    }
                    break;
                default:
                    System.out.println("Opción inválida.");
                    break;
            }
        }
    }
}
