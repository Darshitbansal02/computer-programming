# 12. Check if a List is Sorted in Ascending Order
nums = [1, 2, 3, 4, 5]
is_sorted = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
print(is_sorted)  # Output: True
