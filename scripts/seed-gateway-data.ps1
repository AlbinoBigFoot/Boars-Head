# Seed Ignition data dirs from official images (required once on empty host bind mounts).
# Run from repo root before first `docker compose up` if gateways/*/data are empty.

$ErrorActionPreference = "Stop"

New-Item -ItemType Directory -Force -Path gateways\standard\data, gateways\edge\data | Out-Null

function Seed-GatewayData {
  param(
    [string]$Image,
    [string]$TargetDir,
    [string]$TempName
  )
  docker rm -f $TempName 2>$null | Out-Null
  docker create --name $TempName $Image | Out-Null
  docker cp "${TempName}:/usr/local/bin/ignition/data/." $TargetDir
  docker rm $TempName | Out-Null
  Write-Host "Seeded $TargetDir from $Image"
}

Seed-GatewayData -Image "inductiveautomation/ignition:8.1.43" -TargetDir "gateways\standard\data" -TempName "bh-seed-std"
Seed-GatewayData -Image "inductiveautomation/ignition:8.3.7" -TargetDir "gateways\edge\data" -TempName "bh-seed-edge"

Write-Host "Done. Next: docker compose up -d"
