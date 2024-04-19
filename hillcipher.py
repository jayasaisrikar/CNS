import numpy as np

def encrypt(message, key_matrix):
    message = message.upper().replace(" ", "")
    n = len(key_matrix)
    message += "X" * ((-len(message)) % n)
    return "".join([chr(sum(key_matrix[i][j] * (ord(char) - 65) % 26 for j, char in enumerate(message[k:k+n])) % 26 + 65) for k in range(0, len(message), n) for i in range(n)])

def decrypt(encrypted_message, key_matrix):
    determinant = int(round(np.linalg.det(key_matrix)))
    adjugate = np.round(np.linalg.inv(key_matrix) * determinant) % 26
    return "".join([chr(int(sum(adjugate[i][j] * (ord(char) - 65) % 26 for j, char in enumerate(encrypted_message[k:k+len(key_matrix)])) % 26) + 65) for k in range(0, len(encrypted_message), len(key_matrix)) for i in range(len(key_matrix))])

# Dynamic inputs
message = input("Enter the message to encrypt: ")
key_matrix = np.array([[17, 17, 5], [18, 21, 2], [2, 19, 0]])

# Encryption
encrypted_message = encrypt(message, key_matrix)
print("Encrypted message:", encrypted_message)

# Decryption
decrypted_message = decrypt(encrypted_message, key_matrix)
print("Decrypted message:", decrypted_message)