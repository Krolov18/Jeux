#coding: utf-8

import codecs
import sys
from re import *
#import pyglet
from random import sample


debug=0
acceptWords = ["Ouais","OUAIS","ouais","Oui","oui","ok","Ok","OK","o","O","1"]

def nettoyer_mots(liste_reponse):
	listemots=[]
	with codecs.open(liste_reponse,'rb','utf-8') as listedemots:
		for mot in listedemots:
			mot=mot.strip()
			if not (" " in mot or "'" in mot or "-" in mot):
				listemots.append(mot)
	return listemots
			
			
def lecturephonemes(lettre):
	with codecs.open('PhoneBase.txt','rb','utf-8') as phonemes:
		for ligne in phonemes:
			ligne=ligne.replace('\\n','\n')
			ligne=ligne.split(';')
			if lettre == ligne[0]:
				return ligne

def mot(liste):
	listesamplee=sample(liste,5)
	for mot in listesamplee:
		isWin = analyse_son(mot)
		if isWin:
			reponse=input("Super! Retape le mot sans les crochets et fais <entrer> pour passer au mot suivant: ")
			while reponse != mot:
				input("Try again! :-)")
			input("\nAllez, c'est parti, nouveau mot! (fais <entrer>)")
		else:
			print("Ne perds pas espoir, tu gagneras peut-être une autre fois!")
			break


def augmenterPendaison(nbEssai, maxEssai):
	nbEssai+=1
	if (nbEssai >= maxEssai):
		print('Tu as été pendu')
		return nbEssai, False
	return nbEssai, True


def analyse_son(mot):
	essais=10
	essai=0
	isAlive=True
	for lettre in mot:
		ligne=lecturephonemes(lettre)
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



print ( "Bonjour ! J'ai envie de faire un pendu ! :)")
game = input ( "Tu veux jouer avec moi ??? : ")


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