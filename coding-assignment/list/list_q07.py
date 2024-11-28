# 7. Count the Occurrences of an Element in a List
nums = [1, 2, 3, 4, 3, 5, 3]
element = 3
count = 0
for num in nums:
    if num == element:  # Check for occurrences
        count += 1
print(count)  # Output: 3
