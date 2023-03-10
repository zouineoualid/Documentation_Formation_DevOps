## Commande Azure CLI
### Machine Virtuelle
#### Commande Network

- Création d'un réseau virtuel avec Subnet

---

az network vnet create --name custom-vnet-benoit --resource-group m2i-formation --address-prefixes 10.0.0.0/16 --subnet-name custom-subvnet-benoit-1 --subnet-prefixe 10.0.0.0/24

---

- Création d'une carte réseau

---

az network nic create --name custom-nic-benoit --resource-group m2i-formation --vnet-name custom-vnet-benoit --subnet custom-subvnet-benoit-1

---

### Commande VM

- Pour voir la liste des images Azure publique

---

az vm image list --output table

---

- Pour voir la liste des tailles pour les instances sur Azure en format table

---

az vm list-sizes --location "eastus" --output table

---

- Création VM

---

az vm create --name benoit-cli-1 --resource-group m2i-formation --image UbuntuLTS --size Standard_B1ls --admin-username benoit --admin-password Formation123456 --nics custom-nic-benoit

- Voir la liste des adresses IP

---

az vm list-ip-addresses --output table

---

- Pour voir la liste des adresses IP publique

---

az network public-ip list --output table

---

- Rattacher une adresse IP publique à un network

---

az network nic ip-config update --name ipconfig1 --resource-group m2i-formation --nic-name custom-nic-benoit --public-ip-address benoitcustompublicip

---