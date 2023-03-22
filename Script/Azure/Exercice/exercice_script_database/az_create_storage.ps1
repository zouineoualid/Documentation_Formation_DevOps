# Variable #
###############################################
$name = 'benoitstoragepowershell'
$ressourceGroup = 'm2i-formation'
$sku = 'Standard_GRS'
$location = 'japaneast'
$access = 'Hot'
###############################################

# Objet avec les informations du compte de stockage #

$azStorage = @{
    Name = $name
    ResourceGroupName = $ressourceGroup
    SkuName = $sku
    Location  = $location
    AccessTier = $access
    AssignIdentity = 1
    EnableHierarchicalNamespace = 1
    EnableLocalUser = 1

}

# Création du compte de stockage #

$createAzStorage = New-AzStorageAccount @azStorage



