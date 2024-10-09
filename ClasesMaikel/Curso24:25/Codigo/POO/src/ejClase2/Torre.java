package ejClase2;

public class Torre {
    // Atributos
    private String nombre;
    private int altura;
    private String pais;

    // Constructor
    public Torre(String nombre, int altura, String pais) {
        this.nombre = nombre;
        this.altura = altura;
        this.pais = pais;
    }

    // Método para comparar si las alturas son iguales
    public boolean mismaAltura(Torre otraTorre) {
        return this.altura == otraTorre.altura;
    }

    // Método para comparar si la altura es mayor que otra torre
    public boolean alturaMayorQue(Torre otraTorre) {
        return this.altura > otraTorre.altura;
    }

    // Método para comparar si la altura es menor que otra torre
    public boolean alturaMenorQue(Torre otraTorre) {
        return this.altura < otraTorre.altura;
    }

    // Método para comparar si el país es el mismo
    public boolean mismoPais(Torre otraTorre) {
        return this.pais.equals(otraTorre.pais);
    }

    // Método toString para representar la torre como una cadena
    @Override
    public String toString() {
        return "Nombre=" + nombre +
               "\nAltura=" + altura +
               "\nPais='" + pais + '\n';
    }
    
    public static void main(String[] args) {
        // Crear instancias de Torre
        Torre torre1 = new Torre("Torre Eiffel", 324, "Francia");
        Torre torre2 = new Torre("Torre de Pisa", 56, "Italia");
        Torre torre3 = new Torre("Torre CN", 553, "Canadá");

        // Imprimir las torres
        System.out.println(torre1);
        System.out.println(torre2);
        System.out.println(torre3);

        // Comparaciones de altura
        System.out.println("¿La Torre Eiffel tiene la misma altura que la Torre de Pisa? " + torre1.mismaAltura(torre2));
        System.out.println("¿La Torre Eiffel es más alta que la Torre CN? " + torre1.alturaMayorQue(torre3));
        System.out.println("¿La Torre CN es más baja que la Torre Eiffel? " + torre3.alturaMenorQue(torre1));

        // Comparación de país
        System.out.println("¿La Torre Eiffel está en el mismo país que la Torre de Pisa? " + torre1.mismoPais(torre2));
        System.out.println("¿La Torre Eiffel está en el mismo país que la Torre CN? " + torre1.mismoPais(torre3));
    }

   
}
