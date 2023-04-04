def verif(chaine_dans_fonction):
    for caractere in chaine_dans_fonction:
        if caractere not in "actg":
            return False
    return True

def main():
    chaine_valide = "actg".lower()
    chaine_invalide = "befhijklmnopqrsuvwxyz".lower()
    est_valide = verif(chaine_valide)
    print(est_valide)
    est_valide = verif(chaine_invalide)
    print(est_valide)

if __name__ == '__main__':
    main()

######################

adn_input = main()

print(adn_input)

