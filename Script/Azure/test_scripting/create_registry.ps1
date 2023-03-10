$registry = @{ 
    ResourceGroupName = "m2i-formation" 
    Name = "benoitPowershellRegistry"
    Sku = "Premium"
    Location = "japaneast"
    EnableAdminUser = True
}

$benoitTestRegistry = New-AzContainerRegistry @registry