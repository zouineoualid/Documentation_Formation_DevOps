def calcul_tuple (a, b):
    return a+b, a-b, a*b, a/b

first_number = int(input("Veuillez entrer un 1er nombre : "))
second_number = int(input("Veuillez entrer un second nombre : "))

my_tuple = (calcul_tuple(first_number, second_number))

print("###################" * my_tuple[0])

print(f"L'addition de deux nombre donne : {my_tuple[0]}")
print(f"La soustraction de deux nombre donne : {my_tuple[1]}")
print(f"La multiplication de deux nombre donne : {my_tuple[2]}")
print(f"La division de deux nombre donne : {my_tuple[3]}")
