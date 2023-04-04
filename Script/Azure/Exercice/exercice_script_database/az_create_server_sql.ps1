# Variable #

$location = 'japaneast'
$name = 'benoit-sql-server-powershell'
$ressourceGroup = 'm2i-formation'
$version = '12.0'

# Objet base de donnée #

$azServerDatabase = @{
    ServerName = $name
    ResourceGroupName = $ressourceGroup
    Location = $location
    ServerVersion = $version
}

$createAzStabase = New-AzSqlServer @azServerDatabase -SqlAdministratorCredentials (Get-Credential)