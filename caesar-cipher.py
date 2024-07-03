# Caesar Cipher
# adapted from Al Sweigart https://www.nostarch.com/crackingcodes/ (used under BSD License)

import pyperclip


# Global variables
# The ecryption/decryption key
KEY = 13
# Every possible symbol that can be encrypted: 
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

print('''

░█▀▀░█▀█░█▀▀░█▀▀░▀█▀░█▀▀░█▄█░█▀█
░█░░░█▀█░█▀▀░▀▀█░░█░░█░█░█░█░█▀█
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀

Welcome to the Caesigma Machine.''')

# Choose whether the program encrypts or decrypts
mode_sel = input('Would you like to encrypt (E) or decrypt (D): ' )
if mode_sel == 'E' or mode_sel == 'e':
    mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.
elif mode_sel == 'D' or mode_sel == 'd':
     mode = 'decrypt'

# The string to be encrypted/decrypted:
original_message = input('Please input a message: \n')


# Store the encrypted/decrypted form of the message:
new_message = ''

# Shift characters and add to the new message
for symbol in original_message:
        # Note: Only symbols within the the SYMBOLS string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + KEY
            elif mode =='decrypt':
                 translatedIndex = symbolIndex - KEY
            
            # Handle wraparound, if needed
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