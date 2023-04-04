from random import randint, choice
from colorama import Fore


hauteur = int(input("Saisir la hauteur du sapin : "))
tronc = int(input("Saisir la hauteur du tronc : "))
colors = [
    Fore.MAGENTA,
    Fore.RED,
    Fore.YELLOW,
    Fore.CYAN,
    Fore.BLUE
]

for i in range(1, hauteur + 1):
    if i == 1:
        print(Fore.YELLOW + f"{'A':^{2 * hauteur -1}}")
    else:
        for j in range(1, hauteur-i+1):
            print(" ", end="")
        chars = ""
        for i in range(1, 2*i):
            ball_color = choice(colors)
            chars += Fore.GREEN + '*' if randint(1, 8) > 3 else ball_color + 'o'
        print(chars)

print(Fore.RED, end="")
for i in range(1, tronc):
    print(f"{'| |':^{(1 + (hauteur-1)*2)}}")

print(f"{'■ ■|_|■ ■':^{(1 + (hauteur-1)*2)}}")

print('😎😎😎😎')
