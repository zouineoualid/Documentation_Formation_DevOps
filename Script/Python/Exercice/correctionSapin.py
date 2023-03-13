hauteur = int(input("saisir la hauteur du triangle : "))
for i in range(1, hauteur + 1):
    print(f"{(i - 1)* '**' + '*':^2{2 * hauteur -1}}")