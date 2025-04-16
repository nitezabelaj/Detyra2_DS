from PIL import Image
import json

# Po e hapim fajllin key.json per me i kthy ngjyrat ne karaktere
with open('key.json', 'r') as f:
    key = json.load(f)

# Kthejm çelesin ne format ku ngjyra eshte  çelesi, e karakteri eshte vlera
reverse_key = {v.upper(): k for k, v in key.items()}

# Parametrat qe na duhen
block_size = 20                     # Madhesia e bllokut 20x20 piksel
padding_color = (255, 255, 255)     # Ngjyra e bardhe qe e kemi përdor si padding

# Hapim imazhin ku jan te kodume karakteret
img = Image.open('output.png')
pixels = img.load()                # Marrim qasjen te pikslat
width, height = img.size           # Madhesia e imazhit
grid_size = width // block_size    # Sa blloqe ka per nje rresht ose kolone

# Ketu fillojme me kriju tekstin e dekriptum//inputi mu marr prej konsoles
decrypted_text = ""

# E bojmë loop per secilin rresht e kolone ne rrjeten e blloqeve
for row in range(grid_size):
    for col in range(grid_size):
        start_x = col * block_size     # Koordinata X ku fillon blloku
        start_y = row * block_size     # Koordinata Y ku fillon blloku

        # Marrim ngjyren e pikes qe eshte ne mes te bllokut
        sample_x = start_x + block_size // 2
        sample_y = start_y + block_size // 2
        color_rgb = pixels[sample_x, sample_y]
        # Nese e hasim padding-un (ngjyren e bardhe), e kalojme qet bllok
        if color_rgb == padding_color:
            continue

        # E konvertojme ngjyren RGB ne hexadecimal format
        color_hex = '#%02x%02x%02x' % color_rgb

        # Marrim karakterin perkates per qet ngjyre – nese nuk ekziston, vendos '?'
        char = reverse_key.get(color_hex.upper(), '?')

        # Shtojme karakterin ne tekstin final te dekriptuar
        decrypted_text += char

# Printojme tekstin e dekriptuar ne fund
print("Teksti i dekriptuar:")
print(decrypted_text)