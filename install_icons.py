from PIL import Image
import os, shutil

img = Image.open("quiz_icon.png").convert("RGBA")

sizes = {
    "mipmap-mdpi":    48,
    "mipmap-hdpi":    72,
    "mipmap-xhdpi":   96,
    "mipmap-xxhdpi":  144,
    "mipmap-xxxhdpi": 192,
}

base = "./app/src/main/res"

for folder, size in sizes.items():
    path = os.path.join(base, folder)
    os.makedirs(path, exist_ok=True)
    resized = img.resize((size, size), Image.LANCZOS)
    resized.save(os.path.join(path, "ic_launcher.png"))
    resized.save(os.path.join(path, "ic_launcher_round.png"))
    print(f"✅ {folder}: {size}x{size}px")

print("All icons installed.")
