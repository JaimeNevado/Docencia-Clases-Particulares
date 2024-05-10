package clase3Mayo2024;

import java.util.Scanner;

public class Cuadrado {
	private double ancho;
	private double alto;
	private int filo; // 1, 2, 3, 4
	
	public Cuadrado (double var1, double var2, int var3) {
		this.ancho = var1;
		this.alto = var2;
		this.filo = var3;
	}

	public double getAncho() {
		return ancho;
	}

	public double getAlto() {
		return alto;
	}

	public int getFilo() {
		return filo;
	}
	
	public void setAlto(double nuevoAlto) {
		this.alto = nuevoAlto;
	}

	public void setAncho(double ancho) {
		this.ancho = ancho;
	}

	public void setFilo(int filo) {
		this.filo = filo;
	}
	
	@Override
	public String toString() {
		return ("Hola soy un cuadrado de " + this.alto + "x" + this.ancho + "cm");
	}
	

}
