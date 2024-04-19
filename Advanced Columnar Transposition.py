def generate_primary_key_order(key):
    primary_key_order = sorted(enumerate(key), key=lambda x: x[1])
    return [index for index, _ in primary_key_order]

def generate_secondary_key_order(secondary_key):
    return sorted(enumerate(secondary_key), key=lambda x: x[1])

def advanced_columnar_encrypt(plaintext, primary_key, secondary_key):
    primary_key_order = generate_primary_key_order(primary_key)
    secondary_key_order = generate_secondary_key_order(secondary_key)
    num_columns = len(primary_key)
    num_rows = (len(plaintext) + num_columns - 1) // num_columns
    matrix = [[''] * num_columns for _ in range(num_rows)]

    for index, char in enumerate(plaintext):
        row = index // num_columns
        col = primary_key_order[index % num_columns]
        matrix[row][col] = char
    
    encrypted_text = ""
    for col in secondary_key_order:
        for row in range(num_rows):
            encrypted_text += matrix[row][col[0]]
    
    return encrypted_text

def advanced_columnar_decrypt(ciphertext, primary_key, secondary_key):
    primary_key_order = generate_primary_key_order(primary_key)
    secondary_key_order = generate_secondary_key_order(secondary_key)
    num_columns = len(primary_key)
    num_rows = (len(ciphertext) + num_columns - 1) // num_columns
    matrix = [[''] * num_columns for _ in range(num_rows)]

    for col, secondary_index in zip(secondary_key_order, range(len(secondary_key))):
        for row in range(num_rows):
            matrix[row][col[0]] = ciphertext[secondary_index * num_rows + row]
    
    decrypted_text = ""
    for index in range(num_rows):
        for col in primary_key_order:
            decrypted_text += matrix[index][col]
    
    return decrypted_text

# Dynamic input
plaintext = input("Enter the plaintext: ")
primary_key = input("Enter the primary key: ")
secondary_key = input("Enter the secondary key: ")

encrypted_text = advanced_columnar_encrypt(plaintext, primary_key, secondary_key)
print("Encrypted text:", encrypted_text)

decrypted_text = advanced_columnar_decrypt(encrypted_text, primary_key, secondary_key)
print("Decrypted text:", decrypted_text)
