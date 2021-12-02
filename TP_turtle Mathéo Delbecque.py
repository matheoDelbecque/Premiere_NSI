from turtle import *

###1
##down
##forward(100)
##left(90)
##forward(100)
##left(90)
##forward(100)
##left(90)
##forward(100)
##left(90)
##
###2
##for i in range(4):
##    forward(100)
##    left(90)
##carre()
##
###3
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
##carre(175)
##
###4
##def carreEmboite(cote,nb):
##    """
##    Description de la fonction : Déplace la tortue de sorte qu'elle dessine une succession
##                                de carrés emboîtés régulièrement espacés
##    cote(int) : côté du plus petit carré
##    nb(int): nombre total de carrés
##    return : None
##    """
##    for i in range(nb):
##        carre(cote * (i + 1))
##
##carreEmboite(5,50)

#5
def carreTournant(cote,nb):
    """
    Description de la fonction : Déplace la tortue de sorte qu'elle dessine une succession
                                de carrés tournants régulièrement espacés
    pas(int) : côté du plus petit carré
    nb(int): nombre total de carrés
    return : None
    """
    for i in range(nb):
        carre(cote)
        left(360//nb)
carreTournant(70,50)