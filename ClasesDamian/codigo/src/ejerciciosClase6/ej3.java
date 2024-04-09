package ejerciciosClase6;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ej3 {

    public static void main(String[] args) {
        String fileName = "archivo.txt";
        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(fileName));
            String line;
            while ((line = reader.readLine()) != null) {
                String[] parts = line.split(",");
                String nombre = parts[0];
                String apellido = parts[1];
                int nota = Integer.parseInt(parts[2]);

                if (nota >= 5) {
                    System.out.println(nombre + " " + apellido + " ha aprobado con nota " + nota);
                } else {
                    System.out.println(nombre + " " + apellido + " ha suspendido con nota " + nota);
                }
            }
        } catch (IOException e) {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Error: formato de archivo incorrecto.");
        } catch (NumberFormatException e) {
            System.out.println("Error al convertir la nota a entero: " + e.getMessage());
        } finally {
            try {
                if (reader != null) {
                    reader.close();
                }
            } catch (IOException e) {
                System.out.println("Error al cerrar el archivo: " + e.getMessage());
            }
        }
    }
}