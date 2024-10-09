package clase11;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class claseCSV {

	public static void main(String[] args) {
		String ruta2 = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase11/maikel.csv";
		
		String ruta = "C://miCarpeta/miArchivo.csv";
		 
		BufferedReader reader = null;
	
		

		
		try {
			reader = new BufferedReader (new FileReader(ruta));
			String linea = "";
			while ((linea = reader.readLine()) != null) {
				String[] array = linea.split(",");
				// Lo que quieras hacer con el array
			}	
		} catch (IOException e) {
			e.printStackTrace();
		} finally { 
			try {
				reader.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		
		for (String s : textos) {
			System.out.println(s);
		}
		
	}

}
