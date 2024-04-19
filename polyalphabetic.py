def generate_key_stream(plaintext, key):
    key_stream = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            key_stream += key[key_index % len(key)].upper()
            key_index += 1
        else:
            key_stream += char
    return key_stream

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_stream = generate_key_stream(plaintext, key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key_stream[i]) - 65
            if char.islower():
                ciphertext += chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                ciphertext += chr(((ord(char) - 65 + shift) % 26) + 65)
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_stream = generate_key_stream(ciphertext, key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key_stream[i]) - 65
            if char.islower():
                plaintext += chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                plaintext += chr(((ord(char) - 65 - shift) % 26) + 65)
        else:
            plaintext += char
    return plaintext

# Dynamic input
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
