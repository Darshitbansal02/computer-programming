# 1. Remove Duplicates from a String
# Write a program to remove duplicate characters from a string while preserving the original order.
string = "programming"
result = "".join(sorted(set(string), key=string.index))
print(result)  # Output: "progamin"
