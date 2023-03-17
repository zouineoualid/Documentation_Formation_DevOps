#Variable utilisé dans ce programme

$resourceGroupName = 'm2i-formation'
$nameRegistry = "benoitM2iRegistry"
$sku_Type = "Premium"
$location = "japaneast"
$EnableAdmin = 1  #Cette variable demande un boolean -> 0 pour False | 1 pour True

#Création du registry

$registry = @{ 
    ResourceGroupName = $resourceGroupName 
    Name = $nameRegistry
    Sku = $sku_Type
    Location = $location
    EnableAdminUser = $EnableAdmin
}

$createRegistry = New-AzContainerRegistry @registry