#1
def afficher_ligne(n):
    for c in range(n):
        print('O',end="")
# afficher_ligne(5)
# print()
# afficher_ligne(12)

#2
def afficher_carre(n):
    for c in range(n):
        for ch in range(n):
            print('O',end='')
        print()
# afficher_carre(5)
# print()
# afficher_carre(12)

#3
def afficher_rectangle(hauteur,largeur):
    for c in range(hauteur):
        for ch in range(largeur):
            print('O',end='')
        print()
# afficher_rectangle(8,3)
# print()
# afficher_rectangle(5,20)

#4
def afficher_triangle_rectangle(n):
    nb=n
    for c in range(n):
        nb=nb-1
        for ch in range(n-nb):
            print('O',end='')
        print()
# afficher_triangle_rectangle(5)
# print()
# afficher_triangle_rectangle(10)

#5
def afficher_carre_diagonale(n):
    nb=n
    nb2=n-1
    for c1 in range(n):
        if c1==0 :
            print('X',end='')
            for c2 in range(n-1):
                print('O',end='')
            print()
        else :
            nb=nb-1
            for c3 in range(n-nb):
                print('O',end='')
            print('X',end='')
            nb2=nb2-1
            for c4 in range(nb2):
                print('O',end='')
            print()
# afficher_carre_diagonale(5)
# print()
# afficher_carre_diagonale(15)
        
