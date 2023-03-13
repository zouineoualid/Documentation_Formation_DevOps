# import math 
# import math as mon_module_math
# from math import pi, cos #ici on n'importe que pi et cos() il devient accessible directement sans faire "math."


# print(5 + 3)
# print(5 - 3)

# print(5 * 3) # fois

# print(5 / 3) # division classique
# print(5 // 3) # division entière (sans virgule donc un int est renvoyé)
# print(5 % 3) #modulo

# # puissance (exposant / pow)
# print(4 ** 2) #carré d'entier
# print(4. ** 2) #carré de float

# print(pow(4, 2)) #carré de base (pareil que **)
# print(math.pow(4, 2)) #carré du module math (float)
# print(mon_module_math.pow(4, 2)) #carré du module math (variable du module renommé)

# # module math
# var = 0.999999999999
# print(math.ceil(var)) # arrondi du dessus
# print(round(var)) # arrondi classique (X.4999 ou X.5)
# print(round(1.4))
# print(round(1.5))
# print(math.floor(var)) # arrondi du dessous

# print(math.pi) #avec : import math
# print(pi) #avec : from math import pi

# # Modifications de variables avec un opérateur
# var = 50
# print(var)
# var *= 5  # var = var * 5
# print(var) #250
# var //= 5  # var = var // 5
# print(var) #50

# #operateurs sur les strings
# #concaténation
# str1 = "Bonjour"
# str1 += " et Bienvenue!"
# print(str1)

# #répétition
# str2 = "test " * 50  # entre str et int
# print(str2)


# # Opérateurs de comparaison
# mon_bool = 21 > 5
# print(mon_bool)
# mon_bool = 21 < 5
# print(mon_bool)
# mon_bool = 21 >= 5
# print(mon_bool)
# mon_bool = 21 <= 5
# print(mon_bool)
# mon_bool = 21 == 5
# print(mon_bool)
# mon_bool = 21 != 5
# print(mon_bool)


# Opérateur logiques
print((25 > 5) and (125 != 2))  # ET
print((25 > 5) & (125 != 2))  # ET (non recommandé car différent)

print((25 > 50) or (125 != 2))  # OU
print((25 > 50) | (125 != 2))  # OU (non recommandé car différent)

print((25 < 50) ^ (125 != 2))  # OU EXCLUSIF

print(not True)  # Inversion