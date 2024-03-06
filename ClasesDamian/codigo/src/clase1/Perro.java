package clase1;

public class Perro extends Animal {
	
	
	public Perro(String n, int e, int p) {
		super(n, e, p);
	}

	public void ladrar() {
		System.out.println("Guau guau!");
	}

	public static void main(String[] args) {
		Perro miPerro = new Perro("Manuel", 13, 16);
		
		miPerro.ladrar();
		miPerro.hacerRuido();
		
		
		
	}

}
