# 15. Remove Consecutive Duplicates
# Write a program to remove consecutive duplicate characters from a string.
input_string = "aaabbccdee"
result = ""
previous_char = ""
for char in input_string:
    if char != previous_char:
        result += char
    previous_char = char
print(result)  # Output: "abcde"
