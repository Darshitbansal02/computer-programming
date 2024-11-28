# 9. Check if String is a Pangram
# Write a program to check if a string contains all the letters of the alphabet.
import string
input_string = "The quick brown fox jumps over the lazy dog"
letters = set(input_string.lower())
is_pangram = True
for char in string.ascii_lowercase:
    if char not in letters:
        is_pangram = False
        break
if is_pangram:
    print("Pangram")  # Output: "Pangram"
else:
    print("Not a Pangram")
