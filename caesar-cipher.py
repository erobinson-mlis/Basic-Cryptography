# Caesar Cipher
# adapted from Al Sweigart https://www.nostarch.com/crackingcodes/ (used under BSD License)

import pyperclip

# The string to be encrypted/decrypted:
original_message = input('Please input a message: \n')

# The ecryption/decryption key
KEY = 13

# Whether the program encrypts or decrypts
mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted: 
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# store the encrypted/decrypted form of the message:
new_message = ''

for symbol in original_message:
        # Note: Only symbols within the the SYMBOLS string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + KEY
            elif mode =='decrypt':
                 translatedIndex = symbolIndex - KEY
            
            # Handle wraparound if needed
            if translatedIndex >= len(SYMBOLS):
                 translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                 translatedIndex = translatedIndex + len(SYMBOLS)

            new_message = new_message + SYMBOLS[translatedIndex]
        
        else:
            # Append the symbol without encrypting/decrypting
            new_message = new_message + symbol

# Output the tranlsated string
print(new_message)
pyperclip.copy(new_message)