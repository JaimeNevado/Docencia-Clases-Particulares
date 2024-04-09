package ejerciciosClase6;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class ej4 {

    public static void main(String[] args) {
        int[][] matriz1 = leerMatriz("matriz1.txt");
        int[][] matriz2 = leerMatriz("matriz2.txt");

        if (matriz1.length != matriz2.length || matriz1[0].length != matriz2[0].length) {
            System.out.println("Las matrices no tienen las mismas dimensiones");
            return;
        }

        int[][] resultado = sumarMatrices(matriz1, matriz2);

        System.out.println("Matriz resultado de la suma:");
        imprimirMatriz(resultado);
    }

    private static int[][] leerMatriz(String nombreArchivo) {
        int[][] matriz = null;
        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(nombreArchivo));
            String linea = reader.readLine();
            int filas = 0;
            int columnas = linea.split(",").length;
            matriz = new int[filas][columnas];

            while (linea != null) {
                String[] elementos = linea.split(",");
                for (int j = 0; j < columnas; j++) {
                    matriz[filas][j] = Integer.parseInt(elementos[j]);
                }
                filas++;
                linea = reader.readLine();
            }
        } catch (FileNotFoundException e) {
            System.out.println("Archivo no encontrado");
        } catch (IOException e) {
            System.out.println("Error al leer el archivo");
        } catch (NumberFormatException e) {
            System.out.println("Error al convertir a entero");
        } finally {
            try {
                if (reader != null) {
                    reader.close();
                }
            } catch (IOException e) {
                System.out.println("Error al cerrar el archivo");
            }
        }
        return matriz;
    }

    private static int[][] sumarMatrices(int[][] matriz1, int[][] matriz2) {
        int filas = matriz1.length;
        int columnas = matriz1[0].length;
        int[][] resultado = new int[filas][columnas];

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                resultado[i][j] = matriz1[i][j] + matriz2[i][j];
            }
        }
        return resultado;
    }

    private static void imprimirMatriz(int[][] matriz) {
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[0].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}