# 3. Count Vowels and Consonants in a String
# Write a program to count the number of vowels and consonants in a string.
input_string = "hello world"
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for char in input_string:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1
print("Vowels:", vowel_count)  # Output: 3
print("Consonants:", consonant_count)  # Output: 7
