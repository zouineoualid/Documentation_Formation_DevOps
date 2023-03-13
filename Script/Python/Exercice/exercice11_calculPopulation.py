habitantInitial = int(input("Pouvez-vous rentrer un nombre d'habitant ? : "))
habitantTarget = int(input("Pouvez-vous rentrer un nombre d'habitant ciblé ? : "))
taux = float(input("Pouvez-vous rentrer un taux à respecter ? : "))
nbAnnee = 0


while (habitantInitial <= habitantTarget):
    habitantInitial = habitantInitial + (taux*habitantInitial/100)
    nbAnnee = nbAnnee + 1

print(f"il faudra {nbAnnee} année pour atteindre {habitantTarget} habitants avec un taux de : {taux} % par année, la ville aura précisément {round(habitantInitial)} habitants")
