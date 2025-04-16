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
