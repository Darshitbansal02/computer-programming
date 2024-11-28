# 5. Find the First Non-Repeating Character
# Write a program to find the first non-repeating character in a string.
string = "swiss"
for char in string:
    if string.count(char) == 1:
        print("First non-repeating character:", char)  # Output: "w"
        break
