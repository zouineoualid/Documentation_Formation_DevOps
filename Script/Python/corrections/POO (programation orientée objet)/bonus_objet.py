# Pour créer une classe, il nous faut utiliser le mot-clé 'class'
# Par convention, les classes commencent par des majuscules
class Chien:

    # Pour créer un objet à partir de notre classe, il faudra passer par
    # son constructeur, qui est défini par la méthode __init__(self):
    # En passant des paramètres à cette méthode, on peut les placer dans notre objet
    def __init__(self, age, nom, espece):
        self.attribut_nom = nom # attribut_nom est un attribut de notre instance de chien (self), il sera différent pour chaque instance
        self.age = age  # il reste possible de l'appeler directement self.age, qui est un attribut de notre instance, différent de notre paramêtre du constructeur age
        self.espece = espece

# Pour créer une instance de notre classe Chien, il nous faut faire appel au constructeur Nom_class(params)
# qui va nous renvoyer une variable du type de la classe
mon_chien = Chien(2, "Pepette", "Dobermann") #creation d'un nouveau chien avec le constructeur (une instance/un objet)

print(type(mon_chien))

# Pour accéder aux propriétés de l'objet,
# on se sert de la notation nom_instance.nom_attribut
nom_du_chien = mon_chien.attribut_nom
print(nom_du_chien)
print(mon_chien.age)

mon_2e_chien = Chien(2, "Princesse", "Chiwawa") #creation d'un autre chien avec le même constructeur --> nouvelle instance/objet de la classe Chien
print("Nom du 2e chien : ", mon_2e_chien.attribut_nom)
print("Age du 2e chien : ", mon_2e_chien.age)