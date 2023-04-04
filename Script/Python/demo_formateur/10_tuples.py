def recuperer_nombre_et_carre(nombre):
    return nombre, nombre ** 2 # tuple packing -> on se sert d'un tuple pour retourner plusieurs valeurs

print(recuperer_nombre_et_carre(3))

# Pour déclarer un tuple, on utilise la syntaxe entre parenthèse
# ou simplement on sépare les éléments avec une virgule
ma_tuple = (1, 2, 3, 4, 5)
print(ma_tuple)
ma_tuple = 1, 2, 3, 4, 5
print(ma_tuple)


# principe d'unpacking : on 'découpe' notre tuple en plusieurs variables
# /!\ autant de choses dans le tuple que en dehors
un, deux, trois, quatre, cinq = ma_tuple
print(un)
print(quatre)

ma_tuple2 = un, deux, trois, "huit" #packing
print(ma_tuple2)

un, deux, trois = 1, 2, 3


nombre, carre = recuperer_nombre_et_carre(5)
print(nombre)
print(carre)


print(recuperer_nombre_et_carre(3)[1])
#équivalent
t = recuperer_nombre_et_carre(3)
print(t)
print(t[0])
print(t[1])


# la variable underscore "_" dans python
# sert à "se débarasser" de valeurs inutiles 
_ = 2
print(_)


# for sans utilisation de l'incrément/la variable d'iteration
for _ in range(20):
    print("test")

var1, _, _, _, var5 = ma_tuple
print(var1)
print(var5)
print(_) # contient tuple[3]





# raw-strings "chaines crues" --> caractères spéciaux pas interprétés

print("\n{1}")
print(f"\n{1}")
print(r"\n{1}") # les caractères spéciaux ne sont pas utilisés

print(r"\"")
# print(r""")
print(r'\'')
# print(r'\')
print(r'\\')
print('\\')

# ex : pour les chemins de fichiers (file paths) ou les patterns regex