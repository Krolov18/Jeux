__authors__ = 'LEVEQUE_LANCIEN_FROGET'

# coding: utf-8

from tkinter import *
from tkinter.messagebox import *
import random
import string
import yaml
import webbrowser
import codecs


class Mecanisme():
	"""
		La classe Mecanisme constitue les engrenages du jeu.
		Cette classe contient toutes les méthodes dont le jeu du pendu
		a besoin pour fonctionner correctement.
		Cette classe sera hérité par Interface, classe qui permet
		d'afficher dans une interface le jeu du pendu.
	"""
	def __init__(self, liste):
		"""
			Cette méthode constructrice prend en argument une liste de
			dictionnaire. Dans notre cas c'est un objet YAML.
			On vérifie avec la fonction isinstance(object, type(object))
			objet est dans le type que l'on souhaite. Puis on assigne
			l'argument - ici liste - à self.phrases soit un objet qui
			sera glogal. Il pourra être atteint par n'importe quelle 
			fonction dans la classe.
		"""
		if isinstance(liste, list):
			self.phrases = liste

	def choisir_solution(self):
		"""
			On passe en argument à choice() du module random 
			self.phrases qui permet de choisir au sein de la liste 
			un élément pour jouer.
		"""
		return random.choice(self.phrases)

	def recuperer_indices(self, lettre, mot):
		"""
			recuperer_indice permet de tester la proposition du joueur
			(lettre) dans mot (solution) s'il y a présence de l'un dans
			l'autre alors on récupère les indices que lettre match
			dans la solution.
		"""
		return [indice for indice, strin in enumerate(mot) if strin == lettre]

	def verifier_proposition(self, proposition):
		"""
			Cette méthode prend en argument la proposition du joueur,
			la renvoie uniquement si elle n'est pas plus grande que 1,
			et si elle est comprise dans les caractères alphabétique,
			y compris majuscules, minuscules, caractères accentués et
			ponctuation.
		"""
		if not proposition in string.ascii_letters+string.punctuation+"éêàèçùôöûîïüâ":
			showinfo("erreur","Votre proposition doit uniquement contenir des lettres de l'alphabet")
		elif not len(proposition) is 1:
			showinfo('erreur', "Votre proposition doit être d'une longueur de 1 caractère")
		else:
			return proposition

	def creer_phraseCache(self):
		"""
			On met en local phrase car on n'en aura pas besoin autre 
			part.
			Cette fonction permet de créer les trois objets clés du jeu,
			à savoir la phraseReponse, les catégories, ainsi que la
			phraseCache. Ces trois objets sont aussi mis avec "self."
			pour être accessible à n'importe quel niveau dans la classe.
		"""
		phrase = self.choisir_solution()
		self.phraseReponse = [mot["forme"] for mot in phrase['acte']]
		self.categories = [mot["categorie"] for mot in phrase["acte"]]
		self.phraseCache  = ['_'*len(mot["forme"]) for mot in phrase["acte"]]

	def update_proposition(self, proposition):
		"""
			Au fur et à mesure que je joueur rentre des bonnes réponses
			il faut mettre à jour l'affichage. Cette méthode recherche
			la proposition du joueur dans la réponse et remplace 
			les tirets ("_") dans self.phraseCache par les
			indices matchant dans la solution. 
			Puis on renvoie la nouvelle valeur de self.phraseCache.
		"""
		for position, mot in enumerate(self.phraseReponse):
			indices = self.recuperer_indices(proposition, mot)
			if len(indices) > 0 :
				self.phraseCache[position] = list(self.phraseCache[position])
				for ind in indices :
					self.phraseCache[position][ind] = proposition
		return self.phraseCache

	def afficher_elements(self, liste, master, relx=0.3):
		"""
			On a besoin de cette méthode dans l'interface graphique.
			C'est elle qui affiche aussi bien les mots cachés que les
			différentes catégories.
		"""
		for position, mot in enumerate(liste):
			word = Label(master, text = mot, font=("comic sans ms","10","bold"), fg="White", bg="black")
			word.place(relx=relx,rely=(position+1)/10,x=5)

	def afficher_mauvaisesReponses(self, liste, master):
		"""
			On affiche les mauvaises réponses (et les réponses
			déjà saisies) dans un champ spécifique.
		"""
		mauvaiseReponse = Label(master, text = ", ".join(liste), font=("comic sans ms","10","bold"), fg="black", bg="lightsteelblue4")
		mauvaiseReponse.place(relx=0.002, rely=0.75, x=10)

	def afficher_reussite(self, limite):
		"""
			Cette petite méthode permet de dire au joueur quand il a gagné et quand il a perdu.
		"""
		if len(self.mauvais) >= limite :
			showinfo('Défaite', "Vous avez perdu")
		elif not any('_' in mot for mot in self.phraseCache) :
			showinfo('Victoire', "Vous avez gagné")
	
	def changer_image(self, essai):
		"""
			Changement d'image avec essai en argument.
		"""
		self.image = PhotoImage(file=self.path.format(essai))
		self.label.configure(image = self.image)


class Interface(Mecanisme):
	"""
		Cette classe contient uniquement les objets dont l'interface a
		besoin. Les objets propres à l'interface.
		
		bouttons, champs de saisie, label, et image
	"""
	def __init__(self, parent, dico):
		"""
			Cette méthode constructrice déclare tous les Widgets dont
			on aura besoin avec (pour ceux qui en ont besoin) la 
			déclaration des fonctions qu'ils utiliseront.
			La première lignes en dessous des trois quillemets double
			permet de partager les fonctions de Mecanisme avec 
			interface. La classe Interface hérite alors des méthodes
			de Mecanisme.
		"""
		Mecanisme.__init__(self, dico)
		self.racine = parent
		self.image = PhotoImage(file = "image_pendu/pendu0.gif")
		self.path = "image_pendu/pendu{0}.gif"
		
		LabelBienvenue = Label (parent, text = "Bienvue dans notre pendu !", font=("comic sans ms","12","bold"), fg="White", bg="lightsteelblue4")
		LabelBienvenue.place(relx=0.45, rely=0.01, x=10)	
		
		LabelLettreEssayees = Label (parent, text = "Lettres déjà proposées : ", font=("comic sans ms","10","bold"), fg="white",bg="lightsteelblue4")
		LabelLettreEssayees.place(relx=0.01, rely=0.7, x=10)
		
		jouer_boutton = Button(parent, text = 'JOUER', width=5, height=1, fg="red4", font=("comic sans ms","10","bold"), command = self.jouer)
		jouer_boutton.place(relx=0.8, rely=0.01, x=10)
		
		verifier_boutton = Button(parent, text='VERIFIER',font=("comic sans ms","10","bold"),fg="lightsteelblue4", command = self.verifier)
		verifier_boutton.place(relx=0.78, rely=0.8, x=10)
		
		quitter_boutton = Button(parent, text='QUITTER', width=7, height=1, fg="red4", font=("comic sans ms","10","bold"), command=parent.destroy)
		quitter_boutton.place(relx=0.9, rely=0.8, x=10)
		
		LabelBienvenue = Label (parent, text = "Proposez une lettre :", font=("comic sans ms","10","bold"), fg="White", bg="lightsteelblue4")
		LabelBienvenue.place(relx=0.83, rely=0.6, x=10)
		
		self.Cproposition = Entry(parent)
		self.Cproposition.place(relx=0.83, rely=0.7, x=10)
		self.Cproposition.bind('<Return>', self.verifier)
		
		self.label = Label(parent, image = self.image, width=240, height=320)
		self.label.place(height=320,width=240)
		
		menubar = Menu(parent, tearoff=0)
		menubar.add_command(label="Quitter", command=parent.destroy)
		menubar.add_command(label="Règles", command=self.regles)
		parent.config(menu=menubar)
	


	def jouer(self):
		"""
			Fonction d'initialisation du jeu du pendu.
			essais est mis à 0
			mauvais est mis à 0
			on crée self.phraseCache et self.categories
			puis on les affiche.
		"""
		self.essais = []
		self.mauvais = []
		self.creer_phraseCache()
		self.afficher_elements(self.phraseCache, self.racine)
		self.afficher_elements(self.categories, self.racine, relx=0.6)

	def regles(self):
		"""
			fonction qui permettra au boutton regles, d'afficher
			les regles du jeu.
		"""
		webbrowser.open('regles.html')

	def verifier(self):
		"""
			Cette fonction vérifie la saisie du joueur, met à jour
			l'interface suivant la saisie tapée et affiche les éléments.
		"""
		saisie = self.verifier_proposition(self.Cproposition.get())
		self.Cproposition.delete(0, END)
		if not any(saisie in mot for mot in self.phraseReponse):
			showinfo('Try again!', 'Raté')
			self.essais.append(saisie)
			self.mauvais.append(saisie)
			self.afficher_mauvaisesReponses(self.essais,self.racine)
			self.changer_image(len(self.mauvais))
		else:
			for mot in self.phraseReponse:
				self.afficher_elements(self.update_proposition(saisie),self.racine)
			self.essais.append(saisie)
			self.afficher_mauvaisesReponses(self.essais,self.racine)
		self.afficher_reussite(10)

def main():
	"""
		On instancie Tk(),
		on donne un titre à la fenêtre, une couleur de fond, une taille
		minimale.
		On ouvre notre fichier YAML qu'on met dans la variable phrases.
		on instencie Interface en lui passant en arguments 
		Tk() instancié et phrases puis on ferme la boucle avec 
		mainloop().
	"""
	racine = Tk()
	racine.title('Pendu Syntaxique')
	racine.configure(background='lightsteelblue4')
	racine.minsize(880,480)
	stream = codecs.open("phrases_annotees.yaml","r","utf-8")
	phrases = yaml.load(stream)
	pendu = Interface(racine, phrases)
	racine.mainloop()

## Cette condition permet de lancer le script en ligne de commande ainsi
## que de pouvoir utiliser les objets définis ici dans un autre script.

if __name__ == "__main__":
	main()
