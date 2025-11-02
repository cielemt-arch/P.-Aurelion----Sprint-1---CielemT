# Ejecuta todos los tests unitarios en el proyecto con salida detallada
Write-Host "Ejecutando tests..."
python -m unittest discover -v
$LASTEXITCODE
