
# ----- Your Algorithm -----

# Your task is to encrypt this secret message into ciphertext


#
#  Initialize your ciphertext an empty string

def CaesarCipher (plaintext):
    plaintext = plaintext
    ciphertext = ""
    for character in plaintext:
        number = ord(character)
        encrypted_character = chr(number+6)
        ciphertext += encrypted_character
    print(ciphertext)

plaintext = "This is a secret message."
ciphertext = ""
for character in plaintext:
    # do something to the character to encrypt it
    # YOUR CODE HERE
    number = ord(character)
    encrypted_character = chr(number+6)# CHANGE THIS!
    ciphertext += encrypted_character

print(ciphertext)

CaesarCipher("This is a secret message.")

