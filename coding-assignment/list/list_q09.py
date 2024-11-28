# 9. Remove Duplicates from a List
nums = [1, 2, 3, 3, 4, 4, 5]
unique_nums = []
for num in nums:
    if num not in unique_nums:  # Check if the element is already added
        unique_nums.append(num)
print(unique_nums)  # Output: [1, 2, 3, 4, 5]
