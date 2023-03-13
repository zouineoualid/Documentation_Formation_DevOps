# Concaténation
str1 = "chaine 1"
str2 = "chaine 2"
str3 = "str1 : " + str1 + ", str2 : " + str2
print(str3)

#le print ajoute des espaces entre les arguments par défaut !
print(str1 + str2)
print(str1 + " " + str2)
print(str1, str2)

# concaténation avec un entier
mon_entier = 12
debut = "J'ai "
fin = " ans."
print(debut + str(mon_entier) + fin) #obligation de passer par le cast (transtypage)
print(debut + "mon_entier" + fin)
print(debut, mon_entier, fin)


# Chaines formatées
# "...".format(...)
prenom_enfant = "Titouan"
ma_chaine_formatee = "J'ai {0} ans et je m'appelle {1} (age = {0}) {2}".format(mon_entier, prenom_enfant, "Bonjour tout le monde !")
print(ma_chaine_formatee)
# f-string
ma_chaine_formatee2 = f"J'ai {mon_entier+20} ans et je m'appelle {prenom_enfant}"
print(ma_chaine_formatee2)


# Caractères spéciaux

# retour à la ligne \n
chaine = "Ligne 1\nLigne 2\nLigne 3"
print(chaine)
# equivalent :
chaine = """Ligne 1
Ligne 2
Ligne 3"""
print(chaine)

# tabulation \t
chaine = "Ligne 1\n\tLigne 2\n\t\tLigne 3"
print(chaine)

# pour les guillemets, il faut les échapper avec le \
chaine = "l'alouette"
print(chaine)
chaine = 'l\'alouette'
print(chaine)

chaine = 'il a dit "salut" '
print(chaine)
chaine = "il a dit \"salut\" "
print(chaine)

# écrire des {}
print(f"{{ test }}")

# Découpage de chaines
#         012345678
chaine = "abcdefghi"

# Récupérer un seul caractère avec son indice
print(chaine)
print(chaine[0])
print(type(chaine[6]))
print(chaine[0] + chaine[6])


# Découper une chaine avec un début et une fin
# chaine[<debut>:<fin-1>]
print(chaine[0:4])
print(chaine[:4])
print(chaine[2:4] + chaine[6:])

# Découper avec un pas    
# chaine[<début>:<fin-1>:<pas>]
print(chaine[::2])
print(chaine[::3])
print(chaine[:2:2])

# Découper avec des NEGATIF
#         012345678
chaine = "abcdefghi"
print(chaine[-3:])
print(chaine[:-3])
print(chaine[-5:-2])


# avec un pas négatif
print(chaine[::-1])
print(chaine[::-2])

