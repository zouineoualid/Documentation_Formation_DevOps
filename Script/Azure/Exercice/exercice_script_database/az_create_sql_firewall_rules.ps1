# Variable #

$rulesName = 'rules connexion locale IP'
$ressourceGroup = 'm2i-formation'
$nameServer = 'benoit-sql-server-powershell'


# Objet base de donnée - règle base de donnée #

$azSqlFirewallRules = @{
    ResourceGroupName = $ressourceGroup
    ServerName = $nameServer
    FirewallRuleName = $rulesName
    StartIpAddress = '185.31.149.99'
    EndIpAddress = '185.31.149.99'

}

$createAzServerFirewallRules = New-AzSqlServerFirewallRule @azSqlFirewallRules