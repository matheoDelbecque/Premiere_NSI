#exercice 1

def bac(prenom,nom,moyenne):
    """
    Description de la fonction: dis si une personne à obtenu son bac
    prenom(str): le prenom du candidat
    nom(str): le nom du candidat
    moyenne(int ou float): sa moyenne du bac
    return(None):
    """
    if moyenne >= 10:
        print(prenom,nom,'a obtenu son baccalauréat, Félicitations !')
bac('Alice','Dupont',12)

#exercice 2

def bac2(prenom,nom,moyenne):
    """
    Description de la fonction: dis si une personne à obtenu ou pas son bac
    prenom(str): le prenom du candidat
    nom(str): le nom du candidat
    moyenne(int ou float): la moyenne du candidat au bac
    return(None):
    """
    if moyenne >= 10:
        print(prenom,nom,'a obtenu son baccalauréat, Félicitations !')
    else:
        print(prenom,nom,'n\'a pas obtenu son baccalauréat')
bac2('Bob','Martin',8)

#exercice 3

def maximum(a,b):
    """
    description de la fonction: donne le maximum entre deux nombres
    a(int ou float): le premier nombre
    b(int ou float): le deuxième nombre
    return(int ou float): renvoie le maximum
    """
    if a >= b:
        return(a)
    else:
        return(b)
print(maximum(23,64))

def minimum(a,b):
    """
    description de la fonction: donne le minimum entre deux nombres
    a(int ou float): le premier nombre
    b(int ou float): le deuxième nombre
    return(int ou float): renvoie le minimum
    """
    if a <= b:
        return(a)
    else:
        return(b)
print(minimum(47,29))

def valeur_absolue(a):
    """
    description de la fonction: donne la valeur absolue d'un nombre
    a(int ou float): le nombre dont on veux sa valeur absolue
    return(int ou float): renvoie la valeur absolue de a
    """
    if a >= 0:
        return(a)
    else:
        return(-a)
print(valeur_absolue(-9))

#exercice 4

def bowling(boule1, boule2):
    """
    Description de la fonction : Affiche à l'écran les performances d'un joueur de bowling
    boule1 (int) : nombre de quilles renversées avec la première boule
    boule2 (int) : nombre de quilles renversées avec la deuxième boule
    return (None) :
    préconditions sur les entrées : boule1 + boule2 <= 10 
    """
    if boule1 == 10:
        print("X")
    elif boule1 + boule2 == 10:
        print("/")
    else:
        print(boule1 + boule2)
bowling(2,6)

#exercice 5

def croissant(a,b,c):
    if a <= b :
        if b<= c:
            resultat = True
        else :
            resultat = False
    else :
        resultat = False
    return resultat
print(croissant(5,2,7))

#exercice 7

def triangle(c1,c2,c3):
    """
    description de la fonction : affiche une des caractéristiques du triangle suivante : équilatéral, isocèle ou scalène
    c1, c2, c3 (int ou float) : trois côtés du triangle
    précondition sur les entrées : on considère que les valeurs de c1, c2 et c3 doivent permettre de construire un triangle
    return (None)
    """
    if c1 == c2:
        if c2 == c3:
            print('Le triangle est équilatérale')
        else:
            print('Le triangle est isocèle')
    elif c2 == c3:
        print('Le triangle est isocèle')
    elif c1 == c3:
        print('Le triangle est isocèle')
    else:
        print('Le triangle est scalène')
triangle(3,2,3)
triangle(3,3,2)
triangle(2,3,3)
triangle(3,3,3)
triangle(1,2,3)
