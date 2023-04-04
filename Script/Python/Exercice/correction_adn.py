def adn_est_valide(chaine_adn_dans_fonction):
    # on retourne False si on trouve une erreur
    for chainon in chaine_adn_dans_fonction:
        if chainon not in "actg": #si le chainon est dans la chaine_adn
            return False
    return True
    # Exemples d'utilisation :
    # print(adn_est_valide("abecededeg")) False
    # print(adn_est_valide("agtctgatgta")) True


def saisie_dune_chaine_adn(question):
    # input de chaine --> mettre en minuscule pour autoriser les saisies du style ACtgAgTTA
    ma_chaine_adn = input(question)
    ma_chaine_adn = ma_chaine_adn.lower() # chaine_adn = input("saisir votre chaine : ").lower() # possible de faire le .lower() directement ici
    
    #vérification la chaine, ressaisie si fausse
    while not adn_est_valide(ma_chaine_adn): # ==> adn_est_valide(chaine_adn) == False
        print("Erreur de saisie !!!")
        ma_chaine_adn = input(question).lower()

    #on la retourne dés lors qu'elle est bonne
    return ma_chaine_adn


def occurences_sequence(sequence_adn, chaine_adn):
    return chaine_adn.count(sequence_adn)


def poucentage_sequence(nb_occurences_sequence, sequence, chaine):
    return nb_occurences_sequence * len(sequence) / len(chaine) * 100

    # possible de combiner les 2 fonctions en une seule
    # return chaine_adn.count(sequence_adn) * len(sequence) / len(chaine) * 100


def main():
    #saisir la chaine adn
    chaine_adn = saisie_dune_chaine_adn("Veuillez saisir une chaine adn : ")
    #saisir la séquence
    sequence_adn = saisie_dune_chaine_adn("Veuillez saisir une séquence adn : ")

    #on les affiche
    print("chaine :", chaine_adn)
    print("sequence :", sequence_adn)

    #calculs 
    # occurences de la sequence
    occurence = occurences_sequence(sequence_adn, chaine_adn)
    # print(occurence)

    # proportion de la sequence
    pourcentage = poucentage_sequence(occurence, sequence_adn, chaine_adn)
    # print(pourcentage)

    #affichage des résultats
    print(f"Il y a {pourcentage}% de \"{sequence_adn}\" dans la chaine \"{chaine_adn}\"")


if __name__ == "__main__":
    main()
