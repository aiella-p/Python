# Encrytion/Edcryption program
import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits

chars = list(chars) # string of characters will be typecasted as list
key = chars.copy() # copying the original list using copy method...

random.shuffle(key) # Here we are shuuffle the key .....all the charachters are shuffled in random order...
# If some body try to enter some text to be encrypted it will be relaced every instance of one character within that string..
# Ex:  
print(f" CHARS: {chars} ")
print(f" KEY: {key} ")

# ENCRYPT - converting plain text to cipher text is called ENCRYPTION........reverse process is  called DECRYPTION...
plain_text = input("Enter a message to encrypt: ")
cipher_text = " " # ciphers are secret code...usually one that's created using mathematical algorithm

# For every letter on plain text get the index of each letter then refer to the key at new charcter in the Encrpted message 
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f" Original message: {plain_text} ")
print(f" Encrypted message: {cipher_text} ")

# DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = " "

# For every letter on plain text get the index of each letter then refer to the key at new charcter in the Encrpted message 
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f" Encrypted message: {cipher_text} ")
print(f" Original message: {plain_text} ")
