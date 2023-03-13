#print classique
print("Hello World !")
print('hello world !')

#print avec la syntaxe longue du str
print("""test

test

              test""")

# print multiple (avec plusieurs arguments séparés par des virgules)
print(1, "ma chaine", 3.14)
print()

# une variable
ma_variable = 456
print(ma_variable)

# Si je veux commenter j'utilise le #
# Si je veux commenter plusiquer lignes, j'utilise "ctrl + K + C"
# Si je veux décommenter plusiquer lignes, j'utilise "ctrl + K + U"
# Si je veux commenter et/ou décommenter plusiquer lignes, j'utilise "ctrl + :"

# les variables numériques
var = 23 # int
print(type(var))
var = 23.0 # float
print(type(var))
var = 23. # float
print(type(var))

# variable chaine de caractères
var = "23.0" # str
print(type(var))

# variable booléenne
mon_bool = True
print(mon_bool)
print(type(mon_bool))
mon_bool = False
print(mon_bool)
print(type(mon_bool))


print(4 < 5)
print(4 > 5)
print(4 <= 5)
print(5 <= 5)
print(4 >= 5)
print(5 >= 5)
print(5 == 5)
print(5 != 5)

# input vide avec un print avant
print("saisir un entier")
var = input()
print(type(var))
print(var)
mon_entier = int(var)
print(type(mon_entier))
print(mon_entier)

# input avec argument (saisie sur la même ligne)
variable = input("Saisir quelque chose : ")
print(type(variable))
print(variable)