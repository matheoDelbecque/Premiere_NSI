#exercice 4

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
    
taille_fichier(3)
help(taille_fichier)

#exercice 5

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