package clase1;

public class Gato extends Animal {


	public Gato(String n, int e, int p) {
		super(n, e, p);
		
	}
	
	public void maullar() {
		System.out.println("miaw");
	}
	
	
	

	public static void main(String[] args) {
		Gato michi = new Gato("Doraemon", 15, 100);
		
		michi.hacerRuido();
		michi.maullar();
	}

}
