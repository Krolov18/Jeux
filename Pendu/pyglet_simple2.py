# coding: utf-8

# #Exemple de jeu avec Pyglet

import pyglet, random, codecs
from math import sqrt,atan2,hypot,cos,sin,pi
#from unidecode import unidecode
pause=[False]
text_initial="Hello World!"
#solution=u"filles"
#solution=solution.lower()


# ###Ouvrir BDLexique
# 
# - ouverture du fichier et lecture dans *bdlexique*
# - tirage au sort d'un mot avec mise en minuscules dans *solution*


nomFichier="liste_reponses.txt"
fichierLexique=codecs.open(nomFichier,"r", encoding="utf8")
bdlexique=fichierLexique.readlines()
nbLexemes=len(bdlexique)
numSolution=random.randint(0,nbLexemes)
solution=bdlexique[numSolution].split(";")[0].lower()
print solution
essais=[]


# ###Ouvrir une fenêtre
# 
# - par défaut
#  - fond noir
#  - dimension 
# - fond gris


window = pyglet.window.Window(1920,1080)
pyglet.gl.glClearColor(0.5, 0.5, 0.5, 9)


# ###Placer l'ancre au milieu d'une image


def center_anchor(img):
	img.anchor_x=img.width//2
	img.anchor_y=img.height//2


# ###Créer les étiquettes de texte
# 
# - *mot* pour la partie centrale du jeu
# - *message* pour les messages en haut de la fenêtre
# - *avant* pour afficher le mot le plus proche avant
# - *apres* pour afficher le mot le plus proche après
# - *coups* pour afficher le nombre d'essais courant


mot = pyglet.text.Label(text_initial,
						  font_name='Minion Pro',
						  font_size=64,
						  color=(255,128,0,255),
						  x=window.width//2, y=window.height//2,
						  anchor_x='center', anchor_y='center')

message = pyglet.text.Label('',
						  font_name='Gill Sans',
						  font_size=72,
						  color=(255,255,255,255),
						  x=window.width//2, y=4*window.height//5,
						  anchor_x='center', anchor_y='center')

avant = pyglet.text.Label('',
						  font_name='Gill Sans',
						  font_size=24,
						  color=(255,128,0,255),
						  x=4*window.width//5, y=window.height//5,
						  anchor_x='center', anchor_y='center')

apres = pyglet.text.Label('',
						  font_name='Gill Sans',
						  font_size=24,
						  color=(255,128,0,255),
						  x=window.width//5, y=window.height//5,
						  anchor_x='center', anchor_y='center')

coups = pyglet.text.Label("",
						  font_name='Gill Sans',
						  font_size=64,
						  color=(255,128,0,255),
						  x=0, y=window.height//2,
						  anchor_x='left', anchor_y='center')


# ###Créer un champ de saisie
# 
# Le fonctionnement de document n'est pas très clair. Cette structure permet d'obtenir la saisie des caractères au clavier avec l'événement **on_text**


document = pyglet.text.document.UnformattedDocument()
layout = pyglet.text.layout.IncrementalTextLayout(document, 6, 1)
caret = pyglet.text.caret.Caret(layout)
window.push_handlers(caret)


# ###Evenement clavier


@window.event
def on_key_press(symbol, modifiers):
	if symbol==pyglet.window.key.LEFT:
		mot.x-=10
	elif symbol==pyglet.window.key.RIGHT:
		mot.x+=10
	elif symbol==pyglet.window.key.RETURN:
		mot.text="_"*len(solution)
	elif symbol==pyglet.window.key.BACKSPACE:
		correction=mot.text.split("_")[0][:-1]
		mot.text=correction+"_"*(len(solution)-len(correction))
	elif symbol==pyglet.window.key.SPACE:
		pause[0]=not pause[0]

@window.event
def on_text(text):
	if len(pause)<2:
		mot.text=mot.text.replace("_",text,1)
	if "_" not in mot.text and mot.text!=text_initial:
		essai=mot.text.lower()
		if essai == solution:
			message.text="Bravo !!!"
			pause.append("fin")
		else:
			message.text=u"presque %s"%mot.text
			mot.text="_"*len(solution)

# ###Evenement écran

@window.event
def on_draw():
	window.clear()
	mot.draw()
	message.draw()
	layout.draw()
	


pyglet.app.run()