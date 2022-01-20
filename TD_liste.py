#exercice 2

help(list.insert)

liste = ['Alice', 'Bob', 'Tom']
liste.insert(2,'Marc')
print(liste)

#exercice 3

t = []
for i in range(0,10,2):
    t.append(i**2)
print(t)

#exercice 4

t = [0]*10

for i in range(len(t)):
    t[i] = 10 - i
print(t)

#exercice 5

def longueurNomV1(liste_nom) : 
    liste_longueur = []
    for nom in liste_nom:
        liste_longueur.append(len(nom))
    return liste_longueur
print(longueurNomV1(['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']))

def longueurNomv2(liste_nom) : 
    liste_longueur = [0]*len(liste_nom)
    for i in range(len(liste_nom)):
        liste_longueur[i] = len(liste_nom[i])
    return liste_longueur
print(longueurNomv2(['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']))

#exercice 6

def affiche_liste(liste):
    for c in liste:
        print(c,end=' ')
t=['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
affiche_liste(t)

#exercice 7

def enleveDoublon(liste):
    liste_sans_doublons = []
    for c in liste:
        if not(c in liste_sans_doublons):
            liste_sans_doublons.append(c)
    return liste_sans_doublons
liste_entier = [23, 45, 23, 43, 7, 66, 21, 45, 23, 7, 200, 200]
print(enleveDoublon(liste_entier))

#exercice 8

def alterne(liste1,liste2):
    liste3 = []
    for i in range(len(liste1)):
        liste3.append(liste1[i])
        liste3.append(liste2[i])
    return liste3
t1 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(alterne(t1,t2))
