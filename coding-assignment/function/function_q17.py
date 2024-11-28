# 17. Write a function that computes the greatest common divisor (GCD) of two given numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
print(gcd(56, 98))  # Output: 14
