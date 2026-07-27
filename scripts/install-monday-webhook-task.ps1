# Install a durable At-LogOn scheduled task for the Monday → local agent proxy.

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$StartScript = Join-Path $RepoRoot "scripts\start-monday-webhook.ps1"
$TaskName = "BH-Monday-Local-Agent-Proxy"

if (-not (Test-Path $StartScript)) { throw "Missing $StartScript" }

$action = New-ScheduledTaskAction `
	-Execute "powershell.exe" `
	-Argument ("-NoProfile -ExecutionPolicy Bypass -File `"{0}`"" -f $StartScript) `
	-WorkingDirectory $RepoRoot

$trigger = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$settings = New-ScheduledTaskSettingsSet `
	-AllowStartIfOnBatteries `
	-DontStopIfGoingOnBatteries `
	-StartWhenAvailable `
	-RestartCount 3 `
	-RestartInterval (New-TimeSpan -Minutes 1) `
	-ExecutionTimeLimit ([TimeSpan]::Zero)

$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask `
	-TaskName $TaskName `
	-Action $action `
	-Trigger $trigger `
	-Settings $settings `
	-Principal $principal `
	-Force | Out-Null

Write-Host "Scheduled task '$TaskName' registered (AtLogOn)."
Write-Host "Start now:  Start-ScheduledTask -TaskName '$TaskName'"
Write-Host "Or run:     powershell -File `"$StartScript`""
Write-Host "Stop:       powershell -File `"$(Join-Path $RepoRoot 'scripts\stop-monday-webhook.ps1')`""
