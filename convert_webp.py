import os
from pathlib import Path
from PIL import Image

def convert_to_webp():
    base_dir = Path("d:/強匠鎖店/openlock/assets/images")
    extensions = (".jpg", ".jpeg", ".png")
    count = 0
    errors = 0

    print(f"Starting conversion in {base_dir}...")

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(extensions):
                img_path = Path(root) / file
                webp_path = img_path.with_suffix(".webp")
                
                # Skip if webp already exists (unless you want to overwrite)
                # if webp_path.exists():
                #     continue

                try:
                    with Image.open(img_path) as img:
                        # Convert RGBA to RGB if saving as JPEG-like webp, 
                        # but WebP supports alpha, so we just save.
                        img.save(webp_path, "WEBP", quality=85)
                        print(f"Converted: {img_path.relative_to(base_dir)} -> .webp")
                        count += 1
                except Exception as e:
                    print(f"Error converting {img_path}: {e}")
                    errors += 1

    print(f"\nConversion Finished!")
    print(f"Successfully converted: {count}")
    print(f"Failed: {errors}")

if __name__ == "__main__":
    convert_to_webp()
