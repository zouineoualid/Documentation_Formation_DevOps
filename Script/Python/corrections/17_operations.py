def operations(nombre1, nombre2): #on définit la fonction
    addition = nombre1 + nombre2
    soustraction = nombre1 - nombre2
    multiplication = nombre1 * nombre2
    division = nombre1 / nombre2 
    tuple_operations = (addition, soustraction, multiplication, division) #parenthèse facultatives
    return tuple_operations

def operations(nombre1, nombre2): #celle-ci porte le même nom --> on redéfinit la fonction précédente
    addition = nombre1 + nombre2
    soustraction = nombre1 - nombre2
    multiplication = nombre1 * nombre2
    division = nombre1 / nombre2 
    return addition, soustraction, multiplication, division

#définition de fonction
def operations(nombre1, nombre2): #celle-ci porte encore le même nom --> on redéfinit la fonction précédente
    return nombre1 + nombre2, nombre1 - nombre2, nombre1 * nombre2, nombre1 / nombre2 

# appel de fonction
# operations(2, 3)
# la valeur 2 ira dans le paramètre nombre1
# la valeur 3 ira dans le paramètre nombre2

def saisie_2_nombres():
    return int(input(" veuillez saisir un premier nombre : ")), int(input(" veuillez saisir un deuxième nombre : "))

# méthode classique
# nb1 = int(input(" veuillez saisir un premier nombre : "))
# nb2 = int(input(" veuillez saisir un deuxième nombre : "))

# méthode avec unpacking
# nb1, nb2 = int(input(" veuillez saisir un premier nombre : ")), int(input(" veuillez saisir un deuxième nombre : "))

# méthode avec unpacking et appel de fonction
nb1, nb2 = saisie_2_nombres()


#on passe par un tuple intermédiaire avant d'unpack
mon_tuple = operations(nb1, nb2) #ici on envoit le 'contenu' de nb1 et nb2 dans la fonction
print(mon_tuple)
add, sub, mul, div = mon_tuple #unpack du tuple

# unpack direct
add, sub, mul, div = operations(nb1, nb2)

# correspond à (sans fonction)
add, sub, mul, div = nb1 + nb2, nb1 - nb2, nb1 * nb2, nb1 / nb2

print("L'addition de vos deux nombre donne ", add)
print("La soustraction de vos deux nombre donne ", sub)
print("La multiplication de vos deux nombre donne ", mul)
print("La division de vos deux nombre donne ", div)

# equivalent :
print("L'addition de vos deux nombre donne ", mon_tuple[0])
print("La soustraction de vos deux nombre donne ", mon_tuple[1])
print("La multiplication de vos deux nombre donne ", mon_tuple[2])
print("La division de vos deux nombre donne ", mon_tuple[3])