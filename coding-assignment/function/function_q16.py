# 16. Write a function that converts a given decimal number to binary

def decimal_to_binary(n):
    return bin(n)[2:]

# Example usage
print(decimal_to_binary(10))  # Output: '1010'
