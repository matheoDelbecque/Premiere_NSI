#exos 1,2,3

def accueil2020(prenom,nom,annee):
    """
    Description de la fonction : affiche une phrase de presentation d\'une personne avec son nom,prenom et son age
    prenom (str) : prenom 
    nom (str) : nom
    annee (int) : annee de naissance
    return (None) :
    """
    age = str(2021-annee)
    accueil = 'Bonjour '+prenom+' '+nom+' vous avez '+age+' ans'
    print(accueil)
accueil2020('Alice','MARTIN',2004)

help(accueil2020)

def surface_disque(R):
    """
    Description de la fonction : donne la surface d\'un disque
    R (int) : le rayon du disque
    return (int ou float) : la surface du disque
    """
    calcul = R**2*3.14
    return calcul
surface = surface_disque(2)

print(surface)
help(surface_disque)

#exos 4

def taille_fichier(kio):
    """
    Description de la fonction : donne le nombre d'octet et de bits dans le fichier
    kio (int) : la taille du fichier en kio
    return (None) :
    """
    octet=kio*1024
    bits=octet*8
    phrase='La taille de votre fichier est de '+str(octet)+' octets et '+str(bits)+' bits'
    print(phrase)
    
taille_fichier(5)
help(taille_fichier)

#exos 5

def farenheitToCelsius(tF):
    """
    Description de la fonction : réalise une conversion °F en °C
    tF (int) : temperature en farenheit
    return (None) :   
    """
    tC = (tF - 32) * 5/9
    print(str(tF)+'°F équivaut à '+str(tC)+'°C')
    
farenheitToCelsius(20)
help(farenheitToCelsius)

#exos 6

def calcul_cle(num_secu_sans_cle):
    """
    description de la fonction: calcul la cle du numero de securite sociale
    num_secu_sans_cle(int): le numero de securite sociale sans la cle
    return(None):
    """
    cle = num_secu_sans_cle % 97
    cle = 97 - cle
    print(cle)
calcul_cle(2690549588157)
help(calcul_cle)