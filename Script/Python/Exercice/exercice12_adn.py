#Fonction : Vérifier la chaine de caractère saisie
def valide_input (adn):
    authorize_input=["a","t","g","c"]
    for i in range(len(adn)):
        if adn[i] not in authorize_input:
            return "Erreur de saisie !!!!"
    return (adn)
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
result_1=adn_input()
adn=result_1
sequence=input("Pouvez-vous donner la sequence à vérifier : ")
result=valide_input(adn)
result_2=sequence_adn(adn,sequence)  
print(result)
print(sequence) 
print(f"il y a {result_2} % de {sequence} dans {result_1}")
#Fin programme