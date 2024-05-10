package clase3Mayo2024;

public class CocheElectrico extends Coche {
	private int bateria;

	public CocheElectrico(String modelo, int km, int b) {
		super(modelo, km);
		this.bateria = b;
	}
	
	@Override
	public String toString() {
		return (super.toString() + "\nBatería: " + this.bateria);
	}
}

