import os
import string
import codecs
import sys

""" Ce script a été utilisé sur la version .txt des transcriptions de nos corpora (plusieurs fichiers .txt)
Il a pour but d'ouvrir les transcription d'en extraire chaque mot puis de les enregistrer 
dans un nouveau fichier .txt nommé 'liste de mots' qui servira de lexique de base au pendu """  

# Définition d'une variable que l'on utilisera dans la fonction segmenter_liste.
changer_ponctuation2tiret6 = str.maketrans(string.punctuation,' '*(len(string.punctuation)))


### liste de tuple pour la traduction
trans = [('S','ʃ'),('Z','ʒ'),('N','ŋ'),('J','ɲ'),('H','ɥ'),('E','ɛ'),('2','ø'),('9','œ'),('6','ə'),('O','ɔ'),('è','e'),
         ('ò','o'),('ê','~ɛ'),('û','~œ'),('ô','~ɔ'),('â','~ɑ'),('@','(ə)'),('@','ə'),
         ('n"','(n)'),('t"','(t)'),('z"','(z)'),('R"','(r)'),('p"','(p)')]

def ouverture_fichier(path, element):
    """
    Cette fonction ouvre et lit le fichier ligne par ligne.
    """
    with codecs.open(path+"/"+element,'r','utf-8') as fichier:
        return [ligne.strip() for ligne in fichier]

def creation_liste(caracs,charset):
    """
    Cette fonction "découpe" les mots contenus dans nos transcriptions (on remplace la ponctuation par des espaces, on
    split sur ces espaces puis on ne garde que les éléments non vides).
    """
    return [x.strip() for x in caracs.translate(charset).split(' ') if x != ""]

def segmenter_liste(liste,pathFile):
    """
    Cette fonction a pour but d'étendre la liste créée par creation_liste en lui ajoutant au fur et à mesure les mots des fichiers .txt suivants.
    """
    return [[liste.extend(creation_liste(x,changer_ponctuation2tiret6)) for x in ouverture_fichier(pathFile, os.listdir(pathFile)[i])] for i in range(len(os.listdir(pathFile)))]

def comparer_lexique(lexicon,mots):
    """
    Fonction qui permet de récupérer la colonne phonétique de bdlexique avec les mots orthographiques du corpus.
    """
    nvListe = []
    for x in mots:
        for y in lexicon:
            mot = y.split(';')[0]
            if mot == x:
                nvListe.append(y.split(';')[1])
    return nvListe

def changer_caractere(chaine,charset):
    """
    Cette fonction prend une liste de tuple
    """
    for lettre in list(chaine):
        for element in charset:
            if lettre == element[0]:
                chaine = chaine.replace(lettre,element[1])
    return chaine


# Cette fonction est la fonction principale du script, c'est elle qui lance l'écriture de chaque mot des corpora dans le fichier .txt qui servira pour le pendu. 
def main():
    temp1 = codecs.open(sys.argv[1],'r','utf-8')
    lexique = temp1.readlines()
    pathFile = "/home/krolev/PycharmProjects/Pendu/corpus_Fichiers_TXT_utf8"
    mots = []
    segmenter_liste(mots,pathFile)
    liste = changer_caractere(set(comparer_lexique(lexique,mots)),trans)
    sortie = codecs.open(sys.argv[2],'w','utf-8')
    [sortie.write(x+"\n") for x in liste]

# Condition permettant l'execution automatique du script.
if __name__ == '__main__':
    main()
