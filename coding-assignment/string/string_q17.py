# 17. Check for a Valid Palindrome
# Write a program to check if a string is a valid palindrome, ignoring spaces, punctuation, and case.
import re
input_string = "A man, a plan, a canal, Panama"
clean_string = re.sub(r'[^A-Za-z]', '', input_string).lower()
is_palindrome = True
for i in range(len(clean_string) // 2):
    if clean_string[i] != clean_string[-i - 1]:
        is_palindrome = False
        break
if is_palindrome:
    print("Valid Palindrome")  # Output: "Valid Palindrome"
else:
    print("Not a Valid Palindrome")
