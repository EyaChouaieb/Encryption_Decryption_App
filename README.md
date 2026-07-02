Encryption & Decryption App

Description:
A simple desktop app built with Kivy that lets you encrypt or decrypt messages using a custom cipher. It combines a numeric-key shifting cipher (for letters, numbers, and symbols) with Morse code translation, and automatically copies the result to your clipboard.

Features;
- Encrypt or decrypt any text message
- Uses a secret numeric code as the cipher key
- Combines alphanumeric shifting with Morse code encoding
- Copies the translated result directly to your clipboard

Requirements:
- Python 3
- Kivy

Install Kivy with:
pip install kivy

How to Run:
1. Make sure encryption_and_decryption.py and pngwing.com.png are in the same folder.
2. Run the script:
python encryption_and_decryption.py

How to Use:
1. Type Encrypt or Decrypt in the first input field.
2. Enter the message you want to translate.
3. Enter your secret numeric code (this acts as the cipher key).
4. Press TRANSLATE.
5. The result appears on screen and is automatically copied to your clipboard.

Notes:
- The secret code must be numeric.
- The same code must be used to decrypt a message that was encrypted with it.
