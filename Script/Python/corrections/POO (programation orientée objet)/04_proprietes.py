class Thermometre:
    def __init__(self, temp_base_celsius):
        self.kelvin = temp_base_celsius - 273.15

    def afficher_temperatures(self):
        print("=== Valeurs du thermomètre ===")
        print("Kelvin : ", round(self.kelvin, 2))
        print("Celsius : ", round(self.get_celcius(), 2))
        print("Fahrenheit : ", round(self.fahrenheit, 2))

    # get_celcius est une méthode classique, on l'appelle avec les parenthèses -> getter par méthode
    def get_celcius(self):
        return self.kelvin - 273.15

    # fahrenheit est une propriété, on l'appelle comme un attribut -> getter par propriété
    @property
    def fahrenheit(self):
        return (self.kelvin - 273.15) * 9/5 + 32

    # set_celcius est une méthode classique, on l'appelle avec les parenthèses -> setter par méthode
    def set_celcius(self, valeur_celcius):
        self.kelvin = valeur_celcius + 273.15

    # fahrenheit est une propriété, on l'appelle comme un attribut -> setter par propriété
    @fahrenheit.setter
    def fahrenheit(self, valeur_fahrenheit):
        self.kelvin = (valeur_fahrenheit - 32) / 9/5 + 273.15


if __name__ == '__main__':
    thermo = Thermometre(100.)
    thermo.afficher_temperatures()
    thermo.set_celcius(0.)
    thermo.afficher_temperatures()
    thermo.fahrenheit = 212.0
    thermo.afficher_temperatures()
    thermo.kelvin = 273.15
    thermo.afficher_temperatures()


    
    print(thermo.kelvin)
    print(thermo.fahrenheit)
    print(thermo.get_celcius())
