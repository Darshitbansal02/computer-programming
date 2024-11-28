# 3. Sort a List in Ascending Order Without Using the `sort()` Method
nums = [3, 1, 4, 2, 5]
for i in range(len(nums)):
    for j in range(0, len(nums)-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]  # Swap elements
print(nums)  # Output: [1, 2, 3, 4, 5]
