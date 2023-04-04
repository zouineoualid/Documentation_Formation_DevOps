# Définition des variables utilisé dans ce script

$ipName = 'publicIpAzTpPokemonBuilder2Benoit'
$resourceGroupName = 'm2i-formation'
$nameSecurityGroup = 'security-group-az-powershell-benoit-tp-pokemon'
$location = 'japaneast'
$nameVm = 'vm-az-powershell-builder-benoit'
$imageVm = "UbuntuLTS"
$sizeVm = 'Standard_B1s'
$sshKey = 'ssh-benoit-tp'
$virtualNetwork = 'vm-az-builder-benoit'



# Objet avec les informations de l'adresse IP

$ip = @{
    Name = $ipName
    ResourceGroupName = $resourceGroupName
    AllocationMethod = 'Static'
    IpAddressVersion = 'IPv4'
    Location  = $location
}

# Création de l'adresse ip

$ipConfig = New-AzPublicIpAddress @ip

#Objet avec les informations du groupe de sécurité

# $netSecurityGroup = @{
#     Name = $nameSecurityGroup
#     ResourceGroupName = $resourceGroupName
#     Location  = $location
# }

# # Création d'un security group
# $nsc = New-AzNetworkSecurityGroup @netSecurityGroup

# # Création des règles de sécurité
# $nsc | Add-AzNetworkSecurityRuleConfig -Name web-rule-2 -Description "Allow HTTP" `
#     -Access Allow -Protocol Tcp -Direction Inbound -Priority 102 -SourceAddressPrefix `
#     Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 80 | Set-AzNetworkSecurityGroup

# $nsc | Add-AzNetworkSecurityRuleConfig -Name ssh-rule-2 -Description "Allow SSH" `
#     -Access Allow -Protocol Tcp -Direction Inbound -Priority 101 -SourceAddressPrefix `
#     Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 22 | Set-AzNetworkSecurityGroup

# Création d'une vm

$infoVm = @{
    Name = $nameVm
    ResourceGroupName = $resourceGroupName
    Location  = $location
    Size = $sizeVm
    SecurityGroupName = $nameSecurityGroup
    Image = $imageVm
    PublicIpAddressName = $ipName
    PublicIpSku = "Standard"
    VirtualNetworkName = $virtualNetwork
    SshKeyName = $sshKey
}

$vm = New-AzVM @infoVm