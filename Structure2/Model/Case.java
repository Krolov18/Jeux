// import List
import java.util.*

public interface Case extends Object implements Model {
	List<Object> pions;
	int i, j;
	Plateau plateau;
	
	public void ajouter(Object o){
		pions.add(o);
	}
	public void retirer(Object o){
		pions.remove(o);
	}
}