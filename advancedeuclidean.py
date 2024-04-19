def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

# Example usage
num1 = 48
num2 = 18

gcd, x, y = extended_euclidean_algorithm(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)
print("Coefficients (x, y) for ax + by = gcd:", x, y)
