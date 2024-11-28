# 1. Find the Second Largest Element in a List
nums = [1, 2, 3, 4, 5]
unique_nums = list(set(nums))  # Remove duplicates
unique_nums.sort()  # Sort the list
if len(unique_nums) > 1:
    print(unique_nums[-2])  # Output: 4
else:
    print(None)
