# Reverse Cipher
# adapted from https://www.nostarh.crackingcodes/ (used under BSD License)

import os

original_message = input('Please enter a message you would like to encrypt: \n')

new_message = ''

i = len(original_message) -1
while i >= 0:
    new_message = new_message + original_message[i]
    
    # uncomment this line to view the substitution character by character.
    #print(new_message)  
    
    i = i - 1

# comment out this line retain the original message on the screen after processing.
os.system('clear')       

print(f'\nYour encrypted/decrypted message is below.\n\n{new_message}\n')

