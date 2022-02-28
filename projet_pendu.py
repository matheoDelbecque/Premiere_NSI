from random import randint
SCORE = 8
LETTRES_DEJA_CHOISIES = []

def nettoyage_mot(mot):
    mot = mot.lower()
    mot = mot[0:len(mot)-1]
    accent = ['é','è','ê','ë','à','â','ù','û','ç','ô','ï','î']
    sans_accent = ['e','e','e','e','a','a','u','u','c','o','i','i']
    i = 0
    while i < len(accent):
        mot = mot.replace(accent[i], sans_accent[i])
        i = i + 1
    return mot

def tirage_au_sort(nom_fichier):
    fichier = open(nom_fichier,'r', encoding = 'utf8')
    for chiffre in range(randint(1,22274)):
        chaine = fichier.readline()
    fichier.close()
    return nettoyage_mot(chaine),'-'*len(nettoyage_mot(chaine))

def deja_choisie(lettre):
    global LETTRES_DEJA_CHOISIES
    if lettre in LETTRES_DEJA_CHOISIES:
        print("lettre déjà choisie")
        return True
    else:
        LETTRES_DEJA_CHOISIES = LETTRES_DEJA_CHOISIES + [lettre]
        return False

def jeu_fini():
    global SCORE
    global MOT_MYSTERE
    global MOT_A_DECOUVRIR
    if SCORE == 0 or MOT_MYSTERE == MOT_A_DECOUVRIR:
        return True
    else:
        return False

def afficher_bilan():
    global SCORE
    global MOT_A_DECOUVRIR
    if SCORE == 0:
        print("Vous avez perdu !!\nLe mot recherché était",MOT_A_DECOUVRIR)
    else:
        print("Bravo! Vous avez trouvé le mot",MOT_A_DECOUVRIR,"\nVotre SCORE est de",SCORE)
        
def remplace_tiret(lettre):
    global MOT_MYSTERE
    global MOT_A_DECOUVRIR
    global SCORE
    for i in range(len(MOT_A_DECOUVRIR)):
        if lettre == MOT_A_DECOUVRIR[i]:
           MOT_MYSTERE = MOT_MYSTERE[0:i] + lettre + MOT_MYSTERE[i+1:len(MOT_MYSTERE)]
           resultat = True
        else:
           resultat = False
    if lettre in MOT_A_DECOUVRIR:
        pass
    else:
        SCORE = SCORE - 1
    return resultat

def jouer():
    global MOT_A_DECOUVRIR
    global MOT_MYSTERE
    global SCORE
    global LETTRES_DEJA_CHOISIES
    res = tirage_au_sort('dictionnaire.txt')
    MOT_A_DECOUVRIR = res[0]
    MOT_MYSTERE = res[1]
    print("-------------------------\nBIENVENUE AU JEU DU PENDU\n-------------------------")
    while jeu_fini() == False:
        print("\nMot à découvrir :", MOT_MYSTERE)
        lettre = input("proposez une lettre : ")
        deja_choisie(lettre)
        remplace_tiret(lettre)
        print()
    afficher_bilan()

jouer()
