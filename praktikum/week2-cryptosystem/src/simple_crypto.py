def caesar_cipher_encrypt(plaintext, key_string):

    shift = sum(int(digit) for digit in key_string if digit.isdigit())

    encrypted_text = ""

    for char in plaintext:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char

    return shift, encrypted_text


plaintext = "Kingkin Kurnia Candrawati"
key_string = "230202813"

shift, ciphertext = caesar_cipher_encrypt(plaintext, key_string)

print("Plaintext :", plaintext)
print("Key       :", key_string)
print("Output    :", ciphertext)
