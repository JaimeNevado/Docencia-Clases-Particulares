package ultimoHerencia;

public class Libro extends MaterialBiblioteca {
    private String autor;
    private int numeroPaginas;

    public Libro(String titulo, int anioPublicacion, String autor, int numeroPaginas) {
        super(titulo, anioPublicacion);
        this.autor = autor;
        this.numeroPaginas = numeroPaginas;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getNumeroPaginas() {
        return numeroPaginas;
    }

    public void setNumeroPaginas(int numeroPaginas) {
        this.numeroPaginas = numeroPaginas;
    }

    @Override
    public String toString() {
        return super.toString() + " - Autor: " + this.autor + " - Número de páginas: " + this.numeroPaginas;
    }
}