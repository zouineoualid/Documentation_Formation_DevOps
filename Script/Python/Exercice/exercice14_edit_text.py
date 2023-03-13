import os

def lecture_secret():
     file = open(file_path, "r", encoding="UTF-8")
     print(file.read())

def modification_secret():
            modif_secret = input("Quelle est la modification à effectuer ? : ")
            file = open(file_path, "w", encoding="UTF-8")
            file.seek(0)
            file.write(modif_secret)

def break_program():
    file.close()
    print("au revoir ! ")

#Menu user
def show_menu():
    while True:
        print("""faites votre choix : 
        choix 1 : Voir le secret
        choix 2 : Modifier le secret 
        choix 3 : Quitter le programme""")
        choix_user = input("votre choix 1|2|3 : ")
        #read_secret
        if (choix_user == '1'):
            lecture_secret()   
        #modifier_secret    
        elif (choix_user == '2'):
            modification_secret()
        #sortir_programme    
        elif (choix_user == '3') :
            break_program()
            break
        else:
            print("Erreur, réessayez")

#Je défini le chemin d'accès à mon fichier secret
file_path = "./exercice14_folder_text/fichier_secret.txt"

#Je demande à l'utilisateur de saisir un secret contenu dans la variable user_secret
user_secret = input("Secret n'existe pas encore ! Veuillez saisir un 1er secret : ")

#Condition : si le fichier existe, on vient le modifier pour rentrer le secret du user

if os.path.exists(file_path):
    file = open(file_path, "w", encoding="UTF-8")
    file.write(user_secret)
    file.close()

#print(user_secret)


#appelerFonctionMenu
print(show_menu())








###Edit du fichier txt###

# if os.path.exists(file_path):
#     file = open(file_path, "w", encoding="UTF-8")
#     file.write("Je suis sur que tu as 23 ans ")
#     #print(file.readlines())
#     file.close
# else:
#     file = open(file_path, "w", encoding="UTF-8")
#     file.write("Oh Oh Oh tu t'es loupé ! ")
#     print(file.readlines())
#     file.close