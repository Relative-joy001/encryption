import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)


#print(f"Chars: {chars}")
#print(f"keys: {key}")


# Encryption

plaintext = input("Enter the message to encrypt: ")

ciphertext = " "

for letter in plaintext:
    index = chars.index(letter)
    ciphertext += key[index]


print(f"Original Message: {plaintext}")
print(f"Encripted Message: {ciphertext}")


# Decrypt

ciphertext = input("Enter the message to decrypt: ")

plaintext = " "



for letter in ciphertext:
    index = key.index(letter)
    plaintext += chars[index]



print(f"Decripted Message: {ciphertext}")
print(f"Original Message: {plaintext}")