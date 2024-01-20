package clase10;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class hola {

    public static void main(String[] args) {
        String ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase10/texto.txt";

        File archivo = new File(ruta);

        if (!archivo.exists()) {
            System.out.println("El archivo no existe");
            return;
        } 
        
        System.out.println("Archivo encontrado");
        

        
		try {
			
			
			FileReader reader = new FileReader(archivo);
			BufferedReader buffer = new BufferedReader(reader);
			String linea = "";
			
			while ((linea = buffer.readLine()) != null) {
				System.out.println(linea);
			}
	
			
			
		} catch (FileNotFoundException e) {
			System.out.println("Archivo no encontrado");
		} catch (IOException e) {
			System.out.println("IOException");
		}
        
        
        
        

       
    }
}
