import math


pop_init = int(input("Saisir la population : "))
tx_pct = float(input("Saisir le taux (%) : "))
pop_visee = int(input("Saisir la population visée : "))
annee = 0
pop = pop_init

while pop <= pop_visee:
    annee += 1
    pop *= 1 + tx_pct/100

print(f"La population dépasse la population visée à l'année {annee} ({math.floor(pop)} habitants)")

annee = 0
while (pop_init*(1+tx_pct/100)**annee) <= pop_visee:
    annee += 1


print(f"La population dépasse la population visée à l'année {annee} ({math.floor(pop_init*(1+tx_pct/100)**annee)} habitants)")