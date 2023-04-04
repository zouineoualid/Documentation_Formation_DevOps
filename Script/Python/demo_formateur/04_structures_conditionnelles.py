mon_age = int(input("Quel âge as-tu ? "))

if mon_age >= 21:  # La condition évaluée à l'entrée du bloc
    print("Vous êtes majeur aux USA, vous pouvez entrer !")
elif mon_age >= 18: # La condition évaluée si la condition précédente n'est pas vraie
    print("Vous êtes majeur en France, vous pouvez entrer !")
elif mon_age < 0: # La condition évaluée si la condition précédente n'est pas vraie
    print("Age Invalide !")
else:  # Le chemin par défaut si aucune condition n'est bonne
    print("Vous êtes mineur, retournez en arrière !")

print("Fin")




if True:
    pass
elif True:
    if True:
        pass
    else:
        pass
if True:
    pass