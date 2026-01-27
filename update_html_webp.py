import os
import re
from pathlib import Path
from bs4 import BeautifulSoup

def update_html():
    base_dir = Path("d:/強匠鎖店/openlock")
    html_files = list(base_dir.rglob("*.html"))
    count = 0
    
    # Pattern to match image extensions in common attributes
    img_ext_pattern = re.compile(r'\.(jpg|jpeg|png)$', re.IGNORECASE)

    print(f"Updating HTML files in {base_dir}...")

    for html_path in html_files:
        modified = False
        try:
            with open(html_path, "r", encoding="utf-8") as f:
                content = f.read()
                soup = BeautifulSoup(content, "html.parser")

            # 1. Update <img> src
            for img in soup.find_all("img", src=True):
                src = img["src"]
                if img_ext_pattern.search(src):
                    new_src = img_ext_pattern.sub('.webp', src)
                    img["src"] = new_src
                    modified = True

            # 2. Update <link> href (like favicons if they were png/jpg)
            for link in soup.find_all("link", href=True):
                href = link["href"]
                if img_ext_pattern.search(href):
                    new_href = img_ext_pattern.sub('.webp', href)
                    link["href"] = new_href
                    modified = True

            # 3. Update style attributes (inline background-image)
            for tag in soup.find_all(style=True):
                style = tag["style"]
                if "url(" in style and img_ext_pattern.search(style):
                    new_style = img_ext_pattern.sub('.webp', style)
                    tag["style"] = new_style
                    modified = True

            if modified:
                # Use formatter=None to avoid BeautifulSoup changing entities
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(soup.decode(formatter="html"))
                print(f"Updated: {html_path.relative_to(base_dir)}")
                count += 1

        except Exception as e:
            print(f"Error processing {html_path}: {e}")

    print(f"\nHTML Update Finished!")
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    update_html()
