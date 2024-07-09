# Caesar Cipher
# adapted from Al Sweigart https://www.nostarch.com/crackingcodes/ (used under BSD License)

import os
import pyperclip as pc

# Global variables
# The ecryption/decryption key
KEY = 13
# Every acceptable symbol that can be encrypted: 
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890!?.`~@#$%^&*()_+-=[]|;:<>,/'

print('''

░█▀▀░█▀█░█▀▀░█▀▀░▀█▀░█▀▀░█▄█░█▀█
░█░░░█▀█░█▀▀░▀▀█░░█░░█░█░█░█░█▀█e
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀

Welcome to the Caesigma Machine.''')


# Choose whether the program encrypts or decrypts
mode_sel = input('Would you like to encrypt (E) or decrypt (D):' )
if mode_sel == 'E' or mode_sel == 'e':
    mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.
elif mode_sel == 'D' or mode_sel == 'd':
    mode = 'decrypt'


# The string to be encrypted/decrypted:
original_message = input('\nPlease input a message:\n')

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


# Attach the string to the system clipboard
pc.copy(new_message)

# Print message from clipboard
print(new_message)