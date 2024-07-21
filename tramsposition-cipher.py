# Transposition Cipher Encryption
# adapted from Sweogart, *Cracking Codes with Python*
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)
# Adapted by Eric Robinson
# Released under BSD License

import pyperclip


def main():
    myMessage = input('Please enter a message to encrypt suing the transposition cipher:\n')
    myKey = int(input('Please enter the transposition key you would like to use: '))

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen with
    # a | after it, in case there are spaces at the end of the 
    # encrypted message.
    print(ciphertext + '|')

    # copy the encrypted string in ciphertext to the clipboard
    pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            # Place the character at the currentIndex into the message 
            # at the end of the current column in the ciphertext list. 
            ciphertext[column] += message[currentIndex]
            # Move currentIndex over one position
            currentIndex += key
    
    # Convert the ciphertext list into a single string value and return it.

    return ''.join(ciphertext)

# If transpositionEncrypt.py is run (instead of imported as a module), 
# call the main function
if __name__== '__main__':
    main()
