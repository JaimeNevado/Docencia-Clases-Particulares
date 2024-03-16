package clase4;

public class Coche extends Vehiculo {
	private int puertas;
	public Coche (int puertas) {
		super(20, "Touran", 130);
		this.puertas = puertas;
	}
	
	public int getPuertas() {
		return this.puertas;
	}
	
	public String toString() {
		return this.puertas + this.km;
	}
	public static void main(String[] args) {
		Coche c1 = new Coche(3);
		c1.e
		
		System.out.println("El coche tiene " + c1.getPuertas());
	}

}
