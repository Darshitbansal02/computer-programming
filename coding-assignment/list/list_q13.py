# 13. Move All Zeros to the End of the List
nums = [0, 1, 0, 3, 12]
nums = [num for num in nums if num != 0] + [0] * nums.count(0)
print(nums)  # Output: [1, 3, 12, 0, 0]
