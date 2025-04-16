# Detyra2_DS
This project was made for assignment in Data Security class 2025
# How to execute the program:
This project consists of two main Python scripts:

encrypt.py – used to encrypt a message into a graphical image

decrypt.py – used to decrypt the message from the image
# Encrypting the Message
1.Open your terminal or command prompt.

2.Navigate to the project directory.

3.Run the encryption script: encrypt.py
# What happens during encryption:
The text "HELLO WORLD" is defined as the message to be encrypted.

Each character is mapped to a unique color based on a predefined key from key.json.

A grid image (output.png) is generated, where each 20x20 pixel block represents one character.

The message is centered in a 10x10 grid.

Empty blocks are filled with white color as padding.

# Examples from execution:

![Ekzekutimi encrypt](https://github.com/user-attachments/assets/ed2f5ddb-cf80-4dc6-a943-daefd79f0532)

![output png](https://github.com/user-attachments/assets/545f4b0d-ef48-425d-b1e1-c759ec9b51b3)
# Decrypting the Message
1.After generating the output.png, run the decryption script: decrypt.py
# What happens during decryption:
The image output.png is opened and processed.

Each colored block is checked against the key in key.json.

If a match is found, the corresponding character is retrieved.

The entire original message is reconstructed and printed to the terminal.
# Reconstructs the Text
If a block color matches a character from the key, that character is added to the output string.

If the block is white or unrecognized, it is skipped (assumed to be padding or empty space).

The final message is printed out.
# Examples from execution:
![Ekzekutimi decrypt](https://github.com/user-attachments/assets/98f795eb-c53f-4bc9-836e-bf4cee70a8ad)

