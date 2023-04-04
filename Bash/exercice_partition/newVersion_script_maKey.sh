#!/bin/bash
function help(){
    echo "MAKEY"
    echo "Creation automatique de clées"
    echo "Le programme permet de créer autoomatiquement des clé chiffré et non chiffré"
    echo "Par défaut, le programme ne chiffre pas les conteneurs" 
    echo "pour activer le chiffrement -> utiliser l'argument --crypt"
    echo "Pour accéder au conteneur chiffrer : un fichier de mot de passe sera généré"
    echo " utilisation:"
    echo "--clean      nettoyer la table de partition" 
    echo "--crypt      chiffrer la table de partition"
    echo "--nb         nombre de partitions a creer"
    echo "--device=[device]      device a utiliser"
    echo "--rmv        remove les lv créer"
    echo "exemple de commande : "
    echo "sudo bash newVersion_script_maKey.sh --device=/dev/sda --crypt --1"
}


for arg in $@ #
do
    if [[ $arg =~ ^--device=(.+) ]]
    then
        device=${BASH_REMATCH[1]}
    elif [[ $arg =~ ^--clean ]]
    then
        clean=true
    elif [[ $arg =~ ^--crypt ]]
    then
        crypt=true
    elif [[ $arg =~ ^--rmv ]]
    then
        rmv=true
    elif [[ $arg =~ ^--([0-9]) ]]
    then
        nb_parts=${BASH_REMATCH[1]}
    else
        help
        exit 1
    fi
done 

echo $device

if [ -z $device ]
then
    echo "il faut indiquer un device"
    echo "--device=[device]"
    echo ""
    help
    exit 2
fi

# verification du device
if [ -z $device ]
then
    echo "il faut indiquer un device"
    echo "--device=[device]"
    echo ""
    help
    exit 2
fi

lsblk $device &> /dev/null

if [ $? -ne 0 ]
then
    echo "impossible de travailler avec: '$device'"
    echo "verifiez qu'il sagit bien d'un device "
    echo "et qu'il soit bien branché sur la machine"
    exit
fi

# verification du nombre de partitions

if [ -z $nb_parts ]
then
    echo "Il faut indiquer un nombre de partitions"
    help
    exit
fi

#Vérification argument crypt

if [ $crypt = true ]
then
    encrypt=true
    else
    encrypt=false
fi


# ON COMMENCE
echo "Travaille sur: $device"
read -p "Voulez-vous continuer? Y " choix
if [ -n "$choix" ]
then
    echo "On annule"
    exit
fi


# nettoyer si on a mit --clean

if [ -n $clean ]
then
    dd if=/dev/zero of=$device bs=2048 count=1 > /dev/null
fi

#chiffrer la clé si l'argument --crypt est true

if [ $encrypt = true ]
then
    dd if=/dev/urandom of=mdp_contener bs=50 count=1
    cryptsetup luksFormat $device --key-file mdp_contener
    cryptsetup open $device --key-file mdp_contener
fi


# creer la table de partition

if [ $encrypt = false ] 
then
parted --script $device mklabel gpt
else
pvcreate $device
vgcreate my_group $device
fi 

# creer les partitions
percent=$((100/$nb_parts))
for i in $(seq 0 $(($nb_parts-2)) )
do
    start=$((0+$i*$percent))
    end=$(($start+$percent))
    [ $encrypt = false ] && parted --script $device mkpart primary ext4 $start% $end% && mkfs.ext4 $device$((i+1))
    [ $encrypt = true ] && lvcreate my_group -n part$i -l $percent%VG
    
done


[ $nb_parts -eq 1 ] && end=0 && i=0

if [ $encrypt = false ] 
then
parted --script $device mkpart primary ext4 $end% 100%
mkfs.ext4 $device$((i+1))
else
lvcreate my_group -n part$(($i+1)) -l 100%FREE
mkfs.ext4 $device$((i+1))
fi

#Si --rmv indiqué dans la commande, on démonte les lv montées

if [ '$rmv' = true ]
then
vgremove my_group
lsblk $device
else
lsblk $device
fi

echo ""
echo "[TERMINE]"