#Fonction - voir nom de famille
def see_last_name(set_example):
    print(set_example)

#Fonction - Ajout nom de famille
def add_last_name(set_example):
    last_name = input("Pouvez-vous rentrer le nom de famille à ajouter : ")
    set_example.add(last_name.upper())

#Fonction - modifier un nom de famille du set
def modif_last_name(set_example):
    last_name_modif = input("Pouvez-vous rentrer le nom de famille à modifier: ")
    last_name_new = input("Pouvez-vous rentrer le nom de famille modifié: ")
    if last_name_modif.upper() in set_example:
        set_example.discard(last_name_modif.upper())
        set_example.add(last_name_new.upper())
    else:
        print("Le nom de famille rentré n'existe pas dans la liste : retour au menu")

#Fonction - supprimer un nom de famille du set
def discard_last_name(set_example):
    discard_name = input("Pouvez-vous rentrer le nom de famille à supprimer : ")
    if discard_name.upper() in set_example:
        set_example.discard(discard_name.upper())
    else:
        print("Le nom de famille à supprimer n'est pas dans la liste : retour au menu")

#Fonction - Fonction main qui englobe l'exécution du menu : 
def main():
    #variable utilisé par le programme : 

    last_name_set = set()    #Set définie dans la fonction

    #Menu utilisateur

    while True:
        print("""=== MENU PRINCIPAL ===
        1 - Voir les noms de famille
        2 - Ajouter un nom de famille
        3 - Editer un nom de famille
        4 - Supprimer un nom de famille
        0 - Quitter le programme""")
        choix_user = input("votre choix 1|2|3|4|0 : ")
        if (choix_user == '1'):
            see_last_name(last_name_set)
        elif (choix_user == '2'):
            add_last_name(last_name_set)
        elif (choix_user == '3'):
            modif_last_name(last_name_set)
        elif (choix_user == '4'):
            discard_last_name(last_name_set)
        elif (choix_user == '0'):
            print("Au revoir !")
            break
        else:
            print("Erreur, réessayez")

if __name__ == "__main__":
    main()