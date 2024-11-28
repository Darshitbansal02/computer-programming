# 8. Remove Punctuation from a String
# Write a program to remove all punctuation marks from a string.
import string
input_string = "Hello, world!"
cleaned_string = ""
for char in input_string:
    if char not in string.punctuation:
        cleaned_string += char
print(cleaned_string)  # Output: "Hello world"
