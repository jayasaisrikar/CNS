def generate_key_order(key):
    key_order = sorted(enumerate(key), key=lambda x: x[1])
    return [index for index, _ in key_order]

def columnar_encrypt(plaintext, key):
    key_order = generate_key_order(key)
    num_columns = len(key)
    num_rows = (len(plaintext) + num_columns - 1) // num_columns
    matrix = [[''] * num_columns for _ in range(num_rows)]
    
    for index, char in enumerate(plaintext):
        row = index // num_columns
        col = key_order[index % num_columns]
        matrix[row][col] = char
    
    encrypted_text = ''.join(''.join(row) for row in matrix)
    return encrypted_text

def columnar_decrypt(ciphertext, key):
    key_order = generate_key_order(key)
    num_columns = len(key)
    num_rows = (len(ciphertext) + num_columns - 1) // num_columns
    matrix = [[''] * num_columns for _ in range(num_rows)]
    
    # Populate the matrix with ciphertext characters in column order
    for index, char in enumerate(ciphertext):
        row = index // num_rows
        col = index % num_rows
        matrix[col][key_order[row]] = char
    
    decrypted_text = ''.join(''.join(row) for row in matrix)
    return decrypted_text

# Dynamic input
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

encrypted_text = columnar_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = columnar_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
