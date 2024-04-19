def affine_encrypt(text):
    encrypted_text = ''.join([chr(((3 * (ord(char) - 65) + 12) % 26) + 65) if char.isalpha() else char for char in text.upper()])
    return encrypted_text

def affine_decrypt(encrypted_text):
    decrypted_text = ''.join([chr(((9 * (ord(char) - 65 - 12)) % 26) + 65) if char.isalpha() else char for char in encrypted_text.upper()])
    return decrypted_text

# Dynamic input
text = input("Enter the text: ")

encrypted_text = affine_encrypt(text)
print("Encrypted text:", encrypted_text)

decrypted_text = affine_decrypt(encrypted_text)
print("Decrypted text:", decrypted_text)
