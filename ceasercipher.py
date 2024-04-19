def caesar_cipher(text, shift):
    encrypted_text = ''.join([chr(((ord(char) - 65 + shift) % 26) + 65) if char.isalpha() else char for char in text.upper()])
    return encrypted_text

def caesar_decipher(text, shift):
    decrypted_text = ''.join([chr(((ord(char) - 65 - shift) % 26) + 65) if char.isalpha() else char for char in text.upper()])
    return decrypted_text

# Dynamic input
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_decipher(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
