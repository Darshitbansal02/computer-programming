# 8. Find the Index of an Element in a List
nums = [10, 20, 30, 40, 50]
element = 30
for index in range(len(nums)):
    if nums[index] == element:  # Find the element
        print(index)  # Output: 2
        break
