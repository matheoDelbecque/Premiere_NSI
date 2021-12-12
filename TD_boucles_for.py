#exercice 1

range(2,9)
range(0,25,4)
maChaine = "informatique"
print(list(range(maChaine)))

#exercice 2

for i in range(11):
    print("Pour progresser en programmation, la pratique est le plus important")

#exercice 3

for i in range(1,11):
    print(7*i)
    
for i in range(1,11):
    print("7 *",i,"=",7*i)
    
def tableMultiplication(nb):
    for i in range(1,11):
        print(nb,"*",i,"=",nb*i)
tableMultiplication(3)

def tableMultiplication(nb):
    for i in range(1,11):
        print(nb,"*",i,"=",nb*i)
def plusieursTablesMultiplication(a,b):
    for i in range(a,b+1):
        print(tableMultiplication(i))
plusieursTablesMultiplication(5,9)

#exercice 4

def nombreCaracteres(chaine):
    compteur = 0
    for i in chaine :
        compteur = compteur + 1
    return compteur
print(nombreCaracteres("bonjour"))

# exercice 5

def compterOccurence(chaine,c):
    compteur = 0
    for lettre in chaine:
        if lettre == c :
            compteur = compteur + 1
    return compteur
print(compterOccurence("Guido Van Rossum", 'o'))
print(compterOccurence("Linus Torvalds", 'z'))

# exercice 6

def rechercheIndice(chaine,c):
    """
    Description de la fonction : renvoie l'indice de la première occurence du caractère c dans chaine
    chaine (str) : chaine de caractère dans laquelle la recherche s'effectue
    c (str) : caractère recherché
    return (int ou None) : indice du caractère c danc chaine (None si le caractère c n'apparaît pas dans chaine)
    """
    for i in range(len(chaine)):
        if chaine[i] == c :
            return i
print(rechercheIndice("Stallmann","a"))

# exercice 7

def produitChiffres(n):
    s = 1
    n = str(n)
    for i in range(len(n)):
        s = s * int(n[i])
    return s
print(produitChiffres(4132))

#exercice 9

def repetition(chaine,n):
    m = ""
    for c in chaine:
        m = m + c*4
    return m
print(repetition("Python",4))

#exercice 10

def est_premier(nb):
    non_premier = 0
    for i in range(2,nb):
        if nb % i == 0:
            non_premier = non_premier + 1
    if non_premier >= 1:
        return False
    else:
        return True
print(est_premier(8))
print(est_premier(11))
