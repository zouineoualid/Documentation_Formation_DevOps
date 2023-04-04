#Variable programme

#note_temp = int(input("Pouvez vous saisir une note entre 0 et 20 ? : "))
table_note = []
total_note_temp = sum(table_note)
nb_student = 0

#Boucle saisie des données aléatoire

while True:
    note_temp = int(input("Pouvez vous saisir une note entre 0 et 20 ? : "))
    if note_temp >= 0:
        table_note.append(note_temp)
        nb_student = nb_student + 1
    else :
        print("erreur")
        break

print(table_note)
print(sum(table_note))
print(nb_student)


while True:
    print("""Sélectionner un menu :
    1 - Afficher la meilleure des notes
    2 - Afficher la note la plus basse
    3 - Afficher la moyenne des notes
    4 - Sortir du programme""")
    choix_user = input("votre choix 1|2|3 : ")
    if (choix_user == '1'):
       print(max(table_note))
    elif (choix_user == '2'):
        print(min(table_note))
    elif (choix_user == '3'):
        print(total_note_temp/nb_student)
    elif (choix_user == '4'):
        print("Au revoir !")
        break
    else:
        print("Erreur, réessayez")