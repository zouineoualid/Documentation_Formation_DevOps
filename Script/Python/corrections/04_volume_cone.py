from math import pi


hauteur = float(input("Saisir le hauteur d'un cone : "))
rayon = float(input("Saisir le rayon d'un cone : "))
volume = pi * rayon**2 * hauteur / 3
print(f"volume : {round(volume,2)}") # arrondi à 2 chiffres après la virgule

print(f"volume : {volume:.2f}") # méthode d'affichage spéciale du f-string



# f"   {variable:7,2f}    "
# variable => de type float car on a mis 'f' à la fin
# 7 => nombre de caractère total minimum (avec la virgule et les décimales) réservé pour notre affichage,
#      si moins on mets des espaces avant
# 2 => nombre de chiffres après la virgule
#      on arrondi ou on ajoute des zéros


variable = 55.2091

print(f".{variable:7.5f}.")
print(f".{variable:7.2f}.")
print(f".{variable:7.1f}.")
print(f".{variable:<7.0f}.")


variable = "texte"

print(f".{variable:<9}.")
print(f".{variable:^9}.")
print(f".{variable:>9}.")