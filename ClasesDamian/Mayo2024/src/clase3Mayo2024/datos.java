package clase3Mayo2024;


public class datos {

	public static void main(String[] args) {
		Coche c2 = new Coche("seat", 32178);
		Coche c3 = new Coche("Seat", 32178);
		CocheElectrico lavadora = new CocheElectrico("Tesla", 89, 7);
		
		System.out.println(c2.equals(c3));
		
	}

}
