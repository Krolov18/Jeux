import os
import string
import codecs
import argparse

""" Ce script a été utilisé sur la version .txt des transcriptions de nos corpora (plusieurs fichiers .txt)
Il a pour but d'ouvrir les transcription d'en extraire chaque mot puis de les enregistrer 
dans un nouveau fichier .txt nommé 'liste de mots' qui servira de lexique de base au pendu """  

# Définition d'une variable que l'on utilisera dans la fonction segmenter_liste.
changer_ponctuation2tiret6 = str.maketrans(string.punctuation,' '*(len(string.punctuation)))

# Cette fonction ouvre et lit le fichier ligne par ligne.
def ouverture_fichier(path, element):
	with codecs.open(path+"/"+element,'r','utf-8') as fichier:
		return [ligne.strip() for ligne in fichier]

# Cette fonction "découpe" les mots contenus dans nos transcriptions (on remplace la ponctuation par des espaces, on 
# split sur ces espaces puis on ne garde que les éléments non vides).		
def creation_liste(caracs,charset): 
	return [x.strip() for x in caracs.translate(charset).split(' ') if x != ""]

# Cette fonction a pour but d'étendre la liste créée par creation_liste en lui ajoutant au fur et à mesure les mots des fichiers .txt suivants.	
def segmenter_liste(liste,pathFile):
	return [[liste.extend(creation_liste(x,changer_ponctuation2tiret6)) for x in ouverture_fichier(pathFile, os.listdir(pathFile)[i])] for i in range(len(os.listdir(pathFile)))]

# Cette fonction est la fonction principale du script, c'est elle qui lance l'écriture de chaque mot des corpora dans le fichier .txt qui servira pour le pendu. 
def main():
	sortie = codecs.open('listemots.txt','w','utf-8')
	pathFile = "/home/krolev/Documents/Fichiers_TXT_utf8"
	mots = []
	segmenter_liste(mots,pathFile)
	[sortie.write(x+"\n") for x in mots]

# Condition permettant l'execution automatique du script.	
if __name__ == '__main__':
	main()
