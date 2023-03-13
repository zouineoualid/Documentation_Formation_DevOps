temperature_celcius =  int(input("Saisir la température de l'eau : "))
if temperature_celcius < 0 : 
    print("l'eau est à l'état solide")
elif temperature_celcius <= 100 :
    print("l'eau est à l'état liquide")
else :
    print("l'eau est à l'état gazeux")



# Ternaires
# variable = <Valeur si vrai> if <condition> else <valeur si faux>
etat = "solide" if temperature_celcius < 0 else ("liquide" if temperature_celcius <= 100 else "gazeux")
print(etat) 

