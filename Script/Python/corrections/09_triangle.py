hauteur = int(input("Saisir la hauteur du triangle : "))

# avec le f-string centré et un peu de maths
for i in range(1, hauteur + 1):
    print(f"{(i - 1) * '**' + '*':^{2 * hauteur -1}}")
    # print(f"{'*' * (2 * i -1):^{2 * hauteur -1}}")

# pareil mais avec des variables
for i in range(1, hauteur + 1):
    nombre_etoiles = 2 * i - 1
    taille_max = 2 * hauteur -1
    print(f"{'*' * (nombre_etoiles):^{(taille_max)}}")

# avec 2 boucles (1 pour les espaces et 1 pour les etoiles)
for ligne in range(1, hauteur+1):
    for espace in range(1, hauteur-ligne+1):
        print(" ", end="")
    for etoile in range(1, 2*ligne):
        print('*', end="")
    print()

# avec uniquement de la la répétion de cracatères 
for i in range(1, hauteur+1):
    print(' ' * (hauteur-i) + "*" * (2 * i - 1))


# avec incrementation et decrementation
nb_espaces = hauteur - 1
nb_etoiles = 1
for ligne in range(hauteur):
    print(nb_espaces * " " + nb_etoiles * '*')
    nb_espaces -= 1
    nb_etoiles += 2