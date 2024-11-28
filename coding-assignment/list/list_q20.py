# 20. Find the Largest Number Which is Less Than a Given Value
nums = [10, 20, 30, 40, 50]
value = 35
filtered_nums = [num for num in nums if num < value]
largest_less_than_value = max(filtered_nums) if filtered_nums else None
print(largest_less_than_value)  # Output: 30
