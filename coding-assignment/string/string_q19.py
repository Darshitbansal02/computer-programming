# 19. Remove Leading Zeros
# Write a program to remove leading zeros from a string.
input_string = "0001234"
result = ""
for char in input_string:
    if char != "0" or result:
        result += char
print(result)  # Output: "1234"
