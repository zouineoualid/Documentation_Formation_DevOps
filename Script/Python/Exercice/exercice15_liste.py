#Lire la saisie de l'utilisateur
min = 1
max = int(input("Entrez un chiffre pour voir ses nombres 1er : "))
list_saisie = []
escape_function = " "


for n in range(min,max + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
        list_saisie.append(n)
            

print(list_saisie[-1])

