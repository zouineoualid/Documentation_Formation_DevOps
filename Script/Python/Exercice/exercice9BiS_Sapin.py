import random

hauteur = int(input("Quelle est la hauteur de votre sapin de Noël ? "))
nb_espace = hauteur - 1
nb_stars = 1
tronc_sapin = ("||")
nb_tronc_sapin = int(input("Quelle est la hauteur du tronc de votre sapin de Noël ? "))
gift_left = ("█ █ █")
gift_right = ("█ ■ █")

while hauteur <= 0:
    hauteur = int(input("Saisie incorrect, Veuillez saisir une valeur correct svp : "))

while nb_tronc_sapin <= 0:
    hauteur = int(input("Saisie incorrect, Veuillez saisir une valeur correct svp : "))
 
for i in range(0 , hauteur):
    print(nb_espace*" " + nb_stars*"*")
    nb_espace -= 1
    nb_stars += 2

for t in range(0, nb_tronc_sapin):
    print(tronc_sapin.center(nb_stars-1))

print(f"{gift_left} {gift_right:>12}")