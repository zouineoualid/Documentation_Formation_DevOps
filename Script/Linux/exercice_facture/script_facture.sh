#!/bin/bash

#On demande à l'utilisateur de saisir différentes variable qui vont modifier la facture
read -p "Pouvez-vous donner un numéro de facture ? : " number_facture 
read -p "Pouvez-vous saisir un montant journalier? : " mnt_jour
read -p "Pouvez-vous saisir la date de début de prestation (YYYY/MM/DD) : " debut_presta
read -p "Pouvez-vous donner un nombre de jour travaillé ? : " nb_jours 

#Variable contenant la date de début de prestation et fin presta

start_debut_presta=$(date +'%Y%m%d' -d $debut_presta );

fin_presta=$(date +'%Y%m%d' -d "$debut_presta+$nb_jours days");

#Variable qui totalise la presta + nb jour

result_total_jour=$(($nb_jours*$mnt_jour))

#Outils de débugage

# echo $number_facture
# echo $mnt_jour
# echo $debut_presta
# echo $nb_jours
# echo $result_total_jour
echo $start_debut_presta

#Création dossier de réception du fichier .ods

mkdir modify_ods

#Copier la facture type dans un dossier spécifique

#Unzip du fichier .ods
cp facture_type.ods facture_type_test.ods
unzip facture_type_test.ods -d modify_ods

#modification des fichiers avec un sed
cd modify_ods
sed -i -e 's/DATEFLAG/'$start_debut_presta'/' -e 's/NUMEROFLAG/'$number_facture'/' -e 's/MONTANTFLAG/'$mnt_jour'/' -e 's/TOTALFLAG/'$result_total_jour'/' -e 's/PRIXFLAG/'$mnt_jour'/' -e 's/DATE1FLAG/'$start_debut_presta'/' -e 's/DATE2FLAG/'$fin_presta'/' content.xml

#zip des fichiers 

zip -r ../facture_$number_facture.ods *

#Suppression du dossier modify_ods

cd ../ && rm -r modify_ods/ 

#Conversion .ods to .pdf

libreoffice --convert-to pdf facture_$number_facture.ods

#libreoffice facture_type.ods