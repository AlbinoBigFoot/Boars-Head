# Stop Monday webhook proxy if running

$ErrorActionPreference = "Continue"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$LogDir = Join-Path $RepoRoot "logs\monday-agent"
$PidFile = Join-Path $LogDir "proxy.pid"
$Port = if ($env:MONDAY_WEBHOOK_PORT) { [int]$env:MONDAY_WEBHOOK_PORT } else { 9876 }

if (Test-Path $PidFile) {
	$procId = [int]((Get-Content $PidFile -Raw).Trim())
	if ($procId -gt 0) {
		Write-Host "Stopping PID $procId from proxy.pid"
		Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
	}
	Remove-Item $PidFile -Force -ErrorAction SilentlyContinue
}

Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue |
	Select-Object -ExpandProperty OwningProcess -Unique |
	ForEach-Object {
		$p = Get-Process -Id $_ -ErrorAction SilentlyContinue
		if ($p -and $p.ProcessName -match "python") {
			Write-Host "Stopping python PID $_ on port $Port"
			Stop-Process -Id $_ -Force -ErrorAction SilentlyContinue
		}
	}

Write-Host "Monday webhook proxy stopped (port $Port)"
