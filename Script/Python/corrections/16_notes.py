def saisie_note_0_20():
    note = float(input("Saisir une note : "))
    while note < 0 or note > 20:
        note = float(input("Erreur! Saisir une note : "))
    return note


def saisie_nombre_notes():
    nombre = int(input("Combien de notes voulez-vous ? ")) # possible d'ajouter un contrôle de saisie
    liste_notes = []
    for note in range(nombre):
        liste_notes.append(saisie_note_0_20())
    return liste_notes


def saisie_notes_negatif_stop():
    liste_notes = list()
    while True:
        note = float(input("Saisir une note : "))
        if note < 0 or note > 20: # si la note n'est pas correcte, on sort de la saisie
            print("Note erronée, on arrête la saisie")
            return liste_notes
        liste_notes.append(note)


def saisie_notes_menu():
    while True:
        print("[1] Pour entrer un nombre de note connu\n[2] Pour continuer la saisie jusqu'a une note negative")
        choix = input("Votre choix : ")
        match choix:
            case "1":
                return saisie_nombre_notes()
            case "2":
                return saisie_notes_negatif_stop()
            case _:
                print("Votre choix ne correspond pas, réésayez !")



def menu_min_max_moy(liste_notes):
    while True:
        print("Faites votre choix :")
        print("1 - Afficher note minimale")
        print("2 - Afficher note maximale")
        print("3 - Afficher moyenne")
        print("4 - Quitter programme")
        choix = input("Votre choix : ")

        if choix in "1234" and len(choix) == 1:
            match choix:
                case "1":
                    print("Note min :", min(liste_notes))
                case "2":
                    print("Note max :", max(liste_notes))
                case "3":
                    print("Moyenne :", sum(liste_notes)/len(liste_notes))
                    # import statistics
                    # statistics.mean(liste_notes)
                case "4":
                    return
        else:
            print("Erreur, réessayez !\n")




def main():
    liste_notes = saisie_notes_menu()
    menu_min_max_moy(liste_notes)
    

if __name__ ==  '__main__':
    main()
