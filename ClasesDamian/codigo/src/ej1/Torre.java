package ej1;

public class Torre {
    private String nombre;
    private int altura;
    private String ubicacion;

    public Torre(String nombre, int altura, String ubicacion) {
        this.nombre = nombre;
        this.altura = altura;
        this.ubicacion = ubicacion;
    }

    public boolean mismaAltura(Torre otraTorre) {
        return this.altura == otraTorre.altura;
    }

    public boolean alturaMayorQue(Torre otraTorre) {
        return this.altura > otraTorre.altura;
    }

    public boolean alturaMenorQue(Torre otraTorre) {
        return this.altura < otraTorre.altura;
    }

    public boolean mismaUbicacion(Torre otraTorre) {
        return this.ubicacion.equals(otraTorre.ubicacion);
    }

    public int getAltura() {
        return altura;
    }
    
    public String toString () {
    	return "Torre de "+ this.nombre + " mide " + this.altura + " ubicada en " + this.ubicacion;
    }

    public static void main(String[] args) {
        Torre t1 = new Torre("Pisa", 20, "Italia");
        Torre t2 = new Torre("Torre Eiffel", 300, "Francia");
        
        System.out.println("Información de las torres: ");
        System.out.println(t1);
        System.out.println(t2);
        System.out.println("----------------------------");

        System.out.println("¿Las torres tienen la misma altura? " + t1.mismaAltura(t2));
        System.out.println("¿La altura de la Torre 1 es mayor que la de la Torre 2? " + t1.alturaMayorQue(t2));
        System.out.println("¿La altura de la Torre 1 es menor que la de la Torre 2? " + t1.alturaMenorQue(t2));
        System.out.println("¿La Torre 1 está ubicada en el mismo lugar que la Torre 2? " + t1.mismaUbicacion(t2));
    
    
    }
}
