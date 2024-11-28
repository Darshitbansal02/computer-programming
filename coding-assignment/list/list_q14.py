# 14. Find the First Non-Repeating Element in a List
nums = [4, 5, 4, 6, 7, 6, 7]
for num in nums:
    if nums.count(num) == 1:
        print(num)  # Output: 5
        break
