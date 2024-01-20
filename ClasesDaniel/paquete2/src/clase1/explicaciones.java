package clase1;

import java.util.ArrayList;
import java.util.List;

public class explicaciones {
	
	public static void esPalindroma(List<Integer> l) {
		if (l.get(0) == l.get(l.size() - 1)) {
			System.out.println("Lo es");
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		List<Integer> lista = new ArrayList<>();
		
		lista.add(2);
		lista.add(3);
		lista.add(2);
		lista.add(3);
		
		esPalindroma(lista);
	}



}
