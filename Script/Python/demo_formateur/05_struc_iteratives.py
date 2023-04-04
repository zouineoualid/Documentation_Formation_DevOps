# increment = 0

# while increment < 10:
#     print(increment)
#     increment += 1 # increment = increment + 1

# increment = 0

# while increment < 10:
#     increment += 1 # incrémentation de 1
#     print(increment)

#     if increment == 3:
#         continue # on passe à l'itération suivante, les instructions suivantes ne sont pas exécutées

#     print("test")
    
#     if increment < 5 :
#         print("il est plus petit que 5")

#     if increment == 7:
#         break # on arrête le while directement sans faire les itérations suivantes


# print("Fin")

# range sert à générer des intervales de nombres
# range(fin)                => de 0 à fin-1
# range(debut, fin)         => de debut à fin-1
# range(debut, fin, pas)    => de debut à fin-1 avec une incrémentation de pas

# for i in range(10):
#     print(i)

# for i in range(2, 6):
#     print(i)

# for i in range(1, 12, 2): # itérations avec un pas de 2
#     print(i)

# for i in range(300, 280, -2): #itérations avec un pas de -2, la fin doit etre inférieure au début
#     print(f"La valeur de i est : {i}")




for i in range(10):
    print(f"{i:^{i*2}}.")

print("----+" * 10)