#exercice 1

#1. le caractère \n correspond a un passage de ligne
var = "Le Python\nc'est super"
print(var)
#2.
print(len(var))  #il sera afficher 21 car \n represente 1 seul caractère
print(var[9])    #il affichera un passage de ligne
print(var[-3])   #il affichera "p"
print(var[3:7])  #il affichera "Pyth"
#4.
#dans var 'y' sera l'indice 4
print(var.find('y'))
#5.
print(var[17])
#6.
print(var[-4])

#exercice 2

#1.
help(str.find)
#2.
#il affichera 6
#3.
print(var.find("t"))  #il ne compte pas les espace
#4.
#print(var.find("e"))       affichera 1
#print(var.find(" "))       affichera 2
#print(var.find("p"))       affichera 8
#print(var.find("c'est"))   affichera 10
#print(var.find("z"))       affichera error
#5.
print(var.find("e"))
print(var.find(" "))
print(var.find("p"))
print(var.find("c'est"))
print(var.find("z"))       #il affiche -1 car quand il y a une erreur il affiche -1
