# 8. Find the Maximum and Minimum Elements in a Tuple
# Write a program to find the maximum and minimum elements in a tuple.
input_tuple = (10, 20, 30, 40, 50)
max_val = input_tuple[0]
min_val = input_tuple[0]
for item in input_tuple:
    if item > max_val:
        max_val = item
    if item < min_val:
        min_val = item
print("Max:", max_val)  # Output: 50
print("Min:", min_val)  # Output: 10
