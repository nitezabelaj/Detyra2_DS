from PIL import Image  #
import json


with open('key.json', 'r') as f:
    key = json.load(f)


text = "HELLO WORLD"
text_len = len(text)


block_size = 20
grid_size = 10
img_size = grid_size * block_size
padding_color = (255, 255, 255)