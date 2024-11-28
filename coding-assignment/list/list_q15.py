# 15. Remove Elements Greater Than a Given Value
nums = [1, 2, 3, 4, 5, 6, 7]
value = 4
nums = [num for num in nums if num <= value]
print(nums)  # Output: [1, 2, 3, 4]
