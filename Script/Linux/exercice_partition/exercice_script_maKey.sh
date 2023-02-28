#!bin/bash



#Ce script permet à l'utilisateur de formater et monter une partition



#Nous devons demande à l'utilisateur s'il veut totalement nettoyer la partition :



if [[ $1 -eq 1 ]]

then

    dd if=/dev/zero of=$2 bs=2048 count=1

    echo "La partition a été formaté"

fi



#afficher à l'utilisateur la taille de la partition



lsblk | grep $2 | head -1 | cut -d" " -f1,14



#définir la taille de chaque partition



sizePartition=$((100/$3))



echo $sizePartition



parted --script /dev/$2 mklabel gpt



#Boucle création des partitions



for i in $(seq 0 $(($3-1)))

do parted --script /dev/$2 mkpart ext4 $((0+$i*$sizePartition))% $(($sizePartition+$i*$sizePartition))%

echo $((0+$i*$sizePartition))% $(($sizePartition+$i*$sizePartition))%

done



#Boucle montage/démontage/création de fichiers



for i in $(seq $3)

do

# touch /mnt/hello_world$i

mkfs.ext4 /dev/$2$i >/dev/null

mkdir /mnt/dos$i

mount /dev/$2$i /mnt/dos$i

# umount /dev/$2$i /mnt

done



######################################################

