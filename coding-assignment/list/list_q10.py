# 10. Reverse a List Without Using the `reverse()` Method
nums = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(nums)-1, -1, -1):  # Traverse in reverse order
    reversed_list.append(nums[i])
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
