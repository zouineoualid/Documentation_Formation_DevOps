# le lambda a une syntaxe plus simple que la fonction, on s'en sert rapidement et souvent qu'une seule fois 
# il est souvent utile dans des fonctions qui appliquent des fonctions sur un ensemble de données ex : map, sorted, reduce, ...
fct = lambda x : x**2

def fct2(x):
    return x**2

print(fct(2))
print(fct2(2))

print(fct)
print(fct2)
