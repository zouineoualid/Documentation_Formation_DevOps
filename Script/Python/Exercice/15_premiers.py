def premiers_jusqua_max(maximum):               # on définit une fonction pour 'compter' les premiers
    premiers = []                           # on initialise notre liste de premiers à vide
    for nombre in range(1, maximum + 1):        # on itère sur tout les nombres
        nombre_est_premier = True           # on estime que le nombre est premier tant qu'on a pas trouvé un diviseur
        for diviseur in range(2, nombre):   # on itère sur tout les nombres inférieurs à nombre sauf 1 (car nombre est toujours divisible par 1 et par lui même)
            if nombre % diviseur == 0:      # est-ce que 'diviseur' est un diviseur de nombre
                nombre_est_premier = False  # si oui, nombre n'est pas premier
                break                       # donc on sort de la boucle
        if nombre_est_premier:              # si le booleen est resté à True
            premiers.append(nombre)         # le nombre est premier donc on l'ajoute à la liste
    return premiers                         # enfin on retourne la liste

def main():
    max = int(input("Quelle est la valeur du nombre maximal ? "))
    premiers = premiers_jusqua_max(maximum=max)

    for preums in premiers:
        nb_espaces = premiers.index(preums) + 1 # on calcule le nombre d'espace à l'aide de l'index de l'élément
        print(" " * nb_espaces + str(preums))

    for i in range(len(premiers)):
        print(" " * i, premiers[i])

    for index, preums in enumerate(premiers):
        print(" " * index, preums)
    
    # for i in range(len(premiers)):
    #     print(" " * i, premiers.pop(0))

if __name__ == '__main__':
    main()


# 2e solution avec une fonction pour vérifier chaque nombre à part

def is_prime(num):
    if num <= 1:
        return False
    for diviseur in range(2, num):
        if num % diviseur == 0:
            return False
    return True


def get_all_primes(max):
    list_prime = [1,]

    for nombre in range(1, max + 1):
        if is_prime(nombre):
            list_prime.append(nombre)

    return list_prime


def main():
    max = int(input("Quel est la valeur du nombre maximal ? "))
    list_primes = get_all_primes(max)
    for i in range(0, len(list_primes)):
        print(' '*i, list_primes[i])


if __name__ == "__main__":
    main()





# Program to check if a number is prime or not
def prime(num): 
    # define a flag variable
    flag = True
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                # break out of loop
                break
    return flag


def list_premiers(entier):
    liste =[ x for x in range(1,entier) if prime(x)]
    return liste


n = int(input("\nveillez saisir votre range = \t"))
ma_liste= list_premiers(n)

for index, element in enumerate(ma_liste):
    print( " "*index ,element )