# 12. Find the Elements that Appear More Than Once in a List
nums = [1, 2, 3, 4, 5, 6, 3, 7, 8, 1]
duplicates = [num for num in set(nums) if nums.count(num) > 1]
print(duplicates)  # Output: [1, 3]
