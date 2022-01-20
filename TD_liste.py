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

#exercice 9

a = [8468, 4560, 3941, 3328, 7, 9910, 9208, 8400, 6502, 1076, 5921, 6720, 948, 9561, 7391, 7745, 9007, 9707, 4370, 9636, 
     5265, 2638, 8919, 7814, 5142, 1060, 6971, 4065, 4629, 4490, 2480, 9180, 5623, 6600, 1764, 9846, 7605, 8271, 4681, 
     2818, 832, 5280, 3170, 8965, 4332, 3198, 9454, 2025, 2373, 4067]

b = [9093, 2559, 9664, 8075, 4525, 5847, 67, 8932, 5049, 5241, 5886, 1393, 9413, 8872, 2560, 4636, 9004, 7586, 1461, 350, 
     2627, 2187, 7778, 8933, 351, 7097, 356, 4110, 1393, 4864, 1088, 3904, 5623, 8040, 7273, 1114, 4394, 4108, 7123, 8001, 
     5715, 7215, 7460, 5829, 9513, 1256, 4052, 1585, 1608, 3941]


for i in range(len(a)):
    if a[i] == b[i]:
        print("le nombre",a[i],"d'indice",i,"est dans les deux liste")
