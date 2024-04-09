package ejerciciosClase6;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ej1 {

    public static int contarLineas(String ruta) {
        int contador = 0;
        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(ruta));
            String linea;
            while ((linea = reader.readLine()) != null) {
                contador++;
            }
        } catch (IOException e) {
            System.out.println("Error al leer el archivo: " + e.getMessage());
        } finally {
            try {
                if (reader != null) {
                    reader.close();
                }
            } catch (IOException e) {
                System.out.println("Error al cerrar el BufferedReader: " + e.getMessage());
            }
        }

        return contador;
    }

    public static void main(String[] args) {
        String ruta = "archivo.txt"; // Ruta del archivo a leer
        int cantidadLineas = contarLineas(ruta);
        System.out.println("La cantidad de líneas en el archivo es: " + cantidadLineas);
    }
}