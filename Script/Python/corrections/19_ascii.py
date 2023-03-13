dict_letters_lower = {}
dict_letters_upper = dict()

# for code_ascii in range(97, 97 + 26):
for le_code_ascii_de_ma_lettre in range(ord('a'), ord('z')+1):
    dict_letters_lower[chr(le_code_ascii_de_ma_lettre)] = le_code_ascii_de_ma_lettre

# for code_ascii in range(65, 65 + 26):
for le_code_ascii_de_ma_lettre in range(ord('A'), ord('Z')+1):
    caractere = chr(le_code_ascii_de_ma_lettre) # on récupère le caractère à un certain code ascii
    dict_letters_upper[caractere] = le_code_ascii_de_ma_lettre # on ajoute le caractère en clé avec pour valeur son code ascii

print("=== ASCII lettres minuscules ===")
for cle, valeur in dict_letters_lower.items():
    print(f"{cle:^15}-{valeur:^15}")

print("=== ASCII lettres majuscules ===")
for cle, valeur in dict_letters_upper.items():
    print(f"{cle:^15}-{valeur:^15}")

