def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I").replace("Q", "")
    key += "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    playfair_matrix = []
    for char in key:
        if char not in playfair_matrix:
            playfair_matrix.append(char)
    return playfair_matrix

def generate_playfair_pairs(text):
    pairs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            pairs.append((text[i], "X"))
            break
        if text[i] == text[i + 1]:
            pairs.append((text[i], "X"))
            i += 1
        else:
            pairs.append((text[i], text[i + 1]))
            i += 2
    return pairs

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    pairs = generate_playfair_pairs(text.upper().replace("J", "I").replace("Q", ""))
    encrypted_text = ""
    for pair in pairs:
        row1, col1 = divmod(matrix.index(pair[0]), 5)
        row2, col2 = divmod(matrix.index(pair[1]), 5)
        if row1 == row2:
            encrypted_text += matrix[row1 * 5 + (col1 + 1) % 5]
            encrypted_text += matrix[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += matrix[((row1 + 1) % 5) * 5 + col1]
            encrypted_text += matrix[((row2 + 1) % 5) * 5 + col2]
        else:
            encrypted_text += matrix[row1 * 5 + col2]
            encrypted_text += matrix[row2 * 5 + col1]
    return encrypted_text

def playfair_decrypt(text, key):
    matrix = generate_playfair_matrix(key)
    pairs = generate_playfair_pairs(text)
    decrypted_text = ""
    for pair in pairs:
        row1, col1 = divmod(matrix.index(pair[0]), 5)
        row2, col2 = divmod(matrix.index(pair[1]), 5)
        if row1 == row2:
            decrypted_text += matrix[row1 * 5 + (col1 - 1) % 5]
            decrypted_text += matrix[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += matrix[((row1 - 1) % 5) * 5 + col1]
            decrypted_text += matrix[((row2 - 1) % 5) * 5 + col2]
        else:
            decrypted_text += matrix[row1 * 5 + col2]
            decrypted_text += matrix[row2 * 5 + col1]
    return decrypted_text

# Dynamic input
text = input("Enter the text: ")
key = "ldrp"

encrypted_text = playfair_encrypt(text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = playfair_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
