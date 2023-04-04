class Chien():
    
    # Pour créer des attribut qui sont partagées par toutes les instances de la même classe,
    # il nous faut les déclarer en dehors de notre constructeur
    nb_chiens = 0

    def __init__(self, name, breed, age):
        self.age = age
        self.name = name
        self.breed = breed

        # Pour accéder à l'attribut de classe, il nous faut utiliser la syntaxe NomClass.nom_attribut
        Chien.nb_chiens += 1

    # Pour créer une méthode de classe, il nous faut utiliser le décorateur @classmethod
    #
    # Elles ne peuvent, contrairement aux méthodes classiques, pas accéder aux attributs d'instance (liés à un chien en particulier -> self)
    # Elles peuvent cependant accéder aux attributs de classe, de par l'utilisation du mot-clé 'cls'
    @classmethod
    def aboyer(cls, text): # le premier paramètre est toujours nommé "cls" et référencie la classe
        print(f"The dog says : {text} - {cls.nb_chiens}")

    # Pour créer une méthode statique, il nous faut utiliser le décorateur @staticmethod
    #
    # A contrario des méthodes de classe, les méthodes statiques n'ont pas accès par défaut aux attribut de classe
    # Elles ont un but principal de permettre le regroupement de fonctionnalité sous un même nom de classe
    @staticmethod
    def test_static(): # pas de mots clés du style cls ou self 
        print("La méthode statique")


class Calcul():
    @staticmethod
    def addition(a, b):
        return a + b
    @staticmethod
    def soustraction(a, b):
        return a - b



mon_chien = Chien("Bernie", 'Labrador', 7)
mon_chien_a = Chien("Rex", 'Doberman', 4)


# Pour accéder à l'attribut de classe, il nous faut utiliser la syntaxe NomClass.nom_attribut
print(Chien.nb_chiens)

mon_chien_a = Chien("Princesse", 'Chiwawa', 4)
# Pour déclencher une méthode de classe, on utilise la syntaxe NomClass.nom_method()
Chien.aboyer('Ouaf woof')

# Pour déclencher une méthode statique, on utilise encore une fois la notation nom_classe.nom_methode()
Chien.test_static()




print(Calcul.addition(1, 5))

print(Calcul()) # pas de __init__ mais un objet Calcul "vide" est quand même créé