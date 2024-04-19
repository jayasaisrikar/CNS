def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Dynamic inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = euclidean_algorithm(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd)
