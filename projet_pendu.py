from random import randint
LETTRE_DEJA_CHOISIES = []

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
    return chaine

def deja_choisie(lettre):
    global LETTRES_DEJA_CHOISIES
    if lettre in LETTRE_DEJA_CHOISIES:
        print("lettre déjà choisie")
        return True
    else:
        LETTRE_DEJA_CHOISIES = LETTRE_DEJA_CHOISIES + [lettre]
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
    if score == 0:
        print("Vous avez perdu !!\nLe mot recherché était",MOT_A_DECOUVRIR)
    else:
        print("Bravo! Vous avez trouvé le mot",MOT_A_DECOUVRIR,"\nVotre SCORE est de",SCORE)
        
def remplace_tiret(lettre):
    global MOT_MYSTERE
    global MOT_A_DECOUVRIR
    for i in range(len(MOT_A_DECOUVRIR)):
        if lettre == MOT_A_DECOUVRIR[i]:
           MOT_MYSTERE = MOT_MYSTERE[0:i] + lettre + MOT_MYSTERE[i+1:len(MOT_MYSTERE)+1]
           resultat = True
        else:
           resultat = False
    return
