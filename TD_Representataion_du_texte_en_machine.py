#exercice 10

def est_un_chiffre(chiffre):
    return ord(chiffre) >= 48 and ord(chiffre) <= 57
print(est_un_chiffre('6'))
print(est_un_chiffre('e'))

def en_majuscule(lettre):
    return chr(ord(lettre) - 32)
print(en_majuscule('a'))