# 20. Write a function that checks if a given number is an Armstrong number.
               
def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == n

# Example usage
print(is_armstrong(153))  # Output: True
