package clase11;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class leerArchivo {

	public static void main(String[] args) {
        String ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase11/archivo_salida.csv";

        BufferedWriter writer = null;

        try {
            writer = new BufferedWriter(new FileWriter(ruta));

            // Supongamos que tienes un array de datos que quieres escribir en el archivo
            int[][] datos = {{1, 2}, {2, 2},  {3, 4}};

            // Convertir y escribir cada elemento en el archivo CSV
            for (int i = 0; i < datos.length; i++) {
            	for (int j = 0; j < datos[i].length; j++) {
            		writer.write(Integer.toString(datos[i][j]) + " ");
         
            	}

                writer.write("\n");
            }

            // Agregar una nueva línea al final del archivo
            writer.newLine();
            
            System.out.println("Archivo escrito");

        } catch (IOException e) {
            System.out.println("Error de escritura en el archivo CSV: " + e.getMessage());
        } finally {
            try {
                if (writer != null) {
                    writer.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
	}
}
