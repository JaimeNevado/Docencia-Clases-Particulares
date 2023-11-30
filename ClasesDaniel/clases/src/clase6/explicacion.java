package clase6;

import java.util.Random;
import java.util.Scanner;

public class explicacion {

	public static int[] crearMesas(int a) {
		Random rand = new Random();
		int[] resultado = new int[a];
		for (int i = 0; i < resultado.length; i++) {
			resultado[i] = rand.nextInt(5);
		}
		return resultado;
	}
	
	public static String estadoMesa(int[] mesas) {
		String resultado = "";
		String apoyo = "";
		for (int i = 0; i < mesas.length; i++) {
			apoyo = "Mesa " + (i + 1) + " -> " + mesas[i] + " personas";
			resultado = resultado + apoyo + "\n";
		}
		
		return resultado;
	}
	
	public static void main(String[] args) {
		final int NUM_MESAS = 10;
		
		int[] mesas = crearMesas(NUM_MESAS);
		
		String resultado = estadoMesa(mesas);
		System.out.println(resultado);
		
	}
	
}
