#!/bin/bash
### Création instance Ubuntu dans Azure ###

#Création du vnet de notre instance avec subnet

az network vnet create --name vnet-ubuntu-benoit \
    --resource-group m2i-formation \
    --address-prefixes 10.0.0.0/16 \
    --subnet-name subnet-ubuntu-benoit \
    --subnet-prefixe 10.0.0.0/24 \
    --location westus

    
    #Création carte réseau

az network nic create --name nic-ubuntu-benoit \
    --resource-group m2i-formation \
    --vnet-name vnet-ubuntu-benoit \
    --subnet subnet-ubuntu-benoit \
    --location westus


    #Création de l'instance

az vm create --name vm-ubuntu-benoit \
    --resource-group m2i-formation \
    --image UbuntuLTS \
    --size Standard_DS2_v2 \
    --private-ip-address 10.0.0.4 \
    --admin-username azureuser \
    --admin-password  Azure123456! \
    --nics nic-ubuntu-benoit \
    --location westus







