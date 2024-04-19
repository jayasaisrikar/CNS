def caesar_encrypt(message, shift):
    encrypted_message = "".join([chr(((ord(char) - 65 + shift) % 26) + 65) if char.isalpha() else char for char in message.upper()])
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    decrypted_message = "".join([chr(((ord(char) - 65 - shift) % 26) + 65) if char.isalpha() else char for char in encrypted_message.upper()])
    return decrypted_message

# Dynamic input
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted_message = caesar_encrypt(message, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = caesar_decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)
