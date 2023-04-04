#!/bin/bash
function help(){
    echo "xMAKEY"
    echo "Creation et sauvegarde d'un fichier archive et compresse sur une clée chifrée/partionnée LVM"
    echo "Par défaut, le programme ne chiffre pas les conteneurs" 
    echo " utilisation:"
    echo "--file=[file]                 détermine les fichiers à archiver + compression + placer sur le device" 
    echo "--device=[device]      device a utiliser"
    echo "exemple d'utilisation"
    echo "sudo bash xmaKey.sh device=/dev/sde files=Downloads/film.mp4,~/Downloads/img.png,/home/user2/file.txt"
    echo "pour le files="
                    echo    "l'utilisateur peut rentrer un chemin absolu,relatif"
                    echo    "et commencant par ~pour l'exercice '~' represente le home directory"
                    echo    "de l'utilisateur qui a utilise sudo"
                    echo    "donc ~ ne sera pas egal a "/root" mais a "/home/user/" "

for arg in $@ #
do
    if [[ $arg =~ ^--device=(.+) ]]
    then
        device=${BASH_REMATCH[1]}
    elif [[ $arg =~ ^--files=([~\/A-z]*) ]]
    then
        files=${BASH_REMATCH[1]}
    fi
done
#[~\/][A-z]*
echo $files