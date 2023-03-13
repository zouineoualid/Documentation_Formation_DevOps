age = int(input("Saisir age : "))
sal = int(input("Saisir salaire minimum demandé : "))
xp = int(input("Saisir années d'expérience : "))

if age < 30:
    print("trop jeune")
elif sal > 40000:
    print("salaire demandé trop élevé")
elif xp < 5:
    print("pas assez d'expérience jeune homme/femme")
else:
    print("Bienvenue dans l'entreprise futur collègue !")


# v2 
# arrêt du programme si un critère ne correspond pas à la saisie

age = int(input("Veuillez entrer votre âge : \n"))
if age < 30 :
    print("Vous n'avez pas l'âge requis pour cette candidature.")
    exit()
salaire = int(input("Salaire demandé \n"))
if salaire > 40000 :
    print("Saisie invalide.")
    exit()
experience = int(input("Combien d'années d'expérience avez-vous ? \n"))
if experience < 5 :
    print("Vous n'avez pas l'expérience requise pour cette candidature.")
    exit()
print("Vous avez tous les critères pour être embauché(e).")


# v3
# modification de la variable message en fonction des critères pour afficher plusieurs problèmes

print("Entrez votre profil pour la validation de votre adéquation au poste")
age = int(input("Quel est votre age?\n"))
salaire = int(input("Quel salaire souhaitez vous?\n"))
experience = int(input("Combien d'années d'expérience avez vous ?\n"))

message = ""
convient = True

if age < 30:
    message = "Vous n'avez pas l'age minimum requis\n"
    convient = False
if salaire > 40000:
    message += "Le salaire exigé est trop élevé\n"
    convient = False
if experience < 5:
    message += "Vous n'avez pas assez d'expérience"
    convient = False
if convient: # même résultat que "convient == True"
    message = "Votre profil convient"

print(message)