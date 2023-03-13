temperature_input = input("Pouvez-vous indiquer la température de l'eau ? : ")
temperature = float(temperature_input)

if temperature < 0:
    print("l'eau est à l'état : SOLIDE")
elif temperature <= 100:
    print("l'eau est à l'état : LIQUIDE")
else :
    print("l'eau est à l'état : GAZEUX")    
