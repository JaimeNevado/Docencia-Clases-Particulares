package clase11;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class claseCSV {

	public static void main(String[] args) {
		String ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesMiguel/clasesDef/src/clase11/maikel.csv";
		
		BufferedWriter escritor = null;
		
		
		int edades[] = {19, 14};
		int edades2[] = {19, 14};
		
		
		try {
			escritor = new BufferedWriter(new FileWriter(ruta));
			
			escritor.write("Hola Mundo");
			
			System.out.println("Se ha escrito");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				escritor.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

	}

}
