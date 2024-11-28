# 6. Check for an Anagram
# Write a program to check if two strings are anagrams of each other.
string1 = "listen"
string2 = "silent"
if sorted(string1) == sorted(string2):
    print("Anagram")  # Output: "Anagram"
else:
    print("Not Anagram")
