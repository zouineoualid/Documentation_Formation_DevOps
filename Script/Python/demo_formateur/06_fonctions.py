# Définition de la fonction
def test():
    print("Hello World !")

# Appel(s) de la fonction
test()
# test()



def bonjour_qui(nom):
    print(f"Bonjour {nom}!")

bonjour_qui("Guillaume")
# bonjour_qui("Jose")
# bonjour_qui(10)
# bonjour_qui(True)


def bonjour_jose_par_defaut(nom="Jose"):
    print(f"Bonjour {nom}!")
    
bonjour_jose_par_defaut()
bonjour_jose_par_defaut("au fils de Charles")

def je_fais_une_addition(a,b):
    print('j\'additionne...')
    print(f"{a}+{b}={a+b}")
    return a+b

print(je_fais_une_addition(1,1)+40)
c = je_fais_une_addition(50,41)
print("c=" + str(c))


# /!\ GESTION DES VARIABLES GLOBALES DANS LES FONCTIONS

# a est une variable globale au programme
a = 10

def test():
    print(a)  # a est la variable globale (Mauvaise pratique !!!)

test()


def test2(a):
    print(a) # a est le paramètre de la fonction

test2(6) 


def test3():
    a = 20 # a est modifié dans la fonction mais la variable globale ne change pas !
    print(a)

test3()
print(a)

def test4():
    global a
    a = 300 # la variable globale est modifiée grace au mot clé global
    print(a)

test4()
print(a)


def concatenation():
    global ma_variable # définie gloabalement dans le programme
    ma_variable = "test"

#print(ma_variable) # pas encore défini --> erreur
concatenation()
print(ma_variable)

def fonction_vide():
    pass # pass ne fait RIEN
    # pas de return == return None

def fonction_vide2():
    return #return seul == return None

def fonction_vide3():
    return None


print(fonction_vide())
print(fonction_vide2())
print(fonction_vide3())

# fonction qui retourne une chaine selon si un nombre est pair ou impair 
def return_oui_si_pair(entier):
    if entier%2 == 0:
        return "oui"
    print("l'entier est impair")
    return "non"


print(return_oui_si_pair(3))
print(return_oui_si_pair(2))


def ma_fonction(mon_premier_parametre, mon_deuxieme_parametre):
    ma_chaine_concatenee = mon_premier_parametre + mon_deuxieme_parametre
    return ma_chaine_concatenee

def concatenation(chaine_debut, chaine_fin):
    ma_chaine_concatenee = chaine_debut + chaine_fin
    return ma_chaine_concatenee

chaine1 = ma_fonction("Début ", "fin.")
print(chaine1)
chaine1 = ma_fonction("Il fait beau", " aujourd'hui.")
print(chaine1)

chaine2 = concatenation("Début ", "fin.")
print(chaine2)
chaine2 = concatenation("Il fait beau ", "aujourd'hui.")
print(chaine2)







def addition(a : int, b : int):
    return a + b

# addition("test", 2)
# addition(2.3, 2)
print(addition(2, 2))

chaine = "aBcdEfGghabcde".lower() #.lower() permat de mettre en minuscule si l'utilisateur saisie mal
chaine_verif = "abcd"
for char in chaine: # => pour chaque caratères dans la chaine, faire :
    print(char)
    if char in chaine_verif: