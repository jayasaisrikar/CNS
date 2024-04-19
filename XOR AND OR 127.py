def manipulate_string(input_string, operation):
    result = ""
    for char in input_string:
        if operation == 'AND':
            manipulated_char = ord(char) & 127
        elif operation == 'XOR':
            manipulated_char = ord(char) ^ 127
        result += chr(manipulated_char)
    return result

input_string = input("Enter a string: ")
operation = input("Choose operation (AND/XOR): ").upper()
while operation not in ['AND', 'XOR']:
    operation = input("Invalid operation. Choose operation (AND/XOR): ").upper()

result = manipulate_string(input_string, operation)
print(f"Result after {operation}ing each character with 127:", result)

'''
string = 'Hello world'
result_and = "".join([chr(ord(char) & 127) for char in string])
result_xor = "".join([chr(ord(char) ^ 127) for char in string])

print("Result of AND operation:", result_and)
print("Result of XOR operation:", result_xor)

'''