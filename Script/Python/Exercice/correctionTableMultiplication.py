nb_table = int(input("Saisir le nom de table (>0) : "))

while nb_table <= 0:
    nb_table = int(input("Saisie incorrect !!!\n Saisir nb table ()>0) : "))

print(" Table de multiplications : ".center(41))
print("="*30 + "\n|", end="")
for i in range(1,11):
    print (f"{i:^3}", end='|')
print("\n" + "="*41)
for i in range(1, nb_table+1):
    print("|", end="")
    for j in range(1,11):
        print(f"{i*j:3^}", end='|')
    print("\n" +  "---+"*10)

    #avec un seul print et concatenation
