# Transposition Cipher Encrypt/Decrypt File
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'the_time_machine.encrypted.txt'

    # BE CAREFUL! If a file with the outputFilename name already exists,
    # this program will overwrite that file:
    outputFilename = 'the_time_machine.3.txt'
    myKey = 15
    myMode = 'decrypt' # Set to 'encrypt' or 'decrypt'.
    
    # If the input file does not exist, the program terminates early:
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...' % (inputFilename))
        sys.exit()

    # If the output file already exists, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (C)ontinue or (Q)uit?' %
              (outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()
    
    # Read in the message from the input file:
    with open(inputFilename, 'r') as fileObj:
        content = fileObj.read()
    
    print('%sing...' % (myMode.title()))

    # Measure how long the 
    # cencryption/decryption takes:
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 4)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # Write out the translated message to the output file:
    with open(outputFilename, 'w') as outputFileObj:
        outputFileObj.write(translated)
    
    print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))

# If transpositionCipherFile.py is run (instead of imported as a module),   
# call the main() function:
if __name__ == '__main__':
    main()