# 18. Write a function to check if a number is a perfect number (the sum of its divisors equals the number).

def is_perfect_number(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Example usage
print(is_perfect_number(28))  # Output: True
