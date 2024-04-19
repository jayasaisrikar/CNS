def rail_fence_encrypt(plaintext, rails):
    encrypted_text = ""
    for i in range(rails):
        encrypted_text += ''.join([plaintext[j] for j in range(i, len(plaintext), rails)])
    return encrypted_text

def rail_fence_decrypt(ciphertext, rails):
    cycle_length = 2 * rails - 2
    plaintext = [''] * len(ciphertext)
    for i in range(len(ciphertext)):
        j = i % cycle_length
        if j < rails:
            plaintext[i] = ciphertext[j * (len(ciphertext) // cycle_length) + i // cycle_length]
        else:
            plaintext[i] = ciphertext[(cycle_length - j) * (len(ciphertext) // cycle_length) + i // cycle_length]
    return ''.join(plaintext)

# Dynamic input
plaintext = input("Enter the plaintext: ")
rails = int(input("Enter the number of rails: "))

encrypted_text = rail_fence_encrypt(plaintext, rails)
print("Encrypted text:", encrypted_text)

decrypted_text = rail_fence_decrypt(encrypted_text, rails)
print("Decrypted text:", decrypted_text)
