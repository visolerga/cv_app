# Patterns to exclude (case-insensitive)
$excluded_patterns = @("envCV", "__pycache__")

$output = tree /F /A
$output | Out-File -FilePath "raw_output.txt" -Encoding UTF8
Write-Host "Output sin filtrar guardado en raw_output.txt"


$filtered_output = $output -split "`n" | ForEach-Object {
    $line = $_
    $is_excluded = $excluded_patterns | ForEach-Object { $line -match $_ }

    # Mostrar información de depuración
    Write-Host "Procesando línea: $line"
    Write-Host "Excluida: $is_excluded"

    if (-not $is_excluded) {
        $line  # Devuelve la línea si no es excluida
    }
}
