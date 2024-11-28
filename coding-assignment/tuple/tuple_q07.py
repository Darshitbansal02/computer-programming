# 7. Remove Duplicate Elements from a Tuple
# Write a program to remove duplicates from a tuple.
input_tuple = (1, 2, 2, 3, 4, 5, 5)
no_duplicates = []
for item in input_tuple:
    if item not in no_duplicates:
        no_duplicates.append(item)
result_tuple = tuple(no_duplicates)
print(result_tuple)  # Output: (1, 2, 3, 4, 5)
