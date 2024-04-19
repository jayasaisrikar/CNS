import pyDes

def des_encrypt(plaintext, key):
    des = pyDes.des(key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_text = des.encrypt(plaintext)
    return encrypted_text

def des_decrypt(ciphertext, key):
    des = pyDes.des(key, pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    decrypted_text = des.decrypt(ciphertext)
    return decrypted_text

# Dynamic input
plaintext = input("Enter the plaintext: ")
key = input("Enter the 8-byte key: ")

encrypted_text = des_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = des_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
