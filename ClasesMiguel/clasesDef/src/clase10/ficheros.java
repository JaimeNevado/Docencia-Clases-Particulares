package clase10;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class ficheros {
	
    public static void main(String[] args) {
        // Obtén la ruta del archivo en el mismo paquete
        String fileName = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase10/texto.txt";

        // Crea un objeto File utilizando la ruta del archivo
        File file = new File(fileName);

        if (!file.exists()) {
            System.err.println("El archivo no pudo ser encontrado: " + fileName);
            return;
        }
        

        try {
        	FileReader reader = new FileReader(file);
        	
        	BufferedReader buffer = new BufferedReader(reader);
            String line;
            while ((line = buffer.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
}


