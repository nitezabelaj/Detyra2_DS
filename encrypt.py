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