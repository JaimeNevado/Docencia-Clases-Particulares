package clase3Mayo2024;

public class Coche {
	private int numPuertas = 4;
	private String modelo;
	private int km;
	
	public Coche(String modelo, int km) {
		this.modelo = modelo;
		this.km = km;
	}

	public int getNumPuertas() {
		return numPuertas;
	}

	public void setNumPuertas(int numPuertas) {
		this.numPuertas = numPuertas;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
	}

	public int getKm() {
		return km;
	}

	public void setKm(int km) {
		this.km = km;
	}
	
	@Override
	public String toString() {
		return ("Modelo: " + this.modelo + "\nKilómetros: " + this.km + "km");
	}
	
	public void acelerar(int km) {
		System.out.println("Estoy acelerando a " + km + " por hora");
	}
	
	@Override
	public boolean equals(Object obj) {
		Coche coche2 = (Coche) obj;
		return this.km == coche2.km && this.modelo.equalsIgnoreCase(coche2.modelo);
	}
}
