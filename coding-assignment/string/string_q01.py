# 1. Remove Duplicates from a String
# Write a program to remove duplicate characters from a string while preserving the original order.
input_string = "programming"
result = ""
for char in input_string:
    if char not in result:
        result += char
print(result)  # Output: "progamin"
