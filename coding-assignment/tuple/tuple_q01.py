# 1. Count Occurrences of an Element in a Tuple
# Write a program to count how many times a specific element appears in a tuple.
input_tuple = (1, 2, 3, 1, 4, 1, 5)
element = 1
count = 0
for item in input_tuple:
    if item == element:
        count += 1
print(count)  # Output: 3
