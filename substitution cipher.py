import random

def generate_key():
    letters = [chr(i) for i in range(65, 91)]
    random.shuffle(letters)
    return {chr(i + 65): letters[i] for i in range(26)}

def substitution_encrypt(message, key):
    encrypted_message = "".join([key[char] if char.isalpha() else char for char in message.upper()])
    return encrypted_message

def substitution_decrypt(encrypted_message, key):
    inverted_key = {v: k for k, v in key.items()}
    decrypted_message = "".join([inverted_key[char] if char.isalpha() else char for char in encrypted_message.upper()])
    return decrypted_message

# Dynamic input
message = input("Enter the message: ")
key = generate_key()

encrypted_message = substitution_encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = substitution_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
