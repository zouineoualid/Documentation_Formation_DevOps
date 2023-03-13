# # on crée un liste avec des crochets []
# ma_liste = [
#     1,
#     2,
#     3,
#     'test',
#     True,
#     ['a', True, 25.]
# ]
# # equivalent sur une ligne : ma_liste = [1, 2, 3, 'test', True, ['a', True, 25.]]
# print(ma_liste)

# # afficher un élément de la liste (elle commence à l'index 0)
# print(ma_liste[0])
# print(ma_liste[5])

# # si on veut afficher un élément de la liste contenue dans la première
# print(ma_liste[5][2])

# ma_2e_liste = ma_liste[5]
# print(ma_2e_liste[2])

# # Modifier un élément à un index précis
# # ma_liste[6] = "test" # --> la liste n'est pas assez grande donc erreur
# ma_liste[0] = 80
# print(ma_liste)


# ma_liste = [1, 4, 5, 2, 3, ]
# # pour trier une liste on utilise la methode .sort()
# ma_liste.sort()
# print(ma_liste)
# ma_liste.sort(reverse=True) # par défaut false
# print(ma_liste)

# ma_liste = ["a","1", "ab", "A", "!", "?", ""]
# ma_liste.sort()
# print(ma_liste)

# # pour trier une liste on peut aussi utiliser la fonction sorted()
# # donne une nouvelle liste triée mais ne change pas ma_liste
# ma_liste = ["a","1", "ab", "A", "!", "?", ""]
# ma_liste2 = sorted(ma_liste)
# print(ma_liste2)
# print(ma_liste)

# # pour ajouter à la liste, on peut utiliser la méthode .append() (à la fin)
# ma_liste = [1, 4, 5, 2, 3, ]
# ma_liste.append(30)
# print(ma_liste)

# # pour ajouter à un index précis, on utilise la méthode .insert(index, élément)
# ma_liste.insert(2, 6)
# print(ma_liste)

# #pour ajouter une liste à la suite d'une autre 
# ma_liste = [1, 4, 5, 2, 3, ]
# ma_liste.extend(["Test", True])
# print(ma_liste)
# print(len(ma_liste))

# # /!\ si on utilise append, on ajoutera la 2e liste DANS la première (en temps qu'élément)
# ma_liste = [1, 4, 5, 2, 3, ]
# ma_liste.append(["Test", True])
# print(ma_liste)
# print(len(ma_liste))

# # pour retirer un élément avec son index et renvoyer l'élément
# print(ma_liste.pop(4))
# print(ma_liste)

# # pour retirer un élément avec son contenu (la première qui correspond)
# ma_liste.remove(4)
# print(ma_liste)


# # pour itérer sur une liste
# for element in ma_liste:
#     print(element)

# for element in ma_liste:
#     print(element)
#     if isinstance(element, list): # si l'élément est de type liste
#         print("Sous éléments de la liste : ")
#         for element2 in element: 
#             print(" -", element2) #on affiche chacun de ses sous-éléments
        

# for index, element in enumerate(ma_liste):
#     print(index, "=>", element)

# print(enumerate(ma_liste))
# print(list(enumerate(ma_liste)))

# #cast de range vers list
# liste = list(range(1, 11))
# print(liste)


# List comprehension
liste_a = []
for x in range(1, 11):
    liste_a.append(x)
print(liste_a)

liste_a = [x for x in range(1, 11)]
print(liste_a)


# Il est possible d'altérer l'entrée de l'itérateur
# en modifiant l'expression à gauche de la list comprehension
liste_b = [(x ** 2) for x in range(1, 11)]
liste_b = [x ** 2 for x in range(1, 11)] # pareil mais les parenthèses peuvent aider à se reperer
print(liste_b)


# Il est également possible de filter les valeurs, équivalent à un filter()
liste_d = [x for x in range(1, 11) if x % 2 == 0]
print(liste_d)

# équivalent
liste_a = []
for x in range(1, 11):
    if x % 2 == 0:
        liste_a.append(x)
print(liste_a)


liste_a = [x for x in range(1, 11)]
for element in liste_a:
    print("element :", element)
    print("son index :", liste_a.index(element))
    
print("L'élément 9 est à l'index :", liste_a.index(9))


liste_a = [[y for y in range(x)] for x in range(1, 11)]

print(liste_a)

for liste in liste_a:
    print(liste)



