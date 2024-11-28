# 12. Replace Spaces with Underscore
# Write a program to replace all spaces in a string with underscores.
string = "hello world"
modified_string = ""
for char in string:
    if char == " ":
        modified_string += "_"
    else:
        modified_string += char
print(modified_string)  # Output: "hello_world"
