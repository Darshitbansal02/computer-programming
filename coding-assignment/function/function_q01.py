# 1. Create a function that counts the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
print(count_vowels("hello"))  # Output: 2 (e, o)
