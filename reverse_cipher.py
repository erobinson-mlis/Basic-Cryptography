# Reverse Cipher
# https://www.nostarh.crackingcodes/ (BSD Licensed)

import os

message = input('Please enter a message you would like to encrypt: \n')

translated = ''

i = len(message) -1
while i >= 0:
    translated = translated + message[i]
    print(translated)
    i = i - 1

#os.system('clear')
print(f'Your encrypted/decrypted message is below.\n{translated}\n')

