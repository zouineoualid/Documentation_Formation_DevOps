multiplicateur = int(input("nombre de table de multiplication ? "))
print("")
afficher_table = " "
titre="table de multiplication"
print(f"{titre:^45}")
print(f"")
for i in range (1,multiplicateur+1):
    print(f"{i:^4}", end="")
print(" ")
print("=" + "===="*multiplicateur)
for n in range(1,multiplicateur+1):
    print("|", end='' )
    for i in range(1,multiplicateur+1):
        print(f"{i*n:^3}",end='')
        print(end="|")
    print("\n+" + "---+"*multiplicateur)