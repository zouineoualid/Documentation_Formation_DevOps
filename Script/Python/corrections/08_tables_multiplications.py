nb_table = int(input("Saisir le nombre de tables (>0) : "))

# contrôle de saisie
while nb_table <= 0:
    nb_table = int(input("Saisie incorrecte !!!!\nSaisir le nombre de tables (>0) : "))

print("Tables de multiplications:".center(41))
print("="*41 + "\n|", end="")
for i in  range(1,11):
    print(f"{i:^3}", end='|')
print("\n" + "="*41)
for i in range(1, nb_table+1):
    print("|", end="")
    for j in range(1,11):
        print(f"{i*j:^3}", end='|')
    print("\n+" + "---+"*10)

# avec un seul prin et de la concatenation

chaine = "Tables de multiplications:".center(41) + "\n"
chaine += '=' * 41  + "\n"
for chiffre in range(1, 11):
    if chiffre == 1 :
        ligne = "|"
    ligne += f"{chiffre:^3}|"
chaine+= ligne + '\n=' + '=' * 40 + "\n"

for table in range(1, nb_table+1):
    for chiffre in range(1, 11):
        if chiffre == 1 :
            ligne = "|"
        ligne += f"{table*chiffre:^3}|"
    chaine += ligne + '\n+' + "---+" * 10 + "\n"

print(chaine)