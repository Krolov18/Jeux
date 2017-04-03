# -*- coding: utf-8 -*-
# Pendu

import codecs
import sys
import re
#import tkinter
from random import sample



try:
	listedemots=codecs.open(sys.argv[1],'r','utf-8')
except IOError:
	print("Erreur avec votre fichier")


try:
	phonemes=codecs.open(sys.argv[2],'r','utf-8')
except IOError:
	print("Erreur avec votre fichier")


Mots=listedemots.readlines()
listedemots.close()


Phones=phonemes.readlines()
phonemes.close()



#class pendu_treatment(random,pyglet):
#"Cet objet permet d'intérroger deux fichiers txt, un qui est une liste de mots de n caractères, un autre qui est un assignation d'un caractère (phonème) à une série d'informations concernant ce phonème."
liste=sample(Mots,5)
print(liste)


lettres=[]
reponses=[]
for mot in liste:
	for lettre in mot:
		if lettre not in lettres:
			lettres.append(lettre)
for ligne in Phones:
	phone=Phones[0]
	if phone in lettre:
		if ligne not in reponses:
			reponses.append(ligne)
			
def lettre2phone(lettre,liste):
	for ligne in liste:
		ligne=ligne.replace('\\n','\n')
		ligne=ligne.split(';')
		if lettre == ligne[0]:
			return ligne

def motexo(liste):
	for mot in liste:
		lettreexo(mot)
		
def lettreexo(mot):
	for lettre in mot:
		ligne=lettre2phone(lettre,Phones)
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
		
		if ind1 != None:
			reponse=input(ind1)
			while reponse != reponse2:
				reponse=input(faux1)
				#apparition d'une barre de pendaison
			print(vrai1)
		else:
			continue
		if ind2 != None:
			reponse=input(ind2)
			while reponse != reponse3:
				reponse=input(faux2)
				#apparition d'une barre de pendaison
			print(vrai2)
		else:
			continue
		if ind3 != None:
			reponse=input(ind3)
			while reponse != reponse1:
				reponse=input(faux3)
				#apparition d'une barre de pendaison
			print(vrai3)
			input('continuons au suivant, fais <entrer>')
		else:
			print('Problem')





print ( "Bonjour ! J'ai envie de faire un pendu ! :)")
game = input ( "Tu veux jouer avec moi ??? : ")
acceptWords = ["Ouais","ouais","Oui","oui","ok","Ok","OK"];

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
		
#ici s'arrête le chat d'intro, j'ai essayé d'être "friendly user" ^^


motexo(liste)
