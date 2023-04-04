age_input = input("pouvez-vous indiquer l'âge du candidat ? : ")
salaire_input = input("pouvez-vous indiquer le salaire demandé par le candidat ? : ")
nbAnnee_input = input("pouvez-vous indiquer le nombre d'année d'expérience du candidat ? : ")

age = int(age_input)
salaire = int(salaire_input)
nbAnnee = int(nbAnnee_input)

if age < 18 :
    print("Le candidat n'est pas assez âgé")
elif age >= 30 and age < 18 :
    print("Le candidat est trop âgé")
elif salaire > 40000:
    print ("le salaire demandé est trop elevé")
elif nbAnnee < 5:
    print("le candidat n'a pas assez d'expérience")
else:
   print("Le candidat rempli toute les conditions pour travailler avec nous")        