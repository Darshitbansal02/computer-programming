# 10. Extract Digits from a String
# Write a program to extract all digits from a string and return them as a string.
input_string = "hello 123, how are you 456?"
digits = ""
for char in input_string:
    if char.isdigit():
        digits += char
print(digits)  # Output: "123456"
