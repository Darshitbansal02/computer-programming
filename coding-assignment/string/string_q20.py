# 20. Convert String to Number
# Write a program to convert a string representation of a number to an integer.
string = "12345"
number = 0
for char in string:
    number = number * 10 + int(char)
print(number)  # Output: 12345