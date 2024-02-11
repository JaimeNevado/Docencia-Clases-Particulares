package clase8;

public class Persona {
	
	private int edad;
	private String nombre;
	
	public Persona(int edad, String s) {
		this.edad = edad;
		this.nombre = s;
	}

	public void saludar() {
		System.out.println("Mi nombre es " + nombre + " " + edad);
	}
	
	public String getNombre() {
		return nombre;
	}
	
	public void setNombre(String n) {
		this.nombre = n;
	}
	
	@Override
	public String toString() {
		return "soy jaime";
		
	}
	public static void main(String[] args) {
		Persona alumno = new Persona(13, "Jaime");
		
		alumno.setNombre("Roberto");
		String edad = alumno.getNombre();
		System.out.println(alumno);
		
		
	}

}
