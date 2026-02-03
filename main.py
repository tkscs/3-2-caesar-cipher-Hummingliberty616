
# ----- Your Algorithm -----

# Your task is to encrypt this secret message into ciphertext


#
#  Initialize your ciphertext an empty string

plaintext = "This is a secret message."
ciphertext = ""
for character in plaintext:
    # do something to the character to encrypt it
    # YOUR CODE HERE
    number = ord(character)
    ascii_letter = chr(number+6)
    encrypted_character = ascii_letter # CHANGE THIS!
    ciphertext += encrypted_character

print(ciphertext)

