import os
# import os.path as p


file_path = "./demos/08_fichiers/fichier2.txt"
# file_path = "./fichier1.txt"

# os.path.pathsep # variable avec le séparateur dans le path ("/" ou "\")

if os.path.exists(file_path):
    file = open(file_path, "r", encoding="UTF-8") # ouvrir le fichier en lecture ("r")
    print(file.readline()) # lire la première ligne (contient le retour à la ligne aussi)
    print('test')
    print(file.readlines()) # lire les lignes (à partir du curseur) et en faire une liste de chaines
    file.seek(0) # Déplacer le curseur à un certain caractère (toujours caractère-1)
    print(file.read()) # Lire toute la suite du fichier à partir du curseur
    file.close()
else:
    file = open(file_path, 'w', encoding="UTF-8") # Ecrire et ecraser le fichier 
    # UTF-8 -> ajoute les caractères complexes : ç, accents, ¿, 😎, ...
    # ASCII -> caractères basiques
    file.write("Primera linea del fichero\n") # J'écris une ligne dans mon fichier
    file.close()

    file = open(file_path, 'a', encoding="UTF-8") # Ajouter au fichier (à la fin)
    file.writelines(['Seconde Ligne\n', 'Troisième ligne']) # J'écris plusieurs lignes dans mon fichie
    file.close()


# /!\ ne pas oublier l'encoding du fichier pour éviter les erreurs avec certains caractères


# exemple avec du binaire
file = open(file_path, "rb")
print(file.read())
file.close()




file = open(file_path, "r", encoding="UTF-8") 
print(file.read())
file.close()

# au lieu d'appeler le file.close(), il est possible d'utiliser le bloc with
# cela permet de s'assurer que notre fichier est bien fermé à la fin du bloc 
with open(file_path, "w", encoding="UTF-8") as mon_fichier: # ici 'as' met le résultat de open() dans la variable mon_fichier
    print(mon_fichier)




# with 4 as entier: # ne fonctionne pas car 4 ne peut pas être "ouvert" ou "entré" (__enter__())
#     print(entier)