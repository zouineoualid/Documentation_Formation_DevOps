# Variable dictionnaire
my_dict_min = {}
my_dict_max = {}
 
# Condition dictionnaire
for i in range(ord('a'), ord('z')+1):
    my_dict_min[chr(i)] = i

for i in range(ord('A'), ord('Z')+1):
    my_dict_max[chr(i)] = i

#Affichage dictionnaire

print("Dictionnaire majuscule : \n")

for q in my_dict_max:
    print(f"{q} - {my_dict_max[q]}\n")

print('#########\n')

print("Dictionnaire minuscule : \n")

for k in my_dict_min:
    print(f"{k} - {my_dict_min[k]}\n")