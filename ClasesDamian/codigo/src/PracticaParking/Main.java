package PracticaParking;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Coche[] parking = new Coche[20]; // Tamaño máximo de coches en el parking

        int opcion;
        do {
            System.out.println("1. Registrar entrada y salida de coche");
            System.out.println("2. Calcular ganancias");
            System.out.println("3. Salir");
            opcion = scanner.nextInt();
            scanner.nextLine(); // Consumir el salto de línea

            switch (opcion) {
                case 1:
                    System.out.print("Introduce la matrícula: ");
                    String matricula = scanner.nextLine();
                    System.out.print("Introduce la hora de entrada: ");
                    int horaEntrada = scanner.nextInt();
                    System.out.print("Introduce la hora de salida: ");
                    int horaSalida = scanner.nextInt();
                    registrarCoche(parking, matricula, horaEntrada, horaSalida);
                    break;
                case 2:
                    calcularGanancias(parking);
                    break;
                case 3:
                    // No hacer nada, simplemente salir del bucle
                    break;
                default:
                    System.out.println("Opción no válida. Inténtalo de nuevo.");
            }
        } while (opcion != 3);
    }

    private static void registrarCoche(Coche[] parking, String matricula, int horaEntrada, int horaSalida) {
        for (int i = 0; i < parking.length; i++) {
            if (parking[i] == null) {
                parking[i] = new Coche(matricula, horaEntrada, horaSalida);
                System.out.println("Coche registrado correctamente.");

                // Escribir datos en el archivo aparcamiento.txt
                escribirDatos(matricula, horaEntrada, horaSalida);
                return;
            }
        }
        System.out.println("No hay espacio disponible en el parking.");
    }

    private static void calcularGanancias(Coche[] parking) {
        double gananciasTotales = 0;
        for (Coche coche : parking) {
            if (coche != null) {
                int horas = coche.getHoraSalida() - coche.getHoraEntrada();
                double precio = horas * 10; // 10 euros por hora
                gananciasTotales += precio;
            }
        }
        System.out.println("Ganancias totales del parking: " + gananciasTotales + " euros");
    }

    private static void escribirDatos(String matricula, int horaEntrada, int horaSalida) {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter("aparcamiento.txt", true));
            writer.write(matricula + " " + horaEntrada + " " + horaSalida);
            writer.newLine();
            writer.close();
        } catch (IOException e) {
            System.out.println("Error al escribir los datos en el archivo.");
            e.printStackTrace();
        }
    }
}
