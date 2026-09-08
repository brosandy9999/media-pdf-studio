$ProgressPreference = 'SilentlyContinue'
$url = "https://github.com/mozilla/pdf.js/releases/download/v4.5.136/pdfjs-4.5.136-dist.zip"
$zipPath = "pdfjs.zip"
$extractPath = "template/pdfjs"

Write-Host "Downloading PDF.js..."
Invoke-WebRequest -Uri $url -OutFile $zipPath

Write-Host "Extracting..."
Expand-Archive -Path $zipPath -DestinationPath $extractPath -Force

Write-Host "Cleaning up..."
Remove-Item -Path $zipPath

Write-Host "Done."
