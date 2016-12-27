package Model;

public class Score {
	private int compteur;
	public void ajoute(int i){
		// TODO ajouter un nombre au compteur.
		this.compteur += i;
	}

	public void retire(int i){
		// TODO retrancher un nombre au compteur.
		this.compteur -= i;
	}

	public void mettreAZero(){
		// TODO mettre à zéro le compteur du score.
		this.compteur = 0;
	}

	public int getCompteur() {
		return compteur;
	}

	public void setCompteur(int compteur) {
		this.compteur = compteur;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
}
