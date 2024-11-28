# 17. Count the Number of Even and Odd Numbers in a List
nums = [1, 2, 3, 4, 5, 6, 7, 8]
even_count = len([num for num in nums if num % 2 == 0])
odd_count = len([num for num in nums if num % 2 != 0])
print(f"Even count: {even_count}, Odd count: {odd_count}")  # Output: Even count: 4, Odd count: 4
