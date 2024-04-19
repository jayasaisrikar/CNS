def generate_autokey(plaintext, key):
    autokey = key.upper()
    for char in plaintext:
        if char.isalpha():
            autokey += char.upper()
    return autokey

def autokey_encrypt(plaintext, key):
    ciphertext = ""
    autokey = generate_autokey(plaintext, key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(autokey[i]) - 65
            if char.islower():
                ciphertext += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                ciphertext += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:
            ciphertext += char
    return ciphertext

def autokey_decrypt(ciphertext, key):
    plaintext = ""
    autokey = generate_autokey(ciphertext, key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(autokey[i]) - 65
            if char.islower():
                plaintext += chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                plaintext += chr(((ord(char) - 65 - shift) % 26) + 65)
            autokey += plaintext[-1].upper()
        else:
            plaintext += char
    return plaintext

# Dynamic input
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

encrypted_text = autokey_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = autokey_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
