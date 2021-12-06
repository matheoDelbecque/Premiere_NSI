from turtle import *

#1
down
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

#2
for i in range(4):
    forward(100)
    left(90)
carre()

#3
def carre(pas):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine un carré
                                 et revienne au point de départ (même position et orientation)
    pas(int) : côté du carré
    return : None
    """
    for i in range(4):
        forward(pas)
        left(90)
    return
carre(175)

#4
def carreEmboite(cote,nb):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine une succession
                                de carrés emboîtés régulièrement espacés
    cote(int) : côté du plus petit carré
    nb(int): nombre total de carrés
    return : None
    """
    for i in range(nb):
        carre(cote * (i + 1))
    return

carreEmboite(5,50)

#5
def carreTournant(cote,nb):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine une succession
                                de carrés tournants régulièrement espacés
    pas(int) : côté du plus petit carré
    nb(int): nombre total de carrés
    return : None
    """
    speed(50)
    for i in range(nb):
        carre(cote)
        left(360/nb)
    return
carreTournant(70,50)

#6
def ligne2carre(nb,cote,espacement):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine une ligne de carré
    nb(int) : nombre de carrés dessinés
    cote(int): côté du carré
    espacement(int) : espacement entre 2 carrés successifs
    return : None
    """
    speed(50)
    for i in range(nb):
        carre(cote)
        up()
        forward(cote+espacement)
        down()
    return
ligne2carre(20,6,10)

#7
def damier(longueur,hauteur,cote,espacement):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine un damier
    longueur(int) : nombre de carrés par ligne
    hauteur(int) : nombre de carrés par colonne
    cote(int): côté du carré
    espacement(int) : espacement entre 2 carrés successifs
    return : None
    """
    speed(50)
    for i in range(hauteur):
        ligne2carre(longueur,cote,espacement)
        up()
        backward(cote*longueur+espacement*longueur)
        right(90)
        forward(cote+espacement)
        left(90)
        down()
damier(30,20,10,2)
