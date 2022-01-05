import geometrie_triangle
import math

def nombre_pots(base, hauteur, surface_couvrante):
    """
    Calcul du nombre de pots nécessaires
    paramètre base (float) : valeur de la base de la pièce
    paramètre hauteur (float) : valeur de la hauteur de la pièce
    paramètre surface_couvrante (float) ; valeur de la surface couvrante d'1 pot de peinture
    retour (int) : Nombre de pots de peintures nécessaires
    pré-conditions : la base, la hauteur et la surface_couvrante sont des valeurs strictement positives
    post-conditions : Néant
    """
    return math.ceil(geometrie_triangle.aire(base,hauteur)/surface_couvrante)

def nombre_baches(base, hauteur, surface_couvrante):
    """
    Calcul du nombre de bâches nécessaires
    paramètre base (float) : valeur de la base de la pièce
    paramètre hauteur (float) : valeur de la hauteur de la pièce
    paramètre surface_couvrante (float) ; valeur de la surface couvrante d'1 bâche
    retour (int) : Nombre de bâches nécessaires
    pré-conditions : la base, la hauteur et la surface_couvrante sont des valeurs strictement positives
    post-conditions : Néant
    """
    return math.ceil(geometrie_triangle.aire(base,hauteur)/surface_couvrante)

def nombre_rubans(base, hauteur, perimetre_couvrante):
    """
    Calcul du nombre de rubans nécessaires
    paramètre base (float) : valeur de la base de la pièce
    paramètre hauteur (float) : valeur de la hauteur de la pièce
    paramètre perimetre_couvrante (float) ; valeur du périmètre couvrant d'1 ruban
    retour (int) : Nombre de rubans nécessaires
    pré-conditions : la base, la hauteur et la perimetre_couvrante sont des valeurs strictement positives
    post-conditions : Néant
    """
    return math.ceil(geometrie_triangle.perimetre(base,hauteur)/perimetre_couvrante)

def salaire(base, hauteur):
    """
    Calcul du salaire du peintre, sachant que le peintre couvre 1m * 1m en 1 heure pour 7,5€
    paramètre base (float) : valeur de la base de la pièce
    paramètre hauteur (float) : valeur de la hauteur de la pièce
    retour (float) : Salaire du peintre
    pré-conditions : la base, la hauteur et la surface_couvrante sont des valeurs strictement positives
    post-conditions : Néant
    """
    return geometrie_triangle.aire(base,hauteur) * 7.5

def est_reparation_couverte(total_couts):
    """
    Indique si les réparations sont couvertes
    paramètre total_couts (float) ; valeur totale des coûuts
    retour (bool) : True si le forfait couvre l'ensemble des coûts
    pré-conditions : le total des coûts est strictement positif
    post-conditions : Néant
    """
    return total_couts <= 500