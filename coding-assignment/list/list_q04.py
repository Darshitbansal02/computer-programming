# 4. Remove All Occurrences of a Specific Element from a List
nums = [1, 2, 3, 4, 3, 5, 3]
element = 3
while element in nums:
    nums.remove(element)  # Remove the element
print(nums)  # Output: [1, 2, 4, 5]
