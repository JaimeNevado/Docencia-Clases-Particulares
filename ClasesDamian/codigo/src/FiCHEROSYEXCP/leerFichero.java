package FiCHEROSYEXCP;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class leerFichero {

	public static void main(String[] args) {
		String ruta = "C:/miCarpeta/texto.txt";
		
		BufferedReader reader = null;
		String linea = "";
		int tamaño = 3;
		
		String [] nombres = new String[tamaño];
		
		try {
			reader = new BufferedReader(new FileReader(ruta));
			while ((linea = reader.readLine()) != null) {
				nombres = linea.split(",");
			}
		} catch (FileNotFoundException e) {
			System.out.println("Illo no existe ese archivo");
		} catch (IOException e) {
			System.out.println("IOException ha ocurrido");
		} catch (Exception e) {
			System.out.println("Excepcion general");
		}
		
		finally {
			try {
				reader.close();
			} catch (IOException e) {
				System.out.println("No se ha podido cerrar el archivo");
			}
		}
		
		System.out.println(nombres[0]);
		System.out.println(nombres[1]);
		System.out.println(nombres[2]);
		
		
	}

}
