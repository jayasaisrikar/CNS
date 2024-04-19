def xor_string(input_string):
    result = ""
    for char in input_string:
        # XOR each character with 0
        xor_result = ord(char) ^ 0
        result += chr(xor_result)
    return result

input_string = input("Enter a string: ")
result = xor_string(input_string)
print("Result after XORing each character with 0:", result)

#or

'''
string = 'Hello world.'
result = "".join([chr(ord(char) ^ 0) for char in string])
print(result)
'''