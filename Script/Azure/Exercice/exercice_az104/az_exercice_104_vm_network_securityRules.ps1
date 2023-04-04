# # Objet avec les informations de l'adresse IP

# $ip = @{
#     Name = 'publicIpAzPowershell1Benoit'
#     ResourceGroupName = 'm2i-formation'
#     AllocationMethod = 'Static'
#     IpAddressVersion = 'IPv4'
#     Location  = "koreacentral"
# }

# # Création de l'adresse ip

# $ipConfig = New-AzPublicIpAddress @ip

# # Objet avec les informations de l'adresse IP

# $ip2 = @{
#     Name = 'publicIpAzPowershell2Benoit'
#     ResourceGroupName = 'm2i-formation'
#     AllocationMethod = 'Static'
#     IpAddressVersion = 'IPv4'
#     Location  = "koreacentral"
# }

# # Création de l'adresse ip

# $ipConfig2 = New-AzPublicIpAddress @ip2

# #Objet avec les informations du VNET

# $vnet = @{
#     Name = 'VNet-benoit'
#     ResourceGroupName = 'm2i-formation'
#     Location = 'koreacentral'
#     AddressPrefix = '10.0.0.0/16'
# }

# #Objet Subnet

# $frontendSubnet = New-AzVirtualNetworkSubnetConfig -Name frontendSubnet -AddressPrefix "10.0.1.0/24"
# $backendSubnet  = New-AzVirtualNetworkSubnetConfig -Name backendSubnet  -AddressPrefix "10.0.2.0/24"

# $virtualNetwork = New-AzVirtualNetwork @vnet -Subnet $frontendSubnet,$backendSubnet

# #Objet avec les informations du groupe de sécurité

# $netSecurityGroup = @{
#     Name = "security-group-az-powershell-benoit-2"
#     ResourceGroupName = "m2i-formation"
#     Location  = "koreacentral"
# }

# # Création d'un security group
# $nsc = New-AzNetworkSecurityGroup @netSecurityGroup

# # Création des règles de sécurité
# $nsc | Add-AzNetworkSecurityRuleConfig -Name web-rule-2 -Description "Allow HTTP" `
#     -Access Allow -Protocol Tcp -Direction Inbound -Priority 102 -SourceAddressPrefix `
#     Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 80 | Set-AzNetworkSecurityGroup

# $nsc | Add-AzNetworkSecurityRuleConfig -Name RDP-rule-2 -Description "Allow SSH" `
#     -Access Allow -Protocol Tcp -Direction Inbound -Priority 101 -SourceAddressPrefix `
#     185.31.149.99 -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 3389 | Set-AzNetworkSecurityGroup

# $nsc | Add-AzNetworkSecurityRuleConfig -Name web-rule-3 -Description "Allow HTTPS" `
#     -Access Allow -Protocol Tcp -Direction Inbound -Priority 103 -SourceAddressPrefix `
#     Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 443 | Set-AzNetworkSecurityGroup

# Création d'une vm

$infoVm = @{
    Name = 'vm-az-powershell-benoit'
    ResourceGroupName = 'm2i-formation'
    Location  = "koreacentral"
    SecurityGroupName = $nsc
    Image = "UbuntuLTS"
    PublicIpAddressName = "publicIpAzPowershell1Benoit"
    PublicIpSku = "Standard"
    SubnetName = "frontendSubnet"
    VirtualNetworkName = "VNet-benoit"
}

$vm = New-AzVM @infoVm -Credential (Get-Credential)


# Création d'une vm

# $infoVm2 = @{
#     Name = 'vm-az-powershell-benoit-2'
#     ResourceGroupName = 'm2i-formation'
#     Location  = "koreacentral"
#     SecurityGroupName = $nsc
#     Image = "UbuntuLTS"
#     PublicIpAddressName = "publicIpAzPowershell2Benoit"
#     PublicIpSku = "Standard"
#     SubnetName = "backendSubnet"
#     VirtualNetworkName = "VNet-benoit"
# }

# $vm = New-AzVM @infoVm2 -Credential (Get-Credential)