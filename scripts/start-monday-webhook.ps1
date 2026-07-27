# Start Monday → local agent webhook proxy (foreground or background)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
if (-not $RepoRoot) { $RepoRoot = "C:\Users\dylan.jones\Documents\Bors" }

$PythonCmd = Get-Command python -ErrorAction SilentlyContinue
$Python = if ($PythonCmd) { $PythonCmd.Source } else { $null }
if (-not $Python) { $Python = "C:\Users\dylan.jones\AppData\Local\Programs\Python\Python314\python.exe" }
if (-not (Test-Path $Python)) { throw "python not found" }

$Port = if ($env:MONDAY_WEBHOOK_PORT) { [int]$env:MONDAY_WEBHOOK_PORT } else { 9876 }
$LogDir = Join-Path $RepoRoot "logs\monday-agent"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$OutLog = Join-Path $LogDir "proxy-stdout.log"
$ErrLog = Join-Path $LogDir "proxy-stderr.log"

# Stop any existing listener on the port (our previous proxy)
$existing = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue |
	Select-Object -ExpandProperty OwningProcess -Unique
foreach ($procId in $existing) {
	try {
		$p = Get-Process -Id $procId -ErrorAction SilentlyContinue
		if ($p -and $p.ProcessName -match "python") {
			Write-Host "Stopping existing python PID $procId on port $Port"
			Stop-Process -Id $procId -Force -ErrorAction SilentlyContinue
		}
	} catch {}
}

$script = Join-Path $RepoRoot "scripts\monday_webhook_proxy.py"
$argList = @($script, "--port", "$Port", "--bind", "127.0.0.1")
if ($env:MONDAY_AGENT_DRY_RUN -in @("1", "true", "yes")) {
	$argList += "--dry-run"
}

Write-Host "Starting monday_webhook_proxy on 127.0.0.1:$Port"
Write-Host "Logs: $OutLog / $ErrLog"

$proc = Start-Process -FilePath $Python `
	-ArgumentList $argList `
	-WorkingDirectory $RepoRoot `
	-RedirectStandardOutput $OutLog `
	-RedirectStandardError $ErrLog `
	-WindowStyle Hidden `
	-PassThru

# Persist PID for stop script
$proc.Id | Set-Content -Path (Join-Path $LogDir "proxy.pid") -Encoding ascii
Start-Sleep -Seconds 1

# Health check
try {
	$h = Invoke-RestMethod -Uri "http://127.0.0.1:$Port/" -TimeoutSec 5
	Write-Host ("OK service={0} pid={1}" -f $h.service, $proc.Id)
} catch {
	Write-Warning "Proxy started (pid $($proc.Id)) but health check failed: $_"
}

# Ensure Funnel path still maps /monday-webhook → 9876 (idempotent)
$ts = Get-Command tailscale -ErrorAction SilentlyContinue
if ($ts) {
	$funnel = & tailscale funnel status 2>&1 | Out-String
	if ($funnel -notmatch "/monday-webhook") {
		Write-Host "Configuring Tailscale Funnel /monday-webhook → 127.0.0.1:$Port"
		& tailscale serve --bg --yes --set-path /monday-webhook ("http://127.0.0.1:{0}" -f $Port) 2>&1 | Out-Host
	} else {
		Write-Host "Funnel /monday-webhook already configured"
	}
}
