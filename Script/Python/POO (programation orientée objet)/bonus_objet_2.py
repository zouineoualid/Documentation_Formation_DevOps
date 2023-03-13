class Chien():
    def __init__(self, nom, age, race):
        self.nom = nom 
        self.age = age 
        self.race = race 
    
    # Pour faire une méthode, il nous faut faire une fonction dans notre classe
    # qui possède comme premier paramètre le mot-clé self (ce qui l'attachera à notre instance)
    #
    # Via ce mot clé, il nous est également possible d'accéder à toutes les propriétés et méthodes de notre instance
    def aboyer(self, texte):
        print(f"{self.nom} aboie la phrase : {texte}")


mon_chien = Chien("Rex", 5, "Pit")
mon_2e_chien = Chien("Princesse", 2, "Chihuahua") 

liste_chien = [
    mon_chien,
    mon_2e_chien,
    Chien("Speedy", 2, "Lévrier")
]

for chien in liste_chien:
    print(chien.nom)


for i in range(1,4):
    liste_chien.append(Chien(f"pif{i}", 0, "Labrador"))

for chien in liste_chien:
    print(chien.nom)


for chien in liste_chien:
    chien.aboyer("ouaf")

