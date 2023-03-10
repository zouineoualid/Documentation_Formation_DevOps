#!/bin/bash
### Création instance Ubuntu dans Azure ###

az network nsg create --name nsg-ubuntu-benoit \
    --resource-group m2i-formation \
    --location northcentralus 

    #Création règle de filtrage - HTTP

az network nsg rule create \
  --resource-group m2i-formation \
  --nsg-name nsg-ubuntu-benoit \
  --name Allow-Web \
  --access Allow \
  --protocol Tcp \
  --direction Inbound \
  --priority 100 \
  --source-port-range "*" \
  --destination-port-range 80 

    #Création règle de filtrage - SSH

az network nsg rule create \
  --resource-group m2i-formation \
  --nsg-name nsg-ubuntu-benoit \
  --name Allow-SSH \
  --access Allow \
  --protocol Tcp \
  --direction Inbound \
  --priority 110 \
  --source-port-range "*" \
  --destination-port-range 22 

    #Création du vnet de notre instance avec subnet

az network vnet create --name vnet-ubuntu-benoit \
    --resource-group m2i-formation \
    --address-prefixes 10.0.0.0/16 \
    --subnet-name subnet-ubuntu-benoit \
    --subnet-prefixe 10.0.0.0/24 \
    --location northcentralus \
    --network-security-group nsg-ubuntu-benoit

    
    #Création carte réseau

az network nic create --name nic-ubuntu-benoit \
    --resource-group m2i-formation \
    --vnet-name vnet-ubuntu-benoit \
    --subnet subnet-ubuntu-benoit \
    --location northcentralus

    #Création ip publique 

az network public-ip create \
    --resource-group m2i-formation \
    --name publicIp-ubuntu-benoit \
    --version IPv4 \
    --sku Standard \
    --location northcentralus

    #Attachement de l'IP publique au vnet

az network nic ip-config update \
  --name ipconfig-ubuntu-benoit \
  --nic-name nic-ubuntu-benoit \
  --resource-group m2i-formation \
  --public-ip-address publicIp-ubuntu-benoit \


    #Création de l'instance

az vm create --name vm-ubuntu-benoit \
    --resource-group m2i-formation \
    --image UbuntuLTS \
    --size Standard_DS2_v2 \
    --private-ip-address 10.0.0.4 \
    --admin-username azureuser \
    --admin-password  Azure123456! \
    --nics nic-ubuntu-benoit \
    --public-ip-address publicIp-ubuntu-benoit \
    --nsg nsg-ubuntu-benoit \
    --location northcentralus
