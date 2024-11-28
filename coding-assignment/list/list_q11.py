# 11. Find the Maximum Product of Two Numbers in a List
nums = [1, 10, -5, 2, 3]
nums.sort()
max_product = nums[-1] * nums[-2]  # Max product of two largest numbers
print(max_product)  # Output: 30
