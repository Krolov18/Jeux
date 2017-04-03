__author__ = 'krolev'


import subprocess
import shlex

file = "France_Argentine_match_2.wav"
nomSortie = "France_Argentine_match_cut_{0}_{1}.wav"

#Récupérer dans une liste les temps de début et de fin et se servir de ces balises pour découper une séquence sonore.
# àa terme cette liste sera extraite de tes fichiers
listeTimes = \
    [
    ("15:23","15:28"),
    ("19:34","19:41"),
    ("24:48","24:58"),
    ("30:55","31:02"),
    ("33:42","33:50"),
    ("37:01","37:10"),
    ("36:50","36:55"),
    ("1:03:13","1:03:20"),
    ("1:10:36","1:10:43"),
    ("1:19:41","1:19:48"),
    ("1:32:12","1:32:22"),
    ("1:35:41","1:35:46"),
    ("1:38:38","1:38:47"),
    ("1:41:05","1:41:13"),
    ("1:41:15","1:41:21"),
    ("1:43:19","1:43:25")
]

### Fonction qui convertit des heures et des minutes en secondes pour sox.

def convertir_secondes(string):
    temp = string.split(':')
    if len(temp) == 2:
        return int(temp[0]) * 60 + int(temp[1])
    elif len(temp) == 3:
        return int(temp[0]) * 3600 + int(temp[1]) * 60 + int(temp[2])

## listeTimes est composée de tuples (deux élément par tuple), 
## on crée le nom du fichier de sortie avec les données du tuple ainsi que le calcul de la durée dont a besoin sox.
## exemple pour sox: "sox nomFichier.wav sortie.wav trim pointeur_debut dureeCapture"
def decouper_son():
	for temps in listeTimes:
		debut=temps[0]
		debutModifie=debut.replace(":","-")
		fin=temps[1]
		finModifie=fin.replace(":","-")
		nomsortieModifie = nomSortie.format(debutModifie,finModifie)
		
		duree = convertir_secondes(fin)-convertir_secondes(debut)
		## shlex prends une chaine de caractères et la découpe pour qu'elle soit au bon format pour ^^etre lu par un terminal
		commandeSplitee = shlex.split('sox {0} {1} trim {2} {3}'.format(file, nomsortieModifie, debut, duree))
		## Ce print sert à voir ce que fait le script
		print(commandeSplitee)
		## Popen sert à donner un ordre au terminal
		appelCommande = subprocess.Popen(commandeSplitee)
		## la fonction .communicate() sert à arreter la commande Popen
		finCommande = appelCommande.communicate()
	return

## condition qui sert à lancer la fonction principale du script soit decouper_son()
if __name__ == "__main__":
	decouper_son()