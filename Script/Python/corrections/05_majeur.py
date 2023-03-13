age = int(input("Quel est ton age ? "))
majeur = age >= 18
print(majeur)

# equivalent en une seule ligne :
# print(int(input("Quel est ton age ? ")) >= 18)

# conversions en booléens
print(bool(0))
print(bool(1))
print(bool(1181))
print(bool(-1181))

print(bool(0.))
print(bool(11.))
print(bool(11.564))

print(bool(""))
print(bool("sdgziuerf"))
print(bool("False"))
print(bool("True"))

print(bool(None))


print(type(None))


print(print()) #print ne renvoie rien (None) donc si on print le retour d'un print => None