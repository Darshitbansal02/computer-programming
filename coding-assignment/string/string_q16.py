# 16. Find Common Characters in Two Strings
# Write a program to find the common characters between two strings.
string1 = "abcdef"
string2 = "acdfgh"
common_chars = ""
for char in string1:
    if char in string2:
        common_chars += char
print("Common characters:", common_chars)  # Output: "acdf"
