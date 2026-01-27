$baseDir = "d:\強匠鎖店\openlock\digital-locks"
$files = Get-ChildItem "$baseDir\*.html"

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    # 修正相對路徑
    # 匹配 "image": ["../assets/images/..." 或 "image": "../assets/images/..."
    $content = $content -replace '"image":\s*\[?"\.\./assets/images/([^"]+)"', '"image": ["https://openlock.tw/assets/images/$1"'
    
    # 修正 DDL702-FVP 等頁面的錯誤網域
    $content = $content -replace 'https://www\.openlock\.com\.tw/images/products/', 'https://openlock.tw/assets/images/service-digital-locks/philips/'
    
    Set-Content $file.FullName $content -Encoding UTF8
    Write-Host "Updated $($file.Name)"
}
