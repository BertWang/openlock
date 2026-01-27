import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup

def check_resources():
    base_dir = Path("d:/強匠鎖店/openlock")
    html_files = list(base_dir.rglob("*.html"))
    results = []
    
    print(f"Total HTML files found: {len(html_files)}")
    
    for html_path in html_files:
        relative_html = html_path.relative_to(base_dir)
        print(f"Scanning {relative_html}...")
        
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "html.parser")
                
                # Check <a> tags
                for a in soup.find_all("a", href=True):
                    href = a["href"].split("?")[0].split("#")[0]
                    if not href or href.startswith(("tel:", "mailto:", "javascript:", "http:", "https:")):
                        continue
                    
                    # Resolve relative path
                    target_path = (html_path.parent / href).resolve()
                    if not target_path.exists():
                        results.append({
                            "file": str(relative_html),
                            "type": "LINK",
                            "target": href,
                            "status": "404 NOT FOUND"
                        })
                
                # Check <img> tags
                for img in soup.find_all("img", src=True):
                    src = img["src"].split("?")[0].split("#")[0]
                    if not src or src.startswith("http"):
                        continue
                    
                    target_path = (html_path.parent / src).resolve()
                    if not target_path.exists():
                        results.append({
                            "file": str(relative_html),
                            "type": "IMAGE",
                            "target": src,
                            "status": "404 NOT FOUND"
                        })
        except Exception as e:
            print(f"Error reading {relative_html}: {e}")

    # Output to File
    report_file = base_dir / "link_audit_report.json"
    with open(report_file, "w", encoding="utf-8") as j:
        json.dump(results, j, indent=4, ensure_ascii=False)

    # Print Summary (ASCII friendly)
    if not results:
        print("\nSUCCESS: All links and images are valid!")
    else:
        print(f"\nFAILED: Found {len(results)} broken resources.")
        print(f"Detailed report saved to: {report_file}")
        for res in results[:20]:  # Show first 20 in console
            print(f"[{res['type']}] {res['file']} -> {res['target']}")

if __name__ == "__main__":
    check_resources()
