package ultimoHerencia;

public class MaterialBiblioteca {
    private String titulo;
    private int anioPublicacion;
    private boolean prestado;

    public MaterialBiblioteca(String titulo, int anioPublicacion) {
        this.titulo = titulo;
        this.anioPublicacion = anioPublicacion;
        this.prestado = false;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public int getAnioPublicacion() {
        return anioPublicacion;
    }

    public void setAnioPublicacion(int anioPublicacion) {
        this.anioPublicacion = anioPublicacion;
    }

    public void prestar() {
        this.prestado = true;
    }

    public void devolver() {
        this.prestado = false;
    }

    public boolean estaPrestado() {
        return this.prestado;
    }
    
    @Override
    public String toString() {
    	return "Titulo: " + this.titulo + " - Año de publicación: " + this.anioPublicacion;
    }
}
