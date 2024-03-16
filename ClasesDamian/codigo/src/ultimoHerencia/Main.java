package ultimoHerencia;

public class Main {
    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca(100);

        Libro libro1 = new Libro("Harry Potter y la piedra filosofal", 1997, "J.K. Rowling", 336);
        Revista revista1 = new Revista("National Geographic", 2022, "National Geographic Society", 100);

        biblioteca.agregarMaterial(libro1, 0);
        biblioteca.agregarMaterial(revista1, 1);

        // Ejemplo de búsqueda de un material en la biblioteca
        MaterialBiblioteca encontrado = biblioteca.buscarMaterial("National Geographic");
        if (encontrado != null) {
            System.out.println("Material encontrado: " + encontrado.getTitulo());
        } else {
            System.out.println("Material no encontrado.");
        }
        
        biblioteca.getMateriales()[0].
    }
}
