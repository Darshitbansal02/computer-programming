# 3. Count Vowels and Consonants in a String
# Write a program to count the number of vowels and consonants in a string.
string = "hello world"
vowels = "aeiou"
vowel_count = sum(1 for char in string if char in vowels)
consonant_count = sum(1 for char in string if char.isalpha() and char not in vowels)
print("Vowels:", vowel_count)  # Output: 3
print("Consonants:", consonant_count)  # Output: 7
