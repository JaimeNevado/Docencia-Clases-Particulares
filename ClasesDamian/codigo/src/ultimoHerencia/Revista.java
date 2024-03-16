package ultimoHerencia;

public class Revista extends MaterialBiblioteca {
    private String editor;
    private int numeroEdicion;

    public Revista(String titulo, int anioPublicacion, String editor, int numeroEdicion) {
        super(titulo, anioPublicacion);
        this.editor = editor;
        this.numeroEdicion = numeroEdicion;
    }

    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }

    public int getNumeroEdicion() {
        return numeroEdicion;
    }

    public void setNumeroEdicion(int numeroEdicion) {
        this.numeroEdicion = numeroEdicion;
    }

    @Override
    public String toString() {
    	// "Titulo: " + this.titulo + " - Año de publicación: " + this.anioPublicacion
        return super.toString() + " - Editor: " + this.editor + " - Número de edición: " + this.numeroEdicion;
    }
}