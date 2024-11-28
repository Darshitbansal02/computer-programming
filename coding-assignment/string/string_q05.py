# 5. Find the First Non-Repeating Character
# Write a program to find the first non-repeating character in a string.
input_string = "swiss"
for char in input_string:
    if input_string.count(char) == 1:
        print("First non-repeating character:", char)  # Output: "w"
        break
 
