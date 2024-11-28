# 2. Swap the Case of Each Character
# Write a program to swap the case of each character in the given string.
input_string = "Hello World"
swapped_string = ""
for char in input_string:
    if char.isupper():
        swapped_string += char.lower()
    else:
        swapped_string += char.upper()
print(swapped_string)  # Output: "hELLO wORLD"
