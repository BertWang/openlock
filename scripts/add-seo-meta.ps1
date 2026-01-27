# SEO Meta Batch Add Script
# Add canonical URL and Twitter Card to product pages

$productFiles = @(
    "AS850", "DDL702-FVP", "DDL702E", "DDL703k", "DDL705E", "DDL709-FVP",
    "MDL-400F", "MDL-7150", "MI-570F", "MI-570S", "MI-6450", "MI-6500F",
    "ML660", "P70MAX", "SENSORS-K1", "SENSORS-S1", "SENSORS-V8", "SR60MAX", "SY30MAX"
)

$basePath = "d:\強匠鎖店\openlock\digital-locks"

foreach ($file in $productFiles) {
    $filePath = Join-Path $basePath "$file.html"
    if (-not (Test-Path $filePath)) {
        Write-Host "File not found: $filePath" -ForegroundColor Yellow
        continue
    }
    
    $content = Get-Content $filePath -Raw -Encoding UTF8
    
    # Check if canonical already exists
    if ($content -match 'rel="canonical"') {
        Write-Host "Already has canonical: $file.html" -ForegroundColor Green
        continue
    }
    
    # Extract og:title and og:description from content
    $ogTitle = ""
    $ogDesc = ""
    
    if ($content -match 'og:title"\s+content="([^"]+)"') {
        $ogTitle = $matches[1]
    }
    elseif ($content -match '<title>([^<]+)</title>') {
        $ogTitle = $matches[1]
    }
    
    if ($content -match 'og:description"[\s\S]*?content="([^"]+)"') {
        $ogDesc = $matches[1]
    }
    elseif ($content -match 'name="description"[\s\S]*?content="([^"]+)"') {
        $ogDesc = $matches[1]
    }
    
    # Build Twitter Card and canonical tags
    $twitterCard = @"

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="$ogTitle" />
  <meta name="twitter:description" content="$ogDesc" />
  <meta name="twitter:image" content="https://openlock.tw/assets/images/service-digital-locks/og-default.webp" />
  <!-- Canonical URL -->
  <link rel="canonical" href="https://openlock.tw/digital-locks/$file.html" />
"@
    
    # Find Bootstrap CSS link position and insert before it
    if ($content -match '(\s*<!-- Bootstrap 5\.3 -->)') {
        $insertPoint = $matches[1]
        $newContent = $content -replace [regex]::Escape($insertPoint), "$twitterCard`r`n`r`n$insertPoint"
        
        [System.IO.File]::WriteAllText($filePath, $newContent, [System.Text.Encoding]::UTF8)
        Write-Host "Processed: $file.html" -ForegroundColor Cyan
    }
    else {
        Write-Host "Insert point not found: $file.html" -ForegroundColor Red
    }
}

Write-Host "Done!" -ForegroundColor Green
