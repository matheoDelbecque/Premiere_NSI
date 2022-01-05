import devis

# les données communiquées au peintre sur les dimensions de la pièce à restaurer
longueur = 7.8 # en m
largeur = 6.6 # en m

# les données communiquées par le peintre sur le descriptif des articles (coût unitaire, pouvoir couvrant)
cout_pot = 37.9 # en euros
cout_bache = 0.95 # en euros
cout_ruban = 2.85 # en euros
surface_couvrante_pot = 13 # en m²
surface_couvrante_bache = 12 # en m²
longueur_couvrante_ruban = 5 # en m

# les données à détailler
nb_pots = devis.nombre_pots(longueur,largeur,surface_couvrante_pot) # TODO : Utiliser le retour de la fonction nombre_pots ?
nb_baches = devis.nombre_baches(longueur,largeur,surface_couvrante_bache)# TODO : Utiliser le retour de la fonction nombre_baches ?
nb_rubans = devis.nombre_rubans(longueur,largeur,longueur_couvrante_ruban) # TODO : Utiliser le retour de la fonction nombre_rubans ?
salaire = devis.salaire(longueur,largeur) # TODO : Utiliser le retour de la fonction salaire ?

total = nb_pots * cout_pot + nb_baches * cout_bache + nb_rubans * cout_ruban + salaire

print("+------------------+----------+--------+")
print("+     Article      + Quantité +  Coût  +")
print("+------------------+----------+--------+")
print("+ Pots de peinture + ", '%6s' % str(nb_pots), " + ", '%5s' % str(nb_pots * cout_pot), "+")
print("+ Bâches           + ", '%6s' % str(nb_baches), " + ", '%5s' % str(nb_baches * cout_bache), "+")
print("+ Rubans           + ", '%6s' % str(nb_rubans), " + ", '%5s' % str(nb_rubans * cout_ruban), "+")
print("+ Salaire          +          + ", '%5s' % str(round(salaire, 2)), "+")
print("+------------------+----------+--------+")
print("+ Total            +          + ", '%5s' % str(round(total, 2)), "+")
print("+------------------+----------+--------+")
print("Est-ce que le forfait assurance de 500€ couvre les dépenses ?", devis.est_reparation_couverte(total))