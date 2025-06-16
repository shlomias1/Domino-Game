from PIL import Image
import os
os.environ["NUMBA_DISABLE_JIT"] = "1"
from rembg import remove

# Load the domino image sheet
sheet_path = r"C:/Users/shlomias/Downloads/Domino/images/dominoes/domino_white.png"
sheet = Image.open(sheet_path)

# Set grid dimensions
cols, rows = 7, 4  # 7 tiles per row, 4 rows = 28 tiles
tile_width = sheet.width // cols
tile_height = sheet.height // rows

# Prepare output directory
output_dir = r"C:/Users/shlomias/Downloads/Domino/images/dominoes/"
os.makedirs(output_dir, exist_ok=True)

# Crop and save each tile
tile_values = [(i, j) for i in range(7) for j in range(i, 7)]
tile_index = 0
for row in range(rows):
    for col in range(cols):
        if tile_index >= len(tile_values):
            break

        left = col * tile_width
        upper = row * tile_height
        right = left + tile_width
        lower = upper + tile_height

        tile = sheet.crop((left, upper, right, lower))
        a, b = tile_values[tile_index]
        filename = f"domino-{a}-{b}.png"
        tile.save(os.path.join(output_dir, filename))
        tile_index += 1

print(f"✔️ Done! Saved {tile_index} tiles to: {output_dir}")