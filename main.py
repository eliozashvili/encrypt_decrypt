from random import shuffle
from string import ascii_letters, punctuation, digits

chars = list(" " + punctuation + digits + ascii_letters)
key = chars.copy()
shuffle(key)
# encrypt
plain_text = input("Input message to encrypt: ")
cipher_text = ""
# we loop over plain_text to get a letter
# then we get the index of letter in key[]
# then we find a character in chars[]
# finally we append those characters to cipher_text
for letter in plain_text:
    cipher_text += chars[key.index(letter)]

print(plain_text)
print(cipher_text)
# decrypt
cipher_text = input("Input message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    plain_text += key[chars.index(letter)]

print(cipher_text)
print(plain_text)
