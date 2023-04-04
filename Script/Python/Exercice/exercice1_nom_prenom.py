# first_name = "Théo"  last_name = "Silverberg" = firstname_lastname = print(f"Bonjour Mr ou Mme : {first_name} {last_name}")

# Correction :

prenom = input("Quel est votre prénom ? : ")
nom = input("Quel est votre nom ? : ")

prenom = prenom.capitalize()
nom = nom.upper()

print("Bonjour M. ou Mme " + prenom + " " + nom + ".")
