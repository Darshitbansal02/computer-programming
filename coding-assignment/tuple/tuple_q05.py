# 5. Check if an Element Exists in a Tuple
# Write a program to check if an element exists in a tuple.
input_tuple = (1, 2, 3, 4, 5)
element = 3
exists = False
for item in input_tuple:
    if item == element:
        exists = True
        break
print(exists)  # Output: True
