package clase4;

public class Vehiculo {

	protected int km;
	protected String modelo;
	protected double velocidad;
	
	public Vehiculo(int km, String modelo, double velocidad) {
		this.km = km;
		this.modelo = modelo;
		this.velocidad = velocidad;
	}
	
	@Override
	public boolean equals(Object obj) {
		if (obj == this)
			return true;
		Vehiculo apoyo = (Vehiculo) obj;
		
		
		if (apoyo.modelo == this.modelo) {
			return true;
		}
		return false;
		
	}

}

