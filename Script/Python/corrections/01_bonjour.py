prenom = input("Quel est votre prénom ? ")
nom = input("Quel est votre nom ? ")

prenom = prenom.capitalize()
nom = nom.upper()

print("Bonjour M. Ou Mme " + prenom + " " + nom + ".")
# print(f"Bonjour M. Ou Mme {prenom} {nom}.") #equivalent
# print("Bonjour M. Ou Mme", prenom, nom + ".") #equivalent

# variantes en une seule ligne
# print("Bonjour M. Ou Mme", input("Quel est votre prénom ? "), input("Quel est votre nom ? ") + ".") 
# print("Bonjour M. Ou Mme " + input("Quel est votre prénom ? ") + " " + input("Quel est votre nom ? ") + ".")


# méthodes pour normaliser les chaines de caractères
# exemples 
print("cHainE de TESt !".lower())
print("cHainE de TESt !".upper())
print("cHainE de TESt !".capitalize())
print("cHainE de TESt !".title())