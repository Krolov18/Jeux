__authors__ = "LANCIEN Mélanie, LEVEQUE Korantin"

# -*- coding: utf8 -*-

# Import des modules. 
from tkinter import * 
from tkinter.messagebox import *
from random import choice
import argparse
import codecs

# Gestion de la lecture du lexique.
parseur = argparse.ArgumentParser()
parseur.add_argument('bdlexique')
arguments = parseur.parse_args()
bdlexique = arguments.bdlexique

# Sélection d'un mot à deviner.
def chercher_reponse(fichierTxt):
	lettres = ["a","z","e","r","t","y","u","i","o","p","s","d","f","g","j","k","l","m","w","v","b","n"]
	with codecs.open(fichierTxt,mode = "r",encoding = "utf-8") as reponses:
		tempListe = reponses.readlines()
		listelettres = set("".join(tempListe))
		lettres_poubelle = list(listelettres - set(lettres))
		reponse = choice([x.strip().split(';')[1] for x in tempListe if (len(x.strip().split(';')[1]) == 7) and ( not any(lettre in x.strip().split(';')[1] for lettre in lettres_poubelle))])
		return reponse


# La ligne qui suit fonctionne comme une fonction grâce au mot clé "lambda". Ici lambda équivaut à "def", les deux mots qui suivent correspondent aux arguments, et
# ce qui suit les ":" est l'action à accomplir, soit ici une liste compréhension.
# De plus cette ligne s'appelle comme une fonction soit recuperer_indices(mot, lettre).

recuperer_indices = lambda mot, lettre: [indice for indice, string in enumerate(mot) if string==lettre]

class Pendu(Frame): 
	def __init__(self, parent):
		"""
		Fonction d'initialisation. Dans ce cas-ci, cette fonction va définir toute la partie graphique.
		Les paramètres de la fenêtre principale, les boutons, les labels (qui correspondent à des zones
		de texte), et les champs de saisie, sans oublier l'image.	"""
		Frame.__init__(self, parent)
		parent.title('Pendu')
		self.mot2discover = ""
		self.motCache  = ""
		self.nbEssai = 0
		self.img = PhotoImage(file = "image_pendu/pendu0.gif")
		self.path = "image_pendu/pendu{0}.gif"
		self.configure(background='lightsteelblue3')
		

		bouton = Button(self, text='[kite]', width=5, height=1, fg="red4", font=("comic sans ms","10","bold"), command=self.quit)
		bouton.grid(row=5 , column=2)

		bouton = Button(self, text='[ʒuwe]', width=5, height=1, fg="red4", font=("comic sans ms","10","bold"), command = self.initialiser_jeu)
		bouton.grid(row=0 , column=3, sticky=E)

		bouton = Button(self, text='ok',font=("comic sans ms","10","bold"),fg="black", command= self.jouer)
		bouton.grid(row=2 , column=3, columnspan=2)

		self.label = Label(self, image = self.img, width=240, height=320)
		self.label.grid(row = 0, rowspan=5, column=0,sticky="W" )

		label = Label(self, text=' Bienvenue dans notre pendu phonétique ! Clique sur ',font=("comic sans ms", "11", "bold"), fg="black")
		label.grid(row =0, column=2)
		
		label = Label(self, text=' [mo a dekuvrir] ',font=("comic sans ms", "10", "bold"), fg="black")
		label.grid(row =1, column=2, sticky=W)

		label = Label(self, text=' [tape yn lɛtrə] ',font=("comic sans ms", "10", "bold"), fg="black")
		label.grid(row =2, column=2, sticky=W)

		self.entreemotCache = Entry(self)
		self.entreemotCache.grid(row =1, column =2)

		self.entreeUtilisateur = Entry(self)
		self.entreeUtilisateur.grid(row =2, column =2)

	
	def verifier_proposition(self, proposition):
		"""
		Vérification de la longueur et la valeur alphabétique de la proposition de l'utilisateur.
		Valeur renvoyée : proposition type : 'string' """
		if len(proposition) != 1 and proposition.isalpha():
			showinfo('[erœr]','[problɛm avɛk la lõgœr]')
		elif not proposition.isalpha():
			showinfo('[erœr]', "[la propozisjõ ne pa alfabetik]")
		else:
			return proposition
	

	def afficher_proposition(self, lettre):
		"""
		Création de motcache en une liste afin de pouvoir changer ses '_' par les proposition de l'utilisateur faisant partie du mot à trouver.
		Valeur renvoyee : motCache type : 'string' 		"""
		indices = recuperer_indices(self.mot2discover, lettre)
		if len(indices) > 0 :
			listMotcache = list(self.motCache)
			for ind in indices :
				listMotcache[ind] = lettre
			self.motCache = "".join(listMotcache)
 
	def rafraichir_jeu(self):
		"""
		Fonction qui va permettre de remettre à zéro la zone de la variable motCache (soit remplacer les caractères présents par les '_' de départ.
		Effacement du champ suivi de l'insertion de la variable motCache à son état initial		"""
		self.entreemotCache.delete(0, END)
		self.entreemotCache.insert(0, self.motCache)

 
	def creer_motCache(self):
		"""
		Choix d'un mot dans une liste, mot qu'on va transformer en une liste de tirets de la longueur du mot lui-même. motCache servira de base pour la fonction afficher_proposition
		Valeur renvoyée : motCache ; type: 'string' 	"""
		self.mot2discover = chercher_reponse(bdlexique)
		self.motCache  = ''.join(['_' for lettre in self.mot2discover])
 
	def initialiser_jeu(self):
		"""
		On lance les fonctions creer_motCache et raffraichir_jeu, fonction qui servira de gachette pour le bouton 'jouer' """
		self.creer_motCache()
		self.rafraichir_jeu()
		self.img = PhotoImage(file = "image_pendu/pendu0.gif")
 
	def afficher_reussite(self):
		"""
		fonction qui fait apparaitre les message de réussite ou d'erreur du joueur."""
		if self.nbEssai >= 10 :
			showinfo(self, message = "/ju: 'lɒst/")
		elif '_' not in self.motCache :
			showinfo(self, message = "/ju: 'wɪn/")

	def changer_image(self, essai):
		"""
		Changement d'image par la variable essai 	"""
		self.img = PhotoImage(file=self.path.format(essai))
		self.label.configure(image = self.img)


	def jouer(self):
		"""
		Mécanisme principal du script. Bloc conditionnel qui permet de voir si la proposition du joueur est dans le mot-solution ou pas.
		'if' vérifie si la saisie du joueur n'est pas dans mot2discover. Il sera alors ajouté 1 à nbEssai et nbEssai est passé en argument à afficher_pendu(nbEssai)."""
		saisie = self.verifier_proposition(self.entreeUtilisateur.get())
		self.entreeUtilisateur.delete(0, END)
		if saisie not in self.mot2discover:
			self.nbEssai += 1
			self.changer_image(self.nbEssai)
		else:
			self.afficher_proposition(saisie)
			self.rafraichir_jeu()
		self.afficher_reussite()

# Initialisation et lancement de la fenêtre tkinter
root = Tk() 
root.configure(background='lightsteelblue3')
root.minsize(650,350) 
pendu = Pendu(root) 
pendu.pack() 
root.mainloop()
