from PIL import Image  #
import json             # Importojme json-in për me lexu çelesin nga fajlli .json
import math             # Importojme math ne rast qe na duhet me bo llogaritje matematikore

# Po e hapim fajllin key.json edhe po e ngarkojme çelesin
with open('key.json', 'r') as f:
    key = json.load(f)

# Teksti qe po dojme me e enkriptu
text = "HELLO WORLD"
text_len = len(text)  # Gjatesia e tekstit (sa shkronja i ka)

# Parametrat
block_size = 20       # Madhesia e çdo blloku ngjyrash ne piksel (20x20)
grid_size = 10        # Madhesia e rrjetes, dmth 10 rreshta me 10 kolona
img_size = grid_size * block_size  #llogarit madhesinë totale te fotos në piksel
padding_color = (255, 255, 255)    # Ngjyra per padding - e bardhe

# Llogarit sa blloqe ka gjithsej ne foto
total_blocks = grid_size * grid_size

# Llogarit ku me fillu tekstin qe me qene ne mes të imazhit
start_index = (total_blocks - text_len) // 2

# Krijon ni imazh te ri, komplet te bardhe
img = Image.new('RGB', (img_size, img_size), color=padding_color)
pixels = img.load()  # Merr qasjen per me ndryshu pikselat e imazhit

# Qetu po i vendosim shkronjat nje nga nje prej qendres
for i, char in enumerate(text):
    pos = start_index + i          # Pozita prej ku fillon vendosja
    row = pos // grid_size         # Llogarit rreshtin
    col = pos % grid_size          # Llogarit kolonen

    start_x = col * block_size     # Koordinata x e fillimit per bllokun
    start_y = row * block_size     # Koordinata y e fillimit per bllokun

    # Merr ngjyren per shkronjen perkatese prej key.json
    color_hex = key.get(char.upper(), "#FFFFFF")
    # Kthen ngjyren prej hexadecimal në RGB format
    color_rgb = tuple(int(color_hex.lstrip("#")[j:j+2], 16) for j in (0, 2, 4))


    # Mbush krejt bllokun 20x20 me ngjyren e shkronjes
    for x in range(start_x, start_x + block_size):
        for y in range(start_y, start_y + block_size):
            pixels[x, y] = color_rgb  # Vendose ngjyren te pikseli

# Ruan imazhin e krijum
img.save("output.png")
print("Fotoja u krijua me sukses si ""output.png"".")  # Tregon qe gjithçka ka perfundu me sukses



