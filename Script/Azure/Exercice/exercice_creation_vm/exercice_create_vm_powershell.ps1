# Objet avec les informations de l'adresse IP
$ip = @{
    Name = 'public-ip-az-powershell-2-benoit'
    ResourceGroupName = 'm2i-formation'
    AllocationMethod = 'Static'
    IpAddressVersion = 'IPv4'
    Location  = "northcentralus"
}
# Création de l'adresse ip
$ipConfig = New-AzPublicIpAddress @ip

# Objet avec les informations du groupe de sécurité

$netSecurityGroup = @{
    Name = "security-group-az-powershell-benoit-2"
    ResourceGroupName = "m2i-formation"
    Location  = "northcentralus"
}

# Création d'un security group
$nsc = New-AzNetworkSecurityGroup @netSecurityGroup

# Création des règles de sécurité
$nsc | Add-AzNetworkSecurityRuleConfig -Name web-rule-2 -Description "Allow HTTP" `
    -Access Allow -Protocol Tcp -Direction Inbound -Priority 102 -SourceAddressPrefix `
    Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 80 | Set-AzNetworkSecurityGroup

$nsc | Add-AzNetworkSecurityRuleConfig -Name ssh-rule-2 -Description "Allow SSH" `
    -Access Allow -Protocol Tcp -Direction Inbound -Priority 101 -SourceAddressPrefix `
    Internet -SourcePortRange * -DestinationAddressPrefix * -DestinationPortRange 22 | Set-AzNetworkSecurityGroup

# Création d'une vm

$infoVm = @{
    Name = 'vm-az-powershell-benoit'
    ResourceGroupName = 'm2i-formation'
    Location  = "northcentralus"
    SecurityGroupName = $nsc
    Image ="UbuntuLTS"
    PublicIpAddressName = $ipConfig
}