# # n = 10
# # m = 10
# # a = [[0] * m] * n
# # T=np.arange(n)
# # #print(a)
# # for i in range(len(T)):
# #         print(T[i], end='                 ')
# # print()
# # print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
# # for i in range(len(a)):
# #     for j in range(len(a[i])):
# #         a[i][j]=i*j
# #         print(a[i][j], end='                 ')
# #     print()

# # multiplicateur = int(input("nombre de table de multiplication ? "))

# # for i in range (0,multiplicateur):
# #     print(i, end=" ")

# import random
# hauteur = int(input("Quelle est la hauteur de votre sapin de Noël ? "))
# nb_espace = hauteur - 1
# nb_stars = 1
# tronc_sapin = ("||")
# nb_tronc_sapin = int(input("Quelle est la hauteur du tronc de votre sapin de Noël ? "))
# gift_left = ("█ █ █")
# gift_right = ("█ ■ █")
# while hauteur <= 0:
#     hauteur = int(input("Saisie incorrect, Veuillez saisir une valeur correct svp : "))
# while nb_tronc_sapin <= 0:
#     hauteur = int(input("Saisie incorrect, Veuillez saisir une valeur correct svp : "))
# for i in range(0 , hauteur):
#     print(nb_espace*" " + nb_stars*"*")
#     nb_espace -= 1
#     nb_stars += 2
# for t in range(0, nb_tronc_sapin):
#     print(tronc_sapin.center(nb_stars-2))
# print(f"{gift_left} {gift_right:>12}")

#Fonction : Vérifier la chaine de caractère saisie
def valide_input (adn):
    authorize_input=["a","t","g","c"]
    for i in range(len(adn)):
        if adn[i] not in authorize_input:
            return False
    return True
# Fonction : Saisie de caractère correspondant à une chaine d'ADN
def adn_input():
    p=input("Pouvez-vous saisir la chaine d'ADN ? : ")
    p=p.lower()
    if valide_input == False:
        return "False"
    return p
#Fonction : Séquencage des ADN
def sequence_adn(adn, sequence_adn):
    s = adn.count(sequence_adn)
    return((s/(len(adn)))*100)    
#Fin saisie des fonction
#----------------------------------------------------------------------------------------------------------------------------#
#Debut programme
adn=result_1=adn_input()
sequence=input("Pouvez-vous donner la sequence à vérifier : ")
result=valide_input(adn)
result_2=sequence_adn(adn,sequence)  
print(result_1)
print(result) 
print(result_2)
#Fin programme