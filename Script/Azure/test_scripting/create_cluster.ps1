$sshKey = "{HOME}\.ssh\1678889157.pub"
$resourceGroupName = 'm2i-formation'
$nameRegistry = "benoitM2iRegistry"
$location = "japaneast"
$subnet = "subnet-tp-benoit"

$cluster = @{ 
    ResourceGroupName = $resourceGroupName
    Name = $nameRegistry
    NodeCount = 1
    SshKeyValue = $sshKey
    Location = $location
    SubnetName = $subnet
}

$create_cluster = New-AzAksCluster @cluster