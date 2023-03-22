# Variable #

$location = 'japaneast'
$nameDatabase = 'benoit-sql-database-powershell'
$ressourceGroup = 'm2i-formation'
$nameServer = 'benoit-sql-server-powershell'
$edition = 'Free'

# Objet base de donnée #

$azSqlDatabase = @{
    ResourceGroupName = $ressourceGroup
    DatabaseName = $nameDatabase
    ServerName = $nameServer
    Edition = $edition
}

$createAzDatabase = New-AzSqlDatabase @azSqlDatabase
