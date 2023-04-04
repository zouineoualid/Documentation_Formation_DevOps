Install-Module posh-git -Scope CurrentUser -Force `
Install-Module PowerShellGet -Force -SkipPublisherCheck `
Import-Module posh-git `
Add-PoshGitToProfile -AllHosts `
Install-WindowsFeature -name Web-Server -IncludeManagementTools `
Set-Location C:\ `
git clone https://github.com/mdn/html-examples.git `
Remove-Item C:\inetpub\wwwroot\* `
Copy-Item "C:\html-examples\*" -Destination "C:\inetpub\wwwroot\" 

