import java.util.ArrayList;
import java.util.List;

public class HolaMundo {

    public static void escribirLista(List<String> luis){
        for(int i = 0; i < luis.size(); i++){
            System.out.print(luis.get(i) + " | ");
        }
    }


    public static void main(String[] args) {
        int edad = 20;
        //String nombre = "Jaime";
        double altura = 1.6;

        List<String> miLista = new ArrayList<>();

        miLista.add("Jaime");

        for (int i = 0; i < 13; i++){
            miLista.add("Luis");
        }

        escribirLista(miLista);









    }
}
