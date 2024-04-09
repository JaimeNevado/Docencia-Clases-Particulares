package ejerciciosClase6;


import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

class ej2 {
    public static String palabraMasLarga(String ruta) {
        String palabraMasLarga = "";
        String linea;
        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(ruta));
            while ((linea = reader.readLine()) != null) {
                if (linea.length() > palabraMasLarga.length()) {
                    palabraMasLarga = linea;
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("Archivo no encontrado: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Error de lectura: " + e.getMessage());
        } finally {
            try {
                if (reader != null) {
                    reader.close();
                }
            } catch (IOException e) {
                System.out.println("Error al cerrar el archivo: " + e.getMessage());
            }
        }

        return palabraMasLarga;
    }

    public static void main(String[] args) {
        String ruta = "ruta/del/archivo.txt";
        String palabra = palabraMasLarga(ruta);
        System.out.println("La palabra más larga en el archivo es: " + palabra);
    }
}