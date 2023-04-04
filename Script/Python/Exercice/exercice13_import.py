import correction_adn
def main():
    #saisir la chaine adn
    chaine_adn = correction_adn.saisie_dune_chaine_adn("Veuillez saisir une chaine adn : ")
    #saisir la séquence
    sequence_adn = correction_adn.saisie_dune_chaine_adn("Veuillez saisir une séquence adn : ")
    #on les affiche
    print("chaine :", chaine_adn)
    print("sequence :", sequence_adn)
    #calculs 
    # occurences de la sequence
    occurence = correction_adn.occurences_sequence(sequence_adn, chaine_adn)
    # print(occurence)
    # proportion de la sequence
    pourcentage = correction_adn.poucentage_sequence(occurence, sequence_adn, chaine_adn)
    # print(pourcentage)
    #affichage des résultats
    print(f"Il y a {pourcentage}% de {sequence_adn} dans la chaine {chaine_adn}")

if __name__ == "__main__":
   main()