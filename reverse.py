# reverse.py
# takes a string of any length and returns an inversion of it


plaintext = input('Enter a string that you would like to encrypt: ')

s = plaintext.split()
length = len(s)

print(f'string is {length} characters long')
new_string = []
i = length

while i >= 0: 
    new_string.prepend(s[i])
    i += 1
print(s)
