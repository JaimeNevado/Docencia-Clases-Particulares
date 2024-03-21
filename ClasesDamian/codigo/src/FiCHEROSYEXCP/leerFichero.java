package FiCHEROSYEXCP;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class leerFichero {

	public static void main(String[] args) {
		String ruta = "/Users/jaimenevado/Desktop/Docencia-Clases-Particulares/ClasesDamian/codigo/src/FiCHEROSYEXCP/texto.txt";
		
		BufferedReader reader = null;
		
		String linea = "";
		String texto = "";
		
		try {
			reader = new BufferedReader(new FileReader(ruta));
			while ((linea = reader.readLine()) != null) {
				texto = texto + linea + "\n";
			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		try {
			reader.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		System.out.println(texto);

	}

}
