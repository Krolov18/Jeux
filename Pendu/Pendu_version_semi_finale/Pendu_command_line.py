# -*- Authors: LEVEQUE Korantin LANCIEN Mélanie -*-
# -*- coding: utf-8 -*-
# Pendu

#Lignes 5 à 9 : import des modules nécessaires
import codecs
import sys
from re import *
#import pyglet
from random import sample

#outil pour aider en cas de bug du script : si on change le 0 en 1, des éléments supplémentaires vont s'afficher
debug=0

#Lignes 15 à 20 : création d'une liste de mots à partir d'un fichier txt. Cette liste contiendra les mots donnés à deviner
listemots=[]
with codecs.open('liste_reponses.txt','rb','utf-8') as listedemots:
	for mot in listedemots:
		mot=mot.strip()
		if not (" " in mot or "'" in mot or "-" in mot):
			listemots.append(mot)
#Lignes 22 à 28 : ouverture et lecture du fichier contenant les différents phonèmes et les indices/feedbacks/réponses correspondants
def lecturephonemes(lettre):
	with codecs.open('PhoneBase.txt','rb','utf-8') as phonemes:
		for ligne in phonemes:
			ligne=ligne.replace('\\n','\n')
			ligne=ligne.split(';')
			if lettre == ligne[0]:
				return ligne

def mot(listemots):
	listesamplee=sample(listemots,5)
	for mot in listesamplee:
		isWin = analyse_son(mot)
		if isWin:
			reponse=input("Super! Retape le mot sans les crochets et fais <entrer> pour passer au mot suivant: ")
			while reponse != mot:
				input("Try again! :-)")
			input("\nAllez, c'est parti, nouveau mot! (fais <entrer>)")
		else:
			print("Ne perds pas espoir, tu gagneras peut etre une autre fois")
			break

# Renvoie le nombre d'essai actuel et si la personne est vivante
def augmenterPendaison(nbEssai, maxEssai):
	nbEssai+=1
	if (nbEssai >= maxEssai):
		print('Tu as été pendu')
		return nbEssai, False
	return nbEssai, True

# Renvoie si la personne a trouve le mot
def analyse_son(mot):
	essais=10
	essai=0
	isAlive=True
	for lettre in mot:
		ligne=lecturephonemes(lettre)
		reponse1=ligne[0]
		reponse2=ligne[1]
		reponse3=ligne[2]
		ind1=ligne[3]
		ind2=ligne[4]
		ind3=ligne[5]
		faux1=ligne[6]
		faux2=ligne[7]
		faux3=ligne[8]
		vrai1=ligne[9]
		vrai2=ligne[10]
		vrai3=ligne[11]
		if ind1 != '' and isAlive:
			reponse=input(ind1)
			while (reponse != reponse2) and isAlive:
				reponse=input(faux1)
				#apparition d'une barre de pendaison
				essai, isAlive = augmenterPendaison(essai, essais)
			if isAlive:
				print(vrai1)
		if ind2 != '' and isAlive:
			reponse=input(ind2)
			while (reponse != reponse3) and isAlive:
				reponse=input(faux2)
				#apparition d'une barre de pendaison
				essai, isAlive = augmenterPendaison(essai, essais)
			if isAlive:
				print(vrai2)
		if ind3 != '' and isAlive:
			reponse=input(ind3)
			while (reponse != reponse1) and isAlive:
				reponse=input(faux3)
				#apparition d'une barre de pendaison
				essai, isAlive = augmenterPendaison(essai, essais)
			if isAlive:
				print(vrai3+'\n')
				input('continuons au suivant, fais <entrer>\n')
		if not isAlive:
			return False
	return True

#Lignes 93 à 107 : discution d'introduction du jeu et explication des règles.
print ( "Bonjour ! J'ai envie de faire un pendu ! :)")
game = input ( "Tu veux jouer avec moi ??? : ")
acceptWords = ["Ouais","ouais","Oui","oui","ok","Ok","OK","o","O","1"];

while game not in acceptWords:
	game = input("Tu es sûr(e) ?? Allez ! S'il te plait !!! :3  : ")
else :
	print ("Super ! Alors, voici les règles : je vais te faire deviner un mot")
	print ("Mais au lieu de le faire lettre par lettre on va faire ça phonème par phonème !\n(attention ne mets pas les crochets quand tu écris un phonème) ")
	print ("Je te donnerai des indices en lien avec la phonétique expérimentale,\nComme par exemple la présence d'une barre de voisement sur le spectrogramme,\nAinsi que des indices articulatoires,\ncomme par exemple le fait que le phonème soit alvéolaire.")
	game = input ("Prêt(e) ? : ")
	while game not in acceptWords :
		game = input ("Allez ! Dis oui !!! :3 : ")
	else :
		print ("C'est parti !")


mot(listemots)

## creer une liste de traits à mettre à l'échaffaud et lire la liste